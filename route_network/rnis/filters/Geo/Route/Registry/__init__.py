from .create  import create
from .delete  import delete
from .fact    import fact
from .read    import read
from .to_list import to_list
from .update  import update


class Registry:
    create  = create
    delete  = delete
    fact    = fact
    read    = read
    to_list = to_list
    update  = update