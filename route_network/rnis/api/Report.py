from ..filters import Filters
from ..request import Request


class Schedule:
    '''Schedule'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Report.Schedule.create'''
        url  = self.URL.get(self.URL.Report.Schedule.create)
        json = Filters.Report.Schedule.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Report.Schedule.delete'''
        url  = self.URL.get(self.URL.Report.Schedule.delete)
        json = Filters.Report.Schedule.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Report.Schedule.read'''
        url  = self.URL.get(self.URL.Report.Schedule.read)
        json = Filters.Report.Schedule.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Report.Schedule.to_list'''
        url  = self.URL.get(self.URL.Report.Schedule.to_list)
        json = Filters.Report.Schedule.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Report.Schedule.update'''
        url  = self.URL.get(self.URL.Report.Schedule.update)
        json = Filters.Report.Schedule.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Tablet:
    '''Tablet'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def kiutr(self, **d):
        '''kiutr | Report.Tablet.kiutr'''
        url  = self.URL.get(self.URL.Report.Tablet.kiutr)
        json = Filters.Report.Tablet.kiutr(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def summary(self, **d):
        '''summary | Report.Tablet.summary'''
        url  = self.URL.get(self.URL.Report.Tablet.summary)
        json = Filters.Report.Tablet.summary(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def unit(self, **d):
        '''unit | Report.Tablet.unit'''
        url  = self.URL.get(self.URL.Report.Tablet.unit)
        json = Filters.Report.Tablet.unit(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Template:
    '''Template'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Report.Template.delete'''
        url  = self.URL.get(self.URL.Report.Template.delete)
        json = Filters.Report.Template.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Report.Template.to_list'''
        url  = self.URL.get(self.URL.Report.Template.to_list)
        json = Filters.Report.Template.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Report:
    '''Report'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Schedule = Schedule(session, URL)
        self.Tablet   = Tablet(session, URL)
        self.Template = Template(session, URL)


    @Request.All_pages
    @Request.Retry
    async def available(self, **d):
        '''available | Report.available'''
        url  = self.URL.get(self.URL.Report.available)
        json = Filters.Report.available(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Report.create'''
        url  = self.URL.get(self.URL.Report.create)
        json = Filters.Report.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def integration_log(self, **d):
        '''integration_log | Report.integration_log'''
        url  = self.URL.get(self.URL.Report.integration_log)
        json = Filters.Report.integration_log(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def parameter(self, **d):
        '''parameter | Report.parameter'''
        url  = self.URL.get(self.URL.Report.parameter)
        json = Filters.Report.parameter(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Report.to_list'''
        url  = self.URL.get(self.URL.Report.to_list)
        json = Filters.Report.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)