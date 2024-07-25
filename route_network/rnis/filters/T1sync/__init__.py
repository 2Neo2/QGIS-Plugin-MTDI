from .Device  import Device
from .History import History
from .Odometr import Odometr

from .event    import event
from .extended import extended
from .mileage  import mileage
from .motohour import motohour


class T1sync:
    Device  = Device
    History = History
    Odometr = Odometr
    
    event    = event
    extended = extended
    mileage  = mileage
    motohour = motohour