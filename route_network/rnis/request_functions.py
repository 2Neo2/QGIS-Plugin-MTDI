import asyncio

from functools import wraps


def get_request_body(
        token: str,
        pagination: bool = False,
        order: bool = False,
        filters: bool = False,
        response_data: bool = False,
    ) -> dict:
    """Получить тело запроса"""
    def default_request_body():
        """Вернуть стандартное тело запроса"""
        request_body = {
            'headers': {
                'meta': {},
                'token': token
            },
            'payload': {},
        }
        return request_body
    
    def add_pagination(request_body: dict) -> dict:
        """Добавить пагинацию"""
        request_body['headers']['meta']['pagination'] = {'page': 1, 'limit': 25}
        return request_body
    
    def add_order(request_body: dict) -> dict:
        """Добавить сортировку"""
        request_body['headers']['meta']['order'] = {'column': 'uuid', 'direction': 'asc'}
        return request_body
    
    def add_filters(request_body: dict) -> dict:
        """Добавить фильтры"""
        request_body['headers']['meta']['filters'] = {}
        request_body['headers']['meta']['filters']['withComponent'] = 'kiutr'
        return request_body

    def add_response_data(request_body: dict) -> dict:
        """Добавить возращаемые данные"""
        request_body['headers']['meta']['response_data'] = ["items/uuid"]
        return request_body
    
    request_body = default_request_body()
    if pagination:
        request_body = add_pagination(request_body)
    if order:
        request_body = add_order(request_body)
    if filters:
        request_body = add_filters(request_body)
    if response_data:
        request_body = add_response_data(request_body)
    return request_body


# Повторные запросы
def retry_request(func):
    @wraps(func)
    async def request(*args, **kwargs):
        delay   = kwargs.get('delay', 60)       # Задержка в секундах
        retries = kwargs.get('retries', 4)      # Кол-во повторных попыток
        for i in range(retries):
            try:
                return await check_response(
                       await func(*args, **kwargs))
            except Exception as e:
                await asyncio.sleep(delay*i)
                e = list(e.args)[0]
                kwargs['error'] = [{'text': e}] if type(e) == str else e
                if kwargs.get('print_error'):
                    print(f'''\nПопытка: {i}, задержка {delay*i}\nОшибка:  {kwargs['error']}''')
        return kwargs['error']
    return request


async def check_response(response):
    """Проверка ответа от сервера"""
    if response.status == 200:
        data = await response.json()
        if data['success']:
            return data
        else:
            raise Exception(data["errors"])
    else:
        raise Exception([{'text':f'Ответ сервера - {response.status}'}])


def chunks(lst, n):
    """Получение последовательных фрагментов размером n из списка"""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


# Загрузка всех страниц
def get_all_pages(func):
    @wraps(func)
    async def request(*args, **kwargs):
        concurrency = kwargs.get('concurrency', 10)     # Кол-во потоков запросов
        all_pages   = kwargs.get('all_pages', False)    # Загрузка всех страниц
        data = await func(*args, **kwargs)
        total_pages = data['headers']['meta']['pagination']['total_pages']
        if total_pages > 1 and all_pages is True:
            for total_pages in chunks([page for page in range(2, total_pages + 1)], concurrency):
                tasks = [
                    func(*args, **dict(kwargs, page=page))
                    for page in total_pages
                ]
                for response in await asyncio.gather(*tasks):
                    for item in response.get('payload', {}).get('items', []):
                        data['payload']['items'].append(item)
        return data
    return request