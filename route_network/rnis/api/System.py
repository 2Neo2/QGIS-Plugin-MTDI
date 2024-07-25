from ..filters import Filters
from ..request import Request


class Activity:
    '''Activity'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def online(self, **d):
        '''online | System.Activity.online'''
        url  = self.URL.get(self.URL.System.Activity.online)
        json = Filters.System.Activity.online(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def store(self, **d):
        '''store | System.Activity.store'''
        url  = self.URL.get(self.URL.System.Activity.store)
        json = Filters.System.Activity.store(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Audit:
    '''Audit'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def search(self, **d):
        '''search | System.Audit.search'''
        url  = self.URL.get(self.URL.System.Audit.search)
        json = Filters.System.Audit.search(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def store(self, **d):
        '''store | System.Audit.store'''
        url  = self.URL.get(self.URL.System.Audit.store)
        json = Filters.System.Audit.store(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Entity:
    '''Entity'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def block(self, **d):
        '''block | System.Entity.block'''
        url  = self.URL.get(self.URL.System.Entity.block)
        json = Filters.System.Entity.block(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def is_block(self, **d):
        '''is_block | System.Entity.is_block'''
        url  = self.URL.get(self.URL.System.Entity.is_block)
        json = Filters.System.Entity.is_block(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def name(self, **d):
        '''name | System.Entity.name'''
        url  = self.URL.get(self.URL.System.Entity.name)
        json = Filters.System.Entity.name(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def unblock(self, **d):
        '''unblock | System.Entity.unblock'''
        url  = self.URL.get(self.URL.System.Entity.unblock)
        json = Filters.System.Entity.unblock(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Log:
    '''Log'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def code(self, **d):
        '''code | System.Log.code'''
        url  = self.URL.get(self.URL.System.Log.code)
        json = Filters.System.Log.code(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def search(self, **d):
        '''search | System.Log.search'''
        url  = self.URL.get(self.URL.System.Log.search)
        json = Filters.System.Log.search(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def store(self, **d):
        '''store | System.Log.store'''
        url  = self.URL.get(self.URL.System.Log.store)
        json = Filters.System.Log.store(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Maintenance:
    '''Maintenance'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def status(self, **d):
        '''status | System.Maintenance.status'''
        url  = self.URL.get(self.URL.System.Maintenance.status)
        json = Filters.System.Maintenance.status(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def time(self, **d):
        '''time | System.Maintenance.time'''
        url  = self.URL.get(self.URL.System.Maintenance.time)
        json = Filters.System.Maintenance.time(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Message:
    '''Message'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | System.Message.create'''
        url  = self.URL.get(self.URL.System.Message.create)
        json = Filters.System.Message.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | System.Message.delete'''
        url  = self.URL.get(self.URL.System.Message.delete)
        json = Filters.System.Message.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | System.Message.to_list'''
        url  = self.URL.get(self.URL.System.Message.to_list)
        json = Filters.System.Message.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | System.Message.update'''
        url  = self.URL.get(self.URL.System.Message.update)
        json = Filters.System.Message.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Schema:
    '''Schema'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def store(self, **d):
        '''store | System.Schema.store'''
        url  = self.URL.get(self.URL.System.Schema.store)
        json = Filters.System.Schema.store(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | System.Schema.update'''
        url  = self.URL.get(self.URL.System.Schema.update)
        json = Filters.System.Schema.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Table:
    '''Table'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | System.Table.create'''
        url  = self.URL.get(self.URL.System.Table.create)
        json = Filters.System.Table.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | System.Table.read'''
        url  = self.URL.get(self.URL.System.Table.read)
        json = Filters.System.Table.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | System.Table.update'''
        url  = self.URL.get(self.URL.System.Table.update)
        json = Filters.System.Table.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Tooltip:
    '''Tooltip'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | System.Tooltip.to_list'''
        url  = self.URL.get(self.URL.System.Tooltip.to_list)
        json = Filters.System.Tooltip.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | System.Tooltip.update'''
        url  = self.URL.get(self.URL.System.Tooltip.update)
        json = Filters.System.Tooltip.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Trash:
    '''Trash'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def search(self, **d):
        '''search | System.Trash.search'''
        url  = self.URL.get(self.URL.System.Trash.search)
        json = Filters.System.Trash.search(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def store(self, **d):
        '''store | System.Trash.store'''
        url  = self.URL.get(self.URL.System.Trash.store)
        json = Filters.System.Trash.store(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class System:
    '''System'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Activity = Activity(session, URL)
        self.Audit = Audit(session, URL)
        self.Entity = Entity(session, URL)
        self.Log = Log(session, URL)
        self.Maintenance = Maintenance(session, URL)
        self.Message = Message(session, URL)
        self.Schema = Schema(session, URL)
        self.Table = Table(session, URL)
        self.Tooltip = Tooltip(session, URL)
        self.Trash = Trash(session, URL)


    @Request.All_pages
    @Request.Retry
    async def down(self, **d):
        '''down | System.down'''
        url  = self.URL.get(self.URL.System.down)
        json = Filters.System.down(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def status(self, **d):
        '''status | System.status'''
        url  = self.URL.get(self.URL.System.status)
        json = Filters.System.status(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def up(self, **d):
        '''up | System.up'''
        url  = self.URL.get(self.URL.System.up)
        json = Filters.System.up(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def version(self, **d):
        '''version | System.version'''
        url  = self.URL.get(self.URL.System.version)
        json = Filters.System.version(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)