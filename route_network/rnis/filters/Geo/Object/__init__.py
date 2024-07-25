from .create  import create
from .delete  import delete
from .layer   import layer
from .mo      import mo
from .read    import read
from .to_list import to_list
from .update  import update
from .search  import search


class Object:
    create  = create
    delete  = delete
    layer   = layer
    mo      = mo
    read    = read
    to_list = to_list
    update  = update