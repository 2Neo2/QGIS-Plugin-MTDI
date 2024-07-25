from .create  import create
from .delete  import delete
from .read    import read
from .repair  import repair
from .to_list import to_list
from .update  import update


class Part:
    create  = create
    delete  = delete
    read    = read
    repair  = repair
    to_list = to_list
    update  = update