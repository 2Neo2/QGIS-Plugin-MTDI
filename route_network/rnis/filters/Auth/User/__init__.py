from .Dismissal import Dismissal
from .Education import Education
from .Position  import Position

from .by_unit   import by_unit
from .can import can
from .create import create
from .created import created
from .delete import delete
from .deleted import deleted
from .read import read
from .refresh import refresh
from .search import search
from .tachograph import tachograph
from .to_list import to_list
from .update import update
from .updated import updated


class User:
    Dismissal = Dismissal
    Education = Education
    Position  = Position
    
    by_unit = by_unit
    can     = can
    create  = create
    created = created
    delete  = delete
    deleted = deleted
    read    = read
    search  = search
    to_list = to_list
    update  = update
    updated = updated
