from ..filters import Filters
from ..request import Request


class Warnings:
    '''Warnings'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Portal.Agreement.Warnings.create'''
        url  = self.URL.get(self.URL.Portal.Agreement.Warnings.create)
        json = Filters.Portal.Agreement.Warnings.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Portal.Agreement.Warnings.to_list'''
        url  = self.URL.get(self.URL.Portal.Agreement.Warnings.to_list)
        json = Filters.Portal.Agreement.Warnings.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Portal.Agreement.Warnings.update'''
        url  = self.URL.get(self.URL.Portal.Agreement.Warnings.update)
        json = Filters.Portal.Agreement.Warnings.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Agreement:
    '''Agreement'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Warnings = Warnings(session, URL)


    @Request.All_pages
    @Request.Retry
    async def document(self, **d):
        '''document | Portal.Agreement.document'''
        url  = self.URL.get(self.URL.Portal.Agreement.document)
        json = Filters.Portal.Agreement.document(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Portal.Agreement.to_list'''
        url  = self.URL.get(self.URL.Portal.Agreement.to_list)
        json = Filters.Portal.Agreement.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Portal.Agreement.update'''
        url  = self.URL.get(self.URL.Portal.Agreement.update)
        json = Filters.Portal.Agreement.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Captcha:
    '''Captcha'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Portal.Captcha.read'''
        url  = self.URL.get(self.URL.Portal.Captcha.read)
        json = Filters.Portal.Captcha.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def validate(self, **d):
        '''validate | Portal.Captcha.validate'''
        url  = self.URL.get(self.URL.Portal.Captcha.validate)
        json = Filters.Portal.Captcha.validate(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Confirm:
    '''Confirm'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Portal.Confirm.create'''
        url  = self.URL.get(self.URL.Portal.Confirm.create)
        json = Filters.Portal.Confirm.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Portal.Confirm.read'''
        url  = self.URL.get(self.URL.Portal.Confirm.read)
        json = Filters.Portal.Confirm.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Portal.Confirm.to_list'''
        url  = self.URL.get(self.URL.Portal.Confirm.to_list)
        json = Filters.Portal.Confirm.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def unit(self, **d):
        '''unit | Portal.Confirm.unit'''
        url  = self.URL.get(self.URL.Portal.Confirm.unit)
        json = Filters.Portal.Confirm.unit(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Portal.Confirm.update'''
        url  = self.URL.get(self.URL.Portal.Confirm.update)
        json = Filters.Portal.Confirm.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class FAQ:
    '''FAQ'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Portal.FAQ.create'''
        url  = self.URL.get(self.URL.Portal.FAQ.create)
        json = Filters.Portal.FAQ.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Portal.FAQ.delete'''
        url  = self.URL.get(self.URL.Portal.FAQ.delete)
        json = Filters.Portal.FAQ.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Portal.FAQ.read'''
        url  = self.URL.get(self.URL.Portal.FAQ.read)
        json = Filters.Portal.FAQ.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Portal.FAQ.to_list'''
        url  = self.URL.get(self.URL.Portal.FAQ.to_list)
        json = Filters.Portal.FAQ.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Portal.FAQ.update'''
        url  = self.URL.get(self.URL.Portal.FAQ.update)
        json = Filters.Portal.FAQ.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class News:
    '''News'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Portal.News.create'''
        url  = self.URL.get(self.URL.Portal.News.create)
        json = Filters.Portal.News.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Portal.News.delete'''
        url  = self.URL.get(self.URL.Portal.News.delete)
        json = Filters.Portal.News.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Portal.News.read'''
        url  = self.URL.get(self.URL.Portal.News.read)
        json = Filters.Portal.News.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def tag(self, **d):
        '''tag | Portal.News.tag'''
        url  = self.URL.get(self.URL.Portal.News.tag)
        json = Filters.Portal.News.tag(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Portal.News.to_list'''
        url  = self.URL.get(self.URL.Portal.News.to_list)
        json = Filters.Portal.News.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Portal.News.update'''
        url  = self.URL.get(self.URL.Portal.News.update)
        json = Filters.Portal.News.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Page:
    '''Page'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Portal.Page.create'''
        url  = self.URL.get(self.URL.Portal.Page.create)
        json = Filters.Portal.Page.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Portal.Page.delete'''
        url  = self.URL.get(self.URL.Portal.Page.delete)
        json = Filters.Portal.Page.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Portal.Page.read'''
        url  = self.URL.get(self.URL.Portal.Page.read)
        json = Filters.Portal.Page.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Portal.Page.to_list'''
        url  = self.URL.get(self.URL.Portal.Page.to_list)
        json = Filters.Portal.Page.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Portal.Page.update'''
        url  = self.URL.get(self.URL.Portal.Page.update)
        json = Filters.Portal.Page.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Register:
    '''Register'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def check(self, **d):
        '''check | Portal.Register.check'''
        url  = self.URL.get(self.URL.Portal.Register.check)
        json = Filters.Portal.Register.check(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Portal.Register.create'''
        url  = self.URL.get(self.URL.Portal.Register.create)
        json = Filters.Portal.Register.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Portal.Register.read'''
        url  = self.URL.get(self.URL.Portal.Register.read)
        json = Filters.Portal.Register.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Portal.Register.to_list'''
        url  = self.URL.get(self.URL.Portal.Register.to_list)
        json = Filters.Portal.Register.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Portal.Register.update'''
        url  = self.URL.get(self.URL.Portal.Register.update)
        json = Filters.Portal.Register.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class TemplateDocument:
    '''TemplateDocument'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Portal.TemplateDocument.create'''
        url  = self.URL.get(self.URL.Portal.TemplateDocument.create)
        json = Filters.Portal.TemplateDocument.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def document(self, **d):
        '''document | Portal.TemplateDocument.document'''
        url  = self.URL.get(self.URL.Portal.TemplateDocument.document)
        json = Filters.Portal.TemplateDocument.document(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def next_version(self, **d):
        '''next_version | Portal.TemplateDocument.next_version'''
        url  = self.URL.get(self.URL.Portal.TemplateDocument.next_version)
        json = Filters.Portal.TemplateDocument.next_version(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Portal.TemplateDocument.read'''
        url  = self.URL.get(self.URL.Portal.TemplateDocument.read)
        json = Filters.Portal.TemplateDocument.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Portal.TemplateDocument.to_list'''
        url  = self.URL.get(self.URL.Portal.TemplateDocument.to_list)
        json = Filters.Portal.TemplateDocument.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Portal.TemplateDocument.update'''
        url  = self.URL.get(self.URL.Portal.TemplateDocument.update)
        json = Filters.Portal.TemplateDocument.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Portal:
    '''Portal'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Agreement = Agreement(session, URL)
        self.Captcha = Captcha(session, URL)
        self.Confirm = Confirm(session, URL)
        self.FAQ = FAQ(session, URL)
        self.News = News(session, URL)
        self.Page = Page(session, URL)
        self.Register = Register(session, URL)
        self.TemplateDocument = TemplateDocument(session, URL)


    @Request.All_pages
    @Request.Retry
    async def feedback(self, **d):
        '''feedback | Portal.feedback'''
        url  = self.URL.get(self.URL.Portal.feedback)
        json = Filters.Portal.feedback(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def login(self, **d):
        '''login | Portal.login'''
        url  = self.URL.get(self.URL.Portal.login)
        json = Filters.Portal.login(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)