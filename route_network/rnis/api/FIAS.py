from ..filters import Filters
from ..request import Request


class FIAS:
    '''FIAS'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | FIAS.read'''
        url  = self.URL.get(self.URL.FIAS.read)
        json = Filters.FIAS.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def search(self, **d):
        '''search | FIAS.search'''
        url  = self.URL.get(self.URL.FIAS.search)
        json = Filters.FIAS.search(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)