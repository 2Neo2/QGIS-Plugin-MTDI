from .Permission import Permission
from .Role       import Role
from .User       import User

from .entity import entity
from .login  import login
from .logout import logout


class Auth:
    Permission = Permission
    Role       = Role
    User       = User

    entity = entity
    login  = login
    logout = logout