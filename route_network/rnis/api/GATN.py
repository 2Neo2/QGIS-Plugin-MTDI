from ..filters import Filters
from ..request import Request


class GATN:
    '''GATN'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def journal(self, **d):
        '''journal | GATN.journal'''
        url  = self.URL.get(self.URL.GATN.journal)
        json = Filters.GATN.journal(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | GATN.to_list'''
        url  = self.URL.get(self.URL.GATN.to_list)
        json = Filters.GATN.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)