class Help:
    def __init__(self):
        self.data = {
            "com.rnis.auth.action.unit.permissions.list": {
                "request": "Auth.Permission.Unit.read",
                "filter": {},
                "description": "Список структурных прав предприятия по отношению к другим предприятиям"
            },
            "com.rnis.auth.action.unit.permissions.update": {
                "request": "Auth.Permission.Unit.update",
                "filter": {},
                "description": "Сохранение структурных прав предприятия"
            },
            "com.rnis.auth.action.permissions.store": {
                "request": "Auth.Permission.store",
                "filter": {},
                "description": "Обновление набора прав доступа сервиса"
            },
            "com.rnis.auth.action.permission.list": {
                "request": "Auth.Permission.to_list",
                "filter": {},
                "description": "Список доступных прав доступа"
            },
            "com.rnis.auth.event.permissions.collect": {
                "request": "Auth.Permission.update",
                "filter": {},
                "description": "Событие, инициирующее обновление набора прав доступа сервисами"
            },
            "com.rnis.auth.action.user.permissions": {
                "request": "Auth.Permission.user",
                "filter": {},
                "description": "Получение прав пользователя"
            },
            "com.rnis.auth.action.role.create": {
                "request": "Auth.Role.create",
                "filter": {},
                "description": "Создание роли пользователя"
            },
            "com.rnis.auth.action.role.created": {
                "request": "Auth.Role.created",
                "filter": {},
                "description": "Событие создания роли пользователя"
            },
            "com.rnis.auth.action.role.delete": {
                "request": "Auth.Role.delete",
                "filter": {},
                "description": "Удаление роли пользователя"
            },
            "com.rnis.auth.event.role.deleted": {
                "request": "Auth.Role.deleted",
                "filter": {},
                "description": "Событие удаления роли пользователя"
            },
            "com.rnis.auth.action.role.list": {
                "request": "Auth.Role.read",
                "filter": {},
                "description": "Список доступных ролей пользователей"
            },
            "com.rnis.auth.action.role.update": {
                "request": "Auth.Role.update",
                "filter": {},
                "description": "Редактирование роли пользователя"
            },
            "com.rnis.auth.event.role.updated": {
                "request": "Auth.Role.updated",
                "filter": {},
                "description": "Событие редактирования роли пользователя"
            },
            "com.rnis.auth.action.user.position.create": {
                "request": "Auth.User.Position.create",
                "filter": {},
                "description": "Создание записи о должности сотрудника"
            },
            "com.rnis.auth.action.user.position.delete": {
                "request": "Auth.User.Position.delete",
                "filter": {},
                "description": "Удаление записи о должности сотрудника"
            },
            "com.rnis.auth.action.user.dismissals": {
                "request": "Auth.User.Dismissal.read",
                "filter": {},
                "description": "График отклонений сотрудника"
            },
            "com.rnis.auth.action.user.position.update": {
                "request": "Auth.User.Position.update",
                "filter": {},
                "description": "Редактирование записи о должности сотрудника"
            },
            "com.rnis.auth.action.user.education.create": {
                "request": "Auth.User.Education.create",
                "filter": {},
                "description": "Создание записи об учебном заведении сотрудника"
            },
            "com.rnis.auth.action.user.education.delete": {
                "request": "Auth.User.Education.delete",
                "filter": {},
                "description": "Удаление записи об учебном заведении сотрудника"
            },
            "com.rnis.auth.action.user.educations": {
                "request": "Auth.User.Education.read",
                "filter": {},
                "description": "Учебные заведения сотрудника"
            },
            "com.rnis.auth.action.user.education.update": {
                "request": "Auth.User.Education.update",
                "filter": {},
                "description": "Редактирование записи об учебном заведении сотрудника"
            },
            "com.rnis.auth.action.user.positions": {
                "request": "Auth.User.Position.read",
                "filter": {},
                "description": "Должности сотрудника"
            },
            "com.rnis.auth.action.user.by_units.list": {
                "request": "Auth.User.by_unit",
                "filter": {},
                "description": "Список пользователей по предприятиям"
            },
            "com.rnis.auth.action.user.can": {
                "request": "Auth.User.can",
                "filter": {},
                "description": "Проверка структурного права"
            },
            "com.rnis.auth.action.user.create": {
                "request": "Auth.User.create",
                "filter": {},
                "description": "Создание пользователя"
            },
            "com.rnis.auth.event.user.created": {
                "request": "Auth.User.created",
                "filter": {},
                "description": "Событие создания пользователя"
            },
            "com.rnis.auth.action.user.delete": {
                "request": "Auth.User.delete",
                "filter": {},
                "description": "Удаление пользователей"
            },
            "com.rnis.auth.event.user.deleted": {
                "request": "Auth.User.deleted",
                "filter": {},
                "description": "Событие удаления пользователя"
            },
            "com.rnis.auth.action.user.get": {
                "request": "Auth.User.read",
                "filter": {},
                "description": "Получение информации о пользователе"
            },
            "com.rnis.auth.action.user.refresh": {
                "request": "Auth.User.refresh",
                "filter": {},
                "description": "Сброс сессии пользователя"
            },
            "com.rnis.auth.action.user.search": {
                "request": "Auth.User.search",
                "filter": {},
                "description": "Поиск пользователей"
            },
            "com.rnis.auth.action.user.tachographs": {
                "request": "Auth.User.tachograph",
                "filter": {},
                "description": "Тахографы водителя"
            },
            "com.rnis.auth.action.user.list": {
                "request": "Auth.User.to_list",
                "filter": {},
                "description": "Список пользователей"
            },
            "com.rnis.auth.action.user.update": {
                "request": "Auth.User.update",
                "filter": {},
                "description": "Редактирование пользователя"
            },
            "com.rnis.auth.event.user.updated": {
                "request": "Auth.User.updated",
                "filter": {},
                "description": "Событие редактирования пользователя"
            },
            "com.rnis.auth.action.entity": {
                "request": "Auth.entity",
                "filter": {},
                "description": "Запрос сущности"
            },
            "com.rnis.auth.action.login": {
                "request": "Auth.login",
                "filter": {
                    'login': {'type': 'str', 'name': 'Логин'},
                    'password': {'type': 'str', 'name': 'Пароль'},
                },
                "description": "Аутентификация"
            },
            "com.rnis.auth.action.logout": {
                "request": "Auth.logout",
                "filter": {},
                "description": "Деаутентификация"
            },
            "com.rnis.converter.action.convert.docx_to_pdf": {
                "request": "Convert.docx_to_pdf",
                "filter": {},
                "description": "Конвертирование docx в pdf"
            },
            "com.rnis.converter.action.convert.html_to_pdf": {
                "request": "Convert.html_to_pdf",
                "filter": {},
                "description": "Конвертирование html в pdf"
            },
            "com.rnis.converter.action.convert.html_to_xls": {
                "request": "Convert.html_to_xls",
                "filter": {},
                "description": "Конвертирование html в xls"
            },
            "com.rnis.converter.action.convert.png_to_pdf": {
                "request": "Convert.png_to_pdf",
                "filter": {},
                "description": "Конвертирование png в pdf"
            },
            "com.rnis.dictionary.action.create": {
                "request": "Dictionary.create",
                "filter": {},
                "description": "Добавление документа в справочник"
            },
            "com.rnis.dictionary.action.delete": {
                "request": "Dictionary.delete",
                "filter": {},
                "description": "Удаление документа из справочника"
            },
            "com.rnis.dictionary.action.lists": {
                "request": "Dictionary.list_many",
                "filter": {},
                "description": "Получение списка документов нескольких справочников"
            },
            "com.rnis.dictionary.action.meta": {
                "request": "Dictionary.meta",
                "filter": {},
                "description": "Получение мета-информации справочника"
            },
            "com.rnis.dictionary.action.off_day.get": {
                "request": "Dictionary.off_day",
                "filter": {},
                "description": "Получение выходного дня"
            },
            "com.rnis.dictionary.action.find": {
                "request": "Dictionary.read",
                "filter": {},
                "description": "Получение документа справочника по uuid"
            },
            "com.rnis.dictionary.action.structure": {
                "request": "Dictionary.structure",
                "filter": {},
                "description": "Получение структуры справочников"
            },
            "com.rnis.dictionary.action.list": {
                "request": "Dictionary.to_list",
                "filter": {},
                "description": "Получение списка документов"
            },
            "com.rnis.dictionary.action.update": {
                "request": "Dictionary.update",
                "filter": {},
                "description": "Обновление документа в справочнике"
            },
            "com.rnis.garbage.action.object.create": {
                "request": "Garbage.create",
                "filter": {},
                "description": "Создание объекта"
            },
            "com.rnis.garbage.action.object.delete": {
                "request": "Garbage.delete",
                "filter": {},
                "description": "Удаление объекта"
            },
            "com.rnis.garbage.action.object.get": {
                "request": "Garbage.read",
                "filter": {},
                "description": "Получение объекта"
            },
            "com.rnis.garbage.action.object.list": {
                "request": "Garbage.to_list",
                "filter": {},
                "description": "Получение списка объектов"
            },
            "com.rnis.garbage.action.object.update": {
                "request": "Garbage.update",
                "filter": {},
                "description": "Редактирование объекта"
            },
            "com.rnis.geo.action.stop_point_pavilion.create": {
                "request": "Geo.BusStop.Pavilion.create",
                "filter": {},
                "description": "Создание остановочного павильона"
            },
            "com.rnis.geo.action.stop_point_pavilion.delete": {
                "request": "Geo.BusStop.Pavilion.delete",
                "filter": {},
                "description": "Удаление остановочного павильона"
            },
            "com.rnis.geo.action.stop_point_pavilion.get": {
                "request": "Geo.BusStop.Pavilion.read",
                "filter": {},
                "description": "Получение остановочного павильона по идентификатору"
            },
            "com.rnis.geo.action.stop_point_pavilion.list": {
                "request": "Geo.BusStop.Pavilion.to_list",
                "filter": {},
                "description": "Получение списка остановочных павильонов"
            },
            "com.rnis.geo.action.stop_point_pavilion.update": {
                "request": "Geo.BusStop.Pavilion.update",
                "filter": {},
                "description": "Редактирование остановочного павильона"
            },
            "com.rnis.geo.action.stop_point.closest.get": {
                "request": "Geo.BusStop.closest",
                "filter": {},
                "description": "Получение ближайшей остановки по координатам"
            },
            "com.rnis.geo.action.stop_point.find_by_coords": {
                "request": "Geo.BusStop.coord",
                "filter": {},
                "description": "Поиск остановок по координатам"
            },
            "com.rnis.geo.action.stop_point.create": {
                "request": "Geo.BusStop.create",
                "filter": {},
                "description": "Создание остановки"
            },
            "com.rnis.geo.action.stop_point.delete": {
                "request": "Geo.BusStop.delete",
                "filter": {},
                "description": "Удаление записи остановки по uuid"
            },
            "com.rnis.geo.action.stop_point.get": {
                "request": "Geo.BusStop.read",
                "filter": {},
                "description": "Получение остановки по uuid"
            },
            "com.rnis.geo.action.stop_point.routes": {
                "request": "Geo.BusStop.route",
                "filter": {},
                "description": "Получение данных по маршрутам, проходящим через остановку"
            },
            "com.rnis.geo.action.stop_point.route.runs": {
                "request": "Geo.BusStop.run",
                "filter": {},
                "description": "Получение данных по рейсам маршрута, проходящим через остановку"
            },
            "com.rnis.geo.action.stop_point.list": {
                "request": "Geo.BusStop.to_list",
                "filter": {},
                "description": "Получение всех текущих записей остановок"
            },
            "com.rnis.geo.action.stop_point.update": {
                "request": "Geo.BusStop.update",
                "filter": {},
                "description": "Обновление записи остановки по uuid"
            },
            "com.rnis.geo.action.contract.create": {
                "request": "Geo.Contract.create",
                "filter": {},
                "description": "Создание контракта"
            },
            "com.rnis.geo.action.contract.delete": {
                "request": "Geo.Contract.delete",
                "filter": {},
                "description": "Удаление контракта"
            },
            "com.rnis.geo.action.contract.plan_summary": {
                "request": "Geo.Contract.plan",
                "filter": {},
                "description": "Получение сводной информации по плану ТС контракта"
            },
            "com.rnis.geo.action.contract.get": {
                "request": "Geo.Contract.read",
                "filter": {},
                "description": "Получение контракта по идентификатору"
            },
            "com.rnis.geo.action.contract.list": {
                "request": "Geo.Contract.to_list",
                "filter": {},
                "description": "Получение списка контрактов"
            },
            "com.rnis.geo.action.contract.units_plan_summary": {
                "request": "Geo.Contract.unit",
                "filter": {},
                "description": "Получение сводной информации по плану ТС контрактов предприятий"
            },
            "com.rnis.geo.action.contract.update": {
                "request": "Geo.Contract.update",
                "filter": {},
                "description": "Редактирование контракта"
            },
            "com.rnis.geo.action.display_configuration.create": {
                "request": "Geo.Display.Configuration.create",
                "filter": {},
                "description": "Создание конфигурации табло"
            },
            "com.rnis.geo.action.display_configuration.delete": {
                "request": "Geo.Display.Configuration.delete",
                "filter": {},
                "description": "Удаление конфигурации табло по uuid"
            },
            "com.rnis.geo.action.display_configuration.get": {
                "request": "Geo.Display.Configuration.read",
                "filter": {},
                "description": "Получение конфигурации табло по uuid"
            },
            "com.rnis.geo.action.display_configuration.list": {
                "request": "Geo.Display.Configuration.to_list",
                "filter": {},
                "description": "Получение списка конфигураций табло"
            },
            "com.rnis.geo.action.display_configuration.update": {
                "request": "Geo.Display.Configuration.update",
                "filter": {},
                "description": "Обновление конфигурации табло по uuid"
            },
            "com.rnis.geo.action.display_log.create": {
                "request": "Geo.Display.Log.create",
                "filter": {},
                "description": "Создание лога табло"
            },
            "com.rnis.geo.action.display_log.list": {
                "request": "Geo.Display.Log.read",
                "filter": {},
                "description": "Получение логов табло"
            },
            "com.rnis.geo.action.display.create": {
                "request": "Geo.Display.create",
                "filter": {},
                "description": "Создание табло"
            },
            "com.rnis.geo.action.display.delete": {
                "request": "Geo.Display.delete",
                "filter": {},
                "description": "Удаление табло по uuid"
            },
            "com.rnis.geo.action.display.get": {
                "request": "Geo.Display.read",
                "filter": {},
                "description": "Получение табло по uuid"
            },
            "com.rnis.geo.action.display.list": {
                "request": "Geo.Display.to_list",
                "filter": {},
                "description": "Получение списка табло"
            },
            "com.rnis.geo.action.display.update": {
                "request": "Geo.Display.update",
                "filter": {},
                "description": "Обновление табло по uuid"
            },
            "com.rnis.geo.action.layer.create": {
                "request": "Geo.Layer.create",
                "filter": {},
                "description": "Создание слоя"
            },
            "com.rnis.geo.action.layer.delete": {
                "request": "Geo.Layer.delete",
                "filter": {},
                "description": "Удаление слоя по uuid"
            },
            "com.rnis.geo.action.layer.get": {
                "request": "Geo.Layer.read",
                "filter": {},
                "description": "Получение слоя по uuid"
            },
            "com.rnis.geo.action.layer.list": {
                "request": "Geo.Layer.to_list",
                "filter": {},
                "description": "Получение всех слоев"
            },
            "com.rnis.geo.action.layer.update": {
                "request": "Geo.Layer.update",
                "filter": {},
                "description": "Обновление слоя по uuid"
            },
            "com.rnis.geo.action.user_geo_object.create": {
                "request": "Geo.Object.create",
                "filter": {},
                "description": "Создание пользовательского объекта"
            },
            "com.rnis.geo.action.user_geo_object.delete": {
                "request": "Geo.Object.delete",
                "filter": {},
                "description": "Удаление пользовательского объекта по uuid"
            },
            "com.rnis.geo.action.user_geo_object.list_by_layers": {
                "request": "Geo.Object.layer",
                "filter": {},
                "description": "Получение всех пользовательских объектов по массиву слоев"
            },
            "com.rnis.geo.action.user_geo_object.mo": {
                "request": "Geo.Object.mo",
                "filter": {},
                "description": "Получение всех МО"
            },
            "com.rnis.geo.action.user_geo_object.get": {
                "request": "Geo.Object.read",
                "filter": {},
                "description": "Получение пользовательского объекта по uuid"
            },
            "com.rnis.geo.action.user_geo_object.search": {
                "request": "Geo.Object.search",
                "filter": {},
                "description": "Поиск пользовательских объектов на карте"
            },
            "com.rnis.geo.action.user_geo_object.list": {
                "request": "Geo.Object.to_list",
                "filter": {},
                "description": "Получение всех пользовательских объектов"
            },
            "com.rnis.geo.action.user_geo_object.update": {
                "request": "Geo.Object.update",
                "filter": {},
                "description": "Обновление пользовательского объекта по uuid"
            },
            "com.rnis.geo.action.order.defect.create": {
                "request": "Geo.Order.Defect.create",
                "filter": {},
                "description": "Создание брака план-наряда"
            },
            "com.rnis.geo.action.order.defect.update": {
                "request": "Geo.Order.Defect.update",
                "filter": {},
                "description": "Редактирование брака план-наряда"
            },
            "com.rnis.geo.action.order_execution_recalc.get": {
                "request": "Geo.Order.Execution.read",
                "filter": {},
                "description": "Получение записи пересчета плана выполнения план-наряда"
            },
            "com.rnis.geo.action.order_execution.recalc": {
                "request": "Geo.Order.Execution.recalc",
                "filter": {},
                "description": "Пересчет плана выполнения план-наряда"
            },
            "com.rnis.geo.action.order_execution.statistics": {
                "request": "Geo.Order.Execution.statistic",
                "filter": {},
                "description": "Получение статистики вычислений выполнений план-нарядов"
            },
            "com.rnis.geo.action.order_execution.list": {
                "request": "Geo.Order.Execution.to_list",
                "filter": {},
                "description": "Получение списка выполнений план-нарядов"
            },
            "com.rnis.geo.action.order_execution.units_summary": {
                "request": "Geo.Order.Execution.unit",
                "filter": {},
                "description": "Получение сводной информации по выполнению работы по предприятиям"
            },
            "com.rnis.geo.action.order.list.export.get": {
                "request": "Geo.Order.Export.read",
                "filter": {},
                "description": "Получение результата экспорта план-нарядов"
            },
            "com.rnis.geo.action.order.list.export": {
                "request": "Geo.Order.Export.start",
                "filter": {},
                "description": "Экспорт списка план-нарядов"
            },
            "com.rnis.geo.action.order.list.export.list": {
                "request": "Geo.Order.Export.to_list",
                "filter": {},
                "description": "Получение списка экспорта план-нарядов"
            },
            "com.rnis.geo.action.order_recalc.get": {
                "request": "Geo.Order.Recalc.read",
                "filter": {},
                "description": "Получение пересчитанного план-наряда"
            },
            "com.rnis.geo.action.order_recalc.update": {
                "request": "Geo.Order.Recalc.update",
                "filter": {},
                "description": "Редактирование пересчитанного план-наряда"
            },
            "com.rnis.geo.action.order_run.summary": {
                "request": "Geo.Order.Run.summary",
                "filter": {},
                "description": "Получение сводных данных по план-нарядам"
            },
            "com.rnis.geo.action.order_run.vehicles": {
                "request": "Geo.Order.Run.vehicle",
                "filter": {},
                "description": "Получение списка ТС в рейсах план-наряда"
            },
            "com.rnis.geo.action.order.clone": {
                "request": "Geo.Order.clone",
                "filter": {},
                "description": "Клонирование план-наряда на дату"
            },
            "com.rnis.geo.action.order.delete": {
                "request": "Geo.Order.delete",
                "filter": {},
                "description": "Удаление план-наряда"
            },
            "com.rnis.geo.action.order.drivers_score_summary": {
                "request": "Geo.Order.driver_score",
                "filter": {},
                "description": "Получение сводной информации по рейтингу водителей"
            },
            "com.rnis.geo.action.order.generate": {
                "request": "Geo.Order.generate",
                "filter": {},
                "description": "Запрос на генерацию план-нарядов"
            },
            "com.rnis.geo.action.order.get": {
                "request": "Geo.Order.read",
                "filter": {},
                "description": "Получение план-наряда"
            },
            "com.rnis.geo.action.order.list": {
                "request": "Geo.Order.to_list",
                "filter": {},
                "description": "Получение списка план-нарядов"
            },
            "com.rnis.geo.action.order.update": {
                "request": "Geo.Order.update",
                "filter": {},
                "description": "Редактирование план-наряда"
            },
            "com.rnis.geo.action.order.vehicles": {
                "request": "Geo.Order.vehicle",
                "filter": {},
                "description": "Получение списка ТС из план-нарядов"
            },
            "com.rnis.geo.action.route_deviation.create": {
                "request": "Geo.Route.Deviation.create",
                "filter": {},
                "description": "Переопределение допустимых отклонений маршрута"
            },
            "com.rnis.geo.action.route_deviation.list": {
                "request": "Geo.Route.Deviation.read",
                "filter": {},
                "description": "Получение списка переопределений допустимых отклонений"
            },
            "com.rnis.geo.action.duplication_matrix.calc": {
                "request": "Geo.Route.DuplicationMatrix.calc",
                "filter": {},
                "description": "Получение списка маршрутов для матриц дублирования"
            },
            "com.rnis.geo.action.duplication_matrix.create": {
                "request": "Geo.Route.DuplicationMatrix.create",
                "filter": {},
                "description": "Создание матрицы дублирования"
            },
            "com.rnis.geo.action.duplication_matrix.route_part.list": {
                "request": "Geo.Route.DuplicationMatrix.part",
                "filter": {},
                "description": "Получение списка маршрутов матрицы дублирования по участку"
            },
            "com.rnis.geo.action.duplication_matrix.get": {
                "request": "Geo.Route.DuplicationMatrix.read",
                "filter": {},
                "description": "Получение матрицы дублирования по идентификатору"
            },
            "com.rnis.geo.action.duplication_matrix.recalc": {
                "request": "Geo.Route.DuplicationMatrix.recalc",
                "filter": {},
                "description": "Перерасчет матрицы дублирования"
            },
            "com.rnis.geo.action.duplication_matrix.route.list": {
                "request": "Geo.Route.DuplicationMatrix.route",
                "filter": {},
                "description": "Получение списка маршрутов матрицы дублирования по маршруту"
            },
            "com.rnis.geo.action.duplication_matrix.list": {
                "request": "Geo.Route.DuplicationMatrix.to_list",
                "filter": {},
                "description": "Получение списка матриц дублирования"
            },
            "com.rnis.geo.action.interval_map.clone": {
                "request": "Geo.Route.IntervalMap.clone",
                "filter": {},
                "description": "Клонирование карты интервалов"
            },
            "com.rnis.geo.action.interval_map.create": {
                "request": "Geo.Route.IntervalMap.create",
                "filter": {},
                "description": "Создание карты интервалов"
            },
            "com.rnis.geo.action.interval_map.delete": {
                "request": "Geo.Route.IntervalMap.delete",
                "filter": {},
                "description": "Удаление карты интервалов"
            },
            "com.rnis.geo.action.interval_map.get": {
                "request": "Geo.Route.IntervalMap.read",
                "filter": {},
                "description": "Получение карты интервалов по идентификатору"
            },
            "com.rnis.geo.action.interval_map.list": {
                "request": "Geo.Route.IntervalMap.to_list",
                "filter": {},
                "description": "Получение списка карт интервалов"
            },
            "com.rnis.geo.action.interval_map.update": {
                "request": "Geo.Route.IntervalMap.update",
                "filter": {},
                "description": "Редактирование карты интервалов"
            },
            "com.rnis.geo.action.route_registry.create": {
                "request": "Geo.Route.Registry.create",
                "filter": {},
                "description": "Создание реестра маршрута"
            },
            "com.rnis.geo.action.route_registry.delete": {
                "request": "Geo.Route.Registry.delete",
                "filter": {},
                "description": "Удаление реестра маршрута"
            },
            "com.rnis.geo.action.route_registry.get.fact": {
                "request": "Geo.Route.Registry.fact",
                "filter": {},
                "description": "Получение факта реестра маршрута"
            },
            "com.rnis.geo.action.route_registry.get": {
                "request": "Geo.Route.Registry.read",
                "filter": {},
                "description": "Получение реестра маршрута по идентификатору"
            },
            "com.rnis.geo.action.route_registry.list": {
                "request": "Geo.Route.Registry.to_list",
                "filter": {},
                "description": "Получение списка реестров маршрута"
            },
            "com.rnis.geo.action.route_registry.update": {
                "request": "Geo.Route.Registry.update",
                "filter": {},
                "description": "Редактирование реестра маршрута"
            },
            "com.rnis.geo.action.route_variant.create": {
                "request": "Geo.Route.Variant.create",
                "filter": {},
                "description": "Создание варианта маршрута"
            },
            "com.rnis.geo.action.route_variant.delete": {
                "request": "Geo.Route.Variant.delete",
                "filter": {},
                "description": "Удаление варианта маршрута"
            },
            "com.rnis.geo.action.route_variant.get": {
                "request": "Geo.Route.Variant.read",
                "filter": {},
                "description": "Получение варианта маршрута по идентификатору"
            },
            "com.rnis.geo.action.route_variant.list": {
                "request": "Geo.Route.Variant.to_list",
                "filter": {},
                "description": "Получение списка вариантов маршрута"
            },
            "com.rnis.geo.action.route_variant.update": {
                "request": "Geo.Route.Variant.update",
                "filter": {},
                "description": "Редактирование варианта маршрута"
            },
            "com.rnis.geo.action.route.clone": {
                "request": "Geo.Route.clone",
                "filter": {},
                "description": "Клонирование маршрута"
            },
            "com.rnis.geo.action.route.create": {
                "request": "Geo.Route.create",
                "filter": {},
                "description": "Создание маршрута"
            },
            "com.rnis.geo.action.route.delete": {
                "request": "Geo.Route.delete",
                "filter": {},
                "description": "Удаление маршрута по uuid"
            },
            "com.rnis.geo.action.route.clone_fill": {
                "request": "Geo.Route.fill",
                "filter": {},
                "description": "Перенос наполнения маршрута"
            },
            "com.rnis.geo.action.route.mobile.list": {
                "request": "Geo.Route.mobile",
                "filter": {},
                "description": "Получение маршрутов для МП"
            },
            "com.rnis.geo.action.route.get": {
                "request": "Geo.Route.read",
                "filter": {},
                "description": "Получение маршрута по uuid"
            },
            "com.rnis.routing.action.find": {
                "request": "Geo.Route.search",
                "filter": {},
                "description": "Поиск маршрута по из т. А в т. B"
            },
            "com.rnis.geo.action.route.list.short": {
                "request": "Geo.Route.short",
                "filter": {},
                "description": "Получение паспортов маршрутов в коротком формате"
            },
            "com.rnis.geo.action.route.list": {
                "request": "Geo.Route.to_list",
                "filter": {},
                "description": "Получение паспортов маршрутов"
            },
            "com.rnis.geo.action.route.update": {
                "request": "Geo.Route.update",
                "filter": {},
                "description": "Обновление маршрута по uuid"
            },
            "com.rnis.geo.action.formal_schedule.create": {
                "request": "Geo.Schedule.Formal.create",
                "filter": {},
                "description": "Создание формального расписания"
            },
            "com.rnis.geo.action.formal_schedule.delete": {
                "request": "Geo.Schedule.Formal.delete",
                "filter": {},
                "description": "Удаление формального расписания"
            },
            "com.rnis.geo.action.formal_schedule.get": {
                "request": "Geo.Schedule.Formal.read",
                "filter": {},
                "description": "Получение формального расписания по идентификатору"
            },
            "com.rnis.geo.action.formal_schedule.list": {
                "request": "Geo.Schedule.Formal.to_list",
                "filter": {},
                "description": "Получение списка формальных расписаний"
            },
            "com.rnis.geo.action.formal_schedule.update": {
                "request": "Geo.Schedule.Formal.update",
                "filter": {},
                "description": "Редактирование формального расписания"
            },
            "com.rnis.geo.action.portal_schedule": {
                "request": "Geo.Schedule.Portal.read",
                "filter": {},
                "description": "Получение расписания для портала"
            },
            "com.rnis.geo.action.portal_schedule.route": {
                "request": "Geo.Schedule.Portal.route",
                "filter": {},
                "description": "Получение детализации расписания для портала"
            },
            "com.rnis.geo.action.schedule_switch.create": {
                "request": "Geo.Schedule.Switch.create",
                "filter": {},
                "description": "Создание переключения"
            },
            "com.rnis.geo.action.schedule_switch.delete": {
                "request": "Geo.Schedule.Switch.delete",
                "filter": {},
                "description": "Удаление переключения"
            },
            "com.rnis.geo.action.schedule_switch_hide.list": {
                "request": "Geo.Schedule.Switch.h_list",
                "filter": {},
                "description": "Получение списка скрытых переключений"
            },
            "com.rnis.geo.action.schedule_switch_hide.hide": {
                "request": "Geo.Schedule.Switch.hide",
                "filter": {},
                "description": "Скрытие переключения"
            },
            "com.rnis.geo.action.schedule_switch.get": {
                "request": "Geo.Schedule.Switch.read",
                "filter": {},
                "description": "Получение переключения по идентификатору"
            },
            "com.rnis.geo.action.schedule_switch_hide.show": {
                "request": "Geo.Schedule.Switch.show",
                "filter": {},
                "description": "Показ переключения"
            },
            "com.rnis.geo.action.schedule_switch.list": {
                "request": "Geo.Schedule.Switch.to_list",
                "filter": {},
                "description": "Получение списка переключений"
            },
            "com.rnis.geo.action.schedule_switch.update": {
                "request": "Geo.Schedule.Switch.update",
                "filter": {},
                "description": "Редактирование переключения"
            },
            "post.rnis.geo.action.schedule_turn.create": {
                "request": "Geo.Schedule.Turn.create",
                "filter": {},
                "description": "Создание выхода"
            },
            "com.rnis.geo.action.schedule_turn.delete": {
                "request": "Geo.Schedule.Turn.delete",
                "filter": {},
                "description": "Удаление выхода"
            },
            "com.rnis.geo.action.schedule_turn.get": {
                "request": "Geo.Schedule.Turn.read",
                "filter": {},
                "description": "Получение выхода по идентификатору"
            },
            "com.rnis.geo.action.schedule_turn.list": {
                "request": "Geo.Schedule.Turn.to_list",
                "filter": {},
                "description": "Получение списка выходов"
            },
            "com.rnis.geo.action.schedule_turn.update": {
                "request": "Geo.Schedule.Turn.update",
                "filter": {},
                "description": "Редактирование выхода"
            },
            "com.rnis.geo.action.schedule.clone": {
                "request": "Geo.Schedule.clone",
                "filter": {},
                "description": "Клонирование расписания"
            },
            "com.rnis.geo.action.schedule.create": {
                "request": "Geo.Schedule.create",
                "filter": {},
                "description": "Создание расписания"
            },
            "com.rnis.geo.action.schedule.delete": {
                "request": "Geo.Schedule.delete",
                "filter": {},
                "description": "Удаление расписания"
            },
            "com.rnis.geo.action.schedule.get.info": {
                "request": "Geo.Schedule.info",
                "filter": {},
                "description": "Получение информации о расписании по идентификатору"
            },
            "com.rnis.geo.action.schedule.get": {
                "request": "Geo.Schedule.read",
                "filter": {},
                "description": "Получение расписания по идентификатору"
            },
            "com.rnis.geo.action.schedule.list": {
                "request": "Geo.Schedule.to_list",
                "filter": {},
                "description": "Получение списка расписаний"
            },
            "com.rnis.geo.action.schedule.update": {
                "request": "Geo.Schedule.update",
                "filter": {},
                "description": "Редактирование расписания"
            },
            "com.rnis.geo.action.resource.check": {
                "request": "Geo.Service.check",
                "filter": {},
                "description": "Проверка ресурса на допустимость использования"
            },
            "com.rnis.geo.action.driver.summary": {
                "request": "Geo.Service.driver",
                "filter": {},
                "description": "Получение сводки по режиму труда водителя"
            },
            "com.rnis.geo.action.forecast.get": {
                "request": "Geo.Service.forecast",
                "filter": {},
                "description": "Проверка срабатывания оповещений о времени прибытия"
            },
            "com.rnis.geo.action.service.geocoding": {
                "request": "Geo.Service.geocoding",
                "filter": {},
                "description": "Сервис прямого/обратного геокодирования"
            },
            "com.rnis.geo.action.service.routing": {
                "request": "Geo.Service.routing",
                "filter": {},
                "description": "Сервис прокладывания маршрута"
            },
            "com.rnis.geo.action.service.geocoding.search": {
                "request": "Geo.Service.search",
                "filter": {},
                "description": "Сервис поиска"
            },
            "com.rnis.geo.action.ecp_sign_log.list": {
                "request": "Geo.Service.sign_log",
                "filter": {},
                "description": "Получение лога подписания ЭЦП"
            },
            "com.rnis.geo.action.service.routing.streets": {
                "request": "Geo.Service.street",
                "filter": {},
                "description": "Сервис прокладывания маршрута по перечислению улиц"
            },
            "com.rnis.geo.action.territorial_entity.create": {
                "request": "Geo.TerritorialEntity.create",
                "filter": {},
                "description": "Создание ТО"
            },
            "com.rnis.geo.action.territorial_entity.delete": {
                "request": "Geo.TerritorialEntity.delete",
                "filter": {},
                "description": "Удаление записи ТО по uuid"
            },
            "com.rnis.geo.action.territorial_entity.get": {
                "request": "Geo.TerritorialEntity.read",
                "filter": {},
                "description": "Получение ТО по uuid"
            },
            "com.rnis.geo.action.territorial_entity.list": {
                "request": "Geo.TerritorialEntity.to_list",
                "filter": {},
                "description": "Получение списка ТО"
            },
            "com.rnis.geo.action.territorial_entity.update": {
                "request": "Geo.TerritorialEntity.update",
                "filter": {},
                "description": "Обновление записи ТО по uuid"
            },
            "com.rnis.geo.action.daily_violations.get": {
                "request": "Geo.Violation.Daily.read",
                "filter": {},
                "description": "Получение суточного нарушения"
            },
            "com.rnis.geo.action.daily_violations.list": {
                "request": "Geo.Violation.Daily.to_list",
                "filter": {},
                "description": "Получение списка суточных нарушений"
            },
            "com.rnis.geo.action.violations.list": {
                "request": "Geo.Violation.to_list",
                "filter": {},
                "description": "Получение списка нарушений"
            },
            "com.rnis.kurs.action.contract_work.create": {
                "request": "Kurs.Contract.Work.create",
                "filter": {},
                "description": "Создание работы контракта"
            },
            "com.rnis.kurs.action.contract_work.delete": {
                "request": "Kurs.Contract.Work.delete",
                "filter": {},
                "description": "Удаление работы контракта"
            },
            "com.rnis.kurs.action.contract_work.get": {
                "request": "Kurs.Contract.Work.read",
                "filter": {},
                "description": "Получение работы контракта"
            },
            "com.rnis.kurs.action.contract_work.list": {
                "request": "Kurs.Contract.Work.to_list",
                "filter": {},
                "description": "Получение списка работ контракта"
            },
            "com.rnis.kurs.action.contract_work.update": {
                "request": "Kurs.Contract.Work.update",
                "filter": {},
                "description": "Редактирование работы контракта"
            },
            "com.rnis.kurs.action.contract.create": {
                "request": "Kurs.Contract.create",
                "filter": {},
                "description": "Создание контракта"
            },
            "com.rnis.kurs.action.contract.delete": {
                "request": "Kurs.Contract.delete",
                "filter": {},
                "description": "Удаление контракта"
            },
            "com.rnis.kurs.action.drivers.score": {
                "request": "Kurs.Contract.driver_score",
                "filter": {},
                "description": "Получение сводной информации по рейтингу водителей"
            },
            "com.rnis.kurs.action.contract.get": {
                "request": "Kurs.Contract.read",
                "filter": {},
                "description": "Получение контракта"
            },
            "com.rnis.kurs.action.contract.list": {
                "request": "Kurs.Contract.to_list",
                "filter": {},
                "description": "Получение списка контрактов"
            },
            "com.rnis.kurs.action.contract.update": {
                "request": "Kurs.Contract.update",
                "filter": {},
                "description": "Редактирование контракта"
            },
            "com.rnis.kurs.action.repair_program.create": {
                "request": "Kurs.Repair.create",
                "filter": {},
                "description": "Создание программы ремонта"
            },
            "com.rnis.kurs.action.repair_program.delete": {
                "request": "Kurs.Repair.delete",
                "filter": {},
                "description": "Удаление программы ремонта"
            },
            "com.rnis.kurs.action.repair_program.get": {
                "request": "Kurs.Repair.read",
                "filter": {},
                "description": "Получение программы ремонта"
            },
            "com.rnis.kurs.action.repair_program.list": {
                "request": "Kurs.Repair.to_list",
                "filter": {},
                "description": "Получение списка программ ремонта"
            },
            "com.rnis.kurs.action.repair_program.update": {
                "request": "Kurs.Repair.update",
                "filter": {},
                "description": "Редактирование программы ремонта"
            },
            "com.rnis.kurs.action.road_part.create": {
                "request": "Kurs.Road.Part.create",
                "filter": {},
                "description": "Создание части дороги"
            },
            "com.rnis.kurs.action.road_part.delete": {
                "request": "Kurs.Road.Part.delete",
                "filter": {},
                "description": "Удаление части дороги"
            },
            "com.rnis.kurs.action.road_part.get": {
                "request": "Kurs.Road.Part.read",
                "filter": {},
                "description": "Получение части дороги"
            },
            "com.rnis.kurs.action.road_repair_part.get": {
                "request": "Kurs.Road.Part.repair",
                "filter": {},
                "description": "Получение части участка по ремонту дороги"
            },
            "com.rnis.kurs.action.road_part.list": {
                "request": "Kurs.Road.Part.to_list",
                "filter": {},
                "description": "Получение списка частей дорог"
            },
            "com.rnis.kurs.action.road_part.update": {
                "request": "Kurs.Road.Part.update",
                "filter": {},
                "description": "Редактирование части дороги"
            },
            "com.rnis.kurs.action.road.create": {
                "request": "Kurs.Road.create",
                "filter": {},
                "description": "Создание дороги"
            },
            "com.rnis.kurs.action.road.delete": {
                "request": "Kurs.Road.delete",
                "filter": {},
                "description": "Удаление дороги"
            },
            "com.rnis.kurs.action.road.get": {
                "request": "Kurs.Road.read",
                "filter": {},
                "description": "Получение дороги"
            },
            "com.rnis.kurs.action.road.list": {
                "request": "Kurs.Road.to_list",
                "filter": {},
                "description": "Получение списка дорог"
            },
            "com.rnis.kurs.action.road.update": {
                "request": "Kurs.Road.update",
                "filter": {},
                "description": "Редактирование дороги"
            },
            "com.rnis.kurs.action.skpdi_log.list": {
                "request": "Kurs.SKPDI.log",
                "filter": {},
                "description": "Получение логов СКПДИ"
            },
            "com.rnis.kurs.action.skpdi.import.tasks": {
                "request": "Kurs.SKPDI.task",
                "filter": {},
                "description": "Запуск импорта заданий СКПДИ за сегодня"
            },
            "com.rnis.kurs.action.sto_work.create": {
                "request": "Kurs.STO.Work.create",
                "filter": {},
                "description": "Создание работы по СТО"
            },
            "com.rnis.kurs.action.sto_work.delete": {
                "request": "Kurs.STO.Work.delete",
                "filter": {},
                "description": "Удаление работы по СТО"
            },
            "com.rnis.kurs.action.sto_work.get": {
                "request": "Kurs.STO.Work.read",
                "filter": {},
                "description": "Получение работы по СТО"
            },
            "com.rnis.kurs.action.sto_work.list": {
                "request": "Kurs.STO.Work.to_list",
                "filter": {},
                "description": "Получение списка работ по СТО"
            },
            "com.rnis.kurs.action.sto_work.update": {
                "request": "Kurs.STO.Work.update",
                "filter": {},
                "description": "Редактирование работы по СТО"
            },
            "com.rnis.kurs.action.sto.create": {
                "request": "Kurs.STO.create",
                "filter": {},
                "description": "Создание СТО"
            },
            "com.rnis.kurs.action.sto.delete": {
                "request": "Kurs.STO.delete",
                "filter": {},
                "description": "Удаление СТО"
            },
            "com.rnis.kurs.action.sto.get": {
                "request": "Kurs.STO.read",
                "filter": {},
                "description": "Получение СТО"
            },
            "com.rnis.kurs.action.sto.list": {
                "request": "Kurs.STO.to_list",
                "filter": {},
                "description": "Получение списка СТО"
            },
            "com.rnis.kurs.action.sto.update": {
                "request": "Kurs.STO.update",
                "filter": {},
                "description": "Редактирование СТО"
            },
            "com.rnis.kurs.action.supernumerary_situation.create": {
                "request": "Kurs.Situation.create",
                "filter": {},
                "description": "Создание внештатной ситуации"
            },
            "com.rnis.kurs.action.supernumerary_situation.delete": {
                "request": "Kurs.Situation.delete",
                "filter": {},
                "description": "Удаление внештатной ситуации"
            },
            "com.rnis.kurs.action.supernumerary_situation.get": {
                "request": "Kurs.Situation.read",
                "filter": {},
                "description": "Получение внештатной ситуации"
            },
            "com.rnis.kurs.action.supernumerary_situation.list": {
                "request": "Kurs.Situation.to_list",
                "filter": {},
                "description": "Получение списка внештатных ситуаций"
            },
            "com.rnis.kurs.action.supernumerary_situation.update": {
                "request": "Kurs.Situation.update",
                "filter": {},
                "description": "Редактирование внештатной ситуации"
            },
            "com.rnis.kurs.action.maintenance.create": {
                "request": "Kurs.TO.create",
                "filter": {},
                "description": "Создание ТО"
            },
            "com.rnis.kurs.action.maintenance.delete": {
                "request": "Kurs.TO.delete",
                "filter": {},
                "description": "Удаление ТО"
            },
            "com.rnis.kurs.action.maintenance.get": {
                "request": "Kurs.TO.read",
                "filter": {},
                "description": "Получение ТО"
            },
            "com.rnis.kurs.action.maintenance.list": {
                "request": "Kurs.TO.to_list",
                "filter": {},
                "description": "Получение списка ТО"
            },
            "com.rnis.kurs.action.maintenance.update": {
                "request": "Kurs.TO.update",
                "filter": {},
                "description": "Редактирование ТО"
            },
            "com.rnis.kurs.action.task_template.create": {
                "request": "Kurs.Task.Template.create",
                "filter": {},
                "description": "Создание шаблона задания"
            },
            "com.rnis.kurs.action.task_template.delete": {
                "request": "Kurs.Task.Template.delete",
                "filter": {},
                "description": "Удаление шаблона задания"
            },
            "com.rnis.kurs.action.task_template.get": {
                "request": "Kurs.Task.Template.read",
                "filter": {},
                "description": "Получение шаблона задания"
            },
            "com.rnis.kurs.action.task_template.list": {
                "request": "Kurs.Task.Template.to_list",
                "filter": {},
                "description": "Получение списка шаблонов заданий"
            },
            "com.rnis.kurs.action.task_template.update": {
                "request": "Kurs.Task.Template.update",
                "filter": {},
                "description": "Редактирование шаблона задания"
            },
            "com.rnis.kurs.action.task.create": {
                "request": "Kurs.Task.create",
                "filter": {},
                "description": "Создание задания"
            },
            "com.rnis.kurs.action.date.tasks.done_chart": {
                "request": "Kurs.Task.date",
                "filter": {},
                "description": "Получение факта выполнения заданий по датам"
            },
            "com.rnis.kurs.action.task.delete": {
                "request": "Kurs.Task.delete",
                "filter": {},
                "description": "Удаление задания"
            },
            "com.rnis.kurs.action.task.get": {
                "request": "Kurs.Task.read",
                "filter": {},
                "description": "Получение задания"
            },
            "com.rnis.kurs.action.task.repeat": {
                "request": "Kurs.Task.repeat",
                "filter": {},
                "description": "Повтор задания"
            },
            "com.rnis.kurs.action.task.list": {
                "request": "Kurs.Task.to_list",
                "filter": {},
                "description": "Получение списка заданий"
            },
            "com.rnis.kurs.action.unit.tasks.done_chart": {
                "request": "Kurs.Task.unit",
                "filter": {},
                "description": "Получение процента выполнения заданий по предприятиям"
            },
            "com.rnis.kurs.action.task.update": {
                "request": "Kurs.Task.update",
                "filter": {},
                "description": "Редактирование задания"
            },
            "com.rnis.kurs.action.task.import": {
                "request": "Kurs.Task.upload",
                "filter": {},
                "description": "Импорт задания из СКПДИ"
            },
            "com.rnis.kurs.action.task_violation.list": {
                "request": "Kurs.Task.violation",
                "filter": {},
                "description": "Получение списка нарушений"
            },
            "com.rnis.kurs.action.object_visit.list": {
                "request": "Kurs.Task.visit",
                "filter": {},
                "description": "Получение списка посещений объектов"
            },
            "com.rnis.kurs.action.technocard_assign.create": {
                "request": "Kurs.Technocard.Assign.create",
                "filter": {},
                "description": "Создание назначения технологической карты"
            },
            "com.rnis.kurs.action.technocard_assign.delete": {
                "request": "Kurs.Technocard.Assign.delete",
                "filter": {},
                "description": "Удаление назначения технологической карты"
            },
            "com.rnis.kurs.action.technocard_assign.get": {
                "request": "Kurs.Technocard.Assign.read",
                "filter": {},
                "description": "Получение назначений технологической карты"
            },
            "com.rnis.kurs.action.technocard_assign.list": {
                "request": "Kurs.Technocard.Assign.to_list",
                "filter": {},
                "description": "Получение списка назначений технологических карт"
            },
            "com.rnis.kurs.action.technocard_assign.update": {
                "request": "Kurs.Technocard.Assign.update",
                "filter": {},
                "description": "Редактирование назначения технологической карты"
            },
            "com.rnis.kurs.action.technocard.create": {
                "request": "Kurs.Technocard.create",
                "filter": {},
                "description": "Создание технологической карты"
            },
            "com.rnis.kurs.action.technocard.delete": {
                "request": "Kurs.Technocard.delete",
                "filter": {},
                "description": "Удаление технологической карты"
            },
            "com.rnis.kurs.action.technocard.get": {
                "request": "Kurs.Technocard.read",
                "filter": {},
                "description": "Получение технологической карты"
            },
            "com.rnis.kurs.action.technocard.list": {
                "request": "Kurs.Technocard.to_list",
                "filter": {},
                "description": "Получение списка технологических карт"
            },
            "com.rnis.kurs.action.technocard.update": {
                "request": "Kurs.Technocard.update",
                "filter": {},
                "description": "Редактирование технологической карты"
            },
            "com.rnis.kurs.action.vehicle_fuel_event.list": {
                "request": "Kurs.Vehicle.Fuel.event",
                "filter": {},
                "description": "Получение списка событий об уровне топлива"
            },
            "com.rnis.kurs.action.vehicle_fuel_level.list": {
                "request": "Kurs.Vehicle.Fuel.level",
                "filter": {},
                "description": "Получение списка записей об уровне топлива"
            },
            "com.rnis.kurs.action.fuel.recalc": {
                "request": "Kurs.Vehicle.Fuel.recalc",
                "filter": {},
                "description": "Запуск пересчета показаний топлива"
            },
            "com.rnis.kurs.action.vehicle.mechanism.create": {
                "request": "Kurs.Vehicle.Mechanism.create",
                "filter": {},
                "description": "Создание механизма ТС"
            },
            "com.rnis.kurs.action.vehicle.mechanism.delete": {
                "request": "Kurs.Vehicle.Mechanism.delete",
                "filter": {},
                "description": "Удаление механизма ТС"
            },
            "com.rnis.kurs.action.vehicle.mechanism.get": {
                "request": "Kurs.Vehicle.Mechanism.read",
                "filter": {},
                "description": "Получение механизма по ТС"
            },
            "com.rnis.kurs.action.vehicle.mechanism.list": {
                "request": "Kurs.Vehicle.Mechanism.to_list",
                "filter": {},
                "description": "Получение списка механизмов по ТС"
            },
            "com.rnis.kurs.action.vehicle.mechanism.update": {
                "request": "Kurs.Vehicle.Mechanism.update",
                "filter": {},
                "description": "Редактирование механизма ТС"
            },
            "com.rnis.kurs.action.vehicle.work.create": {
                "request": "Kurs.Vehicle.Work.create",
                "filter": {},
                "description": "Создание работы по ТС"
            },
            "com.rnis.kurs.action.vehicle.work.delete": {
                "request": "Kurs.Vehicle.Work.delete",
                "filter": {},
                "description": "Удаление работы по ТС"
            },
            "com.rnis.kurs.action.vehicle.work.get": {
                "request": "Kurs.Vehicle.Work.read",
                "filter": {},
                "description": "Получение работы по ТС"
            },
            "com.rnis.kurs.action.vehicle.work.list": {
                "request": "Kurs.Vehicle.Work.to_list",
                "filter": {},
                "description": "Получение списка работ по ТС"
            },
            "com.rnis.kurs.action.vehicle.work.update": {
                "request": "Kurs.Vehicle.Work.update",
                "filter": {},
                "description": "Редактирование работы по ТС"
            },
            "com.rnis.kurs.action.vehicle.create": {
                "request": "Kurs.Vehicle.create",
                "filter": {},
                "description": "Создание ТС"
            },
            "com.rnis.kurs.action.vehicle.delete": {
                "request": "Kurs.Vehicle.delete",
                "filter": {},
                "description": "Удаление ТС"
            },
            "com.rnis.kurs.action.vehicle.get": {
                "request": "Kurs.Vehicle.read",
                "filter": {},
                "description": "Получение ТС"
            },
            "com.rnis.kurs.action.vehicle.list": {
                "request": "Kurs.Vehicle.to_list",
                "filter": {},
                "description": "Получение списка ТС"
            },
            "com.rnis.kurs.action.vehicle.update": {
                "request": "Kurs.Vehicle.update",
                "filter": {},
                "description": "Редактирование информации о ТС"
            },
            "com.rnis.kurs.action.vehicle.import": {
                "request": "Kurs.Vehicle.upload",
                "filter": {},
                "description": "Импорт ТС"
            },
            "com.rnis.kurs.action.vehicle.import.get": {
                "request": "Kurs.Vehicle.upload_status",
                "filter": {},
                "description": "Получение состояния импорта ТС"
            },
            "com.rnis.kurs.action.waybill.create": {
                "request": "Kurs.Waybill.create",
                "filter": {},
                "description": "Создание путевого листа"
            },
            "com.rnis.kurs.action.waybill.delete": {
                "request": "Kurs.Waybill.delete",
                "filter": {},
                "description": "Удаление путевого листа"
            },
            "com.rnis.kurs.action.waybill.get": {
                "request": "Kurs.Waybill.read",
                "filter": {},
                "description": "Получение путевого листа"
            },
            "com.rnis.kurs.action.waybill.list": {
                "request": "Kurs.Waybill.to_list",
                "filter": {},
                "description": "Получение списка путевых листов"
            },
            "com.rnis.kurs.action.waybill.update": {
                "request": "Kurs.Waybill.update",
                "filter": {},
                "description": "Редактирование путевого листа"
            },
            "com.rnis.mobile.action.bus.get": {
                "request": "Mobile.Bus.read",
                "filter": {},
                "description": "Получение детальной информации об автобусе"
            },
            "com.rnis.mobile.action.route.bus.list": {
                "request": "Mobile.Bus.route",
                "filter": {},
                "description": "Получение автобусов определенного маршрута"
            },
            "com.rnis.mobile.action.bus.routing": {
                "request": "Mobile.Bus.routing",
                "filter": {},
                "description": "Получение маршрута автобуса"
            },
            "com.rnis.mobile.action.bus.list": {
                "request": "Mobile.Bus.to_list",
                "filter": {},
                "description": "Получение автобусов"
            },
            "com.rnis.mobile.action.contact.create": {
                "request": "Mobile.Contact.create",
                "filter": {},
                "description": "Создание контакта"
            },
            "com.rnis.mobile.action.contact.delete": {
                "request": "Mobile.Contact.delete",
                "filter": {},
                "description": "Удаление контакта"
            },
            "com.rnis.mobile.action.contact.get": {
                "request": "Mobile.Contact.read",
                "filter": {},
                "description": "Получение контакта"
            },
            "com.rnis.mobile.action.contact.list": {
                "request": "Mobile.Contact.to_list",
                "filter": {},
                "description": "Получение списка контактов"
            },
            "com.rnis.mobile.action.contact.update": {
                "request": "Mobile.Contact.update",
                "filter": {},
                "description": "Редактирование контакта"
            },
            "com.rnis.mobile.action.notification.create": {
                "request": "Mobile.Notification.create",
                "filter": {},
                "description": "Создание оповещения"
            },
            "com.rnis.mobile.action.notification.delete": {
                "request": "Mobile.Notification.delete",
                "filter": {},
                "description": "Удаление оповещения"
            },
            "com.rnis.mobile.action.notification.list": {
                "request": "Mobile.Notification.to_list",
                "filter": {},
                "description": "Получение списка оповещений"
            },
            "com.rnis.mobile.action.notification.update": {
                "request": "Mobile.Notification.update",
                "filter": {},
                "description": "Редактирование оповещения"
            },
            "com.rnis.mobile.action.mobile_page.get": {
                "request": "Mobile.Page.read",
                "filter": {},
                "description": "Получение текстовой страницы"
            },
            "com.rnis.mobile.action.mobile_page.list": {
                "request": "Mobile.Page.to_list",
                "filter": {},
                "description": "Получение списка текстовых страниц"
            },
            "com.rnis.mobile.action.mobile_page.update": {
                "request": "Mobile.Page.update",
                "filter": {},
                "description": "Редактирование текстовой страницы"
            },
            "com.rnis.mobile.action.favorite_path.create": {
                "request": "Mobile.Path.create",
                "filter": {},
                "description": "Создание записи в \"Мои маршруты\""
            },
            "com.rnis.mobile.action.favorite_path.delete": {
                "request": "Mobile.Path.delete",
                "filter": {},
                "description": "Удаление записи из \"Мои маршруты\""
            },
            "com.rnis.mobile.action.favorite_path.get": {
                "request": "Mobile.Path.read",
                "filter": {},
                "description": "Получение записи \"Мои маршруты\""
            },
            "com.rnis.mobile.action.favorite_path.list": {
                "request": "Mobile.Path.to_list",
                "filter": {},
                "description": "Получение списка \"Мои маршруты\""
            },
            "com.rnis.mobile.action.favorite_path.update": {
                "request": "Mobile.Path.update",
                "filter": {},
                "description": "Редактирование записи в \"Мои маршруты\""
            },
            "com.rnis.mobile.action.favorite_route.create": {
                "request": "Mobile.Route.create",
                "filter": {},
                "description": "Создание записи в \"Мой транспорт\""
            },
            "com.rnis.mobile.action.favorite_route.delete": {
                "request": "Mobile.Route.delete",
                "filter": {},
                "description": "Удаление записи из \"Мой транспорт\""
            },
            "com.rnis.mobile.action.favorite_route.list": {
                "request": "Mobile.Route.to_list",
                "filter": {},
                "description": "Получение списка для \"Мой транспорт\""
            },
            "com.rnis.mobile.action.stop_point.routes": {
                "request": "Mobile.StopPoint.route",
                "filter": {},
                "description": "Получение маршрутов, проходящих через остановку"
            },
            "com.rnis.mobile.action.stop_point.list": {
                "request": "Mobile.StopPoint.to_list",
                "filter": {},
                "description": "Получение остановок"
            },
            "com.rnis.mobile.action.mobile_user.confirm.check": {
                "request": "Mobile.User.Confirm.check",
                "filter": {},
                "description": "Проверка кода подтверждения мобильного пользователя"
            },
            "com.rnis.mobile.action.mobile_user.confirm.send": {
                "request": "Mobile.User.Confirm.send",
                "filter": {},
                "description": "Отправка SMS для подтверждения мобильного пользователя"
            },
            "com.rnis.mobile.action.mobile_user.login": {
                "request": "Mobile.User.login",
                "filter": {},
                "description": "Авторизация мобильного пользователя"
            },
            "com.rnis.mobile.action.mobile_user.login_by_email": {
                "request": "Mobile.User.login_by_email",
                "filter": {},
                "description": "Авторизация мобильного пользователя по email"
            },
            "com.rnis.mobile.action.mobile_user.get": {
                "request": "Mobile.User.read",
                "filter": {},
                "description": "Получение информации о текущем мобильном пользователе"
            },
            "com.rnis.mobile.action.mobile_user.register": {
                "request": "Mobile.User.register",
                "filter": {},
                "description": "Регистрация мобильного пользователя"
            },
            "com.rnis.mobile.action.mobile_user.update": {
                "request": "Mobile.User.update",
                "filter": {},
                "description": "Редактирование мобильного пользователя"
            },
            "com.rnis.mobile.action.mobile_user.push_token.update": {
                "request": "Mobile.User.update_push_token",
                "filter": {},
                "description": "Обновление push token пользователя."
            },
            "com.rnis.mobile.action.complaint.send": {
                "request": "Mobile.complaint",
                "filter": {},
                "description": "Отправка жалобы"
            },
            "com.rnis.mobile.action.search.save": {
                "request": "Mobile.favorite",
                "filter": {},
                "description": "Сохранение результата поиска в избранном"
            },
            "com.rnis.mobile.action.feedback.send": {
                "request": "Mobile.feedback",
                "filter": {},
                "description": "Отправка обратной связи"
            },
            "com.rnis.mobile.action.routing": {
                "request": "Mobile.routing",
                "filter": {},
                "description": "Построение маршрута"
            },
            "com.rnis.mobile.action.search": {
                "request": "Mobile.search",
                "filter": {},
                "description": "Поиск"
            },
            "com.rnis.notifications.action.notification_event.create": {
                "request": "Notification.Event.create",
                "filter": {},
                "description": "Создание события оповещения"
            },
            "com.rnis.notifications.action.notification_event.delete": {
                "request": "Notification.Event.delete",
                "filter": {},
                "description": "Удаление события оповещения"
            },
            "com.rnis.notifications.action.notification_event.get": {
                "request": "Notification.Event.read",
                "filter": {},
                "description": "Получение события оповещения по идентификатору"
            },
            "com.rnis.notifications.action.notification_event.send": {
                "request": "Notification.Event.send",
                "filter": {},
                "description": "Отправка оповещения по идентификатору"
            },
            "com.rnis.notifications.action.notification_event.list": {
                "request": "Notification.Event.to_list",
                "filter": {},
                "description": "Получение списка событий оповещений"
            },
            "com.rnis.notifications.action.notification_event.update": {
                "request": "Notification.Event.update",
                "filter": {},
                "description": "Редактирование события оповещения"
            },
            "com.rnis.notifications.action.event_rule_notification.create": {
                "request": "Notification.EventRule.Notification.create",
                "filter": {},
                "description": "Создание оповещения правила события"
            },
            "com.rnis.notifications.action.event_rule_notification.delete": {
                "request": "Notification.EventRule.Notification.delete",
                "filter": {},
                "description": "Удаление оповещения правила события"
            },
            "com.rnis.notifications.action.event_rule_notification.get": {
                "request": "Notification.EventRule.Notification.read",
                "filter": {},
                "description": "Получение оповещения правила события по идентификатору"
            },
            "com.rnis.notifications.action.event_rule_notification.list": {
                "request": "Notification.EventRule.Notification.to_list",
                "filter": {},
                "description": "Получение списка оповещений правила события"
            },
            "com.rnis.notifications.action.event_rule_notification.update": {
                "request": "Notification.EventRule.Notification.update",
                "filter": {},
                "description": "Редактирование оповещения правила события"
            },
            "com.rnis.notifications.action.event_rule.create": {
                "request": "Notification.EventRule.create",
                "filter": {},
                "description": "Создание правила события"
            },
            "com.rnis.notifications.action.event_rule.delete": {
                "request": "Notification.EventRule.delete",
                "filter": {},
                "description": "Удаление правила события"
            },
            "com.rnis.notifications.action.event_rule.events": {
                "request": "Notification.EventRule.event",
                "filter": {},
                "description": "Получение списка типов событий"
            },
            "com.rnis.notifications.action.event_rule.get": {
                "request": "Notification.EventRule.read",
                "filter": {},
                "description": "Получение правила события по идентификатору"
            },
            "com.rnis.notifications.action.event_rule.list": {
                "request": "Notification.EventRule.to_list",
                "filter": {},
                "description": "Получение списка правил событий"
            },
            "com.rnis.notifications.action.event_rule.update": {
                "request": "Notification.EventRule.update",
                "filter": {},
                "description": "Редактирование правила события"
            },
            "com.rnis.notifications.action.mailing.create": {
                "request": "Notification.Mailing.create",
                "filter": {},
                "description": "Создание шаблона рассылки"
            },
            "com.rnis.notifications.action.mailing.delete": {
                "request": "Notification.Mailing.delete",
                "filter": {},
                "description": "Удаление шаблона рассылки"
            },
            "com.rnis.notifications.action.mailing.get": {
                "request": "Notification.Mailing.read",
                "filter": {},
                "description": "Получение шаблона рассылки по идентификатору"
            },
            "com.rnis.notifications.action.mailing.list": {
                "request": "Notification.Mailing.to_list",
                "filter": {},
                "description": "Получение списка шаблонов рассылки"
            },
            "com.rnis.notifications.action.mailing.update": {
                "request": "Notification.Mailing.update",
                "filter": {},
                "description": "Редактирование шаблона рассылки"
            },
            "com.rnis.notifications.action.speed_violation.drivers.summary": {
                "request": "Notification.SpeedViolation.driver",
                "filter": {},
                "description": "Получение сводки по нарушениям скорости по водителям"
            },
            "com.rnis.notifications.action.speed_violation.journal": {
                "request": "Notification.SpeedViolation.journal",
                "filter": {},
                "description": "Получение списка нарушений скорости по дням"
            },
            "com.rnis.notifications.action.speed_violation.summary": {
                "request": "Notification.SpeedViolation.summary",
                "filter": {},
                "description": "Получение сводки по нарушениям скорости"
            },
            "com.rnis.notifications.action.speed_violation.list": {
                "request": "Notification.SpeedViolation.to_list",
                "filter": {},
                "description": "Получение списка нарушений скорости"
            },
            "com.rnis.notifications.action.user_notification_setting.create": {
                "request": "Notification.User.create",
                "filter": {},
                "description": "Создание пользовательского конфига оповещения"
            },
            "com.rnis.notifications.action.user_notification_setting.delete": {
                "request": "Notification.User.delete",
                "filter": {},
                "description": "Удаление пользовательского конфига оповещения"
            },
            "com.rnis.notifications.action.user_notification_setting.get": {
                "request": "Notification.User.read",
                "filter": {},
                "description": "Получение пользовательского конфига оповещения по идентификатору"
            },
            "com.rnis.notifications.action.user_notification_setting.list": {
                "request": "Notification.User.to_list",
                "filter": {},
                "description": "Получение списка пользовательских конфигов оповещений"
            },
            "com.rnis.notifications.action.user_notification_setting.update": {
                "request": "Notification.User.update",
                "filter": {},
                "description": "Редактирование пользовательского конфига оповещения"
            },
            "com.rnis.notifications.action.count": {
                "request": "Notification.count",
                "filter": {},
                "description": "Получение кол-ва непрочитанных уведомлений"
            },
            "com.rnis.notifications.action.create": {
                "request": "Notification.create",
                "filter": {},
                "description": "Создание уведомления"
            },
            "com.rnis.notifications.action.read": {
                "request": "Notification.read",
                "filter": {},
                "description": "Пометка уведомлений прочитанными"
            },
            "com.rnis.notifications.action.mail.send": {
                "request": "Notification.send",
                "filter": {},
                "description": "Отправка email сообщения"
            },
            "com.rnis.notifications.action.list": {
                "request": "Notification.to_list",
                "filter": {},
                "description": "Получение списка уведомлений"
            },
            "com.rnis.organizational_units.action.carrier.create": {
                "request": "Organization.Carrier.create",
                "filter": {},
                "description": "Создание перевозчика"
            },
            "com.rnis.organizational_units.action.carrier.delete": {
                "request": "Organization.Carrier.delete",
                "filter": {},
                "description": "Удаление перевозчика"
            },
            "com.rnis.organizational_units.action.carrier.get": {
                "request": "Organization.Carrier.read",
                "filter": {},
                "description": "Получение перевозчика"
            },
            "com.rnis.organizational_units.action.carriers": {
                "request": "Organization.Carrier.to_list",
                "filter": {},
                "description": "Получение списка перевозчиков"
            },
            "com.rnis.organizational_units.action.carrier.update": {
                "request": "Organization.Carrier.update",
                "filter": {},
                "description": "Редактирование перевозчика"
            },
            "com.rnis.organizational_units.action.position.create": {
                "request": "Organization.Position.create",
                "filter": {},
                "description": "Создание должности предприятия"
            },
            "com.rnis.organizational_units.action.position.delete": {
                "request": "Organization.Position.delete",
                "filter": {},
                "description": "Удаление должности предприятия"
            },
            "com.rnis.organizational_units.action.position.get": {
                "request": "Organization.Position.read",
                "filter": {},
                "description": "Получение должности предприятия"
            },
            "com.rnis.organizational_units.action.positions": {
                "request": "Organization.Position.to_list",
                "filter": {},
                "description": "Получение списка должностей предприятия"
            },
            "com.rnis.organizational_units.action.position.update": {
                "request": "Organization.Position.update",
                "filter": {},
                "description": "Редактирование должности предприятия"
            },
            "com.rnis.organizational_units.action.unit.children": {
                "request": "Organization.Unit.children",
                "filter": {},
                "description": "Получение дочерних предприятий"
            },
            "com.rnis.organizational_units.action.unit.create": {
                "request": "Organization.Unit.create",
                "filter": {},
                "description": "Создание предприятия"
            },
            "com.rnis.organizational_units.action.unit.delete": {
                "request": "Organization.Unit.delete",
                "filter": {},
                "description": "Удаление предприятия"
            },
            "com.rnis.organizational_units.action.unit.get": {
                "request": "Organization.Unit.read",
                "filter": {},
                "description": "Получение предприятия"
            },
            "com.rnis.organizational_units.action.units": {
                "request": "Organization.Unit.to_list",
                "filter": {},
                "description": "Получение списка предприятий"
            },
            "com.rnis.organizational_units.action.unit.update": {
                "request": "Organization.Unit.update",
                "filter": {},
                "description": "Редактирование предприятия"
            },
            "com.rnis.organizational_units.action.user_groups": {
                "request": "Organization.user_group",
                "filter": {},
                "description": "Получение списка групп пользователей предприятия"
            },
            "com.rnis.portal.action.cooperation_agreement_warnings.create": {
                "request": "Portal.Agreement.Warnings.create",
                "filter": {},
                "description": "Создание предупреждения для соглашения о взаимодействии."
            },
            "com.rnis.portal.action.cooperation_agreement_warnings.list": {
                "request": "Portal.Agreement.Warnings.to_list",
                "filter": {},
                "description": "Получение списка предупреждений для соглашения о взаимодействии."
            },
            "com.rnis.portal.action.cooperation_agreement_warnings.update": {
                "request": "Portal.Agreement.Warnings.update",
                "filter": {},
                "description": "Редактирование предупреждения для соглашения о взаимодействии."
            },
            "com.rnis.portal.action.cooperation_agreements.document": {
                "request": "Portal.Agreement.document",
                "filter": {},
                "description": "Генерация документа соглашения о взаимодействии."
            },
            "com.rnis.portal.action.cooperation_agreements.list": {
                "request": "Portal.Agreement.to_list",
                "filter": {},
                "description": "Получение списка соглашений о взаимодействии."
            },
            "com.rnis.portal.action.cooperation_agreements.update": {
                "request": "Portal.Agreement.update",
                "filter": {},
                "description": "Редактирование соглашение о взаимодействии."
            },
            "com.rnis.portal.action.captcha.get": {
                "request": "Portal.Captcha.read",
                "filter": {},
                "description": "Получение капчи"
            },
            "com.rnis.portal.action.captcha.validate": {
                "request": "Portal.Captcha.validate",
                "filter": {},
                "description": "Валидация капчи"
            },
            "com.rnis.portal.action.confirm_request.create": {
                "request": "Portal.Confirm.create",
                "filter": {},
                "description": "Создание заявления на подтверждение"
            },
            "com.rnis.portal.action.confirm_request.get": {
                "request": "Portal.Confirm.read",
                "filter": {},
                "description": "Получение заявления на подтрвеждение"
            },
            "com.rnis.portal.action.confirm_request.list": {
                "request": "Portal.Confirm.to_list",
                "filter": {},
                "description": "Получение списка заявлений на подтверждение"
            },
            "com.rnis.portal.action.confirm_request.units": {
                "request": "Portal.Confirm.unit",
                "filter": {},
                "description": "Получение списка идентификаторов предприятий"
            },
            "com.rnis.portal.action.confirm_request.update": {
                "request": "Portal.Confirm.update",
                "filter": {},
                "description": "Редактирование заявления на подтверждение"
            },
            "com.rnis.portal.action.faq.create": {
                "request": "Portal.FAQ.create",
                "filter": {},
                "description": "Создание вопрос-ответа"
            },
            "com.rnis.portal.action.faq.delete": {
                "request": "Portal.FAQ.delete",
                "filter": {},
                "description": "Удаление вопрос-ответа"
            },
            "com.rnis.portal.action.faq.get": {
                "request": "Portal.FAQ.read",
                "filter": {},
                "description": "Получение новости"
            },
            "com.rnis.portal.action.faq": {
                "request": "Portal.FAQ.to_list",
                "filter": {},
                "description": "Получение списка вопрос-ответов"
            },
            "com.rnis.portal.action.faq.update": {
                "request": "Portal.FAQ.update",
                "filter": {},
                "description": "Редактирование вопрос-ответа"
            },
            "com.rnis.portal.action.news.create": {
                "request": "Portal.News.create",
                "filter": {},
                "description": "Создание новости"
            },
            "com.rnis.portal.action.news.delete": {
                "request": "Portal.News.delete",
                "filter": {},
                "description": "Удаление новости"
            },
            "com.rnis.portal.action.news.get": {
                "request": "Portal.News.read",
                "filter": {},
                "description": "Получение новости"
            },
            "com.rnis.portal.action.news.tags": {
                "request": "Portal.News.tag",
                "filter": {},
                "description": "Получение тегов новостей"
            },
            "com.rnis.portal.action.news": {
                "request": "Portal.News.to_list",
                "filter": {},
                "description": "Получение списка новостей"
            },
            "com.rnis.portal.action.news.update": {
                "request": "Portal.News.update",
                "filter": {},
                "description": "Редактирование новости"
            },
            "com.rnis.portal.action.page.create": {
                "request": "Portal.Page.create",
                "filter": {},
                "description": "Создание страницы"
            },
            "com.rnis.portal.action.page.delete": {
                "request": "Portal.Page.delete",
                "filter": {},
                "description": "Удаление страницы"
            },
            "com.rnis.portal.action.page.get": {
                "request": "Portal.Page.read",
                "filter": {},
                "description": "Получение страницы"
            },
            "com.rnis.portal.action.pages": {
                "request": "Portal.Page.to_list",
                "filter": {},
                "description": "Получение списка страниц"
            },
            "com.rnis.portal.action.page.update": {
                "request": "Portal.Page.update",
                "filter": {},
                "description": "Редактирование страницы"
            },
            "com.rnis.portal.action.register_request.create.check": {
                "request": "Portal.Register.check",
                "filter": {},
                "description": "Проверка возможности создания заявления на регистрацию"
            },
            "com.rnis.portal.action.register_request.create": {
                "request": "Portal.Register.create",
                "filter": {},
                "description": "Создание заявления на регистрацию"
            },
            "com.rnis.portal.action.register_request.get": {
                "request": "Portal.Register.read",
                "filter": {},
                "description": "Получение заявления на регистрацию"
            },
            "com.rnis.portal.action.register_request.list": {
                "request": "Portal.Register.to_list",
                "filter": {},
                "description": "Получение списка заявлений на регистрацию"
            },
            "com.rnis.portal.action.register_request.update": {
                "request": "Portal.Register.update",
                "filter": {},
                "description": "Редактирование заявления на регистрацию"
            },
            "com.rnis.portal.action.template_document.create": {
                "request": "Portal.TemplateDocument.create",
                "filter": {},
                "description": "Создание шаблона документов."
            },
            "com.rnis.portal.action.template_document.document": {
                "request": "Portal.TemplateDocument.document",
                "filter": {},
                "description": "Генерация тестового документа."
            },
            "com.rnis.portal.action.template_document.get_next_version": {
                "request": "Portal.TemplateDocument.next_version",
                "filter": {},
                "description": "Получить следующую версию шаблона документов."
            },
            "com.rnis.portal.action.template_document.get": {
                "request": "Portal.TemplateDocument.read",
                "filter": {},
                "description": "Получение шаблона документов."
            },
            "com.rnis.portal.action.template_document.list": {
                "request": "Portal.TemplateDocument.to_list",
                "filter": {},
                "description": "Получение списка шаблона документов."
            },
            "com.rnis.portal.action.template_document.update": {
                "request": "Portal.TemplateDocument.update",
                "filter": {},
                "description": "Редактирование шаблона документов."
            },
            "com.rnis.portal.action.feedback.send": {
                "request": "Portal.feedback",
                "filter": {},
                "description": "Отправка сообщения из блока обратной связи"
            },
            "com.rnis.portal.action.login": {
                "request": "Portal.login",
                "filter": {},
                "description": "Аутентификация по заявлению на регистрацию"
            },
            "com.rnis.reports.action.report_schedule.create": {
                "request": "Report.Schedule.create",
                "filter": {},
                "description": "Создание расписания отчета"
            },
            "com.rnis.reports.action.report_schedule.delete": {
                "request": "Report.Schedule.delete",
                "filter": {},
                "description": "Удаление расписания отчета"
            },
            "com.rnis.reports.action.report_schedule.get": {
                "request": "Report.Schedule.read",
                "filter": {},
                "description": "Получение значения расписания отчета"
            },
            "com.rnis.reports.action.report_schedule.list": {
                "request": "Report.Schedule.to_list",
                "filter": {},
                "description": "Получение списка расписаний отчетов"
            },
            "com.rnis.reports.action.report_schedule.update": {
                "request": "Report.Schedule.update",
                "filter": {},
                "description": "Обновление значения расписания отчета"
            },
            "com.rnis.reports.action.tablet.summary.kiutr": {
                "request": "Report.Tablet.kiutr",
                "filter": {},
                "description": "Получение сводных данных для подсистемы"
            },
            "com.rnis.reports.action.tablet.summary": {
                "request": "Report.Tablet.summary",
                "filter": {},
                "description": "Получение сводных данных для главной страницы ПР"
            },
            "com.rnis.reports.action.tablet.summary.unit": {
                "request": "Report.Tablet.unit",
                "filter": {},
                "description": "Получение сводных данных для предприятия"
            },
            "com.rnis.reports.action.report_template.delete": {
                "request": "Report.Template.delete",
                "filter": {},
                "description": "Удаление шаблона отчета"
            },
            "com.rnis.reports.action.report_templates.list": {
                "request": "Report.Template.to_list",
                "filter": {},
                "description": "Список шаблонов отчета"
            },
            "com.rnis.reports.action.reports.list": {
                "request": "Report.available",
                "filter": {},
                "description": "Получение списка отчетов, доступных для построения"
            },
            "com.rnis.reports.action.report.create": {
                "request": "Report.create",
                "filter": {},
                "description": "Запрос на формирование отчета"
            },
            "com.rnis.reports.action.integration_log.create": {
                "request": "Report.integration_log",
                "filter": {},
                "description": "Сохранение лога интеграции"
            },
            "com.rnis.reports.action.report.parameters": {
                "request": "Report.parameter",
                "filter": {},
                "description": "Получение списка параметров отчета"
            },
            "com.rnis.reports.action.document.list": {
                "request": "Report.to_list",
                "filter": {},
                "description": "Получение сформированных отчетов"
            },
            "com.rnis.storage.action.delete": {
                "request": "Storage.delete",
                "filter": {},
                "description": "Удление файла по uuid"
            },
            "com.rnis.storage.action.get": {
                "request": "Storage.read",
                "filter": {},
                "description": "Получение ифнорамиции по файлу по uuid"
            },
            "com.rnis.storage.action.token": {
                "request": "Storage.token",
                "filter": {},
                "description": "Получение токена на загрузку файла"
            },
            "com.rnis.system.action.activity.online": {
                "request": "System.Activity.online",
                "filter": {},
                "description": "Получение мониторингового состояния всех пользователей онлайн"
            },
            "com.rnis.system.action.activity.store": {
                "request": "System.Activity.store",
                "filter": {},
                "description": "Сохранение мониторингового состояния пользователя"
            },
            "com.rnis.system.action.audit.search": {
                "request": "System.Audit.search",
                "filter": {},
                "description": "Поиск записей об изменении сущностей"
            },
            "com.rnis.system.event.audit.store": {
                "request": "System.Audit.store",
                "filter": {},
                "description": "Сохранение изменений сущности"
            },
            "com.rnis.system.action.entity.block": {
                "request": "System.Entity.block",
                "filter": {},
                "description": "Блокирование сущности"
            },
            "com.rnis.system.action.entity.is_blocked": {
                "request": "System.Entity.is_block",
                "filter": {},
                "description": "Проверка - заблокирована ли сущность."
            },
            "com.rnis.system.action.entity.names": {
                "request": "System.Entity.name",
                "filter": {},
                "description": "Получение текстового названия сущностей"
            },
            "com.rnis.system.action.entity.unblock": {
                "request": "System.Entity.unblock",
                "filter": {},
                "description": "Разблокирование сущности"
            },
            "com.rnis.system.action.log.codes": {
                "request": "System.Log.code",
                "filter": {},
                "description": "Получение списка кодов событий"
            },
            "com.rnis.system.action.log.search": {
                "request": "System.Log.search",
                "filter": {},
                "description": "Поиск записей в логе действий"
            },
            "com.rnis.system.event.log.store": {
                "request": "System.Log.store",
                "filter": {},
                "description": "Сохранение действия пользователя"
            },
            "com.rnis.system.maintenance.status": {
                "request": "System.Maintenance.status",
                "filter": {},
                "description": "Получение статуса выполнения технических работ"
            },
            "com.rnis.system.maintenance.latest.time": {
                "request": "System.Maintenance.time",
                "filter": {},
                "description": "Получение времени последнего включения режима обслуживания"
            },
            "com.rnis.system.message.create": {
                "request": "System.Message.create",
                "filter": {},
                "description": "Создание системного сообщения"
            },
            "com.rnis.system.message.delete": {
                "request": "System.Message.delete",
                "filter": {},
                "description": "Удаление системного сообщения"
            },
            "com.rnis.system.message.all": {
                "request": "System.Message.to_list",
                "filter": {},
                "description": "Получение списка сообщений"
            },
            "com.rnis.system.message.update": {
                "request": "System.Message.update",
                "filter": {},
                "description": "Редактирование системного сообщения"
            },
            "com.rnis.system.action.schema.store": {
                "request": "System.Schema.store",
                "filter": {},
                "description": "Обновление схемы аудита"
            },
            "com.rnis.system.event.schema.collect": {
                "request": "System.Schema.update",
                "filter": {},
                "description": "Событие, инициирующее обновление схемы аудита"
            },
            "com.rnis.system.action.table.export.create": {
                "request": "System.Table.create",
                "filter": {},
                "description": "Создание экспорта таблицы"
            },
            "com.rnis.system.action.table.export.get": {
                "request": "System.Table.read",
                "filter": {},
                "description": "Получение результата экспорта таблицы"
            },
            "com.rnis.system.action.table.export.update": {
                "request": "System.Table.update",
                "filter": {},
                "description": "Обновление экспорта таблицы"
            },
            "com.rnis.system.action.tooltip.list": {
                "request": "System.Tooltip.to_list",
                "filter": {},
                "description": "Получение контекстной справки"
            },
            "com.rnis.system.action.tooltip.update": {
                "request": "System.Tooltip.update",
                "filter": {},
                "description": "Редактирование контекстной справки"
            },
            "com.rnis.system.action.trash.search": {
                "request": "System.Trash.search",
                "filter": {},
                "description": "Поиск записей в корзине"
            },
            "com.rnis.system.event.trash.store": {
                "request": "System.Trash.store",
                "filter": {},
                "description": "Сохранение данных в корзине"
            },
            "com.rnis.system.down": {
                "request": "System.down",
                "filter": {},
                "description": "Включение режима выполнения технических работ"
            },
            "com.rnis.system.action.status.get": {
                "request": "System.status",
                "filter": {},
                "description": "Получение статуса сервисов"
            },
            "com.rnis.system.up": {
                "request": "System.up",
                "filter": {},
                "description": "Выключение режима выполнения технических работ"
            },
            "com.rnis.system.action.version": {
                "request": "System.version",
                "filter": {},
                "description": "Получение версии проектов"
            },
            "com.rnis.t1sync.action.device.arhived_telematics": {
                "request": "T1sync.Device.arhive",
                "filter": {},
                "description": "Получение данных об архивной телематике."
            },
            "com.rnis.t1sync.action.device.score": {
                "request": "T1sync.Device.score",
                "filter": {},
                "description": "Получение баллов водителя"
            },
            "com.rnis.t1sync.action.device.find": {
                "request": "T1sync.Device.search",
                "filter": {},
                "description": "Поиск номера БНСО по коду БНСО"
            },
            "com.rnis.t1sync.action.device.tachograph": {
                "request": "T1sync.Device.tachograph",
                "filter": {},
                "description": "Получение показаний тахографа"
            },
            "com.rnis.t1sync.action.history": {
                "request": "T1sync.History.read",
                "filter": {},
                "description": "Получение исторических данных по маршруту для списка устройств"
            },
            "com.rnis.t1sync.action.history.multiple": {
                "request": "T1sync.History.to_list",
                "filter": {},
                "description": "Получение исторических данных по нескольким устройствам"
            },
            "com.rnis.t1sync.action.odometr": {
                "request": "T1sync.Odometr.read",
                "filter": {},
                "description": "Получение показаний одометра по устройству"
            },
            "com.rnis.t1sync.action.odometr.multiple": {
                "request": "T1sync.Odometr.to_list",
                "filter": {},
                "description": "Получение показаний одометра по устройствам"
            },
            "com.rnis.t1sync.action.events": {
                "request": "T1sync.event",
                "filter": {},
                "description": "Получение событий движения для списка устройств"
            },
            "com.rnis.t1sync.action.extended_data": {
                "request": "T1sync.extended",
                "filter": {},
                "description": "Получение значения на порту по устройству"
            },
            "com.rnis.t1sync.action.mileage": {
                "request": "T1sync.mileage",
                "filter": {},
                "description": "Получение пробега по устройству"
            },
            "com.rnis.t1sync.action.motohours": {
                "request": "T1sync.motohour",
                "filter": {},
                "description": "Получение показаний моточасов по устройству"
            },
            "com.rnis.telematics.action.telematics.portal.clustered": {
                "request": "Telematic.Portal.clustered",
                "filter": {},
                "description": "Получение записей телематики для портала c кластеризацией"
            },
            "com.rnis.telematics.action.telematics.portal.get.count": {
                "request": "Telematic.Portal.count",
                "filter": {},
                "description": "Получение общего количества записей телематики для портала"
            },
            "com.rnis.telematics.action.telematics.portal.modified": {
                "request": "Telematic.Portal.modified",
                "filter": {},
                "description": "Получение измененных записей телематики для портала"
            },
            "com.rnis.telematics.action.telematics.portal.get": {
                "request": "Telematic.Portal.read",
                "filter": {},
                "description": "Получение записей телематики для портала"
            },
            "com.rnis.telematics.action.telematics.bounds": {
                "request": "Telematic.bound",
                "filter": {},
                "description": "Получение bounding box телематики"
            },
            "com.rnis.telematics.action.telematics.logs": {
                "request": "Telematic.log",
                "filter": {},
                "description": "Получение записей журнала лога телематики"
            },
            "com.rnis.telematics.action.panics.get": {
                "request": "Telematic.panic",
                "filter": {},
                "description": "Получение записей срабатывания тревожной кнопки"
            },
            "com.rnis.telematics.action.telematics.get": {
                "request": "Telematic.read",
                "filter": {},
                "description": "Получение записей телематики"
            },
            "com.rnis.telematics.action.telematics.store": {
                "request": "Telematic.store",
                "filter": {},
                "description": "Сохранение записей телематики"
            },
            "com.rnis.telematics.action.telematics.all": {
                "request": "Telematic.to_list",
                "filter": {},
                "description": "Получение всех текущих записей телематики"
            },
            "com.rnis.vehicles.action.bnso_to_vehicle.create": {
                "request": "Vehicle.BNSO.Link.create",
                "filter": {},
                "description": "Создание связи БНСО-ТС"
            },
            "com.rnis.vehicles.action.bnso_to_vehicle.delete": {
                "request": "Vehicle.BNSO.Link.delete",
                "filter": {},
                "description": "Удаление связи БНСО-ТС"
            },
            "com.rnis.vehicles.action.bnso_to_vehicle.get": {
                "request": "Vehicle.BNSO.Link.read",
                "filter": {},
                "description": "Получение значения связи БНСО-ТС"
            },
            "com.rnis.vehicles.action.bnso_to_vehicle.update": {
                "request": "Vehicle.BNSO.Link.update",
                "filter": {},
                "description": "Обновление значения связи БНСО-ТС"
            },
            "com.rnis.vehicles.action.bnso.check.link": {
                "request": "Vehicle.BNSO.check",
                "filter": {},
                "description": "Получение адреса для диагностики БНСО"
            },
            "com.rnis.vehicles.action.bnso.create": {
                "request": "Vehicle.BNSO.create",
                "filter": {},
                "description": "Создание БНСО"
            },
            "com.rnis.vehicles.action.bnso.delete": {
                "request": "Vehicle.BNSO.delete",
                "filter": {},
                "description": "Удаление БНСО"
            },
            "com.rnis.vehicles.action.bnso_periods.list": {
                "request": "Vehicle.BNSO.period",
                "filter": {},
                "description": "Получение периодов установки БНСО"
            },
            "com.rnis.vehicles.action.bnso.get": {
                "request": "Vehicle.BNSO.read",
                "filter": {},
                "description": "Получение значения БНСО"
            },
            "com.rnis.vehicles.action.bnso.geo_search": {
                "request": "Vehicle.BNSO.search",
                "filter": {},
                "description": "Поиск текущего БНСО из ТС по Гос номеру"
            },
            "com.rnis.vehicles.action.bnso.list": {
                "request": "Vehicle.BNSO.to_list",
                "filter": {},
                "description": "Получение значения всех БНСО"
            },
            "com.rnis.vehicles.action.bnso.update": {
                "request": "Vehicle.BNSO.update",
                "filter": {},
                "description": "Обновление значения БНСО"
            },
            "com.rnis.vehicles.action.event.create": {
                "request": "Vehicle.Event.create",
                "filter": {},
                "description": "Создание события для модуля мониторинга"
            },
            "com.rnis.vehicles.action.event.list": {
                "request": "Vehicle.Event.to_list",
                "filter": {},
                "description": "Получение списка событий для модуля мониторинга"
            },
            "com.rnis.vehicles.action.graduation_templates.create": {
                "request": "Vehicle.Graduation.Template.create",
                "filter": {},
                "description": "Создание шаблона градуировки"
            },
            "post.rnis.vehicles.action.graduation_templates.delete": {
                "request": "Vehicle.Graduation.Template.delete",
                "filter": {},
                "description": "Удаление шаблона градуировки"
            },
            "com.rnis.vehicles.action.graduation_templates.get": {
                "request": "Vehicle.Graduation.Template.read",
                "filter": {},
                "description": "Получение шаблона градуировки"
            },
            "com.rnis.vehicles.action.graduation_templates.list": {
                "request": "Vehicle.Graduation.Template.to_list",
                "filter": {},
                "description": "Получение списка шаблона градуировок для конфигуратора портов БНСО"
            },
            "com.rnis.vehicles.action.graduation_templates.update": {
                "request": "Vehicle.Graduation.Template.update",
                "filter": {},
                "description": "Обновление шаблона градуировки"
            },
            "com.rnis.vehicles.action.graduation.create": {
                "request": "Vehicle.Graduation.create",
                "filter": {},
                "description": "Создание градуировки для конфигуратора портов БНСО"
            },
            "com.rnis.vehicles.action.graduation.delete": {
                "request": "Vehicle.Graduation.delete",
                "filter": {},
                "description": "Удаление градуировки"
            },
            "com.rnis.vehicles.action.graduation.get": {
                "request": "Vehicle.Graduation.read",
                "filter": {},
                "description": "Получение градуировки для конфигуратора портов БНСО"
            },
            "com.rnis.vehicles.action.graduation.list": {
                "request": "Vehicle.Graduation.to_list",
                "filter": {},
                "description": "Получение списка градуировок для конфигуратора портов БНСО"
            },
            "com.rnis.vehicles.action.graduation.update": {
                "request": "Vehicle.Graduation.update",
                "filter": {},
                "description": "Обновление градуировки для конфигуратора портов БНСО"
            },
            "com.rnis.vehicles.action.port.create": {
                "request": "Vehicle.Port.create",
                "filter": {},
                "description": "Создание порта БНСО для конфигуратора"
            },
            "com.rnis.vehicles.action.port.delete": {
                "request": "Vehicle.Port.delete",
                "filter": {},
                "description": "Удаление порта"
            },
            "com.rnis.vehicles.action.port.get": {
                "request": "Vehicle.Port.read",
                "filter": {},
                "description": "Получение порта БНСО для конфигуратора"
            },
            "com.rnis.vehicles.action.port.list": {
                "request": "Vehicle.Port.to_list",
                "filter": {},
                "description": "Получение списка портов"
            },
            "com.rnis.vehicles.action.port.update": {
                "request": "Vehicle.Port.update",
                "filter": {},
                "description": "Обновление порта"
            },
            "com.rnis.vehicles.action.vehicle.status.update": {
                "request": "Vehicle.Status.update",
                "filter": {},
                "description": "Обновление статуса ТС"
            },
            "com.rnis.vehicles.action.vehicle.status.massive.update": {
                "request": "Vehicle.Status.update_many",
                "filter": {},
                "description": "Массовое обновление статуса ТС"
            },
            "com.rnis.vehicles.action.vehicle.create": {
                "request": "Vehicle.create",
                "filter": {},
                "description": "Создание ТС"
            },
            "com.rnis.vehicles.action.vehicle.delete": {
                "request": "Vehicle.delete",
                "filter": {},
                "description": "Удаление ТС"
            },
            "com.rnis.geo.action.vehicle_idle_time.list": {
                "request": "Vehicle.idle",
                "filter": {},
                "description": "Получение периодов простоя ТС"
            },
            "com.rnis.vehicles.action.vehicle_malfunctions.list": {
                "request": "Vehicle.malfunction",
                "filter": {},
                "description": "Получение списка ремонтов ТС"
            },
            "com.rnis.vehicles.action.vehicle.list.portal": {
                "request": "Vehicle.portal",
                "filter": {},
                "description": "Получение значения всех ТС для портала"
            },
            "com.rnis.vehicles.action.vehicle.get": {
                "request": "Vehicle.read",
                "filter": {},
                "description": "Получение значения ТС"
            },
            "com.rnis.monitoring.action.retrospective": {
                "request": "Vehicle.retrospective",
                "filter": {},
                "description": "Получение ретроспективы ТС"
            },
            "com.rnis.monitoring.action.vehicles.filter": {
                "request": "Vehicle.search",
                "filter": {},
                "description": "Фильтрация списка ТС"
            },
            "com.rnis.vehicles.action.vehicle.list": {
                "request": "Vehicle.to_list",
                "filter": {},
                "description": "Получение значения всех ТС"
            },
            "com.rnis.vehicles.action.vehicle.by_units.list": {
                "request": "Vehicle.unit",
                "filter": {},
                "description": "Получение ТС по предприятиям"
            },
            "com.rnis.vehicles.action.vehicle.update": {
                "request": "Vehicle.update",
                "filter": {},
                "description": "Обновление значения ТС"
            },
            "com.rnis.vehicles.action.vehicle.import": {
                "request": "Vehicle.upload",
                "filter": {},
                "description": "Импорт ТС"
            },
            "com.rnis.vehicles.action.vehicle.import.get": {
                "request": "Vehicle.upload_status",
                "filter": {},
                "description": "Получение состояния импорта ТС"
            },
            "com.rnis.fias.action.get": {
                "request": "FIAS.read",
                "filter": {},
                "description": "Получение записи по идентификатору"
            },
            "com.rnis.fias.action.search": {
                "request": "FIAS.search",
                "filter": {},
                "description": "Поиск по ФИАС"
            },
            "com.rnis.gatn.action.gatn_violation.list": {
                "request": "GATN.to_list",
                "filter": {},
                "description": "Получение списка нарушений"
            },
            "com.rnis.gatn.action.gatn_violation_journal.list": {
                "request": "GATN.journal",
                "filter": {},
                "description": "Получение журнала нарушений"
            },
        }
    
    @property
    def find(self):
        '''Поиск нудного метода'''
        search = input(
            '''Как искать метод?\n
            1. По названию метода
            2. По описанию метода
            '''.replace('    ', '')
        )
        
        if search in ['1', '2']:
            if search == '1':
                self.by_method
            if search == '2':
                self.by_name
        else:
            print('Произошла ошибка')


    @property
    def by_name(self):
        '''Поиск метода по описанию'''
        name = input('''Введите описание метода: ''').lower()
        method = []
        for key, value in self.data.items():
            if name in value['description'].lower():
                method.append(self.data[key])
        self.parse_data(method)


    @property
    def by_method(self):
        '''Поиск метода по названию'''
        method = input('''Введите метод: ''')
        method = self.data.get(method)
        method = [method] if method is not None else []
        self.parse_data(method)


    @property
    def default_filter(self):
        return {
            'delay': {'type': 'int', 'name': 'Задержка в секундах'},
            'retries': {'type': 'int', 'name': 'Кол-во повторных попыток'},
            'print_error': {'type': 'bool', 'name': 'Вывод ошибки'},
            'all_pages': {'type': 'bool', 'name': 'Загрузка всех страниц'},
            'concurrency': {'type': 'int', 'name': 'Кол-во потоков запросов'},
            'uuid_list': {'type': 'any', 'name': 'Список идентификаторов'},
        }


    def parse_data(self, method):
        if len(method) != 0:
            for i, m in enumerate(method, 1):
                print(f'''
                    Метод № {i}
                    Вызов:\t\t{m['request']}
                    Описание:\t{m['description']}
                    '''.replace('    ', '')
                )
                print('Стандартные атрибуты:')
                for k,v in self.default_filter.items():
                    print(f' {k}\n  Тип: {v["type"]}\n  Описание: {v["name"]}')
                print('\nАтрибуты:')
                for k,v in m['filter'].items():
                    print(f' {k}\n  Тип: {v["type"]}\n  Описание: {v["name"]}')
                print('\n')
        else:
            print(f'Метод не найден')