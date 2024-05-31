# Хедеры
headers = {
    'Host': 'tkp-bi.secgw.ru',
    'Accept': 'application/json',
    'User-Agent': 'Python lib TKP',
    'Origin': 'https://tkp-bi.secgw.ru',
    'Accept-Language': 'ru',
}

url = 'https://tkp-bi.secgw.ru/'        # URL ТКП для запросов

# Метод API
class Method:
    url      = 'https://tkp-bi.secgw.ru/'        # URL ТКП для запросов
    url_api  = url + 'api/'
    card     = url_api + 'card/'
    auth     = url_api + 'session'
    database = url_api + 'database'
    
    class Card:
        def __init__(self, card_id):
            # self.data  = f'{Method.card}/{card_id}'
            self.data  = f'{url}api/card/{card_id}'
            self.query = f'{self.data}/query'
            self.json  = f'{self.query}/json'
            self.xlsx  = f'{self.query}/xlsx'
            self.csv   = f'{self.query}/csv'