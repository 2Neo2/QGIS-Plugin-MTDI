from .Work import Work

from .create  import create
from .delete  import delete
from .read    import read
from .to_list import to_list
from .update  import update
from .driver_score import driver_score


class Contract:
    Work = Work
    
    create  = create
    delete  = delete
    read    = read
    to_list = to_list
    update  = update
    driver_score  = driver_score