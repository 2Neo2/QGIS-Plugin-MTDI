def to_list(data):
    """Преобразование данных в список"""
    if type(data) in [dict, list, set, tuple]:
        return list(data)
    else:
        return [f'{data}']


def to_str(data):
    """Преобразование данных в строку"""
    data = to_list(data)[0]
    return f'{data}'


def add_filter(filters, filter_name, filter_data, func=None):
    """Создание фильтра по заданным параметрам"""
    if filter_data is not None:
        filters[filter_name] = filter_data
        if func:
            filters[filter_name] = func(filter_data)
    return filters


def add_column_search(request_body, column, filter_data):
    """Создание фильтра по заданной колонке"""
    if filter_data is not None:
        request_body['headers']['meta']['column_search'] = request_body['headers']['meta'].get('column_search', [])
        request_body['headers']['meta']['column_search'].append({'column': column, 'value': to_str(filter_data)})
    return request_body


def add_response_data(request_body, response_data):
    """Создание фильтра по выводимым значением ответа"""
    if response_data is not None:
        request_body['headers']['meta']['response_data'] = to_list(response_data)
    return request_body


def add_pagination(request_body, page, limit):
    """Создание пагинации"""
    request_body['headers']['meta']['pagination'] = {'page': page, 'limit': limit}
    return request_body


