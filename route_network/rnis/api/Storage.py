from ..filters import Filters
from ..request import Request


class Storage:
    '''Storage'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Storage.delete'''
        url  = self.URL.get(self.URL.Storage.delete)
        json = Filters.Storage.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Storage.read'''
        url  = self.URL.get(self.URL.Storage.read)
        json = Filters.Storage.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def token(self, **d):
        '''token | Storage.token'''
        url  = self.URL.get(self.URL.Storage.token)
        json = Filters.Storage.token(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)