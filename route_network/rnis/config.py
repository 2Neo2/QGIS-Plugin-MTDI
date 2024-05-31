url = 'https://bus.rnis.mosreg.ru/ajax/request?'    # URL РНИС для запросов
headers = {                                         # Хедеры
    'Host': 'bus.rnis.mosreg.ru',
    'content-type': 'application/json;charset=UTF-8',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
}


# Метод API
class Method:
    auth       = url + 'com.rnis.auth.action.login'
    
    execution  = url + 'com.rnis.geo.action.order_execution.list'
    order      = url + 'com.rnis.geo.action.order.get'
    order_list = url + 'com.rnis.geo.action.order.list'
    
    route               = url + 'com.rnis.geo.action.route.get'
    route_list          = url + 'com.rnis.geo.action.route.list'
    route_registry      = url + 'com.rnis.geo.action.route_registry.get'
    route_registry_list = url + 'com.rnis.geo.action.route_registry.list'
    route_variant       = url + 'com.rnis.geo.action.route_variant.get'
    route_variant_list  = url + 'com.rnis.geo.action.route_variant.list'
    