from .Fuel import Fuel
from .Work import Work
from .Mechanism import Mechanism

from .create  import create
from .delete  import delete
from .read    import read
from .to_list import to_list
from .update  import update
from .upload  import upload
from .upload_status import upload_status


class Vehicle:
    Fuel = Fuel
    Work = Work
    Mechanism = Mechanism
    
    create  = create
    delete  = delete
    read    = read
    to_list = to_list
    update  = update
    upload  = upload
    upload_status = upload_status