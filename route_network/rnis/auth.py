from .config import Method
from .request_filters   import AddFilters
from .request_functions import retry_request, get_request_body, get_all_pages


class Auth:
    def __init__(self, session, login, password):
        self.__login = login
        self.__password = password
        self.session = session
        self.token = None

    
    @retry_request
    async def __get_token(self, **d):
        json = get_request_body(None)
        del json['headers']['token']
        json['payload']['login'] = self.__login
        json['payload']['password'] = self.__password
        return await self.session.post(url=Method.auth, json=json)
        
    
    async def get_token(self):
        if self.token is None:
            data = await self.__get_token(print_error=True)
            self.token = data['payload']['token']
            self.date  = data['payload']['last_login_at']
            self.session.cookie_jar.update_cookies({'token': self.token})
            return self.session, self.token
        else:
            return self.session, self.token