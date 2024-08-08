class Method:
    '''Методы API'''
    def __init__(self, url: str = None) -> None:
        self.url  = 'https://bus.rnis.mosreg.ru/ajax/request?'  # URL РНИС для запросов (дефолт)
        self.host = 'bus.rnis.mosreg.ru'                        # Хост
        if url is not None:
            self.url  = f'https://{url}/ajax/request?'          # URL РНИС для запросов
            self.host = url                                     # Хост


    def get(self, method: str) -> str:
        return self.url + method


    def set(self, url: str) -> None:
        if url is not None:
            self.url  = f'https://{url}/ajax/request?'          # URL РНИС для запросов
            self.host = f'{url}'                                # Хост

    class Auth:
        '''Сервис аутентификация/авторизации'''
        entity = 'com.rnis.auth.action.entity'      # Запрос сущности'''
        login  = 'com.rnis.auth.action.login'       # Аутентификация'''
        logout = 'com.rnis.auth.action.logout'      # Деаутентификация'''

        class Permission:
            '''Права доступа'''
            to_list = 'com.rnis.auth.action.permission.list'            # Список доступных прав доступа'''
            store   = 'com.rnis.auth.action.permissions.store'          # Обновление набора прав доступа сервиса'''
            update  = 'com.rnis.auth.event.permissions.collect'         # Событие, инициирующее обновление набора прав доступа сервисами'''
            user    = 'com.rnis.auth.action.user.permissions'           # Получение прав пользователя'''

            class Unit:
                read   = 'com.rnis.auth.action.unit.permissions.list'   # Список структурных прав предприятия по отношению к другим предприятиям'''
                update = 'com.rnis.auth.action.unit.permissions.update' # Сохранение структурных прав предприятия'''

        class Role:
            '''Роли пользователя'''
            create  = 'com.rnis.auth.action.role.create'           # Создание роли пользователя'''
            read    = 'com.rnis.auth.action.role.list'             # Список доступных ролей пользователей'''
            update  = 'com.rnis.auth.action.role.update'           # Редактирование роли пользователя'''
            delete  = 'com.rnis.auth.action.role.delete'           # Удаление роли пользователя'''
            created = 'com.rnis.auth.action.role.created'          # Событие создания роли пользователя'''
            deleted = 'com.rnis.auth.event.role.deleted'           # Событие удаления роли пользователя'''
            updated = 'com.rnis.auth.event.role.updated'           # Событие редактирования роли пользователя'''

        class User:
            '''Информация о пользователе'''
            create     = 'com.rnis.auth.action.user.create'        # Создание пользователя'''
            read       = 'com.rnis.auth.action.user.get'           # Получение информации о пользователе'''
            update     = 'com.rnis.auth.action.user.update'        # Редактирование пользователя'''
            delete     = 'com.rnis.auth.action.user.delete'        # Удаление пользователей'''
            to_list    = 'com.rnis.auth.action.user.list'          # Список пользователей'''
            created    = 'com.rnis.auth.event.user.created'        # Событие создания пользователя'''
            deleted    = 'com.rnis.auth.event.user.deleted'        # Событие удаления пользователя'''
            updated    = 'com.rnis.auth.event.user.updated'        # Событие редактирования пользователя'''
            search     = 'com.rnis.auth.action.user.search'        # Поиск пользователей'''
            can        = 'com.rnis.auth.action.user.can'           # Проверка структурного права'''
            refresh    = 'com.rnis.auth.action.user.refresh'       # Сброс сессии пользователя'''
            tachograph = 'com.rnis.auth.action.user.tachographs'   # Тахографы водителя'''
            by_unit    = 'com.rnis.auth.action.user.by_units.list' # Список пользователей по предприятиям'''

            class Dismissal:
                '''Должность сотрудника'''
                create  = 'com.rnis.auth.action.user.position.create'      # Создание записи о должности сотрудника'''
                read    = 'com.rnis.auth.action.user.dismissals'           # График отклонений сотрудника'''
                update  = 'com.rnis.auth.action.user.position.update'      # Редактирование записи о должности сотрудника'''
                delete  = 'com.rnis.auth.action.user.position.delete'      # Удаление записи о должности сотрудника'''

            class Education:
                '''Учебное заведение сотрудника'''
                create  = 'com.rnis.auth.action.user.education.create'     # Создание записи об учебном заведении сотрудника'''
                read    = 'com.rnis.auth.action.user.educations'           # Учебные заведения сотрудника'''
                update  = 'com.rnis.auth.action.user.education.update'     # Редактирование записи об учебном заведении сотрудника'''
                delete  = 'com.rnis.auth.action.user.education.delete'     # Удаление записи об учебном заведении сотрудника'''

            class Position:
                '''Должность сотрудника'''
                create  = 'com.rnis.auth.action.user.position.create'      # Создание записи о должности сотрудника'''
                read    = 'com.rnis.auth.action.user.positions'            # Должности сотрудника'''
                update  = 'com.rnis.auth.action.user.position.update'      # Редактирование записи о должности сотрудника'''
                delete  = 'com.rnis.auth.action.user.position.delete'      # Удаление записи о должности сотрудника'''

    class FIAS:
        '''ФИАС'''
        read   = 'com.rnis.fias.action.get'     # Получение записи по идентификатору
        search = 'com.rnis.fias.action.search'  # Поиск по ФИАС

    class GATN:
        '''Нарушения'''
        to_list = 'com.rnis.gatn.action.gatn_violation.list'          # Получение списка нарушений
        journal = 'com.rnis.gatn.action.gatn_violation_journal.list'  # Получение журнала нарушений

    class Geo:
        '''Сервис Гео'''
        class BusStop:
            '''Остановки'''
            create  = 'com.rnis.geo.action.stop_point.create'              # Создание остановки'''
            read    = 'com.rnis.geo.action.stop_point.get'                 # Получение остановки по uuid'''
            update  = 'com.rnis.geo.action.stop_point.update'              # Обновление записи остановки по uuid'''
            delete  = 'com.rnis.geo.action.stop_point.delete'              # Удаление записи остановки по uuid'''
            to_list = 'com.rnis.geo.action.stop_point.list'                # Получение всех текущих записей остановок'''
            closest = 'com.rnis.geo.action.stop_point.closest.get'         # Получение ближайшей остановки по координатам'''
            coord   = 'com.rnis.geo.action.stop_point.find_by_coords'      # Поиск остановок по координатам'''
            route   = 'com.rnis.geo.action.stop_point.routes'              # Получение данных по маршрутам, проходящим через остановку'''
            run     = 'com.rnis.geo.action.stop_point.route.runs'          # Получение данных по рейсам маршрута, проходящим через остановку'''

            class Pavilion:
                '''Остановочный павильон'''
                create  = 'com.rnis.geo.action.stop_point_pavilion.create' # Создание остановочного павильона'''
                read    = 'com.rnis.geo.action.stop_point_pavilion.get'    # Получение остановочного павильона по идентификатору'''
                update  = 'com.rnis.geo.action.stop_point_pavilion.update' # Редактирование остановочного павильона'''
                delete  = 'com.rnis.geo.action.stop_point_pavilion.delete' # Удаление остановочного павильона'''
                to_list = 'com.rnis.geo.action.stop_point_pavilion.list'   # Получение списка остановочных павильонов'''

        class Contract:
            '''Контракты'''
            create  = 'com.rnis.geo.action.contract.create'         # Создание контракта'''
            read    = 'com.rnis.geo.action.contract.get'            # Получение контракта по идентификатору'''
            update  = 'com.rnis.geo.action.contract.update'         # Редактирование контракта'''
            delete  = 'com.rnis.geo.action.contract.delete'         # Удаление контракта'''
            to_list = 'com.rnis.geo.action.contract.list'           # Получение списка контрактов'''
            plan    = 'com.rnis.geo.action.contract.plan_summary'            # Получение сводной информации по плану ТС контракта'''
            unit    = 'com.rnis.geo.action.contract.units_plan_summary'      # Получение сводной информации по плану ТС контрактов предприятий'''

        class Display:
            '''Табло'''
            create  = 'com.rnis.geo.action.display.create'      # Создание табло'''
            read    = 'com.rnis.geo.action.display.get'         # Получение табло по uuid'''
            update  = 'com.rnis.geo.action.display.update'      # Обновление табло по uuid'''
            delete  = 'com.rnis.geo.action.display.delete'      # Удаление табло по uuid'''
            to_list = 'com.rnis.geo.action.display.list'        # Получение списка табло'''

            class Configuration:
                '''Конфигурация табло'''
                create  = 'com.rnis.geo.action.display_configuration.create'        # Создание конфигурации табло'''
                read    = 'com.rnis.geo.action.display_configuration.get'           # Получение конфигурации табло по uuid'''
                update  = 'com.rnis.geo.action.display_configuration.update'        # Обновление конфигурации табло по uuid'''
                delete  = 'com.rnis.geo.action.display_configuration.delete'        # Удаление конфигурации табло по uuid'''
                to_list = 'com.rnis.geo.action.display_configuration.list'          # Получение списка конфигураций табло'''

            class Log:
                '''Лог табло'''
                create = 'com.rnis.geo.action.display_log.create'          # Создание лога табло'''
                read   = 'com.rnis.geo.action.display_log.list'            # Получение логов табло'''

        class Layer:
            '''Слои'''
            create  = 'com.rnis.geo.action.layer.create'      # Создание слоя'''
            read    = 'com.rnis.geo.action.layer.get'         # Получение слоя по uuid'''
            update  = 'com.rnis.geo.action.layer.update'      # Обновление слоя по uuid'''
            delete  = 'com.rnis.geo.action.layer.delete'      # Удаление слоя по uuid'''
            to_list = 'com.rnis.geo.action.layer.list'        # Получение всех слоев'''

        class Order:
            '''План-наряд'''
            generate     = 'com.rnis.geo.action.order.generate'                   # Запрос на генерацию план-нарядов'''
            read         = 'com.rnis.geo.action.order.get'                        # Получение план-наряда'''
            update       = 'com.rnis.geo.action.order.update'                     # Редактирование план-наряда'''
            delete       = 'com.rnis.geo.action.order.delete'                     # Удаление план-наряда'''
            clone        = 'com.rnis.geo.action.order.clone'                      # Клонирование план-наряда на дату'''
            driver_score = 'com.rnis.geo.action.order.drivers_score_summary'      # Получение сводной информации по рейтингу водителей'''
            to_list      = 'com.rnis.geo.action.order.list'                       # Получение списка план-нарядов'''
            vehicle      = 'com.rnis.geo.action.order.vehicles'                   # Получение списка ТС из план-нарядов'''

            class Export:
                '''Экспорт списка план-нарядов'''
                start   = 'com.rnis.geo.action.order.list.export'       # Экспорт списка план-нарядов'''
                read    = 'com.rnis.geo.action.order.list.export.get'   # Получение результата экспорта план-нарядов'''
                to_list = 'com.rnis.geo.action.order.list.export.list'  # Получение списка экспорта план-нарядов'''

            class Defect:
                '''Брак план-наряда'''
                create = 'com.rnis.geo.action.order.defect.create'      # Создание брака план-наряда'''
                update = 'com.rnis.geo.action.order.defect.update'      # Редактирование брака план-наряда'''

            class Execution:
                '''Результаты выполнения план-наряда'''
                details   = 'com.rnis.geo.action.order_execution_details'              # Получение планового и фактического времени план-наряда'''
                read      = 'com.rnis.geo.action.order_execution_recalc.get'           # Получение записи пересчета плана выполнения план-наряда'''
                to_list   = 'com.rnis.geo.action.order_execution.list'                 # Получение списка выполнений план-нарядов'''
                recalc    = 'com.rnis.geo.action.order_execution.recalc'               # Пересчет плана выполнения план-наряда'''
                statistic = 'com.rnis.geo.action.order_execution.statistics'           # Получение статистики вычислений выполнений план-нарядов'''
                unit      = 'com.rnis.geo.action.order_execution.units_summary'        # Получение сводной информации по выполнению работы по предприятиям'''

            class Recalc:
                '''Пересчитанный план-наряд'''
                read   = 'com.rnis.geo.action.order_recalc.get'            # Получение пересчитанного план-наряда'''
                update = 'com.rnis.geo.action.order_recalc.update'         # Редактирование пересчитанного план-наряда'''

            class Run:
                '''Данные по выходам план-наряда'''
                summary = 'com.rnis.geo.action.order_run.summary'   # Получение сводных данных по план-нарядам'''
                vehicle = 'com.rnis.geo.action.order_run.vehicles'  # Получение списка ТС в рейсах план-наряда'''

        class Route:
            '''Маршрут'''
            create  = 'com.rnis.geo.action.route.create'            # Создание маршрута'''
            read    = 'com.rnis.geo.action.route.get'               # Получение маршрута по uuid'''
            update  = 'com.rnis.geo.action.route.update'            # Обновление маршрута по uuid'''
            delete  = 'com.rnis.geo.action.route.delete'            # Удаление маршрута по uuid'''
            to_list = 'com.rnis.geo.action.route.list'              # Получение паспортов маршрутов'''
            short   = 'com.rnis.geo.action.route.list.short'        # Получение паспортов маршрутов в коротком формате'''
            mobile  = 'com.rnis.geo.action.route.mobile.list'       # Получение маршрутов для МП'''
            clone   = 'com.rnis.geo.action.route.clone'             # Клонирование маршрута'''
            fill    = 'com.rnis.geo.action.route.clone_fill'        # Перенос наполнения маршрута'''
            search  = 'com.rnis.routing.action.find'                # Поиск маршрута по из т. А в т. B'''

            class Deviation:
                '''Допустимые отклонения маршрута'''
                create = 'com.rnis.geo.action.route_deviation.create'       # Переопределение допустимых отклонений маршрута'''
                read   = 'com.rnis.geo.action.route_deviation.list'         # Получение списка переопределений допустимых отклонений'''

            class DuplicationMatrix:
                '''Матрица дублирования'''
                create  = 'com.rnis.geo.action.duplication_matrix.create'                   # Создание матрицы дублирования'''
                read    = 'com.rnis.geo.action.duplication_matrix.get'                      # Получение матрицы дублирования по идентификатору'''
                to_list = 'com.rnis.geo.action.duplication_matrix.list'                     # Получение списка матриц дублирования'''
                calc    = 'com.rnis.geo.action.duplication_matrix.calc'                     # Получение списка маршрутов для матриц дублирования'''
                recalc  = 'com.rnis.geo.action.duplication_matrix.recalc'                   # Перерасчет матрицы дублирования'''
                route   = 'com.rnis.geo.action.duplication_matrix.route.list'               # Получение списка маршрутов матрицы дублирования по маршруту'''
                part    = 'com.rnis.geo.action.duplication_matrix.route_part.list'          # Получение списка маршрутов матрицы дублирования по участку'''

            class IntervalMap:
                '''Карты интервалов'''
                create  = 'com.rnis.geo.action.interval_map.create'       # Создание карты интервалов'''
                read    = 'com.rnis.geo.action.interval_map.get'          # Получение карты интервалов по идентификатору'''
                update  = 'com.rnis.geo.action.interval_map.update'       # Редактирование карты интервалов'''
                delete  = 'com.rnis.geo.action.interval_map.delete'       # Удаление карты интервалов'''
                to_list = 'com.rnis.geo.action.interval_map.list'         # Получение списка карт интервалов'''
                clone   = 'com.rnis.geo.action.interval_map.clone'        # Клонирование карты интервалов'''

            class Registry:
                '''Реестр маршрута'''
                create  = 'com.rnis.geo.action.route_registry.create'     # Создание реестра маршрута'''
                read    = 'com.rnis.geo.action.route_registry.get'        # Получение реестра маршрута по идентификатору'''
                update  = 'com.rnis.geo.action.route_registry.update'     # Редактирование реестра маршрута'''
                delete  = 'com.rnis.geo.action.route_registry.delete'     # Удаление реестра маршрута'''
                to_list = 'com.rnis.geo.action.route_registry.list'       # Получение списка реестров маршрута'''
                fact    = 'com.rnis.geo.action.route_registry.get.fact'   # Получение факта реестра маршрута'''

            class Variant:
                '''Вариант маршрута'''
                create  = 'com.rnis.geo.action.route_variant.create'      # Создание варианта маршрута'''
                read    = 'com.rnis.geo.action.route_variant.get'         # Получение варианта маршрута по идентификатору'''
                delete  = 'com.rnis.geo.action.route_variant.delete'      # Удаление варианта маршрута'''
                update  = 'com.rnis.geo.action.route_variant.update'      # Редактирование варианта маршрута'''
                to_list = 'com.rnis.geo.action.route_variant.list'        # Получение списка вариантов маршрута'''

                class NullRun:
                    '''Нулевой рейс варианта маршрута'''
                    create  = 'com.rnis.geo.action.route_variant_null_run.create'      # Создание нулевого рейса варианта маршрута'''
                    read    = 'com.rnis.geo.action.route_variant_null_run.get'         # Получение нулевого рейса варианта маршрута по идентификатору'''
                    update  = 'com.rnis.geo.action.route_variant_null_run.update'      # Редактирование нулевого рейса варианта маршрута'''
                    delete  = 'com.rnis.geo.action.route_variant_null_run.delete'      # Удаление нулевого рейса варианта маршрута'''
                    to_list = 'com.rnis.geo.action.route_variant_null_run.list'        # Получение списка нулевых рейсов вариантов маршрута'''

        class Schedule:
            '''Расписание'''
            create  = 'com.rnis.geo.action.schedule.create'        # Создание расписания'''
            read    = 'com.rnis.geo.action.schedule.get'           # Получение расписания по идентификатору'''
            update  = 'com.rnis.geo.action.schedule.update'        # Редактирование расписания'''
            delete  = 'com.rnis.geo.action.schedule.delete'        # Удаление расписания'''
            to_list = 'com.rnis.geo.action.schedule.list'          # Получение списка расписаний'''
            clone   = 'com.rnis.geo.action.schedule.clone'         # Клонирование расписания'''
            info    = 'com.rnis.geo.action.schedule.get.info'      # Получение информации о расписании по идентификатору'''

            class Switch:
                '''Переключение'''
                create  = 'com.rnis.geo.action.schedule_switch.create'      # Создание переключения'''
                read    = 'com.rnis.geo.action.schedule_switch.get'         # Получение переключения по идентификатору'''
                update  = 'com.rnis.geo.action.schedule_switch.update'      # Редактирование переключения'''
                delete  = 'com.rnis.geo.action.schedule_switch.delete'      # Удаление переключения'''
                to_list = 'com.rnis.geo.action.schedule_switch.list'        # Получение списка переключений'''
                hide    = 'com.rnis.geo.action.schedule_switch_hide.hide'   # Скрытие переключения'''
                show    = 'com.rnis.geo.action.schedule_switch_hide.show'   # Показ переключения'''
                h_list  = 'com.rnis.geo.action.schedule_switch_hide.list'   # Получение списка скрытых переключений'''

            class Turn:
                '''Выход'''
                create  = 'post.rnis.geo.action.schedule_turn.create'       # Создание выхода'''
                read    = 'com.rnis.geo.action.schedule_turn.get'           # Получение выхода по идентификатору'''
                update  = 'com.rnis.geo.action.schedule_turn.update'        # Редактирование выхода'''
                delete  = 'com.rnis.geo.action.schedule_turn.delete'        # Удаление выхода'''
                to_list = 'com.rnis.geo.action.schedule_turn.list'          # Получение списка выходов'''

            class Formal:
                '''Формальное расписание'''
                create  = 'com.rnis.geo.action.formal_schedule.create'      # Создание формального расписания'''
                read    = 'com.rnis.geo.action.formal_schedule.get'         # Получение формального расписания по идентификатору'''
                update  = 'com.rnis.geo.action.formal_schedule.update'      # Редактирование формального расписания'''
                delete  = 'com.rnis.geo.action.formal_schedule.delete'      # Удаление формального расписания'''
                to_list = 'com.rnis.geo.action.formal_schedule.list'        # Получение списка формальных расписаний'''

            class Portal:
                '''Расписание для портала'''
                read  = 'com.rnis.geo.action.portal_schedule'               # Получение расписания для портала'''
                route = 'com.rnis.geo.action.portal_schedule.route'         # Получение детализации расписания для портала'''

        class TerritorialEntity:
            '''Территориальное образование'''
            create  = 'com.rnis.geo.action.territorial_entity.create'       # Создание ТО'''
            read    = 'com.rnis.geo.action.territorial_entity.get'          # Получение ТО по uuid'''
            update  = 'com.rnis.geo.action.territorial_entity.update'       # Обновление записи ТО по uuid'''
            delete  = 'com.rnis.geo.action.territorial_entity.delete'       # Удаление записи ТО по uuid'''
            to_list = 'com.rnis.geo.action.territorial_entity.list'         # Получение списка ТО'''

        class Object:
            '''Пользовательского объекты'''
            create  = 'com.rnis.geo.action.user_geo_object.create'          # Создание пользовательского объекта'''
            read    = 'com.rnis.geo.action.user_geo_object.get'             # Получение пользовательского объекта по uuid'''
            update  = 'com.rnis.geo.action.user_geo_object.update'          # Обновление пользовательского объекта по uuid'''
            delete  = 'com.rnis.geo.action.user_geo_object.delete'          # Удаление пользовательского объекта по uuid'''
            to_list = 'com.rnis.geo.action.user_geo_object.list'            # Получение всех пользовательских объектов'''
            layer   = 'com.rnis.geo.action.user_geo_object.list_by_layers'  # Получение всех пользовательских объектов по массиву слоев'''
            mo      = 'com.rnis.geo.action.user_geo_object.mo'              # Получение всех МО'''
            search  = 'com.rnis.geo.action.user_geo_object.search'          # Поиск пользовательских объектов на карте'''

        class Violation:
            '''Список нарушений'''
            to_list = 'com.rnis.geo.action.violations.list'                 # Получение списка нарушений'''

            class Daily:
                '''Список суточных нарушений'''
                read    = 'com.rnis.geo.action.daily_violations.get'        # Получение суточного нарушения'''
                to_list = 'com.rnis.geo.action.daily_violations.list'       # Получение списка суточных нарушений'''

        class Service:
            '''Сервис ГЕО'''
            search    = 'com.rnis.geo.action.search_geo'                    # Поиск объектов на карте'''
            geocoding = 'com.rnis.geo.action.service.geocoding'             # Сервис прямого/обратного геокодирования'''
            search    = 'com.rnis.geo.action.service.geocoding.search'      # Сервис поиска'''
            routing   = 'com.rnis.geo.action.service.routing'               # Сервис прокладывания маршрута'''
            street    = 'com.rnis.geo.action.service.routing.streets'       # Сервис прокладывания маршрута по перечислению улиц'''
            driver    = 'com.rnis.geo.action.driver.summary'                # Получение сводки по режиму труда водителя'''
            sign_log  = 'com.rnis.geo.action.ecp_sign_log.list'             # Получение лога подписания ЭЦП'''
            check     = 'com.rnis.geo.action.resource.check'                # Проверка ресурса на допустимость использования'''
            forecast  = 'com.rnis.geo.action.forecast.get'                  # Проверка срабатывания оповещений о времени прибытия'''

    class Convert:
        '''Сервис конвертирования'''
        docx_to_pdf = 'com.rnis.converter.action.convert.docx_to_pdf'       # Конвертирование docx в pdf'''
        html_to_pdf = 'com.rnis.converter.action.convert.html_to_pdf'       # Конвертирование html в pdf'''
        html_to_xls = 'com.rnis.converter.action.convert.html_to_xls'       # Конвертирование html в xls'''
        png_to_pdf  = 'com.rnis.converter.action.convert.png_to_pdf'        # Конвертирование png в pdf'''

    class Dictionary:
        '''Справочники'''
        create    = 'com.rnis.dictionary.action.create'        # Добавление документа в справочник'''
        read      = 'com.rnis.dictionary.action.find'          # Получение документа справочника по uuid'''
        update    = 'com.rnis.dictionary.action.update'        # Обновление документа в справочнике'''
        delete    = 'com.rnis.dictionary.action.delete'        # Удаление документа из справочника'''
        to_list   = 'com.rnis.dictionary.action.list'          # Получение списка документов'''
        list_many = 'com.rnis.dictionary.action.lists'         # Получение списка документов нескольких справочников'''
        meta      = 'com.rnis.dictionary.action.meta'          # Получение мета-информации справочника'''
        off_day   = 'com.rnis.dictionary.action.off_day.get'   # Получение выходного дня'''
        structure = 'com.rnis.dictionary.action.structure'     # Получение структуры справочников'''
        unit    = 'com.rnis.grpc-proxy.action.units.get.units' # Получение информации о перевозчиках'''

    class Garbage:
        '''Сервис ТКО'''
        create  = 'com.rnis.garbage.action.object.create'      # Создание объекта'''
        read    = 'com.rnis.garbage.action.object.get'         # Получение объекта'''
        update  = 'com.rnis.garbage.action.object.update'      # Редактирование объекта'''
        delete  = 'com.rnis.garbage.action.object.delete'      # Удаление объекта'''
        to_list = 'com.rnis.garbage.action.object.list'        # Получение списка объектов'''

    class Kurs:
        class Contract:
            '''Контракт'''
            create  = 'com.rnis.kurs.action.contract.create'     # Создание контракта'''
            read    = 'com.rnis.kurs.action.contract.get'        # Получение контракта'''
            update  = 'com.rnis.kurs.action.contract.update'     # Редактирование контракта'''
            delete  = 'com.rnis.kurs.action.contract.delete'     # Удаление контракта'''
            to_list = 'com.rnis.kurs.action.contract.list'       # Получение списка контрактов'''
            driver_score = 'com.rnis.kurs.action.drivers.score'  # Получение сводной информации по рейтингу водителей'''

            class Work:
                '''Работы контракта'''
                create  = 'com.rnis.kurs.action.contract_work.create'      # Создание работы контракта'''
                read    = 'com.rnis.kurs.action.contract_work.get'         # Получение работы контракта'''
                update  = 'com.rnis.kurs.action.contract_work.update'      # Редактирование работы контракта'''
                delete  = 'com.rnis.kurs.action.contract_work.delete'      # Удаление работы контракта'''
                to_list = 'com.rnis.kurs.action.contract_work.list'        # Получение списка работ контракта'''

        class Repair:
            '''Программа ремонта'''
            create  = 'com.rnis.kurs.action.repair_program.create'         # Создание программы ремонта'''
            read    = 'com.rnis.kurs.action.repair_program.get'            # Получение программы ремонта'''
            update  = 'com.rnis.kurs.action.repair_program.update'         # Редактирование программы ремонта'''
            delete  = 'com.rnis.kurs.action.repair_program.delete'         # Удаление программы ремонта'''
            to_list = 'com.rnis.kurs.action.repair_program.list'           # Получение списка программ ремонта'''

        class Road:
            '''Дорога'''
            create  = 'com.rnis.kurs.action.road.create'       # Создание дороги'''
            read    = 'com.rnis.kurs.action.road.get'          # Получение дороги'''
            update  = 'com.rnis.kurs.action.road.update'       # Редактирование дороги'''
            delete  = 'com.rnis.kurs.action.road.delete'       # Удаление дороги'''
            to_list = 'com.rnis.kurs.action.road.list'         # Получение списка дорог'''

            class Part:
                '''Часть дороги'''
                create  = 'com.rnis.kurs.action.road_part.create'      # Создание части дороги'''
                read    = 'com.rnis.kurs.action.road_part.get'         # Получение части дороги'''
                update  = 'com.rnis.kurs.action.road_part.update'      # Редактирование части дороги'''
                delete  = 'com.rnis.kurs.action.road_part.delete'      # Удаление части дороги'''
                to_list = 'com.rnis.kurs.action.road_part.list'        # Получение списка частей дорог'''
                repair  = 'com.rnis.kurs.action.road_repair_part.get'  # Получение части участка по ремонту дороги'''

                class WorkType:
                    '''Виды работ'''
                    check     = 'com.rnis.kurs.action.road_part.work_type.check'           # Проверка корректности вида работ по части дороги в соответствии с технологической картой'''
                    read      = 'com.rnis.kurs.action.road_part.work_types'                # Получение видов работ по части дороги в соответствии с технологической картой'''
                    read_many = 'com.rnis.kurs.action.road_part.work_types.multiple'       # Получение видов работ по части дороги в соответствии с технологической картой'''

        class Situation:
            '''Внештатная ситуация'''
            create = 'com.rnis.kurs.action.supernumerary_situation.create'      # Создание внештатной ситуации'''
            read = 'com.rnis.kurs.action.supernumerary_situation.get'           # Получение внештатной ситуации'''
            update = 'com.rnis.kurs.action.supernumerary_situation.update'      # Редактирование внештатной ситуации'''
            delete = 'com.rnis.kurs.action.supernumerary_situation.delete'      # Удаление внештатной ситуации'''
            to_list = 'com.rnis.kurs.action.supernumerary_situation.list'       # Получение списка внештатных ситуаций'''

        class SKPDI:
            '''СКПДИ'''
            task = 'com.rnis.kurs.action.skpdi.import.tasks'   # Запуск импорта заданий СКПДИ за сегодня'''
            log     = 'com.rnis.kurs.action.skpdi_log.list'       # Получение логов СКПДИ'''

        class STO:
            '''СТО'''
            create  = 'com.rnis.kurs.action.sto.create'        # Создание СТО'''
            read    = 'com.rnis.kurs.action.sto.get'           # Получение СТО'''
            update  = 'com.rnis.kurs.action.sto.update'        # Редактирование СТО'''
            delete  = 'com.rnis.kurs.action.sto.delete'        # Удаление СТО'''
            to_list = 'com.rnis.kurs.action.sto.list'          # Получение списка СТО'''

            class Work:
                '''Работы по СТО'''
                create  = 'com.rnis.kurs.action.sto_work.create'    # Создание работы по СТО'''
                read    = 'com.rnis.kurs.action.sto_work.get'       # Получение работы по СТО'''
                update  = 'com.rnis.kurs.action.sto_work.update'    # Редактирование работы по СТО'''
                delete  = 'com.rnis.kurs.action.sto_work.delete'    # Удаление работы по СТО'''
                to_list = 'com.rnis.kurs.action.sto_work.list'      # Получение списка работ по СТО'''

        class TO:
            '''ТО (техническое обслуживание)'''
            create  = 'com.rnis.kurs.action.maintenance.create'     # Создание ТО'''
            read    = 'com.rnis.kurs.action.maintenance.get'        # Получение ТО'''
            update  = 'com.rnis.kurs.action.maintenance.update'     # Редактирование ТО'''
            delete  = 'com.rnis.kurs.action.maintenance.delete'     # Удаление ТО'''
            to_list = 'com.rnis.kurs.action.maintenance.list'       # Получение списка ТО'''

        class Task:
            '''Задания'''
            create  = 'com.rnis.kurs.action.task.create'            # Создание задания'''
            read    = 'com.rnis.kurs.action.task.get'               # Получение задания'''
            update  = 'com.rnis.kurs.action.task.update'            # Редактирование задания'''
            delete  = 'com.rnis.kurs.action.task.delete'            # Удаление задания'''
            to_list = 'com.rnis.kurs.action.task.list'              # Получение списка заданий'''
            upload  = 'com.rnis.kurs.action.task.import'            # Импорт задания из СКПДИ'''
            repeat  = 'com.rnis.kurs.action.task.repeat'            # Повтор задания'''
            date    = 'com.rnis.kurs.action.date.tasks.done_chart'  # Получение факта выполнения заданий по датам'''
            unit    = 'com.rnis.kurs.action.unit.tasks.done_chart'  # Получение процента выполнения заданий по предприятиям'''
            visit = 'com.rnis.kurs.action.object_visit.list'        # Получение списка посещений объектов'''
            violation  = 'com.rnis.kurs.action.task_violation.list' # Получение списка нарушений'''

            class Template:
                '''Шаблон задания'''
                create  = 'com.rnis.kurs.action.task_template.create'      # Создание шаблона задания'''
                read    = 'com.rnis.kurs.action.task_template.get'         # Получение шаблона задания'''
                update  = 'com.rnis.kurs.action.task_template.update'      # Редактирование шаблона задания'''
                delete  = 'com.rnis.kurs.action.task_template.delete'      # Удаление шаблона задания'''
                to_list = 'com.rnis.kurs.action.task_template.list'        # Получение списка шаблонов заданий'''

        class Technocard:
            '''Технологические карты'''
            create = 'com.rnis.kurs.action.technocard.create'      # Создание технологической карты'''
            read = 'com.rnis.kurs.action.technocard.get'           # Получение технологической карты'''
            update = 'com.rnis.kurs.action.technocard.update'      # Редактирование технологической карты'''
            delete = 'com.rnis.kurs.action.technocard.delete'      # Удаление технологической карты'''
            to_list = 'com.rnis.kurs.action.technocard.list'       # Получение списка технологических карт'''

            class Assign:
                '''Назначение технологической карты'''
                create  = 'com.rnis.kurs.action.technocard_assign.create'      # Создание назначения технологической карты'''
                read    = 'com.rnis.kurs.action.technocard_assign.get'         # Получение назначений технологической карты'''
                update  = 'com.rnis.kurs.action.technocard_assign.update'      # Редактирование назначения технологической карты'''
                delete  = 'com.rnis.kurs.action.technocard_assign.delete'      # Удаление назначения технологической карты'''
                to_list = 'com.rnis.kurs.action.technocard_assign.list'        # Получение списка назначений технологических карт'''

        class Vehicle:
            '''ТС'''
            create  = 'com.rnis.kurs.action.vehicle.create'        # Создание ТС'''
            read    = 'com.rnis.kurs.action.vehicle.get'           # Получение ТС'''
            update  = 'com.rnis.kurs.action.vehicle.update'        # Редактирование информации о ТС'''
            delete  = 'com.rnis.kurs.action.vehicle.delete'        # Удаление ТС'''
            to_list = 'com.rnis.kurs.action.vehicle.list'          # Получение списка ТС'''
            upload  = 'com.rnis.kurs.action.vehicle.import'        # Импорт ТС'''
            upload_status = 'com.rnis.kurs.action.vehicle.import.get'      # Получение состояния импорта ТС'''

            class Fuel:
                '''Топливо'''
                event  = 'com.rnis.kurs.action.vehicle_fuel_event.list'      # Получение списка событий об уровне топлива'''
                level  = 'com.rnis.kurs.action.vehicle_fuel_level.list'      # Получение списка записей об уровне топлива'''
                recalc = 'com.rnis.kurs.action.fuel.recalc'                  # Запуск пересчета показаний топлива'''

            class Mechanism:
                '''Механизм ТС'''
                create  = 'com.rnis.kurs.action.vehicle.mechanism.create'    # Создание механизма ТС'''
                read    = 'com.rnis.kurs.action.vehicle.mechanism.get'       # Получение механизма по ТС'''
                update  = 'com.rnis.kurs.action.vehicle.mechanism.update'    # Редактирование механизма ТС'''
                delete  = 'com.rnis.kurs.action.vehicle.mechanism.delete'    # Удаление механизма ТС'''
                to_list = 'com.rnis.kurs.action.vehicle.mechanism.list'      # Получение списка механизмов по ТС'''

            class Work:
                '''Работа по ТС'''
                create  = 'com.rnis.kurs.action.vehicle.work.create'         # Создание работы по ТС'''
                read    = 'com.rnis.kurs.action.vehicle.work.get'            # Получение работы по ТС'''
                update  = 'com.rnis.kurs.action.vehicle.work.update'         # Редактирование работы по ТС'''
                delete  = 'com.rnis.kurs.action.vehicle.work.delete'         # Удаление работы по ТС'''
                to_list = 'com.rnis.kurs.action.vehicle.work.list'           # Получение списка работ по ТС'''

        class Waybill:
            '''Путевой лист'''
            create  = 'com.rnis.kurs.action.waybill.create'      # Создание путевого листа'''
            read    = 'com.rnis.kurs.action.waybill.get'         # Получение путевого листа'''
            update  = 'com.rnis.kurs.action.waybill.update'      # Редактирование путевого листа'''
            delete  = 'com.rnis.kurs.action.waybill.delete'      # Удаление путевого листа'''
            to_list = 'com.rnis.kurs.action.waybill.list'        # Получение списка путевых листов'''

    class Mobile:
        '''Мобильное приложение'''
        complaint = 'com.rnis.mobile.action.complaint.send'      # Отправка жалобы'''
        feedback  = 'com.rnis.mobile.action.feedback.send'       # Отправка обратной связи'''
        routing   = 'com.rnis.mobile.action.routing'             # Построение маршрута'''
        search    = 'com.rnis.mobile.action.search'              # Поиск'''
        favorite  = 'com.rnis.mobile.action.search.save'         # Сохранение результата поиска в избранном'''

        class Bus:
            '''ТС'''
            read    = 'com.rnis.mobile.action.bus.get'           # Получение детальной информации об автобусе'''
            to_list = 'com.rnis.mobile.action.bus.list'          # Получение автобусов'''
            routing = 'com.rnis.mobile.action.bus.routing'       # Получение маршрута автобуса'''
            route   = 'com.rnis.mobile.action.route.bus.list'    # Получение автобусов определенного маршрута'''

        class Contact:
            '''Rонтакт'''
            create  = 'com.rnis.mobile.action.contact.create'    # Создание контакта'''
            read    = 'com.rnis.mobile.action.contact.get'       # Получение контакта'''
            update  = 'com.rnis.mobile.action.contact.update'    # Редактирование контакта'''
            delete  = 'com.rnis.mobile.action.contact.delete'    # Удаление контакта'''
            to_list = 'com.rnis.mobile.action.contact.list'      # Получение списка контактов'''

        class Page:
            '''Текстовая страница'''
            read    = 'com.rnis.mobile.action.mobile_page.get'    # Получение текстовой страницы'''
            update  = 'com.rnis.mobile.action.mobile_page.update' # Редактирование текстовой страницы'''
            to_list = 'com.rnis.mobile.action.mobile_page.list'   # Получение списка текстовых страниц'''

        class Path:
            '''Мои маршруты'''
            create  = 'com.rnis.mobile.action.favorite_path.create'    # Создание записи в "Мои маршруты"'''
            read    = 'com.rnis.mobile.action.favorite_path.get'       # Получение записи "Мои маршруты"'''
            update  = 'com.rnis.mobile.action.favorite_path.update'    # Редактирование записи в "Мои маршруты"'''
            delete  = 'com.rnis.mobile.action.favorite_path.delete'    # Удаление записи из "Мои маршруты"'''
            to_list = 'com.rnis.mobile.action.favorite_path.list'      # Получение списка "Мои маршруты"'''

        class Route:
            '''Мой транспорт'''
            create  = 'com.rnis.mobile.action.favorite_route.create'   # Создание записи в "Мой транспорт"'''
            delete  = 'com.rnis.mobile.action.favorite_route.delete'   # Удаление записи из "Мой транспорт"'''
            to_list = 'com.rnis.mobile.action.favorite_route.list'     # Получение списка для "Мой транспорт"'''

        class StopPoint:
            '''Остановки'''
            to_list = 'com.rnis.mobile.action.stop_point.list'         # Получение остановок'''
            route   = 'com.rnis.mobile.action.stop_point.routes'       # Получение маршрутов, проходящих через остановку'''

        class User:
            '''Пользователь'''
            read     = 'com.rnis.mobile.action.mobile_user.get'                             # Получение информации о текущем мобильном пользователе'''
            update   = 'com.rnis.mobile.action.mobile_user.update'                          # Редактирование мобильного пользователя'''
            login    = 'com.rnis.mobile.action.mobile_user.login'                           # Авторизация мобильного пользователя'''
            register = 'com.rnis.mobile.action.mobile_user.register'                        # Регистрация мобильного пользователя'''
            login_by_email = 'com.rnis.mobile.action.mobile_user.login_by_email'            # Авторизация мобильного пользователя по email'''
            update_push_token = 'com.rnis.mobile.action.mobile_user.push_token.update'      # Обновление push token пользователя.'''

            class Confirm:
                '''Код подтверждения'''
                check = 'com.rnis.mobile.action.mobile_user.confirm.check'         # Проверка кода подтверждения мобильного пользователя'''
                send  = 'com.rnis.mobile.action.mobile_user.confirm.send'          # Отправка SMS для подтверждения мобильного пользователя'''

                class Email:
                    '''Подтверждения на почту'''
                    check  = 'com.rnis.mobile.action.mobile_user.email.confirm.check'      # Проверка кода подтверждения email мобильного пользователя'''
                    send   = 'com.rnis.mobile.action.mobile_user.email.confirm.send'       # Отправка кода на новую почту для подтверждения изменения email на new_email.'''
                    resend = 'com.rnis.mobile.action.mobile_user.confirm.email.resend'     # Повторная отправка подтверждения email'''
                    reset  = 'com.rnis.mobile.action.mobile_user.email.reset_pass'         # Отправка кода на email для сброса пароля'''
                    new    = 'com.rnis.mobile.action.mobile_user.new_email.confirm.check'  # Проверка кода подтверждения изменения email на new_email'''
                class Phone:
                    '''Подтверждения на телефон'''
                    check = 'com.rnis.mobile.action.mobile_user.phone.confirm.check'       # Проверка кода подтверждения изменения телефона'''
                    send  = 'com.rnis.mobile.action.mobile_user.phone.confirm.send'        # Отправка SMS для подтверждения изменения телефона'''

        class Notification:
            '''Оповещение'''
            create  = 'com.rnis.mobile.action.notification.create'      # Создание оповещения'''
            update  = 'com.rnis.mobile.action.notification.update'      # Редактирование оповещения'''
            delete  = 'com.rnis.mobile.action.notification.delete'      # Удаление оповещения'''
            to_list = 'com.rnis.mobile.action.notification.list'        # Получение списка оповещений'''

    class Notification:
        '''Уведомление'''
        create  = 'com.rnis.notifications.action.create'           # Создание уведомления'''
        read    = 'com.rnis.notifications.action.read'             # Пометка уведомлений прочитанными'''
        to_list = 'com.rnis.notifications.action.list'             # Получение списка уведомлений'''
        count   = 'com.rnis.notifications.action.count'            # Получение кол-ва непрочитанных уведомлений'''
        send    = 'com.rnis.notifications.action.mail.send'        # Отправка email сообщения'''

        class Event:
            '''Событие оповещения'''
            create  = 'com.rnis.notifications.action.notification_event.create'        # Создание события оповещения'''
            read    = 'com.rnis.notifications.action.notification_event.get'           # Получение события оповещения по идентификатору'''
            update  = 'com.rnis.notifications.action.notification_event.update'        # Редактирование события оповещения'''
            delete  = 'com.rnis.notifications.action.notification_event.delete'        # Удаление события оповещения'''
            to_list = 'com.rnis.notifications.action.notification_event.list'          # Получение списка событий оповещений'''
            send    = 'com.rnis.notifications.action.notification_event.send'          # Отправка оповещения по идентификатору'''

        class EventRule:
            '''Правила события'''
            create  = 'com.rnis.notifications.action.event_rule.create'        # Создание правила события'''
            read    = 'com.rnis.notifications.action.event_rule.get'           # Получение правила события по идентификатору'''
            update  = 'com.rnis.notifications.action.event_rule.update'        # Редактирование правила события'''
            delete  = 'com.rnis.notifications.action.event_rule.delete'        # Удаление правила события'''
            to_list = 'com.rnis.notifications.action.event_rule.list'          # Получение списка правил событий'''
            event   = 'com.rnis.notifications.action.event_rule.events'        # Получение списка типов событий'''

            class Notification:
                '''Оповещение правила события'''
                create  = 'com.rnis.notifications.action.event_rule_notification.create'       # Создание оповещения правила события'''
                read    = 'com.rnis.notifications.action.event_rule_notification.get'          # Получение оповещения правила события по идентификатору'''
                update  = 'com.rnis.notifications.action.event_rule_notification.update'       # Редактирование оповещения правила события'''
                delete  = 'com.rnis.notifications.action.event_rule_notification.delete'       # Удаление оповещения правила события'''
                to_list = 'com.rnis.notifications.action.event_rule_notification.list'         # Получение списка оповещений правила события'''

        class Mailing:
            '''Шаблон рассылки'''
            create  = 'com.rnis.notifications.action.mailing.create'       # Создание шаблона рассылки'''
            read    = 'com.rnis.notifications.action.mailing.get'          # Получение шаблона рассылки по идентификатору'''
            update  = 'com.rnis.notifications.action.mailing.update'       # Редактирование шаблона рассылки'''
            delete  = 'com.rnis.notifications.action.mailing.delete'       # Удаление шаблона рассылки'''
            to_list = 'com.rnis.notifications.action.mailing.list'         # Получение списка шаблонов рассылки'''

        class SpeedViolation:
            '''Нарушение скорости'''
            to_list = 'com.rnis.notifications.action.speed_violation.list'                 # Получение списка нарушений скорости'''
            driver  = 'com.rnis.notifications.action.speed_violation.drivers.summary'      # Получение сводки по нарушениям скорости по водителям'''
            journal = 'com.rnis.notifications.action.speed_violation.journal'              # Получение списка нарушений скорости по дням'''
            summary = 'com.rnis.notifications.action.speed_violation.summary'              # Получение сводки по нарушениям скорости'''

        class User:
            '''Пользовательские настройки оповещения'''
            create  = 'com.rnis.notifications.action.user_notification_setting.create'         # Создание пользовательского конфига оповещения'''
            read    = 'com.rnis.notifications.action.user_notification_setting.get'            # Получение пользовательского конфига оповещения по идентификатору'''
            update  = 'com.rnis.notifications.action.user_notification_setting.update'         # Редактирование пользовательского конфига оповещения'''
            delete  = 'com.rnis.notifications.action.user_notification_setting.delete'         # Удаление пользовательского конфига оповещения'''
            to_list = 'com.rnis.notifications.action.user_notification_setting.list'           # Получение списка пользовательских конфигов оповещений'''

    class Organization:
        '''Организационные единицы'''
        user_group = 'com.rnis.organizational_units.action.user_groups'            # Получение списка групп пользователей предприятия'''

        class Carrier:
            '''Перевозчик'''
            create  = 'com.rnis.organizational_units.action.carrier.create'        # Создание перевозчика'''
            read    = 'com.rnis.organizational_units.action.carrier.get'           # Получение перевозчика'''
            update  = 'com.rnis.organizational_units.action.carrier.update'        # Редактирование перевозчика'''
            delete  = 'com.rnis.organizational_units.action.carrier.delete'        # Удаление перевозчика'''
            to_list = 'com.rnis.organizational_units.action.carriers'              # Получение списка перевозчиков'''

        class Position:
            '''Должности предприятия'''
            create  = 'com.rnis.organizational_units.action.position.create'       # Создание должности предприятия'''
            read    = 'com.rnis.organizational_units.action.position.get'          # Получение должности предприятия'''
            update  = 'com.rnis.organizational_units.action.position.update'       # Редактирование должности предприятия'''
            delete  = 'com.rnis.organizational_units.action.position.delete'       # Удаление должности предприятия'''
            to_list = 'com.rnis.organizational_units.action.positions'             # Получение списка должностей предприятия'''

        class Unit:
            '''Предприятие'''
            create   = 'com.rnis.organizational_units.action.unit.create'          # Создание предприятия'''
            read     = 'com.rnis.organizational_units.action.unit.get'             # Получение предприятия'''
            update   = 'com.rnis.organizational_units.action.unit.update'          # Редактирование предприятия'''
            delete   = 'com.rnis.organizational_units.action.unit.delete'          # Удаление предприятия'''
            to_list  = 'com.rnis.organizational_units.action.units'                # Получение списка предприятий'''
            children = 'com.rnis.organizational_units.action.unit.children'        # Получение дочерних предприятий'''

    class Portal:
        '''Портал РНИС'''
        feedback = 'com.rnis.portal.action.feedback.send'      # Отправка сообщения из блока обратной связи'''
        login    = 'com.rnis.portal.action.login'              # Аутентификация по заявлению на регистрацию'''

        class Captcha:
            '''Капча'''
            read     = 'com.rnis.portal.action.captcha.get'            # Получение капчи'''
            validate = 'com.rnis.portal.action.captcha.validate'       # Валидация капчи'''

        class Confirm:
            '''Заявление на подтверждение'''
            create  = 'com.rnis.portal.action.confirm_request.create'      # Создание заявления на подтверждение'''
            read    = 'com.rnis.portal.action.confirm_request.get'         # Получение заявления на подтрвеждение'''
            update  = 'com.rnis.portal.action.confirm_request.update'      # Редактирование заявления на подтверждение'''
            to_list = 'com.rnis.portal.action.confirm_request.list'        # Получение списка заявлений на подтверждение'''
            unit    = 'com.rnis.portal.action.confirm_request.units'       # Получение списка идентификаторов предприятий'''

        class Agreement:
            '''Соглашение о взаимодействии'''
            update   = 'com.rnis.portal.action.cooperation_agreements.update'      # Редактирование соглашение о взаимодействии.'''
            to_list  = 'com.rnis.portal.action.cooperation_agreements.list'        # Получение списка соглашений о взаимодействии.'''
            document = 'com.rnis.portal.action.cooperation_agreements.document'    # Генерация документа соглашения о взаимодействии.'''

            class Warnings:
                '''Предупреждение для соглашения'''
                create  = 'com.rnis.portal.action.cooperation_agreement_warnings.create'       # Создание предупреждения для соглашения о взаимодействии.'''
                update  = 'com.rnis.portal.action.cooperation_agreement_warnings.update'       # Редактирование предупреждения для соглашения о взаимодействии.'''
                to_list = 'com.rnis.portal.action.cooperation_agreement_warnings.list'         # Получение списка предупреждений для соглашения о взаимодействии.'''

        class FAQ:
            '''Вопрос-ответ'''
            create  = 'com.rnis.portal.action.faq.create'       # Создание вопрос-ответа'''
            read    = 'com.rnis.portal.action.faq.get'          # Получение новости'''
            update  = 'com.rnis.portal.action.faq.update'       # Редактирование вопрос-ответа'''
            delete  = 'com.rnis.portal.action.faq.delete'       # Удаление вопрос-ответа'''
            to_list = 'com.rnis.portal.action.faq'              # Получение списка вопрос-ответов'''

        class News:
            '''Новости'''
            create  = 'com.rnis.portal.action.news.create'      # Создание новости'''
            read    = 'com.rnis.portal.action.news.get'         # Получение новости'''
            update  = 'com.rnis.portal.action.news.update'      # Редактирование новости'''
            delete  = 'com.rnis.portal.action.news.delete'      # Удаление новости'''
            tag     = 'com.rnis.portal.action.news.tags'        # Получение тегов новостей'''
            to_list = 'com.rnis.portal.action.news'             # Получение списка новостей'''

        class Page:
            '''Страница'''
            create  = 'com.rnis.portal.action.page.create'      # Создание страницы'''
            read    = 'com.rnis.portal.action.page.get'         # Получение страницы'''
            update  = 'com.rnis.portal.action.page.update'      # Редактирование страницы'''
            delete  = 'com.rnis.portal.action.page.delete'      # Удаление страницы'''
            to_list = 'com.rnis.portal.action.pages'            # Получение списка страниц'''

        class Register:
            '''Заявление на регистрацию'''
            create  = 'com.rnis.portal.action.register_request.create'          # Создание заявления на регистрацию'''
            read    = 'com.rnis.portal.action.register_request.get'             # Получение заявления на регистрацию'''
            update  = 'com.rnis.portal.action.register_request.update'          # Редактирование заявления на регистрацию'''
            to_list = 'com.rnis.portal.action.register_request.list'            # Получение списка заявлений на регистрацию'''
            check   = 'com.rnis.portal.action.register_request.create.check'    # Проверка возможности создания заявления на регистрацию'''

        class TemplateDocument:
            '''Шаблон документов'''
            create   = 'com.rnis.portal.action.template_document.create'        # Создание шаблона документов.'''
            read     = 'com.rnis.portal.action.template_document.get'           # Получение шаблона документов.'''
            update   = 'com.rnis.portal.action.template_document.update'        # Редактирование шаблона документов.'''
            to_list  = 'com.rnis.portal.action.template_document.list'          # Получение списка шаблона документов.'''
            document = 'com.rnis.portal.action.template_document.document'      # Генерация тестового документа.'''
            next_version = 'com.rnis.portal.action.template_document.get_next_version'      # Получить следующую версию шаблона документов.'''

    class Report:
        '''Отчеты'''
        create  = 'com.rnis.reports.action.report.create'            # Запрос на формирование отчета'''
        to_list = 'com.rnis.reports.action.document.list'            # Получение сформированных отчетов'''
        available = 'com.rnis.reports.action.reports.list'           # Получение списка отчетов, доступных для построения'''
        parameter = 'com.rnis.reports.action.report.parameters'      # Получение списка параметров отчета'''
        integration_log = 'com.rnis.reports.action.integration_log.create'      # Сохранение лога интеграции'''

        class Schedule:
            '''Расписание отчета'''
            create  = 'com.rnis.reports.action.report_schedule.create'     # Создание расписания отчета'''
            read    = 'com.rnis.reports.action.report_schedule.get'        # Получение значения расписания отчета'''
            update  = 'com.rnis.reports.action.report_schedule.update'     # Обновление значения расписания отчета'''
            delete  = 'com.rnis.reports.action.report_schedule.delete'     # Удаление расписания отчета'''
            to_list = 'com.rnis.reports.action.report_schedule.list'       # Получение списка расписаний отчетов'''

        class Tablet:
            '''Cводные данные'''
            summary = 'com.rnis.reports.action.tablet.summary'             # Получение сводных данных для главной страницы ПР'''
            kiutr   = 'com.rnis.reports.action.tablet.summary.kiutr'       # Получение сводных данных для подсистемы'''
            unit    = 'com.rnis.reports.action.tablet.summary.unit'        # Получение сводных данных для предприятия'''

        class Template:
            '''Шаблоны'''
            delete = 'com.rnis.reports.action.report_template.delete'      # Удаление шаблона отчета'''
            to_list = 'com.rnis.reports.action.report_templates.list'      # Список шаблонов отчета'''

    class Storage:
        '''Сервис хранилище'''
        read   = 'com.rnis.storage.action.get'         # Получение ифнорамиции по файлу по uuid'''
        delete = 'com.rnis.storage.action.delete'      # Удление файла по uuid'''
        token  = 'com.rnis.storage.action.token'       # Получение токена на загрузку файла'''

    class System:
        '''Системный сервис'''
        up   = 'com.rnis.system.up'            # Выключение режима выполнения технических работ'''
        down = 'com.rnis.system.down'          # Включение режима выполнения технических работ'''
        version = 'com.rnis.system.action.version'         # Получение версии проектов'''
        status  = 'com.rnis.system.action.status.get'      # Получение статуса сервисов'''

        class Activity:
            '''Мониторинговое состояние пользователя'''
            online = 'com.rnis.system.action.activity.online'      # Получение мониторингового состояния всех пользователей онлайн'''
            store  = 'com.rnis.system.action.activity.store'       # Сохранение мониторингового состояния пользователя'''

        class Audit:
            '''Изменение сущности'''
            search = 'com.rnis.system.action.audit.search'         # Поиск записей об изменении сущностей'''
            store  = 'com.rnis.system.event.audit.store'           # Сохранение изменений сущности'''

        class Entity:
            '''Блокирование сущности'''
            block    = 'com.rnis.system.action.entity.block'       # Блокирование сущности'''
            unblock  = 'com.rnis.system.action.entity.unblock'     # Разблокирование сущности'''
            is_block = 'com.rnis.system.action.entity.is_blocked'  # Проверка - заблокирована ли сущность.'''
            name     = 'com.rnis.system.action.entity.names'       # Получение текстового названия сущностей'''

        class Log:
            '''Лог действий'''
            search = 'com.rnis.system.action.log.search'       # Поиск записей в логе действий'''
            store  = 'com.rnis.system.event.log.store'         # Сохранение действия пользователя'''
            code   = 'com.rnis.system.action.log.codes'        # Получение списка кодов событий'''

        class Maintenance:
            '''Режим обслуживания'''
            time   = 'com.rnis.system.maintenance.latest.time' # Получение времени последнего включения режима обслуживания'''
            status = 'com.rnis.system.maintenance.status'      # Получение статуса выполнения технических работ'''

        class Message:
            '''Системные сообщения'''
            create  = 'com.rnis.system.message.create'         # Создание системного сообщения'''
            update  = 'com.rnis.system.message.update'         # Редактирование системного сообщения'''
            delete  = 'com.rnis.system.message.delete'         # Удаление системного сообщения'''
            to_list = 'com.rnis.system.message.all'            # Получение списка сообщений'''

        class Schema:
            '''Схема аудита'''
            update = 'com.rnis.system.event.schema.collect'    # Событие, инициирующее обновление схемы аудита'''
            store  = 'com.rnis.system.action.schema.store'     # Обновление схемы аудита'''

        class Table:
            '''Экспорт таблицы'''
            create = 'com.rnis.system.action.table.export.create'  # Создание экспорта таблицы'''
            read   = 'com.rnis.system.action.table.export.get'     # Получение результата экспорта таблицы'''
            update = 'com.rnis.system.action.table.export.update'  # Обновление экспорта таблицы'''

        class Tooltip:
            '''Контекстная справка'''
            update = 'com.rnis.system.action.tooltip.update'       # Редактирование контекстной справки'''
            to_list = 'com.rnis.system.action.tooltip.list'        # Получение контекстной справки'''

        class Trash:
            '''Корзина'''
            search = 'com.rnis.system.action.trash.search'         # Поиск записей в корзине'''
            store  = 'com.rnis.system.event.trash.store'           # Сохранение данных в корзине'''

    class T1sync:
        '''Микросервис запроса данных из платформы Т1'''
        event    = 'com.rnis.t1sync.action.events'                 # Получение событий движения для списка устройств'''
        extended = 'com.rnis.t1sync.action.extended_data'          # Получение значения на порту по устройству'''
        mileage  = 'com.rnis.t1sync.action.mileage'                # Получение пробега по устройству'''
        motohour = 'com.rnis.t1sync.action.motohours'              # Получение показаний моточасов по устройству'''

        class Device:
            '''Данные по устройству'''
            arhive = 'com.rnis.t1sync.action.device.arhived_telematics'        # Получение данных об архивной телематике.'''
            search = 'com.rnis.t1sync.action.device.find'                      # Поиск номера БНСО по коду БНСО'''
            score  = 'com.rnis.t1sync.action.device.score'                     # Получение баллов водителя'''
            tachograph = 'com.rnis.t1sync.action.device.tachograph'            # Получение показаний тахографа'''

        class History:
            '''Получение исторических данных'''
            read    = 'com.rnis.t1sync.action.history'                 # Получение исторических данных по маршруту для списка устройств'''
            to_list = 'com.rnis.t1sync.action.history.multiple'        # Получение исторических данных по нескольким устройствам'''

        class Odometr:
            '''Показания одометра'''
            read    = 'com.rnis.t1sync.action.odometr'                 # Получение показаний одометра по устройству'''
            to_list = 'com.rnis.t1sync.action.odometr.multiple'        # Получение показаний одометра по устройствам'''

    class Telematic:
        '''Сервис телематики'''
        read    = 'com.rnis.telematics.action.telematics.get'          # Получение записей телематики'''
        to_list = 'com.rnis.telematics.action.telematics.all'          # Получение всех текущих записей телематики'''
        bound   = 'com.rnis.telematics.action.telematics.bounds'       # Получение bounding box телематики'''
        log     = 'com.rnis.telematics.action.telematics.logs'         # Получение записей журнала лога телематики'''
        store   = 'com.rnis.telematics.action.telematics.store'        # Сохранение записей телематики'''
        panic   = 'com.rnis.telematics.action.panics.get'              # Получение записей срабатывания тревожной кнопки'''

        class Portal:
            '''Запись телематики для портала'''
            read      = 'com.rnis.telematics.action.telematics.portal.get'             # Получение записей телематики для портала'''
            count     = 'com.rnis.telematics.action.telematics.portal.get.count'       # Получение общего количества записей телематики для портала'''
            clustered = 'com.rnis.telematics.action.telematics.portal.clustered'       # Получение записей телематики для портала c кластеризацией'''
            modified  = 'com.rnis.telematics.action.telematics.portal.modified'        # Получение измененных записей телематики для портала'''

    class Vehicle:
        '''Транспортные средства'''
        create  = 'com.rnis.vehicles.action.vehicle.create'        # Создание ТС'''
        read    = 'com.rnis.vehicles.action.vehicle.get'           # Получение значения ТС'''
        update  = 'com.rnis.vehicles.action.vehicle.update'        # Обновление значения ТС'''
        delete  = 'com.rnis.vehicles.action.vehicle.delete'        # Удаление ТС'''
        to_list = 'com.rnis.vehicles.action.vehicle.list'          # Получение значения всех ТС'''
        upload  = 'com.rnis.vehicles.action.vehicle.import'                # Импорт ТС'''
        upload_status = 'com.rnis.vehicles.action.vehicle.import.get'      # Получение состояния импорта ТС'''
        portal = 'com.rnis.vehicles.action.vehicle.list.portal'            # Получение значения всех ТС для портала'''
        search = 'com.rnis.monitoring.action.vehicles.filter'              # Фильтрация списка ТС'''
        unit   = 'com.rnis.vehicles.action.vehicle.by_units.list'          # Получение ТС по предприятиям'''
        idle   = 'com.rnis.geo.action.vehicle_idle_time.list'              # Получение периодов простоя ТС'''
        malfunction = 'com.rnis.vehicles.action.vehicle_malfunctions.list' # Получение списка ремонтов ТС'''
        retrospective = 'com.rnis.monitoring.action.retrospective'         # Получение ретроспективы ТС'''

        class BNSO:
            '''БНСО'''
            create  = 'com.rnis.vehicles.action.bnso.create'            # Создание БНСО'''
            read    = 'com.rnis.vehicles.action.bnso.get'               # Получение значения БНСО'''
            update  = 'com.rnis.vehicles.action.bnso.update'            # Обновление значения БНСО'''
            delete  = 'com.rnis.vehicles.action.bnso.delete'            # Удаление БНСО'''
            to_list = 'com.rnis.vehicles.action.bnso.list'              # Получение значения всех БНСО'''
            check   = 'com.rnis.vehicles.action.bnso.check.link'        # Получение адреса для диагностики БНСО'''
            search  = 'com.rnis.vehicles.action.bnso.geo_search'        # Поиск текущего БНСО из ТС по Гос номеру'''
            period  = 'com.rnis.vehicles.action.bnso_periods.list'      # Получение периодов установки БНСО'''

            class Link:
                '''Связь БНСО-ТС'''
                create = 'com.rnis.vehicles.action.bnso_to_vehicle.create' # Создание связи БНСО-ТС'''
                read   = 'com.rnis.vehicles.action.bnso_to_vehicle.get'    # Получение значения связи БНСО-ТС'''
                update = 'com.rnis.vehicles.action.bnso_to_vehicle.update' # Обновление значения связи БНСО-ТС'''
                delete = 'com.rnis.vehicles.action.bnso_to_vehicle.delete' # Удаление связи БНСО-ТС'''

        class Event:
            '''события для модуля мониторинга'''
            create  = 'com.rnis.vehicles.action.event.create'       # Создание события для модуля мониторинга'''
            to_list = 'com.rnis.vehicles.action.event.list'         # Получение списка событий для модуля мониторинга'''

        class Graduation:
            '''Градуировка для конфигуратора портов БНСО'''
            create  = 'com.rnis.vehicles.action.graduation.create'         # Создание градуировки для конфигуратора портов БНСО'''
            read    = 'com.rnis.vehicles.action.graduation.get'            # Получение градуировки для конфигуратора портов БНСО'''
            update  = 'com.rnis.vehicles.action.graduation.update'         # Обновление градуировки для конфигуратора портов БНСО'''
            delete  = 'com.rnis.vehicles.action.graduation.delete'         # Удаление градуировки'''
            to_list = 'com.rnis.vehicles.action.graduation.list'           # Получение списка градуировок для конфигуратора портов БНСО'''

            class Template:
                '''Шаблон градуировки'''
                create  = 'com.rnis.vehicles.action.graduation_templates.create'       # Создание шаблона градуировки'''
                read    = 'com.rnis.vehicles.action.graduation_templates.get'          # Получение шаблона градуировки'''
                update  = 'com.rnis.vehicles.action.graduation_templates.update'       # Обновление шаблона градуировки'''
                delete  = 'post.rnis.vehicles.action.graduation_templates.delete'      # Удаление шаблона градуировки'''
                to_list = 'com.rnis.vehicles.action.graduation_templates.list'         # Получение списка шаблона градуировок для конфигуратора портов БНСО'''

        class Port:
            '''Порт БНСО для конфигуратора'''
            create  = 'com.rnis.vehicles.action.port.create'       # Создание порта БНСО для конфигуратора'''
            read    = 'com.rnis.vehicles.action.port.get'          # Получение порта БНСО для конфигуратора'''
            update  = 'com.rnis.vehicles.action.port.update'       # Обновление порта'''
            delete  = 'com.rnis.vehicles.action.port.delete'       # Удаление порта'''
            to_list = 'com.rnis.vehicles.action.port.list'         # Получение списка портов'''

        class Status:
            '''Обновление статуса ТС'''
            update = 'com.rnis.vehicles.action.vehicle.status.update'                  # Обновление статуса ТС'''
            update_many = 'com.rnis.vehicles.action.vehicle.status.massive.update'     # Массовое обновление статуса ТС'''