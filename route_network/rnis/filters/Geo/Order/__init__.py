from .Defect    import Defect
from .Execution import Execution
from .Export    import Export
from .Recalc    import Recalc
from .Run       import Run

from .clone         import clone
from .delete        import delete
from .driver_score  import driver_score
from .generate      import generate
from .read          import read
from .to_list       import to_list
from .update        import update
from .vehicle       import vehicle


class Order:
    Defect    = Defect
    Execution = Execution
    Export    = Export
    Recalc    = Recalc
    Run       = Run
    
    clone        = clone
    delete       = delete
    driver_score = driver_score
    generate     = generate
    read         = read
    to_list      = to_list
    update       = update
    vehicle      = vehicle