class AddFilters:
    class Route:
        def list_(request_body, **d):
            """Фильтры для списка маршрутов"""
            response_data = ["items/uuid", "items/number", "items/registration_number", "items/title"]
            response_data = d.get('response_data', response_data)
            request_body = add_response_data(request_body, response_data)                  # Какие атрибуты маршрута выводить
            
            filters = request_body['headers']['meta']['filters']
            filters = add_filter(filters, 'withUuid',           d.get('route_uuid'), to_list)       # Фильтрация по идентификатору маршрута
            filters = add_filter(filters, 'withOriginalUnits',  d.get('units'), to_list)            # Фильтрация по организаторам перевозок
            filters = add_filter(filters, 'withCarriers',       d.get('carriers'), to_list)         # Фильтрация по перевозчикам
            filters = add_filter(filters, 'withParentUuid',     d.get('parent_uuid'), to_str)       # Фильтрация по идентификатору корневого паспорта маршрута
            filters = add_filter(filters, 'withActive',         d.get('active'))                    # Фильтрация по активности
            filters = add_filter(filters, 'withStatus',         d.get('status'), to_list)           # Фильтрация по статусам
            filters = add_filter(filters, 'withRouteType',      d.get('route_type'), to_list)       # Фильтрация по типу маршрута
            filters = add_filter(filters, 'withRouteKind',      d.get('route_kind'), to_list)       # Фильтрация по виду маршрута
            filters = add_filter(filters, 'withContracts',      d.get('contracts'), to_list)        # Фильтрация по контрактам
            filters = add_filter(filters, 'withStopPoint',      d.get('busstop'), to_str)           # Фильтрация по входящей в маршрут остановке
            filters = add_filter(filters, 'onlyToday',          d.get('in_order'))                  # Фильтрация по маршрутам, по которым сегодня имеются план-наряды
            filters = add_filter(filters, 'withIsPublic',       d.get('public'), to_list)           # Фильтрация по признаку публичности (массив из 'public', 'not_public)
            filters = add_filter(filters, 'withRouteRegNumbers',d.get('route_reg_number'), to_list) # Фильтрация по рег. номеру маршрута
            filters = add_filter(filters, 'withRouteNumbers',   d.get('route_number'), to_list)     # Фильтрация по номеру маршрута
            filters = add_filter(filters, 'withoutGeometry',    d.get('geometry', True))            # Фильтрация по по геометрии
            filters = add_filter(filters, 'onlyVis',            d.get('vis_transport', False))      # Фильтрация по маршрутам ВИС/РНИС
            filters = add_filter(filters, 'withCommunalMunicipalityUuid', d.get('munic'), to_list)  # Фильтрация по муниципалитету
            filters = add_filter(filters, 'withTransportConnectionType',  d.get('connection_type'), to_list) # Фильтрация по виду сообщения
            
            request_body = add_column_search(request_body, 'title', d.get('route_name'))            # Фильтрация по наименованию маршрута
            request_body = add_pagination(request_body, d.get('page', 1), d.get('limit', 25))       # Присовение номера страницы и лимита
            return request_body
        
        def registry_list(request_body, **d):
            """Фильтры для списка реестров маршрутов"""
            response_data = ["items/uuid", "items/route/registration_number", "items/route/number", "items/route/title", "items/contract/number"]
            response_data = d.get('response_data', response_data)
            request_body = add_response_data(request_body, response_data)                               # Какие атрибуты реестров маршрута выводить
            
            filters = request_body['headers']['meta']['filters']
            filters = add_filter(filters, 'withUuid',            d.get('registry_uuid'), to_list)       # Фильтрация по идентификатору
            filters = add_filter(filters, 'withStatus',          d.get('status'), to_list)              # Фильтрация по статусам
            filters = add_filter(filters, 'withRoute',           d.get('route_uuid'), to_str)           # Фильтрация по маршруту
            filters = add_filter(filters, 'withRouteRegNumbers', d.get('route_reg_number'), to_list)    # Фильтрация по рег номеру маршрута
            filters = add_filter(filters, 'withRouteNumbers',    d.get('route_number'), to_list)        # Фильтрация по номеру маршрута
            filters = add_filter(filters, 'withRouteTypes',      d.get('route_type'), to_list)          # Фильтрация по типу маршрута
            filters = add_filter(filters, 'withRouteKinds',      d.get('route_kind'), to_list)          # Фильтрация по виду маршрута
            filters = add_filter(filters, 'withVisId',           d.get('vis_transport_id'), to_str)     # Фильтрация по идентификатору ВИС Транспорт
            filters = add_filter(filters, 'withUnits',           d.get('units'), to_list)               # Фильтрация по организаторам перевозок
            filters = add_filter(filters, 'withCarriers',        d.get('carriers'), to_list)            # Фильтрация по перевозчикам
            filters = add_filter(filters, 'withContracts',       d.get('contracts'), to_list)           # Фильтрация по контрактам
            filters = add_filter(filters, 'withContractWorkPeriod', d.get('contract_period'), to_list)  # Фильтрация по периоду перевозок контракта $parameters - [string $dateFrom, string $dateTo]
            filters = add_filter(filters, 'withRouteTransportConnectionTypes', d.get('connection_type'), to_list) # Фильтрация по виду сообщения
            
            request_body = add_column_search(request_body, 'route.title',     d.get('route_name'))      # Фильтрация по наименованию маршрута
            request_body = add_column_search(request_body, 'contract.number', d.get('contract_number')) # Фильтрация по номеру контракта
            request_body = add_pagination(request_body, d.get('page', 1), d.get('limit', 25))           # Присовение номера страницы и лимита
            return request_body

        def variant_list(request_body, **d):
            """Фильтры для списка реестров маршрутов"""
            response_data = d.get('response_data')
            request_body = add_response_data(request_body, response_data)                     # Какие атрибуты варианта маршрута выводить
            
            filters = request_body['headers']['meta']['filters']
            filters = add_filter(filters, 'withRoute',      d.get('route_uuid'), to_str)    # Фильтрация по идентификатору паспорта маршрута
            filters = add_filter(filters, 'withStopPoint',  d.get('busstop'), to_str)       # Фильтрация по идентификатору входящей в маршрут остановки
            filters = add_filter(filters, 'withIsStopPointList',     d.get('stop_point_list', False))
            filters = add_filter(filters, 'appendChildrenAttribute', d.get('children_attribute', True))
            
            request_body = add_pagination(request_body, d.get('page', 1), d.get('limit', 25)) # Присовение номера страницы и лимита
            return request_body
    
    class Order:
        def list_(request_body, **d):
            '''Фильтры для списка план-нарядов'''
            response_data = d.get('response_data')
            request_body = add_response_data(request_body, response_data)                               # Какие атрибуты ПН выводить
            
            filters = request_body['headers']['meta']['filters']
            filters = add_filter(filters, 'withUuid',              d.get('order_uuid'), to_list)        # Фильтрация по идентификатору ПН
            filters = add_filter(filters, 'withDate',              d.get('date'), to_str)               # Фильтрация по дате план-наряда (в формате YYYY-MM-DD)
            filters = add_filter(filters, 'withUnits',             d.get('units'), to_list)             # Фильтрация по организаторам перевозок
            filters = add_filter(filters, 'withCarriers',          d.get('carriers'), to_list)          # Фильтрация по перевозчикам
            filters = add_filter(filters, 'withSchedule',          d.get('schedule'), to_str)           # Фильтрация по расписанию
            filters = add_filter(filters, 'withPeriod',            d.get('period'), to_list)            # Фильтрация по периоду $parameters - массив из [$date_from, $date_to]
            filters = add_filter(filters, 'withVehicles',          d.get('vehicles'), to_list)          # Фильтрация по ТС
            filters = add_filter(filters, 'withDrivers',           d.get('drivers'), to_list)           # Фильтрация по водителям
            filters = add_filter(filters, 'withRouteRegNumbers',   d.get('route_reg_number'), to_list)  # Фильтрация по рег. номеру маршрута
            filters = add_filter(filters, 'withRouteNumbers',      d.get('route_number'), to_list)      # Фильтрация по номеру маршрута
            filters = add_filter(filters, 'withExecutionStatuses', d.get('execution'), to_list)         # Фильтрация по статусам выполнения
            filters = add_filter(filters, 'withProvisionStatuses', d.get('provision'), to_list)         # Фильтрация по статусам обеспечения

            request_body = add_column_search(request_body, 'route_name', d.get('route_name'))           # Фильтрация по наименованию маршрута
            request_body = add_column_search(request_body, 'number',     d.get('order_number'))         # Фильтрация по номеру план-наряда
            request_body = add_pagination(request_body, d.get('page', 1), d.get('limit', 25))           # Присовение номера страницы и лимита
            return request_body

        def execution(request_body, **d):
            '''Фильтры для списка план-нарядов'''
            response_data = d.get('response_data')
            request_body = add_response_data(request_body, response_data)                           # Какие атрибуты ПН выводить
            
            filters = request_body['headers']['meta']['filters']
            filters = add_filter(filters, 'withOrderRuns',  d.get('run_uuid'), to_list)             # Фильтрация по идентификаторам рейсов
            filters = add_filter(filters, 'withVehicles',   d.get('vehicles'), to_list)             # Фильтрация фильтр по ТС
            filters = add_filter(filters, 'withOrders',     d.get('order_uuid'), to_list)           # Фильтрация по идентификатору план-наряда
            filters = add_filter(filters, 'withPeriod',     d.get('period'), to_list)               # Фильтрация по периоду
            filters = add_filter(filters, 'withUnits',      d.get('units'), to_list)                # Фильтрация по организаторам перевозок
            filters = add_filter(filters, 'withTypes',      d.get('run_type'), to_list)             # Фильтрация по типу рейсов
            filters = add_filter(filters, 'current',        d.get('current'))                       # Фильтрация по выполняемым в данный момент рейсам
            request_body = add_pagination(request_body, d.get('page', 1), d.get('limit', 300))      # Присовение номера страницы и лимита
            return request_body