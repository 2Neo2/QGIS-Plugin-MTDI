item_type = {
    'date': 'date/single', 
    'text': 'category', 
    'number': 'number/=',
}

directory = {
    '__shit':           ['cat', 'dinfo', 'hsn', 'ver'],
    'card':             ['card', 'card_name', 'card_type', 'cat', 'cuid', 'TPAY'],
    'carrier_id':       ['company_id', 'ID', 'IDTP', 'P_TRC_ID', 'trc_id', 'TRCID'],
    'carrier_name':     ['company', 'company_name', 'P_TRC_NAME', 'ptp', 'trc', 'trc_name'],
    'code':             ['acode', 'code', 'hsn', 'status'],
    'count':            ['cnt', 'cnt_zn', 'conductor', 'proc', 'trip_no', 'zn'],
    'date':             ['bdate', 'date', 'dt', 'rdate', 'report_date', 'sdate'],
    'date_from':        ['bdate', 'date_from', 'P_FD'],
    'date_to':          ['date_to', 'edate', 'P_TD'],
    'distillation':     ['part'],
    'driver':           ['DRIVER'],
    'group_by':         ['bd', 'caserep', 'checkdat', 'cnt_tran', 'cs', 'dir', 'fl', 'flgr', 'flt', 'mta', 'sto'],
    'occupancy':        ['proc', 'procMax', 'sr', 'zend', 'zstart'],
    'pan':              ['conductor_pan', 'pan'],
    'route_name':       ['route_name'],
    'route_number':     ['BUS_NUM', 'num', 'route_num', 'routenum'],
    'route_reg':        ['reg', 'reg_num', 'regnum', 'route_var_uid'],
    'route_reg_type':   ['reg_type', 'rote_type', 'route_type', 'route_type_name'],
    'run':              ['trip', 'trip_no'],
    'shift':            ['mn', 'oper_shift', 'shift', 'direction'],
    'terminal':         ['hm', 'P_MSAM', 'P_TID', 'smid', 'trm', 'TRM_ID'],
    'time_from':        ['btime', 'hh_from', 'HH1', 'mm1', 't1', 'tm1'],
    'time_to':          ['etime', 'hh_to', 'HH2', 'mm2', 't2', 'tm2'],
    'transaction_id':   ['tkp_id', 'tran_id'],
    'vehicle':          ['grz', 'P_GRZ', 'vehicle_num', 'vehicle_number', 'vehicle_reg_number'],
    'vehicle_capacity': ['place', 'typets'],
}


class Parameters:
    def __init__(self, data: dict) -> None: 
        data = data.get('dataset_query', {})
        data = data.get('native', {})
        self.tags = data.get('template-tags', [])
    
    
    def to_list(self, data: any) -> list:
        """Преобразование данных в список"""
        if type(data) in [dict, list, set, tuple]:
            return [f'{d}' for d in list(data)]
        else:
            return [f'{data}']


    def to_str(self, data: any, many: bool) -> str:
        """Преобразование данных в строку"""
        data = self.to_list(data)
        data = ','.join(data) if many else data[0]
        return f'{data}'


    def __parse_param(self, param) -> dict:
        keys = ['id', 'type', 'value', 'target']
        return {k:param[k] for k in keys}


    def get_param(self, tag_data: dict, tag_name: str) -> dict:
        """Создание параметров из карточки объекта"""
        param = {}
        param['id']     = tag_data['id']
        param['name']   = 'зпт' in tag_data['display-name']
        param['type']   = item_type[tag_data['type']]
        param['value']  = tag_data.get('default')
        param['target'] = ["variable", ["template-tag", tag_name]]
        return param

    
    @property
    def create(self, **d) -> list:
        """Добавление параметров из карточки объекта"""
        parameters = []
        for tag_name, tag_data in self.tags.items():
            param = self.get_param(tag_data, tag_name)
            parameters.append(param)
        self.parameters = parameters
        return self.parameters


    def __get_parameters(self, **d) -> list:
        """Добавление параметров из карточки объекта"""
        parameters = []
        current = [param for param in d.get('parameters', [])]
        if len(current) > 0:
            for default in self.parameters:
                default_value = default['value']
                for param in current:
                    if param['id'] == default['id']:
                        default['value'] = param['value']
                parameters.append({key: value for key, value in default.items()})
                default['value'] = default_value
        else:
            parameters = self.parameters
        return parameters


    def update(self, **d) -> list:
        """Обновление парметров данными от пользователя"""
        data = []
        id_list = []
        for param in self.__get_parameters(**d):
            tag_name = param['target'][1][1].lower()
            for key, value in d.items():
                if tag_name in directory.get(key, []):
                    param['value'] = None if value is None else self.to_str(value, param['name'])
                    if type(value) == list:
                        del value[0]
                    data.append(self.__parse_param(param))
                    id_list.append(param['id'])
                    break
            if param['value'] is not None and param['id'] not in id_list:
                data.append(self.__parse_param(param))
        data = [d for d in data if d['value'] is not None]
        return data