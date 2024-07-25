from .Auth       import Auth
from .Convert    import Convert
from .Dictionary import Dictionary
from .FIAS       import FIAS
from .Garbage    import Garbage
from .GATN       import GATN
from .Geo        import Geo
from .Kurs       import Kurs
from .Mobile     import Mobile
from .Notification import Notification
from .Organization import Organization
from .Portal    import Portal
from .Report    import Report
from .Storage   import Storage
from .System    import System
from .T1sync    import T1sync
from .Telematic import Telematic
from .Vehicle   import Vehicle
from ..request    import Request



class API:
    def __init__(self, session: object, road: bool = False):#, session, token):
        URL = Request.Method('rnis.mosreg.ru') if road else Request.Method()
        self.Auth       = Auth(session, URL)
        self.Convert    = Convert(session, URL)
        self.Dictionary = Dictionary(session, URL)
        self.FIAS       = FIAS(session, URL)
        self.Garbage    = Garbage(session, URL)
        self.GATN       = GATN(session, URL)
        self.Geo        = Geo(session, URL)
        self.Kurs       = Kurs(session, URL)
        self.Mobile     = Mobile(session, URL)
        self.Notification = Notification(session, URL)
        self.Organization = Organization(session, URL)
        self.Portal     = Portal(session, URL)
        self.Report     = Report(session, URL)
        self.Storage    = Storage(session, URL)
        self.System     = System(session, URL)
        self.T1sync     = T1sync(session, URL)
        self.Telematic  = Telematic(session, URL)
        self.Vehicle    = Vehicle(session, URL)