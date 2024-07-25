from ...request import Request


def login(**d):
    json = Request.Body.default()       # Дефолтный JSON
    Request.Body.payload(json, 'login',    d.get('login'))
    Request.Body.payload(json, 'password', d.get('password'))
    # Request.Body.token(json)          # Пустые фильтры
    # Request.Body.filters(json)        # Пустые фильтры
    # Request.Body.filters(json, 'key', d.get('key')) # Фильтры по ключу можно добавить функции 'to_str', 'to_list'
    # Request.Body.order(json)          # Дефолтная сортировка по UUID
    # Request.Body.order(json, d.get('column'), d.get('direction')) # Сортировка по заданным параметрам
    # Request.Body.pagination(json)     # Дефолтная пагинация
    # Request.Body.pagination(json, d.get('page'), d.get('limit')   # Дефолтная пагинация
    # Request.Body.column_search(json, 'key', d.get('key')) # 
    # Request.Body.payload(json, 'key', d.get('key')) # 
    # Request.Body.response_data(json)  # Дефолтный вывод атрибутов в списке
    # Request.Body.response_data(json, d.get(response_data))  # Вывод атрибутов в списке заданные пользователем
    return json