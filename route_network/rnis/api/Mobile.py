from ..filters import Filters
from ..request import Request


class Bus:
    '''Bus'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Mobile.Bus.read'''
        url  = self.URL.get(self.URL.Mobile.Bus.read)
        json = Filters.Mobile.Bus.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def route(self, **d):
        '''route | Mobile.Bus.route'''
        url  = self.URL.get(self.URL.Mobile.Bus.route)
        json = Filters.Mobile.Bus.route(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def routing(self, **d):
        '''routing | Mobile.Bus.routing'''
        url  = self.URL.get(self.URL.Mobile.Bus.routing)
        json = Filters.Mobile.Bus.routing(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Mobile.Bus.to_list'''
        url  = self.URL.get(self.URL.Mobile.Bus.to_list)
        json = Filters.Mobile.Bus.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Contact:
    '''Contact'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Mobile.Contact.create'''
        url  = self.URL.get(self.URL.Mobile.Contact.create)
        json = Filters.Mobile.Contact.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Mobile.Contact.delete'''
        url  = self.URL.get(self.URL.Mobile.Contact.delete)
        json = Filters.Mobile.Contact.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Mobile.Contact.read'''
        url  = self.URL.get(self.URL.Mobile.Contact.read)
        json = Filters.Mobile.Contact.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Mobile.Contact.to_list'''
        url  = self.URL.get(self.URL.Mobile.Contact.to_list)
        json = Filters.Mobile.Contact.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Mobile.Contact.update'''
        url  = self.URL.get(self.URL.Mobile.Contact.update)
        json = Filters.Mobile.Contact.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Notification:
    '''Notification'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Mobile.Notification.create'''
        url  = self.URL.get(self.URL.Mobile.Notification.create)
        json = Filters.Mobile.Notification.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Mobile.Notification.delete'''
        url  = self.URL.get(self.URL.Mobile.Notification.delete)
        json = Filters.Mobile.Notification.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Mobile.Notification.to_list'''
        url  = self.URL.get(self.URL.Mobile.Notification.to_list)
        json = Filters.Mobile.Notification.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Mobile.Notification.update'''
        url  = self.URL.get(self.URL.Mobile.Notification.update)
        json = Filters.Mobile.Notification.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Page:
    '''Page'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Mobile.Page.read'''
        url  = self.URL.get(self.URL.Mobile.Page.read)
        json = Filters.Mobile.Page.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Mobile.Page.to_list'''
        url  = self.URL.get(self.URL.Mobile.Page.to_list)
        json = Filters.Mobile.Page.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Mobile.Page.update'''
        url  = self.URL.get(self.URL.Mobile.Page.update)
        json = Filters.Mobile.Page.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Path:
    '''Path'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Mobile.Path.create'''
        url  = self.URL.get(self.URL.Mobile.Path.create)
        json = Filters.Mobile.Path.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Mobile.Path.delete'''
        url  = self.URL.get(self.URL.Mobile.Path.delete)
        json = Filters.Mobile.Path.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Mobile.Path.read'''
        url  = self.URL.get(self.URL.Mobile.Path.read)
        json = Filters.Mobile.Path.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Mobile.Path.to_list'''
        url  = self.URL.get(self.URL.Mobile.Path.to_list)
        json = Filters.Mobile.Path.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Mobile.Path.update'''
        url  = self.URL.get(self.URL.Mobile.Path.update)
        json = Filters.Mobile.Path.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Route:
    '''Route'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Mobile.Route.create'''
        url  = self.URL.get(self.URL.Mobile.Route.create)
        json = Filters.Mobile.Route.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Mobile.Route.delete'''
        url  = self.URL.get(self.URL.Mobile.Route.delete)
        json = Filters.Mobile.Route.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Mobile.Route.to_list'''
        url  = self.URL.get(self.URL.Mobile.Route.to_list)
        json = Filters.Mobile.Route.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class StopPoint:
    '''StopPoint'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def route(self, **d):
        '''route | Mobile.StopPoint.route'''
        url  = self.URL.get(self.URL.Mobile.StopPoint.route)
        json = Filters.Mobile.StopPoint.route(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Mobile.StopPoint.to_list'''
        url  = self.URL.get(self.URL.Mobile.StopPoint.to_list)
        json = Filters.Mobile.StopPoint.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Confirm:
    '''Confirm'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def check(self, **d):
        '''check | Mobile.User.Confirm.check'''
        url  = self.URL.get(self.URL.Mobile.User.Confirm.check)
        json = Filters.Mobile.User.Confirm.check(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def send(self, **d):
        '''send | Mobile.User.Confirm.send'''
        url  = self.URL.get(self.URL.Mobile.User.Confirm.send)
        json = Filters.Mobile.User.Confirm.send(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class User:
    '''User'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Confirm = Confirm(session, URL)


    @Request.All_pages
    @Request.Retry
    async def login(self, **d):
        '''login | Mobile.User.login'''
        url  = self.URL.get(self.URL.Mobile.User.login)
        json = Filters.Mobile.User.login(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def login_by_email(self, **d):
        '''login_by_email | Mobile.User.login_by_email'''
        url  = self.URL.get(self.URL.Mobile.User.login_by_email)
        json = Filters.Mobile.User.login_by_email(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Mobile.User.read'''
        url  = self.URL.get(self.URL.Mobile.User.read)
        json = Filters.Mobile.User.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def register(self, **d):
        '''register | Mobile.User.register'''
        url  = self.URL.get(self.URL.Mobile.User.register)
        json = Filters.Mobile.User.register(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Mobile.User.update'''
        url  = self.URL.get(self.URL.Mobile.User.update)
        json = Filters.Mobile.User.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update_push_token(self, **d):
        '''update_push_token | Mobile.User.update_push_token'''
        url  = self.URL.get(self.URL.Mobile.User.update_push_token)
        json = Filters.Mobile.User.update_push_token(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Mobile:
    '''Mobile'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Bus = Bus(session, URL)
        self.Contact = Contact(session, URL)
        self.Notification = Notification(session, URL)
        self.Page = Page(session, URL)
        self.Path = Path(session, URL)
        self.Route = Route(session, URL)
        self.StopPoint = StopPoint(session, URL)
        self.User = User(session, URL)


    @Request.All_pages
    @Request.Retry
    async def complaint(self, **d):
        '''complaint | Mobile.complaint'''
        url  = self.URL.get(self.URL.Mobile.complaint)
        json = Filters.Mobile.complaint(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def favorite(self, **d):
        '''favorite | Mobile.favorite'''
        url  = self.URL.get(self.URL.Mobile.favorite)
        json = Filters.Mobile.favorite(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def feedback(self, **d):
        '''feedback | Mobile.feedback'''
        url  = self.URL.get(self.URL.Mobile.feedback)
        json = Filters.Mobile.feedback(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def routing(self, **d):
        '''routing | Mobile.routing'''
        url  = self.URL.get(self.URL.Mobile.routing)
        json = Filters.Mobile.routing(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def search(self, **d):
        '''search | Mobile.search'''
        url  = self.URL.get(self.URL.Mobile.search)
        json = Filters.Mobile.search(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)