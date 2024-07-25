from .create   import create
from .document import document
from .next_version import next_version
from .read     import read
from .to_list  import to_list
from .update   import update


class TemplateDocument:
    create   = create
    document = document
    next_version = next_version
    read     = read
    to_list  = to_list
    update   = update