from .config import Method
from .request_filters   import AddFilters
from .request_functions import retry_request, get_request_body, get_all_pages


class Order:
    """Обращение к план-нарядам (API РНИС)"""
    def __init__(self, session, token):
        self.__session = session
        self.__token   = token


    @retry_request
    async def by_uuid(self, **d):
        """Получение план-наряда по идентификатору"""
        json = get_request_body(self.__token)
        json['payload']['uuid'] = d.get('uuid')
        return await self.__session.post(url=Method.order, json=json)

    
    @get_all_pages
    @retry_request
    async def list_(self, **d):
        """Получение списка план-нарядов"""
        json = get_request_body(self.__token, pagination=True, order=True, filters=True, response_data=True)
        json = AddFilters.Order.list_(json, **d)
        return await self.__session.post(url=Method.order_list, json=json)

    
    @get_all_pages
    @retry_request
    async def execution(self, **d):
        """Получение результатов выполнения план-нарядов по идентификатору план-наряда (внутри класса)"""
        json = get_request_body(self.__token, pagination=True, order=True, filters=True)
        json = AddFilters.Order.execution(json, **d)
        return await self.__session.post(url=Method.execution, json=json)