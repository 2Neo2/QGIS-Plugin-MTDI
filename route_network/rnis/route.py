from .config import Method
from .request_filters   import AddFilters
from .request_functions import retry_request, get_request_body, get_all_pages


class Route:
    """Обращение к марщрутам (API РНИС)"""
    def __init__(self, session, token):
        self.__session = session
        self.__token   = token


    @retry_request
    async def by_uuid(self, **d):
        """Получение маршрута по идентификатору"""
        json = get_request_body(self.__token)
        json['payload']['uuid'] = d.get('uuid')
        return await self.__session.post(url=Method.route, json=json)

    
    @get_all_pages
    @retry_request
    async def list_(self, **d):
        """Получение списка маршрутов"""
        json = get_request_body(self.__token, pagination=True, order=True, filters=True, response_data=True)
        json = AddFilters.Route.list_(json, **d)
        return await self.__session.post(url = Method.route_list, json = json)
    

    @retry_request
    async def registry(self, **d):
        """Получение реестра маршрутов по идентификатору"""
        json = get_request_body(self.__token)
        json['payload']['uuid'] = d.get('uuid')
        return await self.__session.post(url=Method.route_registry, json=json)
    

    @get_all_pages
    @retry_request
    async def registry_list(self, **d):
        """Получение списка реестра маршрутов"""
        json = get_request_body(self.__token, pagination=True, order=True, filters=True, response_data=True)
        json = AddFilters.Route.registry_list(json, **d)
        return await self.__session.post(url=Method.route_registry_list, json=json)
    
    
    @retry_request
    async def variant(self, **d):
        """Получение варианта маршрута по идентификатору"""
        json = get_request_body(self.__token)
        json['payload']['uuid'] = d.get('uuid')
        return await self.__session.post(url=Method.route_variant, json=json)
    
    
    @get_all_pages
    @retry_request
    async def variant_list(self, **d):
        """Получение варианта маршрута по идентификатору"""
        json = get_request_body(self.__token, pagination=True, order=True, filters=True)
        json = AddFilters.Route.variant_list(json, **d)
        return await self.__session.post(url=Method.route_variant_list, json=json)