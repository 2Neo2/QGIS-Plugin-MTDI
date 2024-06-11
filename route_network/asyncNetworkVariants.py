from PyQt5.QtWidgets import *
from qgis.core import *
from qgis.PyQt.QtGui import *
from PyQt5.QtCore import *
import asyncio
import json
import pandas as pd
from .tkp import TKP_API
from .rnis import RnisAPI

class AsyncNetworkVariants():

    def __init__(self, dialog, filepath, date, time, company, isSOBOP, delay=5):
        self.filepath = filepath
        self.date = str(date)
        self.delay = delay
        self.dialog = dialog
        self.sobop_data = []
        self.time = time
        self.isSOBOP = isSOBOP
        self.getStopPoint = False
        self.company = company
        self.sobop_stop_point_data = []
        self.tkp = TKP_API
        self.rnis = RnisAPI
        self.login_tkp = 'AnichenkovAnA@mosreg.ru'
        self.password_tkp = 'atQ495Lp!'
        self.login_rnis = 'Karpenko'
        self.password_rnis = 'H7DneQW3'

######### RNIS #########

    async def get_data_from_outfit_plan(self, array_regs):
        """Получаем варианты маршрутов из план нарядов."""
        async with RnisAPI(self.login_rnis, self.password_rnis) as rnis:
                    all_data = []
                    self.dialog.status_label.setText('Получаем маршруты...')
                    route_list = await rnis.Route.list_(
                        retries = 8,                                                            
                        delay = 30,
                        date = self.date,                                                                                                                  
                        print_error = True,                                                     
                        all_pages = True,                                                       
                        concurrency = 1,   
                        status = '1abd2f98-7845-11e7-be3f-3a4e0357cc4a',                                                                                                                                                                   
                        route_reg_number = array_regs
                    )
                    percent = 0
                    self.dialog.status_label.setText('Получаем варианты...')
                    for route in route_list['payload']['items']:
                        percent += 100 / len(route_list)
                        self.dialog.progress.setValue(percent)

                        variant_list = await rnis.Route.variant_list(
                            retries = 8,                                                            
                            delay = 30,
                            all_pages = True,
                            concurrency = 1,
                            route_uuid = route['uuid']
                        )

                        result_item = {
                            'route_reg_number': route['registration_number'],
                            'route_name': route['title'],
                            'route_number': route['number'],
                            'variants': variant_list.get('payload', {}).get('items', [])
                        }

                        if result_item not in all_data:
                            all_data.append(result_item)
                    return all_data

######################################################################################################################################################


######### SOBOP #########

    async def get_stop_point_data(self, **d):
        """Получаем ИЗ СОБОП входы и выходы соц и ком по uuid."""
        async with self.tkp(self.login_tkp, self.password_tkp) as tkp:
            card = tkp.Card
            await card(3451)
            card.parameters_update(
                route_reg = d.get('uuid'),
                shift = 'прямое',
                date_from = d.get('date'),
                date_to = d.get('date')
            )

            forwards = await card.json

            card.parameters_update(
                route_reg = d.get('uuid'),
                shift = 'обратное',
                date_from = d.get('date'),
                date_to = d.get('date')
            )

            reverses = await card.json

        return forwards, reverses
    

    async def get_type_payment(self, **d):
        """Получаем инфо из СОБОП по типам оплаты: БК, СК, КОЛ-ВСЕГО"""
        company = 1 if self.company == 'МТА' else 2
        sobop_data = []
        async with self.tkp(self.login_tkp, self.password_tkp) as tkp:
            card = tkp.Card
            await card(3192)

            card.parameters_update (
                date_from = d.get('date'),
                date_to = d.get('date'),
                # date_from = '2024-03-01',
                # date_to = '2024-03-31',
                route_reg = d.get('array_regs', []),
                group_by = [1, 0, company]
            )
            data = await card.json
            for item in data:
                if len(item) != 0:
                    sobop_data.append({'reg': item['РЕГ НОМЕР'], 'data': data})
        return sobop_data


    async def get_zagr_passp(self, **d):
        """"""
        async with self.tkp(self.login_tkp, self.password_tkp) as tkp:
            card = tkp.Card
            await card(3451)

            card.parameters_update (
                date_from = d.get('date'),
                date_to = d.get('date'),
                shift = d.get('route_type'),
                route_reg = d.get('var_uid')
            )
            data = await card.json
        return data


    async def get_workload_tkp(self, **d):
        """Получаем из СОБОП загруженность."""
        sobop_data = []
        time_values = d.get('time').split('-')
        code = 3279 if self.company == 'МТА' else 3408
        async with self.tkp(self.login_tkp, self.password_tkp) as tkp:
            card = tkp.Card
            await card(code)
            for reg in d.get('array_regs', []):
                card.parameters_update(
                    route_reg = reg,
                    date = d.get('date'),
                    time_from = f"{time_values[0]}:00",
                    time_to = f"{time_values[1]}:00",
                    occupancy = 0
                )
                data = await card.json
                if len(data) != 0:
                    sobop_data.append({'reg': reg, 'data': data})
        return sobop_data

