from .Formal         import Formal
from .Portal       import Portal
from .Switch          import Switch
from .Turn           import Turn

from .clone   import clone
from .create  import create
from .delete  import delete
from .info    import info
from .read    import read
from .to_list import to_list
from .update  import update


class Schedule:
    Formal = Formal
    Portal = Portal
    Switch = Switch
    Turn   = Turn

    clone   = clone
    create  = create
    info    = info
    delete  = delete
    read    = read
    to_list = to_list
    update  = update