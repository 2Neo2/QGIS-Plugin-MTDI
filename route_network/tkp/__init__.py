# TKP
import aiohttp

from .config import headers
from .auth   import Auth
from .card   import Card


class TKP_API:
    def __init__(self, 
                 login     : str = None, 
                 password  : str = None, 
                 device_id : str = None, 
                 session_id: str = None
    ) -> None:
        self.session      = aiohttp.ClientSession(headers=headers)
        self.__login      = str(login)
        self.__password   = str(password)
        self.device_id  = device_id
        self.session_id = session_id


    async def __aenter__(self) -> object:
        auth = Auth(self.session, self.__login, self.__password, self.device_id, self.session_id)
        self.session = await auth()
        self.device_id  = auth.device_id
        self.session_id = auth.session_id
        self.Card = Card(self.session)
        return self


    async def __aexit__(self, *args, **kwargs) -> None:
        await self.session.close()