from .body      import Add
from .functions import retry_request, get_all_pages, token
from .headers   import headers
from .Method    import Method
from .help      import Help


class Request:
    Body = Add
    Retry = retry_request
    All_pages = get_all_pages
    Method = Method
    Help = Help
    headers = headers
    token = token