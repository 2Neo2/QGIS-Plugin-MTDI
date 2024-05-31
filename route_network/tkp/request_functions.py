import asyncio
import json

from functools    import wraps
from urllib.parse import unquote


# Повторные запросы
def retry_request(func):
    @wraps(func)
    async def request(*args, **kwargs) -> object or list:
        delay   = kwargs.get('delay', 60)           # Задержка в секундах
        retries = kwargs.get('retries', 4)          # Кол-во повторных попыток
        for i in range(retries):
            try:
                return await check_response(
                       await func(*args, **kwargs))
            except Exception as error:
                await asyncio.sleep(delay*i)
                kwargs['error'] = get_error(error)
                if kwargs.get('print_error'):
                    print(f'''\nПопытка: {i}, задержка {delay*i}\nОшибка:  {kwargs['error']}''')
        return kwargs['error']
    return request


async def check_response(response: object) -> object or list:
    """Проверка ответа от сервера"""
    if response.status in [200, 202]:
        return response
    else:
        raise Exception([{'text': f'Ответ сервера - {response.status}'}])


def get_error(error: object) -> list:
    """Формирование текста ошибки"""
    error = list(error.args)[0]
    if type(error) == str:
        return [{'text': error}]
    return error


def check_error(func):
    @wraps(func)
    async def check_response(*args, **kwargs) -> dict or list:
        response = await func(*args, **kwargs)
        if 'json' in response['type']:
            response = json.loads(response['data'])
        if type(response) is dict:
            error = response.get('error')
            if error is not None:
                return [{'text': f'{error}'}]
        return response
    return check_response


def get_filename(response) -> str or None:
    try:
        filename = response.content_disposition.filename
    except:
        return None
    filename = unquote(filename)
    filename = normolize_name(filename)
    return filename


def check_error_(content: object) -> tuple[str or bytes, str or object]:
    """Обработка ошибок при парсинге CSV, XLSX"""
    try:
        content = content.decode("utf-8")
    except:
        content = content
    try:
        error = json.loads(content).get('error')
    except:
        error = None
    return content, error


def parse_response(func):
    @wraps(func)
    async def parsed_response(*args, **kwargs) -> dict:
        """Создание парметров по данным из карточки"""
        response = await func(*args, **kwargs)
        try:
            content, error = check_error_(await response.content.read())

        except:
            content, error = response, None
        data  = {}
        data['filename'] = get_filename(response)
        data['type']  = response.headers.get('Content-Type')
        data['data']  = content
        data['error'] = error
        return data
    return parsed_response


def normolize_name(name: str) -> str:
    """Исключение из имени символов не используемых в наименовании в ситемах"""
    for sym in ['\\', '/', ':', '*', '?', '"', '<', '>', '|', '+', '%', '!', '@', '\0']:
        name = name.replace(sym, '_')
    return name