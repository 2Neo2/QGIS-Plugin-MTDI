import asyncio

from .body     import to_list
from functools import wraps
from tqdm      import tqdm


# Повторные запросы
def retry_request(func):
    @wraps(func)
    async def request(*args, **kwargs):
        delay   = kwargs.get('delay', 60)       # Задержка в секундах
        retries = kwargs.get('retries', 4)      # Кол-во повторных попыток
        error_skip = kwargs.get('error_skip', False)   # Пропустить ошибки
        error_code = to_list(kwargs.get('error_code')) # Какой код ошибки пропускать
        for i in range(retries):
            try:
                return await check_response(
                       await func(*args, **kwargs))
            except Exception as e:
                await asyncio.sleep(delay*i)
                e = list(e.args)[0]
                kwargs['error'] = [{'text': e}] if isinstance(e, str) else e
                if kwargs.get('error_print'):
                    print(f'''\nПопытка: {i}, задержка {delay*i}\nОшибка:  {kwargs['error']}\n''')
                    for k,v in kwargs.items():
                        print(f'{k}: {v}')
                e = kwargs['error'][0].get('code')
                e = e if len(error_code) == 1 else int(e)
                if error_skip and e in error_code:
                    return {'payload': {'error': True}}
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
        uuid_list   = kwargs.get('uuid_list', [])       # Список идентификаторов
        uuid_list   = to_list(uuid_list)
        if uuid_list:
            kwargs['uuid'] = kwargs.get('uuid', uuid_list[0])
        response = await func(*args, **kwargs)
        if isinstance(response, dict):
            meta = response.get('headers', {}).get('meta', {})
            meta = meta if meta != [] else dict()
            response = {'payload': [response['payload']]}
            total_pages = len(uuid_list) if uuid_list else meta.get('pagination', {}).get('total_pages', 1)
            object_list = uuid_list if uuid_list else [page for page in range(2, total_pages + 1)]
            if total_pages > 1 and all_pages is True:
                # with tqdm(total=total_pages) as pbar:
                for chunk in chunks(object_list, concurrency):
                    tasks = [
                        func(*args, **dict(kwargs, uuid=c))
                        if uuid_list else
                        func(*args, **dict(kwargs, page=c))
                        for c in chunk
                    ]
                    for r in await asyncio.gather(*tasks):
                        payload = r.get('payload', False)
                        if payload:
                            if not(payload.get('error', False)):
                                response['payload'].append(payload)
                        # pbar.update(len(chunk))
        return response
    return request


def token(session: object) -> str:
    '''Получение token из сессии'''
    for c in session.cookie_jar:
        if c.key == 'token':
            return c.value
    return None