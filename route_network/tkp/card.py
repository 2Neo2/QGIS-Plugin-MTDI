import json

from .config import Method
from .request_filters   import Parameters
from .request_functions import *


class Card:
    """Обращение к API ТКП (карточка отчета)"""
    def __init__(self, 
                 session: object, 
                 card_id: int = None,
    ) -> None:
        if card_id is not None:
            self.url = Method.Card(card_id)
        self.card_id = card_id
        self.session = session

    
    async def __aenter__(self) -> object:
        await self.data
        self.parameters_get
        return self
    
    
    async def __aexit__(self, *args, **kwargs) -> None:
        # print(f'Карточка {self.name} ({self.card_id}) уничтожена (НЕТ)')
        pass


    async def __call__(self, card_id: int or str = None) -> None:
        """Произвести авторизацию"""
        if card_id is not None:
            self.url = Method.Card(card_id)
            self.card_id = card_id
        await self.data
        self.parameters_get


    @check_error
    @parse_response
    @retry_request
    async def api_request(self, url: str, is_post: bool = True, is_json: bool = False, **d) -> object:
        """Запрос к API"""
        if is_json:
            data = {'parameters': self.parameters}
            data = await self.session.post(url=url, json=data)
        else:
            data = {'parameters': json.dumps(self.parameters)}
            data =  await self.session.post(url=url, data=data)
        return data
    
    
    @retry_request
    async def __data(self, **d) -> object:
        """Запрос на получение данных отчета"""
        return await self.session.get(url=self.url.data)


    @property
    async def data(self) -> dict:
        """Получение данных отчета"""
        self.card_data = await self.__data(print_error=True, retries=1)
        self.card_data = await self.card_data.json()
        return self.card_data


    @property
    async def query(self) -> dict:
        """Получение отчета"""
        return await self.api_request(url=self.url.query, is_json=True, print_error=True, retries=1)


    @property
    async def json(self) -> dict:
        """Получение отчета в JSON"""
        return await self.api_request(url=self.url.json, print_error=True, retries=1)


    @property
    async def xlsx(self) -> dict:
        """Получение отчета в XLSX"""
        return await self.api_request(url=self.url.xlsx, print_error=True, retries=1)


    @property
    async def csv(self) -> dict:
        """Получение отчета в CSV"""
        return await self.api_request(url=self.url.csv, print_error=True, retries=1)
    

    @property
    def parameters_get(self) -> None:
        """Создание парметров по данным из карточки"""
        self.name       = normolize_name(self.card_data.get('name'))
        self.__param    = Parameters(self.card_data)
        self.parameters = self.__param.create


    def parameters_update(self, **d) -> None:
        """Обновление парметров данными от пользователя"""
        self.parameters = self.__param.update(**dict(d, parameters=self.parameters))