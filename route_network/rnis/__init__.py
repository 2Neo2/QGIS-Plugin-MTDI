import aiohttp

from .api     import API
from .request import Request


class RNIS:
    def __init__(self, 
                 login: str, 
                 password: str, 
                 token: str = None, 
                 road: bool = False
    ) -> None: 
        self.__login    = str(login)
        self.__password = str(password)
        self.token      = str(token)
        self.__road     = road
        self.Help = Request.Help()
        self.session    = aiohttp.ClientSession(headers=Request.headers)


    @property
    async def auth(self):
        d = await self.API.Auth.login(
                                    login=self.__login, 
                                    password=self.__password, 
                                    print_error=True, 
                                    retries=1
        )
        self.token = d.get('payload', {}).get('token')
        self.session.cookie_jar.update_cookies({'token': self.token})
        self.API = API(session=self.session, road=self.__road)


    @property
    async def check_token(self):
        self.session.cookie_jar.update_cookies({'token': self.token})
        self.API = API(session=self.session, road=self.__road)
        d = await self.API.Auth.User.read(retries=1)
        if type(d) is list:
            await self.auth


    async def __aenter__(self):
        await self.check_token
        return self


    async def __aexit__(self, *args, **kwargs):
        await self.session.close()


    @property
    async def close(self):
        await self.session.close()