from .Schedule import Schedule
from .Tablet   import Tablet
from .Template import Template

from .available import available
from .create    import create
from .integration_log import integration_log
from .parameter import parameter
from .to_list   import to_list


class Report:
    Schedule = Schedule
    Tablet   = Tablet
    Template = Template
    
    available = available
    create    = create
    integration_log = integration_log
    parameter = parameter
    to_list   = to_list