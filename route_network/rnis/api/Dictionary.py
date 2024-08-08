from ..filters import Filters
from ..request import Request


class Dictionary:
    '''Dictionary'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Dictionary.create'''
        url  = self.URL.get(self.URL.Dictionary.create)
        json = Filters.Dictionary.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Dictionary.delete'''
        url  = self.URL.get(self.URL.Dictionary.delete)
        json = Filters.Dictionary.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def list_many(self, **d):
        '''list_many | Dictionary.list_many'''
        url  = self.URL.get(self.URL.Dictionary.list_many)
        json = Filters.Dictionary.list_many(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def meta(self, **d):
        '''meta | Dictionary.meta'''
        url  = self.URL.get(self.URL.Dictionary.meta)
        json = Filters.Dictionary.meta(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def off_day(self, **d):
        '''off_day | Dictionary.off_day'''
        url  = self.URL.get(self.URL.Dictionary.off_day)
        json = Filters.Dictionary.off_day(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Dictionary.read'''
        url  = self.URL.get(self.URL.Dictionary.read)
        json = Filters.Dictionary.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def structure(self, **d):
        '''structure | Dictionary.structure'''
        url  = self.URL.get(self.URL.Dictionary.structure)
        json = Filters.Dictionary.structure(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Dictionary.to_list'''
        url  = self.URL.get(self.URL.Dictionary.to_list)
        json = Filters.Dictionary.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Dictionary.update'''
        url  = self.URL.get(self.URL.Dictionary.update)
        json = Filters.Dictionary.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)

    
    @Request.All_pages
    @Request.Retry
    async def unit(self, **d):
        '''read | Dictionary.unit'''
        url  = self.URL.get(self.URL.Dictionary.unit)
        json = Filters.Dictionary.unit(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)