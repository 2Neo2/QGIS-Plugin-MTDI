from ..filters import Filters
from ..request import Request


class Device:
    '''Device'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def arhive(self, **d):
        '''arhive | T1sync.Device.arhive'''
        url  = self.URL.get(self.URL.T1sync.Device.arhive)
        json = Filters.T1sync.Device.arhive(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def score(self, **d):
        '''score | T1sync.Device.score'''
        url  = self.URL.get(self.URL.T1sync.Device.score)
        json = Filters.T1sync.Device.score(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def search(self, **d):
        '''search | T1sync.Device.search'''
        url  = self.URL.get(self.URL.T1sync.Device.search)
        json = Filters.T1sync.Device.search(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def tachograph(self, **d):
        '''tachograph | T1sync.Device.tachograph'''
        url  = self.URL.get(self.URL.T1sync.Device.tachograph)
        json = Filters.T1sync.Device.tachograph(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class History:
    '''History'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | T1sync.History.read'''
        url  = self.URL.get(self.URL.T1sync.History.read)
        json = Filters.T1sync.History.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | T1sync.History.to_list'''
        url  = self.URL.get(self.URL.T1sync.History.to_list)
        json = Filters.T1sync.History.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Odometr:
    '''Odometr'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | T1sync.Odometr.read'''
        url  = self.URL.get(self.URL.T1sync.Odometr.read)
        json = Filters.T1sync.Odometr.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | T1sync.Odometr.to_list'''
        url  = self.URL.get(self.URL.T1sync.Odometr.to_list)
        json = Filters.T1sync.Odometr.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class T1sync:
    '''T1sync'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Device = Device(session, URL)
        self.History = History(session, URL)
        self.Odometr = Odometr(session, URL)


    @Request.All_pages
    @Request.Retry
    async def event(self, **d):
        '''event | T1sync.event'''
        url  = self.URL.get(self.URL.T1sync.event)
        json = Filters.T1sync.event(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def extended(self, **d):
        '''extended | T1sync.extended'''
        url  = self.URL.get(self.URL.T1sync.extended)
        json = Filters.T1sync.extended(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def mileage(self, **d):
        '''mileage | T1sync.mileage'''
        url  = self.URL.get(self.URL.T1sync.mileage)
        json = Filters.T1sync.mileage(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def motohour(self, **d):
        '''motohour | T1sync.motohour'''
        url  = self.URL.get(self.URL.T1sync.motohour)
        json = Filters.T1sync.motohour(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)