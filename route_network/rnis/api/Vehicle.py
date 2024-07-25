from ..filters import Filters
from ..request import Request


class Link:
    '''Link'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Vehicle.BNSO.Link.create'''
        url  = self.URL.get(self.URL.Vehicle.BNSO.Link.create)
        json = Filters.Vehicle.BNSO.Link.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Vehicle.BNSO.Link.delete'''
        url  = self.URL.get(self.URL.Vehicle.BNSO.Link.delete)
        json = Filters.Vehicle.BNSO.Link.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Vehicle.BNSO.Link.read'''
        url  = self.URL.get(self.URL.Vehicle.BNSO.Link.read)
        json = Filters.Vehicle.BNSO.Link.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Vehicle.BNSO.Link.update'''
        url  = self.URL.get(self.URL.Vehicle.BNSO.Link.update)
        json = Filters.Vehicle.BNSO.Link.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class BNSO:
    '''BNSO'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Link = Link(session, URL)


    @Request.All_pages
    @Request.Retry
    async def check(self, **d):
        '''check | Vehicle.BNSO.check'''
        url  = self.URL.get(self.URL.Vehicle.BNSO.check)
        json = Filters.Vehicle.BNSO.check(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Vehicle.BNSO.create'''
        url  = self.URL.get(self.URL.Vehicle.BNSO.create)
        json = Filters.Vehicle.BNSO.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Vehicle.BNSO.delete'''
        url  = self.URL.get(self.URL.Vehicle.BNSO.delete)
        json = Filters.Vehicle.BNSO.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def period(self, **d):
        '''period | Vehicle.BNSO.period'''
        url  = self.URL.get(self.URL.Vehicle.BNSO.period)
        json = Filters.Vehicle.BNSO.period(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Vehicle.BNSO.read'''
        url  = self.URL.get(self.URL.Vehicle.BNSO.read)
        json = Filters.Vehicle.BNSO.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def search(self, **d):
        '''search | Vehicle.BNSO.search'''
        url  = self.URL.get(self.URL.Vehicle.BNSO.search)
        json = Filters.Vehicle.BNSO.search(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Vehicle.BNSO.to_list'''
        url  = self.URL.get(self.URL.Vehicle.BNSO.to_list)
        json = Filters.Vehicle.BNSO.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Vehicle.BNSO.update'''
        url  = self.URL.get(self.URL.Vehicle.BNSO.update)
        json = Filters.Vehicle.BNSO.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Event:
    '''Event'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Vehicle.Event.create'''
        url  = self.URL.get(self.URL.Vehicle.Event.create)
        json = Filters.Vehicle.Event.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Vehicle.Event.to_list'''
        url  = self.URL.get(self.URL.Vehicle.Event.to_list)
        json = Filters.Vehicle.Event.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Template:
    '''Template'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Vehicle.Graduation.Template.create'''
        url  = self.URL.get(self.URL.Vehicle.Graduation.Template.create)
        json = Filters.Vehicle.Graduation.Template.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Vehicle.Graduation.Template.delete'''
        url  = self.URL.get(self.URL.Vehicle.Graduation.Template.delete)
        json = Filters.Vehicle.Graduation.Template.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Vehicle.Graduation.Template.read'''
        url  = self.URL.get(self.URL.Vehicle.Graduation.Template.read)
        json = Filters.Vehicle.Graduation.Template.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Vehicle.Graduation.Template.to_list'''
        url  = self.URL.get(self.URL.Vehicle.Graduation.Template.to_list)
        json = Filters.Vehicle.Graduation.Template.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Vehicle.Graduation.Template.update'''
        url  = self.URL.get(self.URL.Vehicle.Graduation.Template.update)
        json = Filters.Vehicle.Graduation.Template.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Graduation:
    '''Graduation'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Template = Template(session, URL)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Vehicle.Graduation.create'''
        url  = self.URL.get(self.URL.Vehicle.Graduation.create)
        json = Filters.Vehicle.Graduation.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Vehicle.Graduation.delete'''
        url  = self.URL.get(self.URL.Vehicle.Graduation.delete)
        json = Filters.Vehicle.Graduation.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Vehicle.Graduation.read'''
        url  = self.URL.get(self.URL.Vehicle.Graduation.read)
        json = Filters.Vehicle.Graduation.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Vehicle.Graduation.to_list'''
        url  = self.URL.get(self.URL.Vehicle.Graduation.to_list)
        json = Filters.Vehicle.Graduation.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Vehicle.Graduation.update'''
        url  = self.URL.get(self.URL.Vehicle.Graduation.update)
        json = Filters.Vehicle.Graduation.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Port:
    '''Port'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Vehicle.Port.create'''
        url  = self.URL.get(self.URL.Vehicle.Port.create)
        json = Filters.Vehicle.Port.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Vehicle.Port.delete'''
        url  = self.URL.get(self.URL.Vehicle.Port.delete)
        json = Filters.Vehicle.Port.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Vehicle.Port.read'''
        url  = self.URL.get(self.URL.Vehicle.Port.read)
        json = Filters.Vehicle.Port.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Vehicle.Port.to_list'''
        url  = self.URL.get(self.URL.Vehicle.Port.to_list)
        json = Filters.Vehicle.Port.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Vehicle.Port.update'''
        url  = self.URL.get(self.URL.Vehicle.Port.update)
        json = Filters.Vehicle.Port.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Status:
    '''Status'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Vehicle.Status.update'''
        url  = self.URL.get(self.URL.Vehicle.Status.update)
        json = Filters.Vehicle.Status.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update_many(self, **d):
        '''update_many | Vehicle.Status.update_many'''
        url  = self.URL.get(self.URL.Vehicle.Status.update_many)
        json = Filters.Vehicle.Status.update_many(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Vehicle:
    '''Vehicle'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.BNSO = BNSO(session, URL)
        self.Event = Event(session, URL)
        self.Graduation = Graduation(session, URL)
        self.Port = Port(session, URL)
        self.Status = Status(session, URL)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Vehicle.create'''
        url  = self.URL.get(self.URL.Vehicle.create)
        json = Filters.Vehicle.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Vehicle.delete'''
        url  = self.URL.get(self.URL.Vehicle.delete)
        json = Filters.Vehicle.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def idle(self, **d):
        '''idle | Vehicle.idle'''
        url  = self.URL.get(self.URL.Vehicle.idle)
        json = Filters.Vehicle.idle(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def malfunction(self, **d):
        '''malfunction | Vehicle.malfunction'''
        url  = self.URL.get(self.URL.Vehicle.malfunction)
        json = Filters.Vehicle.malfunction(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def portal(self, **d):
        '''portal | Vehicle.portal'''
        url  = self.URL.get(self.URL.Vehicle.portal)
        json = Filters.Vehicle.portal(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Vehicle.read'''
        url  = self.URL.get(self.URL.Vehicle.read)
        json = Filters.Vehicle.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def retrospective(self, **d):
        '''retrospective | Vehicle.retrospective'''
        url  = self.URL.get(self.URL.Vehicle.retrospective)
        json = Filters.Vehicle.retrospective(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def search(self, **d):
        '''search | Vehicle.search'''
        url  = self.URL.get(self.URL.Vehicle.search)
        json = Filters.Vehicle.search(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Vehicle.to_list'''
        url  = self.URL.get(self.URL.Vehicle.to_list)
        json = Filters.Vehicle.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def unit(self, **d):
        '''unit | Vehicle.unit'''
        url  = self.URL.get(self.URL.Vehicle.unit)
        json = Filters.Vehicle.unit(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Vehicle.update'''
        url  = self.URL.get(self.URL.Vehicle.update)
        json = Filters.Vehicle.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def upload(self, **d):
        '''upload | Vehicle.upload'''
        url  = self.URL.get(self.URL.Vehicle.upload)
        json = Filters.Vehicle.upload(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def upload_status(self, **d):
        '''upload_status | Vehicle.upload_status'''
        url  = self.URL.get(self.URL.Vehicle.upload_status)
        json = Filters.Vehicle.upload_status(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)