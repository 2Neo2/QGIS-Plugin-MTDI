from .Deviation         import Deviation
from .DuplicationMatrix import DuplicationMatrix
from .IntervalMap       import IntervalMap
from .Registry          import Registry
from .Variant           import Variant

from .clone   import clone
from .create  import create
from .delete  import delete
from .fill    import fill
from .mobile  import mobile
from .read    import read
from .search  import search
from .short   import short
from .to_list import to_list
from .update  import update


class Route:
    Deviation         = Deviation
    DuplicationMatrix = DuplicationMatrix
    IntervalMap       = IntervalMap
    Registry          = Registry
    Variant           = Variant

    clone   = clone
    create  = create
    fill    = fill
    mobile  = mobile
    delete  = delete
    read    = read
    search  = search
    short   = short
    to_list = to_list
    update  = update