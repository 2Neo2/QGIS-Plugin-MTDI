from .config import Method
from .request_functions import retry_request


class Auth:
    def __init__(self, 
                 session:    object, 
                 login:      str = None, 
                 password:   str = None, 
                 device_id:  str = None, 
                 session_id: str = None
    ) -> None:
        self.session      = session
        self.__login      = login
        self.__password   = password
        self.device_id  = device_id
        self.session_id = session_id
        self.cookies      = dict()


    def __get_auth_data(self) -> dict:
        """Получение данных для входа"""
        json = dict()
        json['username'] = self.__login
        json['password'] = self.__password
        json['remember'] = True
        return json


    def __update_cookies(self) -> None:
        """Получение данных для входа"""
        self.cookies['metabase.DEVICE']  = self.device_id
        self.cookies['metabase.SESSION'] = self.session_id
        self.cookies['metabase.TIMEOUT'] = 'alive'
        self.session.cookie_jar.update_cookies(self.cookies)


    @retry_request
    async def __get_device_id(self, **d) -> object:
        """Получение device_id из API"""
        response = await self.session.get(Method.url)
        text = str(response.text)
        text = text[text.find('metabase.DEVICE='):]
        text = text[16:text.find(';')]
        self.device_id = text
        return response


    @retry_request
    async def __get_session_id(self, **d) -> object:
        """Получение session_id из API"""
        response = await self.session.post(url=Method.auth, json=self.__get_auth_data())
        text = await response.json()
        self.session_id = text.get('id')
        return response


    @retry_request
    async def __check_auth(self, **d) -> object:
        """Проверка существующих device_id и session_id. Запрос к API."""
        self.__update_cookies()
        return await self.session.get(Method.database)


    async def check_auth_data(self) -> bool:
        """Проверка существующих device_id и session_id."""
        if (self.device_id and self.session_id) is not None:
            response = await self.__check_auth(retries=1)
            if type(response) != list:
                return False
        return True


    # async def perform_auth(self) -> object:
    async def __call__(self) -> object:
        """Произвести авторизацию"""
        if await self.check_auth_data():
            await self.__get_device_id(print_error=True, retries=1)
            await self.__get_session_id(print_error=True, retries=1)
            self.__update_cookies()
            return self.session
        else:
            return self.session