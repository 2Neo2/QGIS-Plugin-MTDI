from .BNSO import BNSO
from .Event import Event
from .Graduation import Graduation
from .Port import Port
from .Status import Status

from .create  import create
from .delete  import delete
from .idle    import idle
from .malfunction   import malfunction
from .portal  import portal
from .read    import read
from .retrospective import retrospective
from .search  import search
from .to_list import to_list
from .unit    import unit
from .update  import update
from .upload  import upload
from .upload_status import upload_status


class Vehicle:
    BNSO = BNSO
    Event = Event
    Graduation = Graduation
    Port = Port
    Status = Status
    
    create  = create
    delete  = delete
    idle    = idle
    malfunction = malfunction
    portal  = portal
    read    = read
    retrospective = retrospective
    search  = search
    to_list = to_list
    unit    = unit
    update  = update
    upload  = upload
    upload_status = upload_status