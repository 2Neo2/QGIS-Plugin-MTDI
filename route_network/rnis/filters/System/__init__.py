from .Activity    import Activity
from .Audit       import Audit
from .Entity      import Entity
from .Log         import Log
from .Maintenance import Maintenance
from .Message     import Message
from .Schema      import Schema
from .Table       import Table
from .Tooltip     import Tooltip
from .Trash       import Trash

from .down    import down
from .status  import status
from .up      import up
from .version import version


class System:
    Activity    = Activity
    Audit       = Audit
    Entity      = Entity
    Log         = Log
    Maintenance = Maintenance
    Message     = Message
    Schema      = Schema
    Table       = Table
    Tooltip     = Tooltip
    Trash       = Trash
    
    down    = down
    status  = status
    up      = up
    version = version