class Add:
    def default() -> dict:
        """Получить стандартное тело запроса"""
        request_body = {
            'headers': {
                'meta': {},
            },
            'payload': {},
        }
        return request_body


    def column_search(request_body: dict, key: str, value: any) -> dict:
        """Создание фильтра по заданной колонке (поиск по колонке)"""
        if value is not None:
            meta = request_body['headers']['meta']
            meta['column_search'] = meta.get('column_search', [])
            meta['column_search'].append({
                'column': key, 
                'value':  to_str(value)
            })
        return request_body


    def filters(request_body: dict, key: any = None, value: any = None, func: str = None) -> dict:
        """Добавить фильтры (по заданным параметрам)"""
        request_body['headers']['meta']['filters'] = request_body['headers']['meta'].get('filters', {})
        filters = request_body['headers']['meta']['filters']
        if key and value is not None:
            if func:
                func = eval(func)
                value = func(value)
            filters[key] = value
        return request_body


    def order(request_body: dict, key: str = 'uuid', value: str = 'asc') -> dict:
        """Добавить сортировку"""
        request_body['headers']['meta']['order'] = {'column': key, 'direction': value}
        return request_body


    def pagination(request_body: dict, page: int = 1, limit: int = 25) -> dict:
        """Добавить пагинацию"""
        request_body['headers']['meta']['pagination'] = {'page': page, 'limit': limit}
        return request_body


    def payload(request_body: dict, key: str, value: str) -> dict:
        """Добавить пагинацию"""
        request_body['payload'][key] = value
        return request_body


    def response_data(request_body: dict, value: any = None) -> dict:
        """Добавить возращаемые данные"""
        if value is not None:
            request_body['headers']['meta']['response_data'] = to_list(value)
        else:
            request_body['headers']['meta']['response_data'] = ["items/uuid"]
        return request_body


    def token(request_body: dict, value: str = None) -> dict:
        """Добавить токен"""
        if value is not None:
            request_body['headers']['token'] = value
        return request_body


def to_list(data: any) -> list:
    """Преобразование данных в список"""
    if type(data) in [dict, list, set, tuple]:
        return list(data)
    else:
        return [f'{data}']


def to_str(data: any) -> str:
    """Преобразование данных в строку"""
    data = to_list(data)[0]
    return f'{data}'