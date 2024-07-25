from ....request import Request


def to_list(**d):
    json = Request.Body.default()            # Дефолтный JSON
    Request.Body.token(json, d.get('token')) # token

    # Фильтры по ключу можно добавить функции 'to_str', 'to_list'
    Request.Body.filters(json, 'short', d.get('short', True))         # фильтрация short
    Request.Body.filters(json, 'withUuid', d.get('uuid'), 'to_list')  # фильтрация по идентификаторам 
    Request.Body.filters(json, 'withDate', d.get('date'), 'to_str')   # фильтрация по дате план-наряда (в формате YYYY-MM-DD)
    Request.Body.filters(json, 'withUnits', d.get('unit'), 'to_list') # фильтрация по организаторам перевозок
    Request.Body.filters(json, 'withPeriod', d.get('period'), 'to_list')    # Фильтр по периоду $parameters - массив из [$date_from, $date_to]
    Request.Body.filters(json, 'withDrivers', d.get('driver'), 'to_list')   # фильтрация по водителям
    Request.Body.filters(json, 'withCarriers', d.get('carrier'), 'to_list') # фильтрация по перевозчикам
    Request.Body.filters(json, 'withSchedule', d.get('schedule'), 'to_str') # фильтрация по расписанию
    Request.Body.filters(json, 'withVehicles', d.get('vehicle'), 'to_list') # фильтрация по ТС
    Request.Body.filters(json, 'withComponent', d.get('component', 'kiutr'), 'to_list') # фильтрация по подсистеме
    Request.Body.filters(json, 'withCreatedBy', d.get('creator'), 'to_list') # фильтрация по создателю
    Request.Body.filters(json, 'withRouteKind', d.get('route_kind'), 'to_list')  # фильтрация по виду маршрута
    Request.Body.filters(json, 'withRouteNumbers', d.get('route_number'), 'to_list') # фильтрация по номеру маршрута
    Request.Body.filters(json, 'withRouteRegNumbers', d.get('route_reg_number'), 'to_list') # фильтрация по рег. номеру маршрута
    Request.Body.filters(json, 'withScheduleTurnRuns', d.get('schedule_run'), 'to_list')    # фильтрация по идентификаторам рейсов расписания 
    Request.Body.filters(json, 'withProvisionStatuses', d.get('provision_status'), 'to_list') # фильтрация по статусам обеспечения возможные значения: - full - Обеспечен - none - Не обеспечен - partial - Не полностью обеспечен - overfull - Сверхобеспечен - partial_full - Перекрыт
    Request.Body.filters(json, 'withExecutionStatuses', d.get('execution_status'), 'to_list') # фильтрация по статусам выполнения возможные значения: - none - - - operational_defect - Оперативный брак - potential_fact_defect - Потенциальный фактический брак - fact_defect - Фактический брак - partial - Частичное выполнение - done - Выполнен
    Request.Body.filters(json, 'withProcessingStatuses', d.get('process_status'), 'to_list')  # фильтрация по статусам обработки возможные значения: - draft - оформляется - active - действует - ended - завершен - closed - закрыт - defect - брак планирования

    Request.Body.column_search(json, 'turn', d.get('turn'))     # Поиск по колонке "№ Выхода"
    Request.Body.column_search(json, 'number', d.get('number')) # Поиск по колонке "Номер"
    Request.Body.column_search(json, 'updated_at', d.get('date_update')) # Поиск по колонке "Дата изменения" | "date;2024-06-03;."
    Request.Body.column_search(json, 'route_name', d.get('route_name'))  # Поиск по колонке "Наименование маршрута"

    Request.Body.order(json) # Дефолтная сортировка по UUID
    Request.Body.pagination(json, d.get('page', 1), d.get('limit', 25))   # Пагинация по заданным параметрам
    Request.Body.response_data(json, d.get('response_data'))  # Вывод атрибутов в списке заданные пользователем
    return json