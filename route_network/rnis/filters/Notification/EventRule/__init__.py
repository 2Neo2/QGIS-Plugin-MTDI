from .Notification  import Notification

from .create  import create
from .delete  import delete
from .event   import event
from .read    import read
from .to_list import to_list
from .update  import update


class EventRule:
    Notification = Notification
    
    create  = create
    delete  = delete
    event   = event
    read    = read
    to_list = to_list
    update  = update