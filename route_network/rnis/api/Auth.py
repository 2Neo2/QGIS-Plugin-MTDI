from ..filters import Filters
from ..request import Request


class Unit:
    '''Unit'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Auth.Permission.Unit.read'''
        url  = self.URL.get(self.URL.Auth.Permission.Unit.read)
        json = Filters.Auth.Permission.Unit.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Auth.Permission.Unit.update'''
        url  = self.URL.get(self.URL.Auth.Permission.Unit.update)
        json = Filters.Auth.Permission.Unit.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Permission:
    '''Permission'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Unit = Unit(session, URL)


    @Request.All_pages
    @Request.Retry
    async def store(self, **d):
        '''store | Auth.Permission.store'''
        url  = self.URL.get(self.URL.Auth.Permission.store)
        json = Filters.Auth.Permission.store(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Auth.Permission.to_list'''
        url  = self.URL.get(self.URL.Auth.Permission.to_list)
        json = Filters.Auth.Permission.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Auth.Permission.update'''
        url  = self.URL.get(self.URL.Auth.Permission.update)
        json = Filters.Auth.Permission.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def user(self, **d):
        '''user | Auth.Permission.user'''
        url  = self.URL.get(self.URL.Auth.Permission.user)
        json = Filters.Auth.Permission.user(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Role:
    '''Role'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Auth.Role.create'''
        url  = self.URL.get(self.URL.Auth.Role.create)
        json = Filters.Auth.Role.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def created(self, **d):
        '''created | Auth.Role.created'''
        url  = self.URL.get(self.URL.Auth.Role.created)
        json = Filters.Auth.Role.created(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Auth.Role.delete'''
        url  = self.URL.get(self.URL.Auth.Role.delete)
        json = Filters.Auth.Role.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def deleted(self, **d):
        '''deleted | Auth.Role.deleted'''
        url  = self.URL.get(self.URL.Auth.Role.deleted)
        json = Filters.Auth.Role.deleted(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Auth.Role.read'''
        url  = self.URL.get(self.URL.Auth.Role.read)
        json = Filters.Auth.Role.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Auth.Role.update'''
        url  = self.URL.get(self.URL.Auth.Role.update)
        json = Filters.Auth.Role.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def updated(self, **d):
        '''updated | Auth.Role.updated'''
        url  = self.URL.get(self.URL.Auth.Role.updated)
        json = Filters.Auth.Role.updated(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Position:
    '''Position'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Auth.User.Position.create'''
        url  = self.URL.get(self.URL.Auth.User.Position.create)
        json = Filters.Auth.User.Position.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Auth.User.Position.delete'''
        url  = self.URL.get(self.URL.Auth.User.Position.delete)
        json = Filters.Auth.User.Position.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Auth.User.Position.update'''
        url  = self.URL.get(self.URL.Auth.User.Position.update)
        json = Filters.Auth.User.Position.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Auth.User.Position.read'''
        url  = self.URL.get(self.URL.Auth.User.Position.read)
        json = Filters.Auth.User.Position.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Dismissal:
    '''Dismissal'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Auth.User.Dismissal.read'''
        url  = self.URL.get(self.URL.Auth.User.Dismissal.read)
        json = Filters.Auth.User.Dismissal.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Education:
    '''Education'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Auth.User.Education.create'''
        url  = self.URL.get(self.URL.Auth.User.Education.create)
        json = Filters.Auth.User.Education.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Auth.User.Education.delete'''
        url  = self.URL.get(self.URL.Auth.User.Education.delete)
        json = Filters.Auth.User.Education.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Auth.User.Education.read'''
        url  = self.URL.get(self.URL.Auth.User.Education.read)
        json = Filters.Auth.User.Education.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Auth.User.Education.update'''
        url  = self.URL.get(self.URL.Auth.User.Education.update)
        json = Filters.Auth.User.Education.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class User:
    '''User'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Position = Position(session, URL)
        self.Dismissal = Dismissal(session, URL)
        self.Education = Education(session, URL)


    @Request.All_pages
    @Request.Retry
    async def by_unit(self, **d):
        '''by_unit | Auth.User.by_unit'''
        url  = self.URL.get(self.URL.Auth.User.by_unit)
        json = Filters.Auth.User.by_unit(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def can(self, **d):
        '''can | Auth.User.can'''
        url  = self.URL.get(self.URL.Auth.User.can)
        json = Filters.Auth.User.can(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Auth.User.create'''
        url  = self.URL.get(self.URL.Auth.User.create)
        json = Filters.Auth.User.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def created(self, **d):
        '''created | Auth.User.created'''
        url  = self.URL.get(self.URL.Auth.User.created)
        json = Filters.Auth.User.created(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Auth.User.delete'''
        url  = self.URL.get(self.URL.Auth.User.delete)
        json = Filters.Auth.User.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def deleted(self, **d):
        '''deleted | Auth.User.deleted'''
        url  = self.URL.get(self.URL.Auth.User.deleted)
        json = Filters.Auth.User.deleted(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Auth.User.read'''
        url  = self.URL.get(self.URL.Auth.User.read)
        json = Filters.Auth.User.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def refresh(self, **d):
        '''refresh | Auth.User.refresh'''
        url  = self.URL.get(self.URL.Auth.User.refresh)
        json = Filters.Auth.User.refresh(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def search(self, **d):
        '''search | Auth.User.search'''
        url  = self.URL.get(self.URL.Auth.User.search)
        json = Filters.Auth.User.search(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def tachograph(self, **d):
        '''tachograph | Auth.User.tachograph'''
        url  = self.URL.get(self.URL.Auth.User.tachograph)
        json = Filters.Auth.User.tachograph(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Auth.User.to_list'''
        url  = self.URL.get(self.URL.Auth.User.to_list)
        json = Filters.Auth.User.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Auth.User.update'''
        url  = self.URL.get(self.URL.Auth.User.update)
        json = Filters.Auth.User.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def updated(self, **d):
        '''updated | Auth.User.updated'''
        url  = self.URL.get(self.URL.Auth.User.updated)
        json = Filters.Auth.User.updated(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Auth:
    '''Auth'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Permission = Permission(session, URL)
        self.Role = Role(session, URL)
        self.User = User(session, URL)


    @Request.All_pages
    @Request.Retry
    async def entity(self, **d):
        '''entity | Auth.entity'''
        url  = self.URL.get(self.URL.Auth.entity)
        json = Filters.Auth.entity(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def login(self, **d):
        '''login | Auth.login'''
        url  = self.URL.get(self.URL.Auth.login)
        json = Filters.Auth.login(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def logout(self, **d):
        '''logout | Auth.logout'''
        url  = self.URL.get(self.URL.Auth.logout)
        json = Filters.Auth.logout(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)