#######################################################################################################################################################


######### GEOJSON #########

    def get_geojson(self):
        data = {
            "type": "FeatureCollection",
            "features": []
        }
        return data


    def get_feature(self, feature_type):
        if feature_type == 'LineString':
            data = {
                "type": "Feature",
                "properties": {
                    "description": "None",
                    "zagr": 'None',
                },
                "geometry": {
                    "type": "LineString",
                    "coordinates": []
                }
            }
        else:
            data = {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Point",
                    "coordinates": []
                },
            }
        return data


    def get_busstop_and_coord(self, route, route_type):
        busstop, coord = [], []
        points = route.get(route_type, False)
        if points:
            for point in points:
                if point.get('point_type') == 'stop_point':
                    lon = point.get('longitude', None)
                    lat = point.get('latitude', None)
                    if lon and lat is not None:
                        busstop.append([lon, lat])
                path = point.get('path_to_the_next_point_geometry', False)
                if path:
                    coordinates = path.get('coordinates', False)
                    if coordinates:
                        if coordinates not in coord:
                            coord.append(coordinates)
        return busstop, coord


    def update_feature_2(self, route, geojson, route_type, data_item):
        busstop, coord = self.get_busstop_and_coord(route, route_type)

        for i, c in enumerate(coord, 1):
            feature = self.get_feature('LineString')
            feature['geometry']['coordinates'] = c
            feature['properties']['description'] = f'Перегон: {i}'
            feature['properties']['peregon'] = i
            feature['properties']['variant_uuid'] = route['uuid']
            feature['properties']['route_number'] = data_item['route_number']
            feature['properties']['route_reg_number'] = data_item['route_reg_number']
            geojson['features'].append(feature)
        return busstop, geojson


    def get_points_geojson_layer(self, geojson, stop_point_data):
        if len(stop_point_data) == 0:
            return geojson
        index = 0
        for item in geojson['features']:
            if item['geometry']['type'] == 'Point':
                if index < len(stop_point_data):
                    item['properties']['description'] = f"Номер остановки {index + 1}"
                    item['properties']['Вышло всего'] = stop_point_data[index]['Вышло всего']
                    item['properties']['Зашло всего'] = stop_point_data[index]['Зашло всего']
                    item['properties']['Вышло СК'] = stop_point_data[index]['Вышло СК']
                    item['properties']['Зашло СК'] = stop_point_data[index]['Зашло СК']
                    item['properties']['Вышло ком'] = stop_point_data[index]['Вышло ком']
                    item['properties']['Зашло ком'] = stop_point_data[index]['Зашло ком']
                    index += 1
        return geojson
    

    def update_feature_layer_2(self, route, geojson, route_type, data_item):
        _, coord = self.get_busstop_and_coord(route, route_type)

        kol_soc = 0
        kol_kom = 0
        kol_total = 0
        flag = True

        if self.isSOBOP:
            for item in self.sobop_data:
                if str(item['reg']) == str(data_item['route_reg_number']):
                    flag = False
                    for value in item['data']:
                        kol_soc += value['КОЛ СОЦ']
                        kol_kom += value['КОЛ КОММ']
                        kol_total += value['КОЛ ВСЕГО']
        
        if flag and self.isSOBOP:
            print(f"{data_item['route_reg_number']} не добавлен! Причина - нет в СОБОП ")
            return geojson

        feature = self.get_feature('LineString')
        feature['properties']['description'] = data_item['route_name']
        feature['properties']['variant_uuid'] = route['uuid']
        feature['properties']['route_number'] = data_item['route_number']
        feature['properties']['route_reg_number'] = data_item['route_reg_number']
        feature['properties']['variant_name'] = f"{route['name']}-{route_type}"
        if self.isSOBOP:
            feature['properties']['kol_soc'] = kol_soc
            feature['properties']['kol_kom'] = kol_kom
            feature['properties']['kol_total'] = kol_total

        for _, c in enumerate(coord, 1):
            for item in c:
                feature['geometry']['coordinates'].append(item)
                
        if len(feature['geometry']['coordinates']) != 0:
            if feature not in geojson['features']:
                geojson['features'].append(feature)
        return geojson
    
