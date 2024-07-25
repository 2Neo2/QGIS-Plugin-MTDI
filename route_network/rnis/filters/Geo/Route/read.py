from ....request import Request


def read(**d):
    json = Request.Body.default()            # Дефолтный JSON
    Request.Body.token(json, d.get('token')) # token
    Request.Body.payload(json, 'uuid', d.get('uuid')) # Добавить данные в вывод
    return json