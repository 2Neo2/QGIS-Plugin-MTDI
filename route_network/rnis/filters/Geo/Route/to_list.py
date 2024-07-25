from ....request import Request


def to_list(**d):
    json = Request.Body.default()            # Дефолтный JSON
    Request.Body.token(json, d.get('token')) # token
    
    Request.Body.filters(json, 'onlyVis',  d.get('is_vis', False))       # фильтрация по маршрутам ВИС/РНИС
    Request.Body.filters(json, 'withUuid', d.get('uuid'), 'to_list')     # фильтрация по идентификаторам
    Request.Body.filters(json, 'withFile', d.get('file'), 'to_list')     # фильтрация по полю "Образ документа"
    Request.Body.filters(json, 'withUnits',  d.get('unit'), 'to_list')   # фильтрация по организатора перевозок
    Request.Body.filters(json, 'onlyToday',  d.get('is_today'))          # фильтрация по маршрутам, по которым сегодня имеются план-наряды
    Request.Body.filters(json, 'withStatus', d.get('status'), 'to_list') # фильтрация по статусам
    Request.Body.filters(json, 'withActive', d.get('is_active'))         # фильтрация по активности
    Request.Body.filters(json, 'withCarriers',  d.get('carrier'), 'to_list') # фильтрация по перевозчикам
    Request.Body.filters(json, 'withIsPublic',  d.get('public'), 'to_list')  # фильтрация по признаку публичности
    Request.Body.filters(json, 'withRouteType', d.get('route_type'), 'to_list') # фильтрация по типу маршрута
    Request.Body.filters(json, 'withRouteKind', d.get('route_kind'), 'to_list') # фильтрация по виду маршрута
    Request.Body.filters(json, 'withContracts', d.get('contract'), 'to_list')   # фильтрация по контрактам
    Request.Body.filters(json, 'withStopPoint', d.get('stop_point'))  # фильтрация по входящей в маршрут остановке
    Request.Body.filters(json, 'withComponent', d.get('component', ['kiutr']), 'to_str') # фильтрация по подсистеме
    Request.Body.filters(json, 'withParentUuid',  d.get('parent'), 'to_str')    # фильтрация по идентификатору корневого паспорта маршрута
    Request.Body.filters(json, 'withoutGeometry', d.get('is_geometry'))         # фильтрация по наличию геометрии
    Request.Body.filters(json, 'withRouteNumbers',  d.get('number'), 'to_list') # фильтрация по номеру маршрута
    Request.Body.filters(json, 'withOriginalUnits', d.get('original_unit'), 'to_list')           # фильтрация по предприятиям маршрута
    Request.Body.filters(json, 'withRouteRegNumbers',   d.get('registration_number'), 'to_list') # фильтрация по рег. номеру маршрута
    Request.Body.filters(json, 'withTerritorialEntity', d.get('territorial_entity'), 'to_list')  # фильтрация по полю "Территориальные Образования"
    Request.Body.filters(json, 'withTransportConnectionType', d.get('transport_connection'), 'to_list') # фильтрация по виду сообщения
    
    Request.Body.column_search(json, 'version',        d.get('version'))         # Поиск по колонке "Версия"
    Request.Body.column_search(json, 'title',          d.get('name'))            # Поиск по колонке "Наименование"
    Request.Body.column_search(json, 'created_at',     d.get('created_at'))      # Поиск по колонке "Дата внесения"
    Request.Body.column_search(json, 'composed_at',    d.get('composed_at'))     # Поиск по колонке "Дата составления"  Пример: "date;2018-01-01;2018-01-01" или "date;2018-01-01;."
    Request.Body.column_search(json, 'length_total',   d.get('length_total'))    # Поиск по колонке "Общая протяженность, м"  Пример: "number;eq;21030" или "number;lte;21030"
    Request.Body.column_search(json, 'length_forward', d.get('length_forward'))  # Поиск по колонке "Протяженность в прямом направлении, м"  Пример: "number;eq;21030" или "number;lte;21030"
    Request.Body.column_search(json, 'length_reverse', d.get('length_reverse'))  # Поиск по колонке "Протяженность в обратном направлении, м"  Пример: "number;eq;21030" или "number;lte;21030"
    Request.Body.column_search(json, 'communal_municipality_uuid', d.get('mun')) # Поиск по колонке "Мун. образование" (UUID)
    
    Request.Body.order(json)          # Дефолтная сортировка по UUID
    Request.Body.pagination(json, d.get('page', 1), d.get('limit', 25))   # Пагинация по заданным параметрам
    Request.Body.response_data(json, d.get('response_data'))  # Вывод атрибутов в списке заданные пользователем
    return json