#######################################################################################################################################################


######### QGIS #########

    def resize_points(self, layer):
        #Resize and set color for points
        symbol = QgsSymbol.defaultSymbol(layer.geometryType())

        # Set the marker symbol layer and its size
        marker_symbol_layer = QgsSimpleMarkerSymbolLayer()
        marker_symbol_layer.setSize(1.6)
        
        color = QColor(96, 96, 96) 
        marker_symbol_layer.setColor(color)

        # Assign the marker symbol layer to the symbol
        symbol.changeSymbolLayer(0, marker_symbol_layer)

        # Set the symbol to the layer
        layer.renderer().setSymbol(symbol)

        # Trigger a repaint to apply changes
        layer.triggerRepaint()


    def add_style_layer(self, layer):
        category_field_name = 'passp'

        # Get the index of the category field
        field_index = layer.fields().indexFromName(category_field_name)

        # Check if the category field exists in the layer
        if field_index != -1:
            values = [feature[field_index] for feature in layer.getFeatures()]
            # Преобразовать значения в целочисленные (если возможно)
            integer_values = [int(value) if value is not None else None for value in values]
            if len(integer_values) != 0:
                # Get unique values in the passp field
                unique_values = set(integer_values)
                min_value = min(unique_values)
                max_value = max(unique_values)
                division = (max_value - min_value)
                
                if division == 0:
                    division = 1
                
                normalized_values = [(value - min_value) / division for value in unique_values]

                # Create a categorized renderer
                renderer = QgsCategorizedSymbolRenderer(category_field_name, [])

                # Create symbols and categories based on unique values
                for value, normalized_value in zip(sorted(unique_values), sorted(normalized_values)):
                    # Определить ваш цвет в зависимости от значения passp
                    color = QgsGradientColorRamp(QColor(0, 255, 0), QColor(255, 0, 0)).color(normalized_value)
                    
                    # Создать символ и установить ширину линии
                    category = QgsRendererCategory(str(value), QgsSymbol.defaultSymbol(layer.geometryType()), str(value))
                    category.symbol().symbolLayer(0).setColor(color)
                    category.symbol().symbolLayer(0).setWidth(1.6)
                    
                    renderer.addCategory(category)

                # Set the renderer for the layer
                layer.setRenderer(renderer)

                # Update the style
                layer.triggerRepaint()
                print("Стиль успешно загружен.")
        else:
            symbol = QgsLineSymbol()
            symbol.setWidth(1.26)
            symbol.setColor(QColor(101, 15, 207))
            layer_renderer = QgsSingleSymbolRenderer(symbol)
            layer.setRenderer(layer_renderer)
            layer.triggerRepaint()
            print(f"Поле '{category_field_name}' не найдено в слое.")


    def add_layer_to_project(self, geojson, name, group_name, stop_points):
        root = QgsProject.instance().layerTreeRoot()
        group = next(
            (child for child in root.children() if isinstance(child, QgsLayerTreeGroup) and child.name() == group_name),
            None)

        geojson_obj = json.dumps(geojson)
        new_layer_line = QgsVectorLayer(geojson_obj + "|geometrytype=LineString", name, "ogr")
        
        if self.getStopPoint == False:
            new_layer_points = QgsVectorLayer(geojson_obj + "|geometrytype=Point", name, "ogr")
        else:
            points_dict = self.get_points_geojson_layer(geojson, stop_points)
            geojson_points = json.dumps(points_dict)
            new_layer_points = QgsVectorLayer(geojson_points + "|geometrytype=Point", name, "ogr")

        self.resize_points(new_layer_points)

        if group is None:
            group = root.addGroup(group_name)

        
        # Добавление слоя в группу и в проект QGIS
        QgsProject.instance().addMapLayer(new_layer_line, False)
        QgsProject.instance().addMapLayer(new_layer_points, False)
        group.insertChildNode(0, QgsLayerTreeLayer(new_layer_line))
        group.insertChildNode(0, QgsLayerTreeLayer(new_layer_points))
        
        if new_layer_line.isValid() is not None:
            self.add_style_layer(new_layer_line)


    def add_one_layer_to_project(self, geojson_obj):
        layer =  QgsVectorLayer("LineString?crs=EPSG:4326", f"Опорная сеть-{self.company}", "memory")
        layer.startEditing()

        layer.addAttribute(QgsField("description", QVariant.String))
        layer.addAttribute(QgsField("zagr", QVariant.String))
        layer.addAttribute(QgsField("variant_uuid", QVariant.String))
        layer.addAttribute(QgsField("route_number", QVariant.String))
        layer.addAttribute(QgsField("route_reg_number", QVariant.String))
        layer.addAttribute(QgsField("variant_name", QVariant.String))

        if self.isSOBOP:
            layer.addAttribute(QgsField("kol_soc", QVariant.String))
            layer.addAttribute(QgsField("kol_kom", QVariant.String))
            layer.addAttribute(QgsField("kol_total", QVariant.String))

        for feature_data in geojson_obj["features"]:
            feature = QgsFeature()
            if self.isSOBOP:
                feature.setAttributes([
                    feature_data["properties"]["description"],
                    feature_data["properties"]["zagr"],
                    feature_data["properties"]["variant_uuid"],
                    feature_data["properties"]["route_number"],
                    feature_data["properties"]["route_reg_number"],
                    feature_data["properties"]["variant_name"],
                    feature_data["properties"]["kol_soc"],
                    feature_data["properties"]["kol_kom"],
                    feature_data["properties"]["kol_total"]
                ])
            else:
                feature.setAttributes([
                    feature_data["properties"]["description"],
                    feature_data["properties"]["zagr"],
                    feature_data["properties"]["variant_uuid"],
                    feature_data["properties"]["route_number"],
                    feature_data["properties"]["route_reg_number"],
                    feature_data["properties"]["variant_name"]
                ])
            geometry = QgsGeometry.fromPolylineXY([
                QgsPointXY(coord[0], coord[1]) for coord in feature_data["geometry"]["coordinates"]
            ])
            feature.setGeometry(geometry)
            layer.addFeature(feature)
        
        symbol = QgsLineSymbol()
        symbol.setWidth(1.26)
        symbol.setColor(QColor(101, 15, 207))
        layer_renderer = QgsSingleSymbolRenderer(symbol)
        layer.setRenderer(layer_renderer)
        
        if not layer.isValid():
            print("Ошибка при создании слоя!")

        layer.commitChanges()
        layer.updateExtents()
        
        root = QgsProject.instance().layerTreeRoot()
        group = next(
            (child for child in root.children() if isinstance(child, QgsLayerTreeGroup) and child.name() == 'Общие стили'),
            None)
        
        if group is None:
            group = root.addGroup('Общие стили')
        
        QgsProject.instance().addMapLayer(layer, False)
        group.insertChildNode(0, QgsLayerTreeLayer(layer))
    
