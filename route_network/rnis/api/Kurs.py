from ..filters import Filters
from ..request import Request

class Kurs:
    '''Pavilion'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Contract = Contract(session, URL)
        self.Repair = Repair(session, URL)
        self.Road = Road(session, URL)
        self.SKPDI = SKPDI(session, URL)
        self.STO = STO(session, URL)
        self.Situation = Situation(session, URL)
        self.TO = TO(session, URL)
        self.Task = Task(session, URL)
        self.Technocard = Technocard(session, URL)
        self.Fuel = Fuel(session, URL)
        self.Vehicle = Vehicle(session, URL)
        self.Waybill = Waybill(session, URL)


class ContractWork:
    '''Work'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Kurs.Contract.Work.create'''
        url  = self.URL.get(self.URL.Kurs.Contract.Work.create)
        json = Filters.Kurs.Contract.Work.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Kurs.Contract.Work.delete'''
        url  = self.URL.get(self.URL.Kurs.Contract.Work.delete)
        json = Filters.Kurs.Contract.Work.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Kurs.Contract.Work.read'''
        url  = self.URL.get(self.URL.Kurs.Contract.Work.read)
        json = Filters.Kurs.Contract.Work.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Kurs.Contract.Work.to_list'''
        url  = self.URL.get(self.URL.Kurs.Contract.Work.to_list)
        json = Filters.Kurs.Contract.Work.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Kurs.Contract.Work.update'''
        url  = self.URL.get(self.URL.Kurs.Contract.Work.update)
        json = Filters.Kurs.Contract.Work.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Contract:
    '''Contract'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Work = ContractWork(session, URL)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Kurs.Contract.create'''
        url  = self.URL.get(self.URL.Kurs.Contract.create)
        json = Filters.Kurs.Contract.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Kurs.Contract.delete'''
        url  = self.URL.get(self.URL.Kurs.Contract.delete)
        json = Filters.Kurs.Contract.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def driver_score(self, **d):
        '''driver_score | Kurs.Contract.driver_score'''
        url  = self.URL.get(self.URL.Kurs.Contract.driver_score)
        json = Filters.Kurs.Contract.driver_score(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Kurs.Contract.read'''
        url  = self.URL.get(self.URL.Kurs.Contract.read)
        json = Filters.Kurs.Contract.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Kurs.Contract.to_list'''
        url  = self.URL.get(self.URL.Kurs.Contract.to_list)
        json = Filters.Kurs.Contract.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Kurs.Contract.update'''
        url  = self.URL.get(self.URL.Kurs.Contract.update)
        json = Filters.Kurs.Contract.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Repair:
    '''Repair'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Kurs.Repair.create'''
        url  = self.URL.get(self.URL.Kurs.Repair.create)
        json = Filters.Kurs.Repair.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Kurs.Repair.delete'''
        url  = self.URL.get(self.URL.Kurs.Repair.delete)
        json = Filters.Kurs.Repair.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Kurs.Repair.read'''
        url  = self.URL.get(self.URL.Kurs.Repair.read)
        json = Filters.Kurs.Repair.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Kurs.Repair.to_list'''
        url  = self.URL.get(self.URL.Kurs.Repair.to_list)
        json = Filters.Kurs.Repair.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Kurs.Repair.update'''
        url  = self.URL.get(self.URL.Kurs.Repair.update)
        json = Filters.Kurs.Repair.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Part:
    '''Part'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Kurs.Road.Part.create'''
        url  = self.URL.get(self.URL.Kurs.Road.Part.create)
        json = Filters.Kurs.Road.Part.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Kurs.Road.Part.delete'''
        url  = self.URL.get(self.URL.Kurs.Road.Part.delete)
        json = Filters.Kurs.Road.Part.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Kurs.Road.Part.read'''
        url  = self.URL.get(self.URL.Kurs.Road.Part.read)
        json = Filters.Kurs.Road.Part.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def repair(self, **d):
        '''repair | Kurs.Road.Part.repair'''
        url  = self.URL.get(self.URL.Kurs.Road.Part.repair)
        json = Filters.Kurs.Road.Part.repair(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Kurs.Road.Part.to_list'''
        url  = self.URL.get(self.URL.Kurs.Road.Part.to_list)
        json = Filters.Kurs.Road.Part.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Kurs.Road.Part.update'''
        url  = self.URL.get(self.URL.Kurs.Road.Part.update)
        json = Filters.Kurs.Road.Part.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Road:
    '''Road'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Part = Part(session, URL)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Kurs.Road.create'''
        url  = self.URL.get(self.URL.Kurs.Road.create)
        json = Filters.Kurs.Road.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Kurs.Road.delete'''
        url  = self.URL.get(self.URL.Kurs.Road.delete)
        json = Filters.Kurs.Road.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Kurs.Road.read'''
        url  = self.URL.get(self.URL.Kurs.Road.read)
        json = Filters.Kurs.Road.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Kurs.Road.to_list'''
        url  = self.URL.get(self.URL.Kurs.Road.to_list)
        json = Filters.Kurs.Road.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Kurs.Road.update'''
        url  = self.URL.get(self.URL.Kurs.Road.update)
        json = Filters.Kurs.Road.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class SKPDI:
    '''SKPDI'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def log(self, **d):
        '''log | Kurs.SKPDI.log'''
        url  = self.URL.get(self.URL.Kurs.SKPDI.log)
        json = Filters.Kurs.SKPDI.log(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def task(self, **d):
        '''task | Kurs.SKPDI.task'''
        url  = self.URL.get(self.URL.Kurs.SKPDI.task)
        json = Filters.Kurs.SKPDI.task(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Kurs.STO.Work.create'''
        url  = self.URL.get(self.URL.Kurs.STO.Work.create)
        json = Filters.Kurs.STO.Work.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Kurs.STO.Work.delete'''
        url  = self.URL.get(self.URL.Kurs.STO.Work.delete)
        json = Filters.Kurs.STO.Work.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Kurs.STO.Work.read'''
        url  = self.URL.get(self.URL.Kurs.STO.Work.read)
        json = Filters.Kurs.STO.Work.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Kurs.STO.Work.to_list'''
        url  = self.URL.get(self.URL.Kurs.STO.Work.to_list)
        json = Filters.Kurs.STO.Work.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Kurs.STO.Work.update'''
        url  = self.URL.get(self.URL.Kurs.STO.Work.update)
        json = Filters.Kurs.STO.Work.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class STO:
    '''STO'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Kurs.STO.create'''
        url  = self.URL.get(self.URL.Kurs.STO.create)
        json = Filters.Kurs.STO.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Kurs.STO.delete'''
        url  = self.URL.get(self.URL.Kurs.STO.delete)
        json = Filters.Kurs.STO.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Kurs.STO.read'''
        url  = self.URL.get(self.URL.Kurs.STO.read)
        json = Filters.Kurs.STO.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Kurs.STO.to_list'''
        url  = self.URL.get(self.URL.Kurs.STO.to_list)
        json = Filters.Kurs.STO.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Kurs.STO.update'''
        url  = self.URL.get(self.URL.Kurs.STO.update)
        json = Filters.Kurs.STO.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Situation:
    '''Situation'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Kurs.Situation.create'''
        url  = self.URL.get(self.URL.Kurs.Situation.create)
        json = Filters.Kurs.Situation.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Kurs.Situation.delete'''
        url  = self.URL.get(self.URL.Kurs.Situation.delete)
        json = Filters.Kurs.Situation.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Kurs.Situation.read'''
        url  = self.URL.get(self.URL.Kurs.Situation.read)
        json = Filters.Kurs.Situation.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Kurs.Situation.to_list'''
        url  = self.URL.get(self.URL.Kurs.Situation.to_list)
        json = Filters.Kurs.Situation.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Kurs.Situation.update'''
        url  = self.URL.get(self.URL.Kurs.Situation.update)
        json = Filters.Kurs.Situation.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class TO:
    '''TO'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Kurs.TO.create'''
        url  = self.URL.get(self.URL.Kurs.TO.create)
        json = Filters.Kurs.TO.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Kurs.TO.delete'''
        url  = self.URL.get(self.URL.Kurs.TO.delete)
        json = Filters.Kurs.TO.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Kurs.TO.read'''
        url  = self.URL.get(self.URL.Kurs.TO.read)
        json = Filters.Kurs.TO.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Kurs.TO.to_list'''
        url  = self.URL.get(self.URL.Kurs.TO.to_list)
        json = Filters.Kurs.TO.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Kurs.TO.update'''
        url  = self.URL.get(self.URL.Kurs.TO.update)
        json = Filters.Kurs.TO.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Template:
    '''Template'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Kurs.Task.Template.create'''
        url  = self.URL.get(self.URL.Kurs.Task.Template.create)
        json = Filters.Kurs.Task.Template.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Kurs.Task.Template.delete'''
        url  = self.URL.get(self.URL.Kurs.Task.Template.delete)
        json = Filters.Kurs.Task.Template.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Kurs.Task.Template.read'''
        url  = self.URL.get(self.URL.Kurs.Task.Template.read)
        json = Filters.Kurs.Task.Template.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Kurs.Task.Template.to_list'''
        url  = self.URL.get(self.URL.Kurs.Task.Template.to_list)
        json = Filters.Kurs.Task.Template.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Kurs.Task.Template.update'''
        url  = self.URL.get(self.URL.Kurs.Task.Template.update)
        json = Filters.Kurs.Task.Template.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Task:
    '''Task'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Template = Template(session, URL)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Kurs.Task.create'''
        url  = self.URL.get(self.URL.Kurs.Task.create)
        json = Filters.Kurs.Task.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def date(self, **d):
        '''date | Kurs.Task.date'''
        url  = self.URL.get(self.URL.Kurs.Task.date)
        json = Filters.Kurs.Task.date(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Kurs.Task.delete'''
        url  = self.URL.get(self.URL.Kurs.Task.delete)
        json = Filters.Kurs.Task.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Kurs.Task.read'''
        url  = self.URL.get(self.URL.Kurs.Task.read)
        json = Filters.Kurs.Task.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def repeat(self, **d):
        '''repeat | Kurs.Task.repeat'''
        url  = self.URL.get(self.URL.Kurs.Task.repeat)
        json = Filters.Kurs.Task.repeat(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Kurs.Task.to_list'''
        url  = self.URL.get(self.URL.Kurs.Task.to_list)
        json = Filters.Kurs.Task.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def unit(self, **d):
        '''unit | Kurs.Task.unit'''
        url  = self.URL.get(self.URL.Kurs.Task.unit)
        json = Filters.Kurs.Task.unit(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Kurs.Task.update'''
        url  = self.URL.get(self.URL.Kurs.Task.update)
        json = Filters.Kurs.Task.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def upload(self, **d):
        '''upload | Kurs.Task.upload'''
        url  = self.URL.get(self.URL.Kurs.Task.upload)
        json = Filters.Kurs.Task.upload(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def violation(self, **d):
        '''violation | Kurs.Task.violation'''
        url  = self.URL.get(self.URL.Kurs.Task.violation)
        json = Filters.Kurs.Task.violation(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def visit(self, **d):
        '''visit | Kurs.Task.visit'''
        url  = self.URL.get(self.URL.Kurs.Task.visit)
        json = Filters.Kurs.Task.visit(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Assign:
    '''Assign'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Kurs.Technocard.Assign.create'''
        url  = self.URL.get(self.URL.Kurs.Technocard.Assign.create)
        json = Filters.Kurs.Technocard.Assign.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Kurs.Technocard.Assign.delete'''
        url  = self.URL.get(self.URL.Kurs.Technocard.Assign.delete)
        json = Filters.Kurs.Technocard.Assign.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Kurs.Technocard.Assign.read'''
        url  = self.URL.get(self.URL.Kurs.Technocard.Assign.read)
        json = Filters.Kurs.Technocard.Assign.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Kurs.Technocard.Assign.to_list'''
        url  = self.URL.get(self.URL.Kurs.Technocard.Assign.to_list)
        json = Filters.Kurs.Technocard.Assign.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Kurs.Technocard.Assign.update'''
        url  = self.URL.get(self.URL.Kurs.Technocard.Assign.update)
        json = Filters.Kurs.Technocard.Assign.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Technocard:
    '''Technocard'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Assign = Assign(session, URL)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Kurs.Technocard.create'''
        url  = self.URL.get(self.URL.Kurs.Technocard.create)
        json = Filters.Kurs.Technocard.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Kurs.Technocard.delete'''
        url  = self.URL.get(self.URL.Kurs.Technocard.delete)
        json = Filters.Kurs.Technocard.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Kurs.Technocard.read'''
        url  = self.URL.get(self.URL.Kurs.Technocard.read)
        json = Filters.Kurs.Technocard.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Kurs.Technocard.to_list'''
        url  = self.URL.get(self.URL.Kurs.Technocard.to_list)
        json = Filters.Kurs.Technocard.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Kurs.Technocard.update'''
        url  = self.URL.get(self.URL.Kurs.Technocard.update)
        json = Filters.Kurs.Technocard.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Fuel:
    '''Fuel'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def event(self, **d):
        '''event | Kurs.Vehicle.Fuel.event'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.Fuel.event)
        json = Filters.Kurs.Vehicle.Fuel.event(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def level(self, **d):
        '''level | Kurs.Vehicle.Fuel.level'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.Fuel.level)
        json = Filters.Kurs.Vehicle.Fuel.level(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def recalc(self, **d):
        '''recalc | Kurs.Vehicle.Fuel.recalc'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.Fuel.recalc)
        json = Filters.Kurs.Vehicle.Fuel.recalc(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Mechanism:
    '''Mechanism'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Kurs.Vehicle.Mechanism.create'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.Mechanism.create)
        json = Filters.Kurs.Vehicle.Mechanism.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Kurs.Vehicle.Mechanism.delete'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.Mechanism.delete)
        json = Filters.Kurs.Vehicle.Mechanism.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Kurs.Vehicle.Mechanism.read'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.Mechanism.read)
        json = Filters.Kurs.Vehicle.Mechanism.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Kurs.Vehicle.Mechanism.to_list'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.Mechanism.to_list)
        json = Filters.Kurs.Vehicle.Mechanism.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Kurs.Vehicle.Mechanism.update'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.Mechanism.update)
        json = Filters.Kurs.Vehicle.Mechanism.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class VehicleWork:
    '''Mechanism'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Kurs.Vehicle.Work.create'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.Work.create)
        json = Filters.Kurs.Vehicle.Work.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Kurs.Vehicle.Work.delete'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.Work.delete)
        json = Filters.Kurs.Vehicle.Work.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Kurs.Vehicle.Work.read'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.Work.read)
        json = Filters.Kurs.Vehicle.Work.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Kurs.Vehicle.Work.to_list'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.Work.to_list)
        json = Filters.Kurs.Vehicle.Work.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Kurs.Vehicle.Work.update'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.Work.update)
        json = Filters.Kurs.Vehicle.Work.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Vehicle:
    '''Vehicle'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Mechanism = Mechanism(session, URL)
        self.Work = VehicleWork(session, URL)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Kurs.Vehicle.create'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.create)
        json = Filters.Kurs.Vehicle.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Kurs.Vehicle.delete'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.delete)
        json = Filters.Kurs.Vehicle.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Kurs.Vehicle.read'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.read)
        json = Filters.Kurs.Vehicle.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Kurs.Vehicle.to_list'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.to_list)
        json = Filters.Kurs.Vehicle.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Kurs.Vehicle.update'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.update)
        json = Filters.Kurs.Vehicle.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def upload(self, **d):
        '''upload | Kurs.Vehicle.upload'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.upload)
        json = Filters.Kurs.Vehicle.upload(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def upload_status(self, **d):
        '''upload_status | Kurs.Vehicle.upload_status'''
        url  = self.URL.get(self.URL.Kurs.Vehicle.upload_status)
        json = Filters.Kurs.Vehicle.upload_status(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Waybill:
    '''Waybill'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Kurs.Waybill.create'''
        url  = self.URL.get(self.URL.Kurs.Waybill.create)
        json = Filters.Kurs.Waybill.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Kurs.Waybill.delete'''
        url  = self.URL.get(self.URL.Kurs.Waybill.delete)
        json = Filters.Kurs.Waybill.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Kurs.Waybill.read'''
        url  = self.URL.get(self.URL.Kurs.Waybill.read)
        json = Filters.Kurs.Waybill.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Kurs.Waybill.to_list'''
        url  = self.URL.get(self.URL.Kurs.Waybill.to_list)
        json = Filters.Kurs.Waybill.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Kurs.Waybill.update'''
        url  = self.URL.get(self.URL.Kurs.Waybill.update)
        json = Filters.Kurs.Waybill.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)