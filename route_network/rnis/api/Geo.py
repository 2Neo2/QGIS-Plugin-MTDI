from ..filters import Filters
from ..request import Request


class Geo:
    '''Pavilion'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.BusStop = BusStop(session, URL)
        self.Contract = Contract(session, URL)
        self.Configuration = Configuration(session, URL)
        self.Display = Display(session, URL)
        self.Layer = Layer(session, URL)
        self.Object = Object(session, URL)
        self.Order = Order(session, URL)
        self.Route = Route(session, URL)
        self.Schedule = Schedule(session, URL)
        self.Service = Service(session, URL)
        self.TerritorialEntity = TerritorialEntity(session, URL)
        self.Violation = Violation(session, URL)


class Pavilion:
    '''Pavilion'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.BusStop.Pavilion.create'''
        url  = self.URL.get(self.URL.Geo.BusStop.Pavilion.create)
        json = Filters.Geo.BusStop.Pavilion.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Geo.BusStop.Pavilion.delete'''
        url  = self.URL.get(self.URL.Geo.BusStop.Pavilion.delete)
        json = Filters.Geo.BusStop.Pavilion.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.BusStop.Pavilion.read'''
        url  = self.URL.get(self.URL.Geo.BusStop.Pavilion.read)
        json = Filters.Geo.BusStop.Pavilion.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.BusStop.Pavilion.to_list'''
        url  = self.URL.get(self.URL.Geo.BusStop.Pavilion.to_list)
        json = Filters.Geo.BusStop.Pavilion.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.BusStop.Pavilion.update'''
        url  = self.URL.get(self.URL.Geo.BusStop.Pavilion.update)
        json = Filters.Geo.BusStop.Pavilion.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class BusStop:
    '''BusStop'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Pavilion = Pavilion(session, URL)


    @Request.All_pages
    @Request.Retry
    async def closest(self, **d):
        '''closest | Geo.BusStop.closest'''
        url  = self.URL.get(self.URL.Geo.BusStop.closest)
        json = Filters.Geo.BusStop.closest(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def coord(self, **d):
        '''coord | Geo.BusStop.coord'''
        url  = self.URL.get(self.URL.Geo.BusStop.coord)
        json = Filters.Geo.BusStop.coord(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.BusStop.create'''
        url  = self.URL.get(self.URL.Geo.BusStop.create)
        json = Filters.Geo.BusStop.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Geo.BusStop.delete'''
        url  = self.URL.get(self.URL.Geo.BusStop.delete)
        json = Filters.Geo.BusStop.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.BusStop.read'''
        url  = self.URL.get(self.URL.Geo.BusStop.read)
        json = Filters.Geo.BusStop.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def route(self, **d):
        '''route | Geo.BusStop.route'''
        url  = self.URL.get(self.URL.Geo.BusStop.route)
        json = Filters.Geo.BusStop.route(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def run(self, **d):
        '''run | Geo.BusStop.run'''
        url  = self.URL.get(self.URL.Geo.BusStop.run)
        json = Filters.Geo.BusStop.run(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.BusStop.to_list'''
        url  = self.URL.get(self.URL.Geo.BusStop.to_list)
        json = Filters.Geo.BusStop.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.BusStop.update'''
        url  = self.URL.get(self.URL.Geo.BusStop.update)
        json = Filters.Geo.BusStop.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Contract:
    '''Contract'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.Contract.create'''
        url  = self.URL.get(self.URL.Geo.Contract.create)
        json = Filters.Geo.Contract.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Geo.Contract.delete'''
        url  = self.URL.get(self.URL.Geo.Contract.delete)
        json = Filters.Geo.Contract.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def plan(self, **d):
        '''plan | Geo.Contract.plan'''
        url  = self.URL.get(self.URL.Geo.Contract.plan)
        json = Filters.Geo.Contract.plan(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Contract.read'''
        url  = self.URL.get(self.URL.Geo.Contract.read)
        json = Filters.Geo.Contract.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Contract.to_list'''
        url  = self.URL.get(self.URL.Geo.Contract.to_list)
        json = Filters.Geo.Contract.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def unit(self, **d):
        '''unit | Geo.Contract.unit'''
        url  = self.URL.get(self.URL.Geo.Contract.unit)
        json = Filters.Geo.Contract.unit(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.Contract.update'''
        url  = self.URL.get(self.URL.Geo.Contract.update)
        json = Filters.Geo.Contract.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Configuration:
    '''Configuration'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.Display.Configuration.create'''
        url  = self.URL.get(self.URL.Geo.Display.Configuration.create)
        json = Filters.Geo.Display.Configuration.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Geo.Display.Configuration.delete'''
        url  = self.URL.get(self.URL.Geo.Display.Configuration.delete)
        json = Filters.Geo.Display.Configuration.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Display.Configuration.read'''
        url  = self.URL.get(self.URL.Geo.Display.Configuration.read)
        json = Filters.Geo.Display.Configuration.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Display.Configuration.to_list'''
        url  = self.URL.get(self.URL.Geo.Display.Configuration.to_list)
        json = Filters.Geo.Display.Configuration.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.Display.Configuration.update'''
        url  = self.URL.get(self.URL.Geo.Display.Configuration.update)
        json = Filters.Geo.Display.Configuration.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Log:
    '''Log'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.Display.Log.create'''
        url  = self.URL.get(self.URL.Geo.Display.Log.create)
        json = Filters.Geo.Display.Log.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Display.Log.read'''
        url  = self.URL.get(self.URL.Geo.Display.Log.read)
        json = Filters.Geo.Display.Log.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Display:
    '''Display'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Log = Log(session, URL)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.Display.create'''
        url  = self.URL.get(self.URL.Geo.Display.create)
        json = Filters.Geo.Display.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Geo.Display.delete'''
        url  = self.URL.get(self.URL.Geo.Display.delete)
        json = Filters.Geo.Display.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Display.read'''
        url  = self.URL.get(self.URL.Geo.Display.read)
        json = Filters.Geo.Display.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Display.to_list'''
        url  = self.URL.get(self.URL.Geo.Display.to_list)
        json = Filters.Geo.Display.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.Display.update'''
        url  = self.URL.get(self.URL.Geo.Display.update)
        json = Filters.Geo.Display.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Layer:
    '''Layer'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.Layer.create'''
        url  = self.URL.get(self.URL.Geo.Layer.create)
        json = Filters.Geo.Layer.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Geo.Layer.delete'''
        url  = self.URL.get(self.URL.Geo.Layer.delete)
        json = Filters.Geo.Layer.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Layer.read'''
        url  = self.URL.get(self.URL.Geo.Layer.read)
        json = Filters.Geo.Layer.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Layer.to_list'''
        url  = self.URL.get(self.URL.Geo.Layer.to_list)
        json = Filters.Geo.Layer.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.Layer.update'''
        url  = self.URL.get(self.URL.Geo.Layer.update)
        json = Filters.Geo.Layer.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Object:
    '''Object'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.Object.create'''
        url  = self.URL.get(self.URL.Geo.Object.create)
        json = Filters.Geo.Object.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Geo.Object.delete'''
        url  = self.URL.get(self.URL.Geo.Object.delete)
        json = Filters.Geo.Object.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def layer(self, **d):
        '''layer | Geo.Object.layer'''
        url  = self.URL.get(self.URL.Geo.Object.layer)
        json = Filters.Geo.Object.layer(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def mo(self, **d):
        '''mo | Geo.Object.mo'''
        url  = self.URL.get(self.URL.Geo.Object.mo)
        json = Filters.Geo.Object.mo(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Object.read'''
        url  = self.URL.get(self.URL.Geo.Object.read)
        json = Filters.Geo.Object.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def search(self, **d):
        '''search | Geo.Object.search'''
        url  = self.URL.get(self.URL.Geo.Object.search)
        json = Filters.Geo.Object.search(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Object.to_list'''
        url  = self.URL.get(self.URL.Geo.Object.to_list)
        json = Filters.Geo.Object.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.Object.update'''
        url  = self.URL.get(self.URL.Geo.Object.update)
        json = Filters.Geo.Object.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Defect:
    '''Defect'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.Order.Defect.create'''
        url  = self.URL.get(self.URL.Geo.Order.Defect.create)
        json = Filters.Geo.Order.Defect.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.Order.Defect.update'''
        url  = self.URL.get(self.URL.Geo.Order.Defect.update)
        json = Filters.Geo.Order.Defect.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Execution:
    '''Execution'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL

    @Request.All_pages
    @Request.Retry
    async def details(self, **d):
        '''details | Geo.Order.Execution.details'''
        url  = self.URL.get(self.URL.Geo.Order.Execution.details)
        json = Filters.Geo.Order.Execution.details(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)
        

    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Order.Execution.read'''
        url  = self.URL.get(self.URL.Geo.Order.Execution.read)
        json = Filters.Geo.Order.Execution.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def recalc(self, **d):
        '''recalc | Geo.Order.Execution.recalc'''
        url  = self.URL.get(self.URL.Geo.Order.Execution.recalc)
        json = Filters.Geo.Order.Execution.recalc(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def statistic(self, **d):
        '''statistic | Geo.Order.Execution.statistic'''
        url  = self.URL.get(self.URL.Geo.Order.Execution.statistic)
        json = Filters.Geo.Order.Execution.statistic(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Order.Execution.to_list'''
        url  = self.URL.get(self.URL.Geo.Order.Execution.to_list)
        json = Filters.Geo.Order.Execution.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def unit(self, **d):
        '''unit | Geo.Order.Execution.unit'''
        url  = self.URL.get(self.URL.Geo.Order.Execution.unit)
        json = Filters.Geo.Order.Execution.unit(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Export:
    '''Export'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Order.Export.read'''
        url  = self.URL.get(self.URL.Geo.Order.Export.read)
        json = Filters.Geo.Order.Export.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def start(self, **d):
        '''start | Geo.Order.Export.start'''
        url  = self.URL.get(self.URL.Geo.Order.Export.start)
        json = Filters.Geo.Order.Export.start(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Order.Export.to_list'''
        url  = self.URL.get(self.URL.Geo.Order.Export.to_list)
        json = Filters.Geo.Order.Export.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Recalc:
    '''Recalc'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Order.Recalc.read'''
        url  = self.URL.get(self.URL.Geo.Order.Recalc.read)
        json = Filters.Geo.Order.Recalc.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.Order.Recalc.update'''
        url  = self.URL.get(self.URL.Geo.Order.Recalc.update)
        json = Filters.Geo.Order.Recalc.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Run:
    '''Run'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def summary(self, **d):
        '''summary | Geo.Order.Run.summary'''
        url  = self.URL.get(self.URL.Geo.Order.Run.summary)
        json = Filters.Geo.Order.Run.summary(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def vehicle(self, **d):
        '''vehicle | Geo.Order.Run.vehicle'''
        url  = self.URL.get(self.URL.Geo.Order.Run.vehicle)
        json = Filters.Geo.Order.Run.vehicle(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Order:
    '''Order'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Defect = Defect(session, URL)
        self.Execution = Execution(session, URL)
        self.Export = Export(session, URL)
        self.Recalc = Recalc(session, URL)
        self.Run = Run(session, URL)


    @Request.All_pages
    @Request.Retry
    async def clone(self, **d):
        '''clone | Geo.Order.clone'''
        url  = self.URL.get(self.URL.Geo.Order.clone)
        json = Filters.Geo.Order.clone(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Geo.Order.delete'''
        url  = self.URL.get(self.URL.Geo.Order.delete)
        json = Filters.Geo.Order.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def driver_score(self, **d):
        '''driver_score | Geo.Order.driver_score'''
        url  = self.URL.get(self.URL.Geo.Order.driver_score)
        json = Filters.Geo.Order.driver_score(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def generate(self, **d):
        '''generate | Geo.Order.generate'''
        url  = self.URL.get(self.URL.Geo.Order.generate)
        json = Filters.Geo.Order.generate(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Order.read'''
        url  = self.URL.get(self.URL.Geo.Order.read)
        json = Filters.Geo.Order.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Order.to_list'''
        url  = self.URL.get(self.URL.Geo.Order.to_list)
        json = Filters.Geo.Order.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.Order.update'''
        url  = self.URL.get(self.URL.Geo.Order.update)
        json = Filters.Geo.Order.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def vehicle(self, **d):
        '''vehicle | Geo.Order.vehicle'''
        url  = self.URL.get(self.URL.Geo.Order.vehicle)
        json = Filters.Geo.Order.vehicle(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Deviation:
    '''Deviation'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.Route.Deviation.create'''
        url  = self.URL.get(self.URL.Geo.Route.Deviation.create)
        json = Filters.Geo.Route.Deviation.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Route.Deviation.read'''
        url  = self.URL.get(self.URL.Geo.Route.Deviation.read)
        json = Filters.Geo.Route.Deviation.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class DuplicationMatrix:
    '''DuplicationMatrix'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def calc(self, **d):
        '''calc | Geo.Route.DuplicationMatrix.calc'''
        url  = self.URL.get(self.URL.Geo.Route.DuplicationMatrix.calc)
        json = Filters.Geo.Route.DuplicationMatrix.calc(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.Route.DuplicationMatrix.create'''
        url  = self.URL.get(self.URL.Geo.Route.DuplicationMatrix.create)
        json = Filters.Geo.Route.DuplicationMatrix.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def part(self, **d):
        '''part | Geo.Route.DuplicationMatrix.part'''
        url  = self.URL.get(self.URL.Geo.Route.DuplicationMatrix.part)
        json = Filters.Geo.Route.DuplicationMatrix.part(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Route.DuplicationMatrix.read'''
        url  = self.URL.get(self.URL.Geo.Route.DuplicationMatrix.read)
        json = Filters.Geo.Route.DuplicationMatrix.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def recalc(self, **d):
        '''recalc | Geo.Route.DuplicationMatrix.recalc'''
        url  = self.URL.get(self.URL.Geo.Route.DuplicationMatrix.recalc)
        json = Filters.Geo.Route.DuplicationMatrix.recalc(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def route(self, **d):
        '''route | Geo.Route.DuplicationMatrix.route'''
        url  = self.URL.get(self.URL.Geo.Route.DuplicationMatrix.route)
        json = Filters.Geo.Route.DuplicationMatrix.route(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Route.DuplicationMatrix.to_list'''
        url  = self.URL.get(self.URL.Geo.Route.DuplicationMatrix.to_list)
        json = Filters.Geo.Route.DuplicationMatrix.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class IntervalMap:
    '''IntervalMap'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def clone(self, **d):
        '''clone | Geo.Route.IntervalMap.clone'''
        url  = self.URL.get(self.URL.Geo.Route.IntervalMap.clone)
        json = Filters.Geo.Route.IntervalMap.clone(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.Route.IntervalMap.create'''
        url  = self.URL.get(self.URL.Geo.Route.IntervalMap.create)
        json = Filters.Geo.Route.IntervalMap.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Geo.Route.IntervalMap.delete'''
        url  = self.URL.get(self.URL.Geo.Route.IntervalMap.delete)
        json = Filters.Geo.Route.IntervalMap.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Route.IntervalMap.read'''
        url  = self.URL.get(self.URL.Geo.Route.IntervalMap.read)
        json = Filters.Geo.Route.IntervalMap.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Route.IntervalMap.to_list'''
        url  = self.URL.get(self.URL.Geo.Route.IntervalMap.to_list)
        json = Filters.Geo.Route.IntervalMap.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.Route.IntervalMap.update'''
        url  = self.URL.get(self.URL.Geo.Route.IntervalMap.update)
        json = Filters.Geo.Route.IntervalMap.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Registry:
    '''Registry'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.Route.Registry.create'''
        url  = self.URL.get(self.URL.Geo.Route.Registry.create)
        json = Filters.Geo.Route.Registry.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Geo.Route.Registry.delete'''
        url  = self.URL.get(self.URL.Geo.Route.Registry.delete)
        json = Filters.Geo.Route.Registry.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def fact(self, **d):
        '''fact | Geo.Route.Registry.fact'''
        url  = self.URL.get(self.URL.Geo.Route.Registry.fact)
        json = Filters.Geo.Route.Registry.fact(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Route.Registry.read'''
        url  = self.URL.get(self.URL.Geo.Route.Registry.read)
        json = Filters.Geo.Route.Registry.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Route.Registry.to_list'''
        url  = self.URL.get(self.URL.Geo.Route.Registry.to_list)
        json = Filters.Geo.Route.Registry.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.Route.Registry.update'''
        url  = self.URL.get(self.URL.Geo.Route.Registry.update)
        json = Filters.Geo.Route.Registry.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Variant:
    '''Variant'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.Route.Variant.create'''
        url  = self.URL.get(self.URL.Geo.Route.Variant.create)
        json = Filters.Geo.Route.Variant.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Geo.Route.Variant.delete'''
        url  = self.URL.get(self.URL.Geo.Route.Variant.delete)
        json = Filters.Geo.Route.Variant.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Route.Variant.read'''
        url  = self.URL.get(self.URL.Geo.Route.Variant.read)
        json = Filters.Geo.Route.Variant.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Route.Variant.to_list'''
        url  = self.URL.get(self.URL.Geo.Route.Variant.to_list)
        json = Filters.Geo.Route.Variant.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.Route.Variant.update'''
        url  = self.URL.get(self.URL.Geo.Route.Variant.update)
        json = Filters.Geo.Route.Variant.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Route:
    '''Route'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Deviation = Deviation(session, URL)
        self.DuplicationMatrix = DuplicationMatrix(session, URL)
        self.IntervalMap = IntervalMap(session, URL)
        self.Registry = Registry(session, URL)
        self.Variant = Variant(session, URL)


    @Request.All_pages
    @Request.Retry
    async def clone(self, **d):
        '''clone | Geo.Route.clone'''
        url  = self.URL.get(self.URL.Geo.Route.clone)
        json = Filters.Geo.Route.clone(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.Route.create'''
        url  = self.URL.get(self.URL.Geo.Route.create)
        json = Filters.Geo.Route.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Geo.Route.delete'''
        url  = self.URL.get(self.URL.Geo.Route.delete)
        json = Filters.Geo.Route.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def fill(self, **d):
        '''fill | Geo.Route.fill'''
        url  = self.URL.get(self.URL.Geo.Route.fill)
        json = Filters.Geo.Route.fill(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def mobile(self, **d):
        '''mobile | Geo.Route.mobile'''
        url  = self.URL.get(self.URL.Geo.Route.mobile)
        json = Filters.Geo.Route.mobile(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Route.read'''
        url  = self.URL.get(self.URL.Geo.Route.read)
        json = Filters.Geo.Route.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def search(self, **d):
        '''search | Geo.Route.search'''
        url  = self.URL.get(self.URL.Geo.Route.search)
        json = Filters.Geo.Route.search(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def short(self, **d):
        '''short | Geo.Route.short'''
        url  = self.URL.get(self.URL.Geo.Route.short)
        json = Filters.Geo.Route.short(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Route.to_list'''
        url  = self.URL.get(self.URL.Geo.Route.to_list)
        json = Filters.Geo.Route.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.Route.update'''
        url  = self.URL.get(self.URL.Geo.Route.update)
        json = Filters.Geo.Route.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Formal:
    '''Formal'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.Schedule.Formal.create'''
        url  = self.URL.get(self.URL.Geo.Schedule.Formal.create)
        json = Filters.Geo.Schedule.Formal.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Geo.Schedule.Formal.delete'''
        url  = self.URL.get(self.URL.Geo.Schedule.Formal.delete)
        json = Filters.Geo.Schedule.Formal.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Schedule.Formal.read'''
        url  = self.URL.get(self.URL.Geo.Schedule.Formal.read)
        json = Filters.Geo.Schedule.Formal.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Schedule.Formal.to_list'''
        url  = self.URL.get(self.URL.Geo.Schedule.Formal.to_list)
        json = Filters.Geo.Schedule.Formal.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.Schedule.Formal.update'''
        url  = self.URL.get(self.URL.Geo.Schedule.Formal.update)
        json = Filters.Geo.Schedule.Formal.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Portal:
    '''Portal'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Schedule.Portal.read'''
        url  = self.URL.get(self.URL.Geo.Schedule.Portal.read)
        json = Filters.Geo.Schedule.Portal.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def route(self, **d):
        '''route | Geo.Schedule.Portal.route'''
        url  = self.URL.get(self.URL.Geo.Schedule.Portal.route)
        json = Filters.Geo.Schedule.Portal.route(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Switch:
    '''Switch'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.Schedule.Switch.create'''
        url  = self.URL.get(self.URL.Geo.Schedule.Switch.create)
        json = Filters.Geo.Schedule.Switch.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Geo.Schedule.Switch.delete'''
        url  = self.URL.get(self.URL.Geo.Schedule.Switch.delete)
        json = Filters.Geo.Schedule.Switch.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def h_list(self, **d):
        '''h_list | Geo.Schedule.Switch.h_list'''
        url  = self.URL.get(self.URL.Geo.Schedule.Switch.h_list)
        json = Filters.Geo.Schedule.Switch.h_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def hide(self, **d):
        '''hide | Geo.Schedule.Switch.hide'''
        url  = self.URL.get(self.URL.Geo.Schedule.Switch.hide)
        json = Filters.Geo.Schedule.Switch.hide(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Schedule.Switch.read'''
        url  = self.URL.get(self.URL.Geo.Schedule.Switch.read)
        json = Filters.Geo.Schedule.Switch.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def show(self, **d):
        '''show | Geo.Schedule.Switch.show'''
        url  = self.URL.get(self.URL.Geo.Schedule.Switch.show)
        json = Filters.Geo.Schedule.Switch.show(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Schedule.Switch.to_list'''
        url  = self.URL.get(self.URL.Geo.Schedule.Switch.to_list)
        json = Filters.Geo.Schedule.Switch.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.Schedule.Switch.update'''
        url  = self.URL.get(self.URL.Geo.Schedule.Switch.update)
        json = Filters.Geo.Schedule.Switch.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Turn:
    '''Turn'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.Schedule.Turn.create'''
        url  = self.URL.get(self.URL.Geo.Schedule.Turn.create)
        json = Filters.Geo.Schedule.Turn.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Geo.Schedule.Turn.delete'''
        url  = self.URL.get(self.URL.Geo.Schedule.Turn.delete)
        json = Filters.Geo.Schedule.Turn.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Schedule.Turn.read'''
        url  = self.URL.get(self.URL.Geo.Schedule.Turn.read)
        json = Filters.Geo.Schedule.Turn.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Schedule.Turn.to_list'''
        url  = self.URL.get(self.URL.Geo.Schedule.Turn.to_list)
        json = Filters.Geo.Schedule.Turn.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.Schedule.Turn.update'''
        url  = self.URL.get(self.URL.Geo.Schedule.Turn.update)
        json = Filters.Geo.Schedule.Turn.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Schedule:
    '''Schedule'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Formal = Formal(session, URL)
        self.Portal = Portal(session, URL)
        self.Switch = Switch(session, URL)
        self.Turn = Turn(session, URL)


    @Request.All_pages
    @Request.Retry
    async def clone(self, **d):
        '''clone | Geo.Schedule.clone'''
        url  = self.URL.get(self.URL.Geo.Schedule.clone)
        json = Filters.Geo.Schedule.clone(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.Schedule.create'''
        url  = self.URL.get(self.URL.Geo.Schedule.create)
        json = Filters.Geo.Schedule.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Geo.Schedule.delete'''
        url  = self.URL.get(self.URL.Geo.Schedule.delete)
        json = Filters.Geo.Schedule.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def info(self, **d):
        '''info | Geo.Schedule.info'''
        url  = self.URL.get(self.URL.Geo.Schedule.info)
        json = Filters.Geo.Schedule.info(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Schedule.read'''
        url  = self.URL.get(self.URL.Geo.Schedule.read)
        json = Filters.Geo.Schedule.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Schedule.to_list'''
        url  = self.URL.get(self.URL.Geo.Schedule.to_list)
        json = Filters.Geo.Schedule.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.Schedule.update'''
        url  = self.URL.get(self.URL.Geo.Schedule.update)
        json = Filters.Geo.Schedule.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Service:
    '''Service'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def check(self, **d):
        '''check | Geo.Service.check'''
        url  = self.URL.get(self.URL.Geo.Service.check)
        json = Filters.Geo.Service.check(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def driver(self, **d):
        '''driver | Geo.Service.driver'''
        url  = self.URL.get(self.URL.Geo.Service.driver)
        json = Filters.Geo.Service.driver(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def forecast(self, **d):
        '''forecast | Geo.Service.forecast'''
        url  = self.URL.get(self.URL.Geo.Service.forecast)
        json = Filters.Geo.Service.forecast(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def geocoding(self, **d):
        '''geocoding | Geo.Service.geocoding'''
        url  = self.URL.get(self.URL.Geo.Service.geocoding)
        json = Filters.Geo.Service.geocoding(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def routing(self, **d):
        '''routing | Geo.Service.routing'''
        url  = self.URL.get(self.URL.Geo.Service.routing)
        json = Filters.Geo.Service.routing(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def search(self, **d):
        '''search | Geo.Service.search'''
        url  = self.URL.get(self.URL.Geo.Service.search)
        json = Filters.Geo.Service.search(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def sign_log(self, **d):
        '''sign_log | Geo.Service.sign_log'''
        url  = self.URL.get(self.URL.Geo.Service.sign_log)
        json = Filters.Geo.Service.sign_log(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def street(self, **d):
        '''street | Geo.Service.street'''
        url  = self.URL.get(self.URL.Geo.Service.street)
        json = Filters.Geo.Service.street(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class TerritorialEntity:
    '''TerritorialEntity'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def create(self, **d):
        '''create | Geo.TerritorialEntity.create'''
        url  = self.URL.get(self.URL.Geo.TerritorialEntity.create)
        json = Filters.Geo.TerritorialEntity.create(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def delete(self, **d):
        '''delete | Geo.TerritorialEntity.delete'''
        url  = self.URL.get(self.URL.Geo.TerritorialEntity.delete)
        json = Filters.Geo.TerritorialEntity.delete(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.TerritorialEntity.read'''
        url  = self.URL.get(self.URL.Geo.TerritorialEntity.read)
        json = Filters.Geo.TerritorialEntity.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.TerritorialEntity.to_list'''
        url  = self.URL.get(self.URL.Geo.TerritorialEntity.to_list)
        json = Filters.Geo.TerritorialEntity.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def update(self, **d):
        '''update | Geo.TerritorialEntity.update'''
        url  = self.URL.get(self.URL.Geo.TerritorialEntity.update)
        json = Filters.Geo.TerritorialEntity.update(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Daily:
    '''Daily'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL


    @Request.All_pages
    @Request.Retry
    async def read(self, **d):
        '''read | Geo.Violation.Daily.read'''
        url  = self.URL.get(self.URL.Geo.Violation.Daily.read)
        json = Filters.Geo.Violation.Daily.read(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Violation.Daily.to_list'''
        url  = self.URL.get(self.URL.Geo.Violation.Daily.to_list)
        json = Filters.Geo.Violation.Daily.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)


class Violation:
    '''Violation'''
    def __init__(self, session: object, URL: object) -> None:
        self.__session = session
        self.URL = URL
        self.Daily = Daily(session, URL)


    @Request.All_pages
    @Request.Retry
    async def to_list(self, **d):
        '''to_list | Geo.Violation.to_list'''
        url  = self.URL.get(self.URL.Geo.Violation.to_list)
        json = Filters.Geo.Violation.to_list(**dict(d, token=Request.token(self.__session)))
        return await self.__session.post(url=url, json=json)