#######################################################################################################################################################


######### CALCULATE FUNCTIONS #########

    def get_peregon_count(self, geojson):
        min = 0
        for feature in geojson['features']:
            if 'properties' in feature.keys():
                if 'peregon' in feature['properties'].keys():
                    if feature['properties']['peregon'] > min:
                        min = feature['properties']['peregon']
        return min


    def find_number_by_peregon_count(self, df, peregon_count, type_name):
        df = df.loc[:, ['Номер', 'N перегона', 'Направление']]
        df = df.where(df['Направление'] == type_name)
        df = df.groupby('Номер')['N перегона'].max().reset_index()
        for items in df.to_numpy():
            if items[1] == peregon_count:
                return items[0]


    def calculate_zagr_passp_by_peregons(self, geojson, df):
        values = []
        peregons = []
        count = 0
        exit_data = []
        for _, row in df.iterrows():
            peregons.append(row['N перегона'])
            exit_data.append((row['Кол-во соц'], row['Кол-во ком']))
            count_pass = row['Кол-во пассажиров']
            count_zagr = round(count_pass / row['Сидячих мест'] * 100, 2)
            values.append((count_pass, count_zagr))
        
        for feature in geojson['features']:
            if 'properties' in feature.keys():
                if 'peregon' in feature['properties'].keys():
                    if count < len(peregons):
                        if feature['properties']['peregon'] != peregons[count]:
                            feature['properties']['zagr'] = 0
                            feature['properties']['passp'] = 0
                            feature['properties']['kol_soc'] = 0
                            feature['properties']['kol_kom'] = 0
                        else:
                            feature['properties']['zagr'] = values[count][1]
                            feature['properties']['passp'] = values[count][0]
                            feature['properties']['kol_soc'] = exit_data[count][0]
                            feature['properties']['kol_kom'] = exit_data[count][1]
                            count += 1
                    else:
                        feature['properties']['zagr'] = 0
                        feature['properties']['passp'] = 0
                        feature['properties']['kol_soc'] = 0
                        feature['properties']['kol_kom'] = 0


    def parse_df(self, df):
        agg_funcs = {
            'Кол-во автобусов': 'first',  
            'Рег.номер': 'first',
            'Загруженность': 'sum',  
            'Маршрут': 'first',
            'Вместимость общая': 'first',
            'Сидячих мест': 'first',
            'Вместимость': 'first',
            'Направление': 'first',
            'ГРЗ': 'first',
            'Кол-во пассажиров': 'sum',
            'Номер': 'first',
            'Кол-во соц': 'first',
            'Кол-во ком': 'first'
        }
        df = df.groupby('N перегона', as_index=False).agg(agg_funcs)
        return df


    async def fetch_sobop_by_hour(self, geojson, reg, type_name):
        if int(reg) in (item['reg'] for item in self.sobop_data):
            peregon_count = self.get_peregon_count(geojson)
            data = [item['data'] for item in self.sobop_data if item['reg'] == int(reg)]
            df = pd.DataFrame(data[0])
            number = self.find_number_by_peregon_count(df, peregon_count, type_name)
            df = df.where(df['Направление'] == type_name)
            df = df.where(df['Номер'] == number).dropna()
            if df.empty != True:
                df = self.parse_df(df)
                self.calculate_zagr_passp_by_peregons(geojson, df)
        else:
            for feature in geojson['features']:
                if 'properties' in feature.keys():
                    feature['properties']['zagr'] = 0
                    feature['properties']['passp'] = 0


    async def fetch_sobop_by_stop_point(self, geojson, reg, type_name):
        uuid = geojson['features'][0]['properties']['variant_uuid']
        data = await self.get_zagr_passp(route_type=type_name, var_uid=uuid, date=self.date)
        index = 0
        for item in data:
            passp = 0
            passp += abs(item['Зашло всего'] - item['Вышло всего'])
            feature = geojson['features'][index]
            if 'properties' in feature.keys():
                if 'peregon' in feature['properties'].keys():
                    if index == item['№ остановки'] - 1:
                        feature['properties']['zagr'] = 0
                        feature['properties']['passp'] = passp
                        feature['properties']['kol_soc'] = item['Зашло СК']
                        feature['properties']['kol_kom'] = item['Зашло ком']
                        index += 1
                        continue
            while(index != item['№ остановки'] - 1):
                geojson['features'][index]['properties']['zagr'] = 0
                geojson['features'][index]['properties']['passp'] = 0
                geojson['features'][index]['properties']['kol_soc'] = 0
                geojson['features'][index]['properties']['kol_kom'] = 0
                index += 1
            geojson['features'][index]['properties']['zagr'] = 0
            geojson['features'][index]['properties']['passp'] = passp
            geojson['features'][index]['properties']['kol_soc'] = item['Зашло СК']
            geojson['features'][index]['properties']['kol_kom'] = item['Зашло ком']
            index += 1


    def get_array_regs(self):
        with open(self.filepath, encoding='utf-8') as f:
            data = json.load(f)
        return data


    def chunks(self, lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

#######################################################################################################################################################


######### TRANSFORM VARIANTS TO DIFFERENT LAYERS #########

    async def distillation(self, variant, data_item):
        number = data_item['route_number']
        name = variant['name']
        reg = data_item['route_reg_number']
        geojson = self.get_geojson()
        busstop = {}
        b, geojson = self.update_feature_2(variant, geojson, 'forward_points', data_item)
        print(reg)
        
        if self.getStopPoint:
            if len(geojson['features']) != 0:
                forward_points_sobop, reverse_points_sobop = await self.get_stop_point_data(date= self.date, uuid=geojson['features'][0]['properties']['variant_uuid'])
            else:
                forward_points_sobop = []
                reverse_points_sobop = []
        else:
            forward_points_sobop = []
            reverse_points_sobop = []

        if len(b) != 0:
            for obj in b:
                try:
                    if obj not in busstop[str(variant['name'])]:
                        busstop[variant['name']].append(obj)
                except:
                    busstop[variant['name']] = [obj]
            for _, v in busstop.items():
                for b in v:
                    feature = self.get_feature('Point')
                    feature['geometry']['coordinates'] = b
                    geojson['features'].append(feature)

            if self.isSOBOP and self.getStopPoint == False:
                await self.fetch_sobop_by_hour(geojson, data_item['route_reg_number'], 'прямое')
            elif self.getStopPoint:
                await self.fetch_sobop_by_stop_point(geojson, data_item['route_reg_number'], 'прямое')

            self.add_layer_to_project(geojson, f'№{number}-{name}-{reg}-прямое', f'forwards-{self.company}', stop_points=forward_points_sobop)

        geojson = self.get_geojson()
        busstop = {}
        b, geojson = self.update_feature_2(variant, geojson, 'reverse_points', data_item)
        if len(b) != 0:
            for obj in b:
                try:
                    if obj not in busstop[str(variant['name'])]:
                        busstop[variant['name']].append(obj)
                except:
                    busstop[variant['name']] = [obj]
            for _, v in busstop.items():
                for b in v:
                    feature = self.get_feature('Point')
                    feature['geometry']['coordinates'] = b
                    geojson['features'].append(feature)

            
            if self.isSOBOP and self.getStopPoint == False:
                await self.fetch_sobop_by_hour(geojson, data_item['route_reg_number'], 'обратное')
            elif self.getStopPoint:
                await self.fetch_sobop_by_stop_point(geojson, data_item['route_reg_number'], 'обратное')

            self.add_layer_to_project(geojson, f'№{number}-{name}-{reg}-обратное', f'reverses-{self.company}', stop_points=reverse_points_sobop)


    async def fetchVariants(self, isStopPoint = False):
        percent = 0
        regs = self.get_array_regs()
        route_list = await self.get_data_from_outfit_plan(regs)
        if self.isSOBOP and isStopPoint == False:
            self.sobop_data = await self.get_workload_tkp(date=self.date, time=self.time, array_regs=regs)
        elif isStopPoint:
            self.getStopPoint = True
        
        for route in route_list:
            self.dialog.status_label.setText('Отрисовка геометрии. ..')
            for variant in route['variants']:
                self.dialog.progress.setValue(percent)
                percent += 100 / len(route['variants'])
                if percent >= len(route['variants']):
                    percent = 0
                await self.distillation(variant, route)
        self.dialog.status_label.setText(f'Загружено маршрутов: {len(route_list)}')

#######################################################################################################################################################


######### TRANSFORM VARIANTS TO ONE LAYER #########

    async def distilation_by_layer(self, geojson, variant, data_item):
        geojson = self.update_feature_layer_2(variant, geojson, 'forward_points', data_item)
        geojson = self.update_feature_layer_2(variant, geojson, 'reverse_points', data_item)


    async def fetchLayerVariants(self):
        percent = 0
        regs = self.get_array_regs()
        route_list = await self.get_data_from_outfit_plan(regs)
        if self.isSOBOP:
            self.sobop_data = await self.get_type_payment(date=self.date, array_regs=regs)
        geojson = self.get_geojson()
        for route in route_list:
            self.dialog.status_label.setText('Отрисовка геометрии. ..')
            for variant in route['variants']:
                self.dialog.progress.setValue(percent)
                percent += 100 / len(route['variants'])
                if percent >= len(route['variants']):
                    percent = 0
                await self.distilation_by_layer(geojson, variant, route)
        self.add_one_layer_to_project(geojson)
        self.dialog.status_label.setText(f'Загружено маршрутов: {len(route_list)}')

#######################################################################################################################################################


######### START UI FUNCTIONS #########

    async def progress_bar(self, type=1):
        self.dialog.progress.setMaximum(100)
        i = 0
        if type == 1:
            task = asyncio.create_task(self.fetchVariants())
        elif type == 2:
            task = asyncio.create_task(self.fetchLayerVariants())
        else:
            task = asyncio.create_task(self.fetchVariants(isStopPoint=True))
        await task

#######################################################################################################################################################