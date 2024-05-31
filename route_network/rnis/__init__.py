# RNIS
import aiohttp

from .config import headers
from .auth   import Auth
from .order  import Order
from .route  import Route


class RnisAPI:
    def __init__(self, login, password):
        self.__login = str(login)
        self.__password = str(password)
        self.session = aiohttp.ClientSession(headers=headers)
    
    async def __aenter__(self):
        auth = Auth(self.session, self.__login, self.__password)
        self.session, self.token = await auth.get_token()
        self.Order = Order(self.session, self.token)
        self.Route = Route(self.session, self.token)
        return self
    
    async def __aexit__(self, *args, **kwargs):
        await self.session.close()