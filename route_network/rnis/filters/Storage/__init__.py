from .delete import delete
from .read  import read
from .token import token


class Storage:
    delete = delete
    read  = read
    token = token