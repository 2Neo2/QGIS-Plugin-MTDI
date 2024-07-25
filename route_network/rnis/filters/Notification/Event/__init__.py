from .create  import create
from .delete  import delete
from .read    import read
from .send    import send
from .to_list import to_list
from .update  import update


class Event:
    create  = create
    delete  = delete
    read    = read
    send    = send
    to_list = to_list
    update  = update