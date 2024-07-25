from .Template  import Template

from .create    import create
from .delete    import delete
from .date      import date
from .read      import read
from .repeat    import repeat
from .to_list   import to_list
from .unit      import unit
from .update    import update
from .upload    import upload
from .violation import violation
from .visit     import visit


class Task:
    Template  = Template
    
    delete    = delete
    date      = date
    read      = read
    repeat    = repeat
    to_list   = to_list
    update    = update
    unit      = unit
    upload    = upload
    violation = violation
    visit     = visit