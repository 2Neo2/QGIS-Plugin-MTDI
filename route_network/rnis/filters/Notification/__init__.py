from .Event     import Event
from .EventRule import EventRule
from .Mailing   import Mailing
from .SpeedViolation import SpeedViolation
from .User      import User

from .count   import count
from .create  import create
from .read    import read
from .send    import send
from .to_list import to_list


class Notification:
    Event     = Event
    EventRule = EventRule
    Mailing   = Mailing
    SpeedViolation = SpeedViolation
    User      = User
    
    count  = count
    create  = create
    read    = read
    send    = send
    to_list = to_list