from ..filters import Filters
from ..request import Request


class Event:
    '''Event'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Notification.Event.create'''
        url  = self.URL.get(self.URL.Notification.Event.create)
        json = Filters.Notification.Event.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Notification.Event.delete'''
        url  = self.URL.get(self.URL.Notification.Event.delete)
        json = Filters.Notification.Event.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Notification.Event.read'''
        url  = self.URL.get(self.URL.Notification.Event.read)
        json = Filters.Notification.Event.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def send(self, **d):
        '''send | Notification.Event.send'''
        url  = self.URL.get(self.URL.Notification.Event.send)
        json = Filters.Notification.Event.send(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Notification.Event.to_list'''
        url  = self.URL.get(self.URL.Notification.Event.to_list)
        json = Filters.Notification.Event.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Notification.Event.update'''
        url  = self.URL.get(self.URL.Notification.Event.update)
        json = Filters.Notification.Event.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class EventRuleNotification:
    '''Notification'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Notification.EventRule.Notification.create'''
        url  = self.URL.get(self.URL.Notification.EventRule.Notification.create)
        json = Filters.Notification.EventRule.Notification.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Notification.EventRule.Notification.delete'''
        url  = self.URL.get(self.URL.Notification.EventRule.Notification.delete)
        json = Filters.Notification.EventRule.Notification.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Notification.EventRule.Notification.read'''
        url  = self.URL.get(self.URL.Notification.EventRule.Notification.read)
        json = Filters.Notification.EventRule.Notification.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Notification.EventRule.Notification.to_list'''
        url  = self.URL.get(self.URL.Notification.EventRule.Notification.to_list)
        json = Filters.Notification.EventRule.Notification.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Notification.EventRule.Notification.update'''
        url  = self.URL.get(self.URL.Notification.EventRule.Notification.update)
        json = Filters.Notification.EventRule.Notification.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class EventRule:
    '''EventRule'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL 
        self.Notification = EventRuleNotification(session, URL)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Notification.EventRule.create'''
        url  = self.URL.get(self.URL.Notification.EventRule.create)
        json = Filters.Notification.EventRule.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Notification.EventRule.delete'''
        url  = self.URL.get(self.URL.Notification.EventRule.delete)
        json = Filters.Notification.EventRule.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def event(self, **d):
        '''event | Notification.EventRule.event'''
        url  = self.URL.get(self.URL.Notification.EventRule.event)
        json = Filters.Notification.EventRule.event(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Notification.EventRule.read'''
        url  = self.URL.get(self.URL.Notification.EventRule.read)
        json = Filters.Notification.EventRule.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Notification.EventRule.to_list'''
        url  = self.URL.get(self.URL.Notification.EventRule.to_list)
        json = Filters.Notification.EventRule.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Notification.EventRule.update'''
        url  = self.URL.get(self.URL.Notification.EventRule.update)
        json = Filters.Notification.EventRule.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Mailing:
    '''Mailing'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Notification.Mailing.create'''
        url  = self.URL.get(self.URL.Notification.Mailing.create)
        json = Filters.Notification.Mailing.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Notification.Mailing.delete'''
        url  = self.URL.get(self.URL.Notification.Mailing.delete)
        json = Filters.Notification.Mailing.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Notification.Mailing.read'''
        url  = self.URL.get(self.URL.Notification.Mailing.read)
        json = Filters.Notification.Mailing.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Notification.Mailing.to_list'''
        url  = self.URL.get(self.URL.Notification.Mailing.to_list)
        json = Filters.Notification.Mailing.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Notification.Mailing.update'''
        url  = self.URL.get(self.URL.Notification.Mailing.update)
        json = Filters.Notification.Mailing.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class SpeedViolation:
    '''SpeedViolation'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def driver(self, **d):
        '''driver | Notification.SpeedViolation.driver'''
        url  = self.URL.get(self.URL.Notification.SpeedViolation.driver)
        json = Filters.Notification.SpeedViolation.driver(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def journal(self, **d):
        '''journal | Notification.SpeedViolation.journal'''
        url  = self.URL.get(self.URL.Notification.SpeedViolation.journal)
        json = Filters.Notification.SpeedViolation.journal(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def summary(self, **d):
        '''summary | Notification.SpeedViolation.summary'''
        url  = self.URL.get(self.URL.Notification.SpeedViolation.summary)
        json = Filters.Notification.SpeedViolation.summary(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Notification.SpeedViolation.to_list'''
        url  = self.URL.get(self.URL.Notification.SpeedViolation.to_list)
        json = Filters.Notification.SpeedViolation.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class User:
    '''User'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Notification.User.create'''
        url  = self.URL.get(self.URL.Notification.User.create)
        json = Filters.Notification.User.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Notification.User.delete'''
        url  = self.URL.get(self.URL.Notification.User.delete)
        json = Filters.Notification.User.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Notification.User.read'''
        url  = self.URL.get(self.URL.Notification.User.read)
        json = Filters.Notification.User.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Notification.User.to_list'''
        url  = self.URL.get(self.URL.Notification.User.to_list)
        json = Filters.Notification.User.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Notification.User.update'''
        url  = self.URL.get(self.URL.Notification.User.update)
        json = Filters.Notification.User.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Notification:
    '''Notification'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Event = Event(session, URL)
        self.EventRule = EventRule(session, URL)
        self.Mailing = Mailing(session, URL)
        self.SpeedViolation = SpeedViolation(session, URL)
        self.User = User(session, URL)


    @Request.All_pages
    @Request.Retry
    async def count(self, **d):
        '''count | Notification.count'''
        url  = self.URL.get(self.URL.Notification.count)
        json = Filters.Notification.count(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Notification.create'''
        url  = self.URL.get(self.URL.Notification.create)
        json = Filters.Notification.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Notification.read'''
        url  = self.URL.get(self.URL.Notification.read)
        json = Filters.Notification.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def send(self, **d):
        '''send | Notification.send'''
        url  = self.URL.get(self.URL.Notification.send)
        json = Filters.Notification.send(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Notification.to_list'''
        url  = self.URL.get(self.URL.Notification.to_list)
        json = Filters.Notification.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)