from .Confirm import Confirm

from .login import login
from .login_by_email import login_by_email
from .read import read
from .register import register
from .update import update
from .update_push_token import update_push_token


class User:
    Confirm  = Confirm

    login = login
    login_by_email = login_by_email
    read = read
    register = register
    update = update
    update_push_token = update_push_token