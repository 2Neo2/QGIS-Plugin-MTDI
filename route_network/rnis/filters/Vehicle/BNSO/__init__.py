from .Link  import Link

from .check   import check
from .create  import create
from .delete  import delete
from .period  import period
from .read    import read
from .search  import search
from .to_list import to_list
from .update  import update


class BNSO:
    Link = Link
    
    check   = check
    create  = create
    delete  = delete
    period  = period
    read    = read
    search  = search
    to_list = to_list
    update  = update