from ..filters import Filters
from ..request import Request


class Portal:
    '''Portal'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def clustered(self, **d):
        '''clustered | Telematic.Portal.clustered'''
        url  = self.URL.get(self.URL.Telematic.Portal.clustered)
        json = Filters.Telematic.Portal.clustered(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def count(self, **d):
        '''count | Telematic.Portal.count'''
        url  = self.URL.get(self.URL.Telematic.Portal.count)
        json = Filters.Telematic.Portal.count(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def modified(self, **d):
        '''modified | Telematic.Portal.modified'''
        url  = self.URL.get(self.URL.Telematic.Portal.modified)
        json = Filters.Telematic.Portal.modified(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Telematic.Portal.read'''
        url  = self.URL.get(self.URL.Telematic.Portal.read)
        json = Filters.Telematic.Portal.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Telematic:
    '''Telematic'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Portal = Portal(session, URL)


    @Request.All_pages
    @Request.Retry
    async def bound(self, **d):
        '''bound | Telematic.bound'''
        url  = self.URL.get(self.URL.Telematic.bound)
        json = Filters.Telematic.bound(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def log(self, **d):
        '''log | Telematic.log'''
        url  = self.URL.get(self.URL.Telematic.log)
        json = Filters.Telematic.log(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def panic(self, **d):
        '''panic | Telematic.panic'''
        url  = self.URL.get(self.URL.Telematic.panic)
        json = Filters.Telematic.panic(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Telematic.read'''
        url  = self.URL.get(self.URL.Telematic.read)
        json = Filters.Telematic.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def store(self, **d):
        '''store | Telematic.store'''
        url  = self.URL.get(self.URL.Telematic.store)
        json = Filters.Telematic.store(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Telematic.to_list'''
        url  = self.URL.get(self.URL.Telematic.to_list)
        json = Filters.Telematic.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)