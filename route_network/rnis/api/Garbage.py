from ..filters import Filters
from ..request import Request


class Garbage:
    '''Garbage'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Garbage.create'''
        url  = self.URL.get(self.URL.Garbage.create)
        json = Filters.Garbage.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Garbage.delete'''
        url  = self.URL.get(self.URL.Garbage.delete)
        json = Filters.Garbage.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Garbage.read'''
        url  = self.URL.get(self.URL.Garbage.read)
        json = Filters.Garbage.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Garbage.to_list'''
        url  = self.URL.get(self.URL.Garbage.to_list)
        json = Filters.Garbage.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Garbage.update'''
        url  = self.URL.get(self.URL.Garbage.update)
        json = Filters.Garbage.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)