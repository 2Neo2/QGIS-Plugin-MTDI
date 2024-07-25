from ....request import Request


def to_list(**d):
    json = Request.Body.default()            # Дефолтный JSON
    Request.Body.token(json, d.get('token')) # token
    Request.Body.filters(json, 'withUuid', d.get('uuid'), 'to_list') # Фильтры по ключу можно добавить функции 'to_str', 'to_list'
    Request.Body.filters(json, 'withSources', d.get('source_list'), 'to_list') # Фильтры по ключу можно добавить функции 'to_str', 'to_list'
    Request.Body.pagination(json, d.get('page'), d.get('limit'))   # Пагинация по заданным параметрам
    Request.Body.order(json)          # Дефолтная сортировка по UUID
    # Хардкод :(
    json['headers']['meta']['filters']['withSource'] = None
    # Request.Body.response_data(json, d.get('response_data'))  # Вывод атрибутов в списке заданные пользователем
    return json