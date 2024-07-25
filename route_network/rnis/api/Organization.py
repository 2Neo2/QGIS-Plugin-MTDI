from ..filters import Filters
from ..request import Request


class Carrier:
    '''Carrier'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Organization.Carrier.create'''
        url  = self.URL.get(self.URL.Organization.Carrier.create)
        json = Filters.Organization.Carrier.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Organization.Carrier.delete'''
        url  = self.URL.get(self.URL.Organization.Carrier.delete)
        json = Filters.Organization.Carrier.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Organization.Carrier.read'''
        url  = self.URL.get(self.URL.Organization.Carrier.read)
        json = Filters.Organization.Carrier.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Organization.Carrier.to_list'''
        url  = self.URL.get(self.URL.Organization.Carrier.to_list)
        json = Filters.Organization.Carrier.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Organization.Carrier.update'''
        url  = self.URL.get(self.URL.Organization.Carrier.update)
        json = Filters.Organization.Carrier.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Position:
    '''Position'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Organization.Position.create'''
        url  = self.URL.get(self.URL.Organization.Position.create)
        json = Filters.Organization.Position.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Organization.Position.delete'''
        url  = self.URL.get(self.URL.Organization.Position.delete)
        json = Filters.Organization.Position.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Organization.Position.read'''
        url  = self.URL.get(self.URL.Organization.Position.read)
        json = Filters.Organization.Position.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Organization.Position.to_list'''
        url  = self.URL.get(self.URL.Organization.Position.to_list)
        json = Filters.Organization.Position.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Organization.Position.update'''
        url  = self.URL.get(self.URL.Organization.Position.update)
        json = Filters.Organization.Position.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Unit:
    '''Unit'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def children(self, **d):
        '''children | Organization.Unit.children'''
        url  = self.URL.get(self.URL.Organization.Unit.children)
        json = Filters.Organization.Unit.children(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Organization.Unit.create'''
        url  = self.URL.get(self.URL.Organization.Unit.create)
        json = Filters.Organization.Unit.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Organization.Unit.delete'''
        url  = self.URL.get(self.URL.Organization.Unit.delete)
        json = Filters.Organization.Unit.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Organization.Unit.read'''
        url  = self.URL.get(self.URL.Organization.Unit.read)
        json = Filters.Organization.Unit.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Organization.Unit.to_list'''
        url  = self.URL.get(self.URL.Organization.Unit.to_list)
        json = Filters.Organization.Unit.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Organization.Unit.update'''
        url  = self.URL.get(self.URL.Organization.Unit.update)
        json = Filters.Organization.Unit.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Organization:
    '''Organization'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Carrier = Carrier(session, URL)
        self.Position = Position(session, URL)
        self.Unit = Unit(session, URL)


    @Request.All_pages
    @Request.Retry
    async def user_group(self, **d):
        '''user_group | Organization.user_group'''
        url  = self.URL.get(self.URL.Organization.user_group)
        json = Filters.Organization.user_group(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)