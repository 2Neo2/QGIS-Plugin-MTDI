from PyQt5.QtWidgets import *
from qgis.core import *
from qgis.PyQt.QtGui import *
from PyQt5.QtCore import *
import asyncio
import json
import pandas as pd
from .tkp import TKP_API
from .rnis import RNIS
import os
import math
from pyproj import Transformer

class AsyncNetworkVariants():
    def __init__(self, 
                 dialog, 
                 regs, 
                 time, 
                 company, 
                 isSOBOP, 
                 date_from, 
                 date_to, 
                 period, 
                 munic_uuid=None, 
                 delay=5
             ):
        self.array_regs = regs if regs else []
        self.date_from = date_from
        self.date_to = date_to
        self.delay = delay
        self.dialog = dialog
        self.sobop_data = []
        self.time = time
        self.isSOBOP = isSOBOP
        self.getStopPoint = False
        self.company = company
        self.sobop_stop_point_data = []
        self.tkp = TKP_API
        self.rnis = RNIS
        self.login_tkp = 'AnichenkovAnA@mosreg.ru'
        self.password_tkp = 'atQ495Lp!'
        self.login_rnis = 'Karpenko'
        self.password_rnis = 'H7DneQW3'
        self.token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJSTklTIiwiYXVkIjoiaHR0cDpcL1wvcm5pcy5jb20iLCJpYXQiOjE3MTExMDAxMjYsIm5iZiI6MTcxMTAxNDAyNiwiaW5mbyI6IntcInVzZXJcIjp7XCJ1dWlkXCI6XCI1N2FjOTMyMC05OWI5LTExZWUtOTNhOS0wMmE1MjBkYTE4NWJcIixcImxvZ2luXCI6XCJTaGVwZWxldlwiLFwiY29tcG9uZW50XCI6XCJvcGVyYXRvclwiLFwiaXNfc3lzdGVtXCI6ZmFsc2UsXCJpc19zdXBlcnZpc29yXCI6ZmFsc2UsXCJpc19zZW1pX2NvbmZpcm1lZFwiOmZhbHNlLFwiaXNfbm90aWZpY2F0ZWRcIjpmYWxzZSxcImluZm9cIjp7XCJ1bml0X3V1aWRcIjpcImU2ZmExZjA0LWNiOTMtMTFlYS1iMWZlLTAyZjQyYjA0MzZlMVwifX19In0.BWzWSVcudo0w9UkyQNQ_-ChbXmc9MO4zuBaH8DY2XK0'
        self.variant_pass_count = 0
        self.downloaded_layers = []
        self.period = period
        self.munic_uuid = munic_uuid


######### RNIS #########

    def get_variant_data(self, points, variant_name):
        data = {
            'variant_uuid': '',
            'name': '',
            'forward_points': {
                'busstop':[], 
                'coord':[]             
            },
            'reverse_points': {
                'busstop':[], 
                'coord':[]
            },
        }
        for point in points:
            data['variant_uuid'] = point.get('route_variant_uuid')
            data['name'] = variant_name.get(data['variant_uuid'])
            type = 'forward_points' if point['is_forward_direction'] else 'reverse_points'
            if point.get('point_type') == 'stop_point':
                lon = point.get('longitude', None)
                lat = point.get('latitude', None)
                if lon and lat is not None:
                    data[type]['busstop'].append([lon, lat])
            path = point.get('path_to_the_next_point_geometry', False)
            if path:
                coordinates = []
                for c in path.get('coordinates', []):
                    coordinates.append(c)
                if len(coordinates) > 0:
                    data[type]['coord'].append(coordinates)
        return data
    

    def get_variant(self, order, variant_name):
        """Получение вариантов"""
        data = {}
        for shift in order.get('shifts', []):
            for run in shift.get('runs', []):
                if run.get('type') in ['production_forward', 'production_reverse']:
                    route = run.get('route_uuid')
                    
                    variant = self.get_variant_data(run.get('points', []), variant_name)
                    data[route] = data.get(route, [])
                    
                    if variant not in data[route]:
                        data[route].append(variant)
        return data


    async def get_munic_data_from_outfit_plan(self):
        progress_value = 0
        
        async with RNIS(login=self.login_rnis, password=self.password_rnis, token=self.token) as rnis:
            self.dialog.munic_status_label.setText('Получаем маршруты...')
            
            route_list = await rnis.API.Geo.Route.to_list(
                all_pages = True,
                concurrency=5,
                delay=10,
                retries=7,
                limit = 1000,
                status=["1abd2f98-7845-11e7-be3f-3a4e0357cc4a"],
                mun = self.munic_uuid,
                response_data=["items/registration_number"]
            )
            route_list = [r['registration_number'] for r in route_list['payload'][0]['items']]
            route_list = list(set(route_list))

            self.dialog.munic_status_label.setText('Получаем план наряды...')
            progress_value += 20
            self.dialog.munic_progress_bar.setValue(progress_value)
            
            # print(json.dumps(route_list, indent=4, ensure_ascii=False))
            
            order_list = await rnis.API.Geo.Order.to_list(
                all_pages = True,
                concurrency=5,
                delay=10,
                retries=7,                                                    
                date = self.date_from,
                route_reg_number = route_list,
                response_data=[]
            )

            order_uuids = [{
                'order_uuid': item['uuid'],
                'route_reg_number': item['route_registration_number'],
                'route_name': item['route_name'],
                'route_number': item['route_number'],
                'route_uuid': item['route_uuid'],
                } for p in order_list['payload'] for item in p['items']]

            self.dialog.munic_status_label.setText('Получаем названия вариантов...')
            progress_value += 20
            self.dialog.munic_progress_bar.setValue(progress_value)

            route_uuid = list(set([r['route_uuid'] for r in order_uuids]))
            variant_name = {}
            for r in route_uuid:
                data = await rnis.API.Geo.Route.Variant.to_list(
                    route_uuid=r,
                    all_pages = True,
                    retries=1,
                    delay=5,
                    response_data=[],
                    print_error=True
                )
                for d in data['payload']:
                    for item in d['items']:
                        variant_name[item['uuid']] = item['name']

            self.dialog.munic_status_label.setText('Получаем варианты...')
            progress_value += 20
            self.dialog.munic_progress_bar.setValue(progress_value)

            variant_list = await rnis.API.Geo.Order.read(
                uuid_list = [item['order_uuid'] for item in order_uuids],
                all_pages = True,
                retries=7,
                delay=10
            )

            variant_list = [self.get_variant(item, variant_name) for item in variant_list['payload']]

            variant_dict = {}

            for variant in variant_list:
                for k, v in variant.items():
                    variant_dict[k] = variant_dict.get(k, [])
                    variant_dict[k].extend(item for item in v if item not in variant_dict[k])

            route_registry = []

            self.dialog.munic_status_label.setText('Получаем тип ТС...')
            progress_value += 20
            self.dialog.munic_progress_bar.setValue(progress_value)

            # for item in order_list:
                # reg = item['route_registration_number']
                # self.array_regs.append(reg)
            registry = await rnis.API.Geo.Route.Registry.to_list(
                reg_number=route_list,
                response_data=['items/vehicle_type_uuid', 'items/route/uuid', 'items/vehicles_plan/vehicle_capacity_type_uuid'],
                all_pages = True,
                retries=5,
                delay=5
            )
            for p in registry['payload']:
                route_registry.append(p['items'])
            
            dictionary = await rnis.API.Dictionary.list_many(
                dictionary=['vehicle_types', 'vehicle_capacity_types'],
                print_error=True,
                retries=3
            )

            dictionary_info = {}
            for item in dictionary['payload'][0]['items']:
                dictionary_info[item['key']] = {}
                for d in item['documents']:
                    dictionary_info[item['key']][d['uuid']] = d['name']
            
            registry_dict = {}

            for item in route_registry:
                for registry in item:
                    new_key = registry['route']['uuid']
                    vehicle_type = registry.get('vehicle_type_uuid', '')
                    name = ''
                    class_name = ''

                    if vehicle_type != '':
                        name = dictionary_info['vehicle_types'].get(vehicle_type)
                    
                    for i in registry['vehicles_plan']:
                        class_name = dictionary_info['vehicle_capacity_types'].get(i['vehicle_capacity_type_uuid'], '')
                        if class_name != '':
                                    break
                        
                    if new_key not in registry_dict.keys():
                        registry_dict[new_key] = {
                            'name': name,
                            'class_name': class_name if class_name is not None else ''
                        }
        
            changed_order_data = []
            for order in order_uuids:
                del order['order_uuid']
                if order not in changed_order_data:
                    changed_order_data.append(order)

            self.dialog.munic_status_label.setText('Подготавливаем варианты...')
            progress_value += 20
            self.dialog.progress.setValue(progress_value)

            result_variants = {}
            for r in changed_order_data:
                u = r['route_uuid']
                result_variants[u] = result_variants.get(u, {})
                result_variants[u]['route_reg_number'] = r['route_reg_number']
                result_variants[u]['route_number'] = r['route_number']
                result_variants[u]['vehicle_type'] = registry_dict[r['route_uuid']]['name'] if r['route_uuid'] in registry_dict.keys() else ''
                result_variants[u]['vehicle_class_type'] = registry_dict[r['route_uuid']]['class_name'] if r['route_uuid'] in registry_dict.keys() else ''
                result_variants[u]['variants'] = variant_dict.get(u, [])
                result_variants[u]['route_name'] = r.get('route_name', [])

            result = [{'route_uuid': k} | v for k,v in result_variants.items()]
            return result
        

    async def get_data_from_outfit_plan(self, array_regs):
        progress_value = 0
        """Получаем варианты маршрутов из план нарядов."""
        async with RNIS(login=self.login_rnis, password=self.password_rnis, token=self.token) as rnis:
            self.dialog.status_general_label.setText('Получаем маршруты...')
            
            order_list = await rnis.API.Geo.Order.to_list(
                all_pages = True,
                concurrency=5,
                delay=10,
                retries=7,                                                    
                date = self.date_from,
                route_reg_number = array_regs,
                response_data=[]
            )

            self.dialog.status_general_label.setText('Получаем план наряды...')
            progress_value += 20
            self.dialog.progress.setValue(progress_value)

            order_uuids = [{
                'order_uuid': item['uuid'],
                'route_reg_number': item['route_registration_number'],
                'route_name': item['route_name'],
                'route_number': item['route_number'],
                'route_uuid': item['route_uuid'],
                } for p in order_list['payload'] for item in p['items']]

            self.dialog.status_general_label.setText('Получаем названия вариантов...')
            progress_value += 20
            self.dialog.progress.setValue(progress_value)

            route_uuid = list(set([r['route_uuid'] for r in order_uuids]))
            variant_name = {}
            for r in route_uuid:
                data = await rnis.API.Geo.Route.Variant.to_list(
                    route_uuid=r,
                    all_pages = True,
                    retries=1,
                    delay=5,
                    response_data=[],
                    print_error=True
                )
                for d in data['payload']:
                    for item in d['items']:
                        variant_name[item['uuid']] = item['name']

            self.dialog.status_general_label.setText('Получаем варианты...')
            progress_value += 20
            self.dialog.progress.setValue(progress_value)

            variant_list = await rnis.API.Geo.Order.read(
                uuid_list = [item['order_uuid'] for item in order_uuids],
                all_pages = True,
                retries=7,
                delay=10
            )

            variant_list = [self.get_variant(item, variant_name) for item in variant_list['payload']]

            variant_dict = {}

            for variant in variant_list:
                for k, v in variant.items():
                    variant_dict[k] = variant_dict.get(k, [])
                    variant_dict[k].extend(item for item in v if item not in variant_dict[k])


            route_registry = []

            self.dialog.status_general_label.setText('Получаем тип ТС...')
            progress_value += 20
            self.dialog.progress.setValue(progress_value)

            for reg_number in array_regs:
                registry = await rnis.API.Geo.Route.Registry.to_list(
                    reg_number=reg_number,
                    response_data=['items/vehicle_type_uuid', 'items/route/uuid', 'items/vehicles_plan/vehicle_capacity_type_uuid'],
                    all_pages = True,
                    retries=5,
                    delay=5
                )
                for p in registry['payload']:
                    route_registry.append(p['items'])
            
            dictionary = await rnis.API.Dictionary.list_many(
                dictionary=['vehicle_types', 'vehicle_capacity_types'],
                print_error=True,
                retries=3
            )

            dictionary_info = {}
            for item in dictionary['payload'][0]['items']:
                dictionary_info[item['key']] = {}
                for d in item['documents']:
                    dictionary_info[item['key']][d['uuid']] = d['name']
            
            registry_dict = {}

            for item in route_registry:
                for registry in item:
                    new_key = registry['route']['uuid']
                    vehicle_type = registry.get('vehicle_type_uuid', '')
                    name = ''
                    class_name = ''

                    if vehicle_type != '':
                        name = dictionary_info['vehicle_types'].get(vehicle_type)
                    
                    for i in registry['vehicles_plan']:
                        class_name = dictionary_info['vehicle_capacity_types'].get(i['vehicle_capacity_type_uuid'], '')
                        if class_name != '':
                                    break
                        
                    if new_key not in registry_dict.keys():
                        registry_dict[new_key] = {
                            'name': name,
                            'class_name': class_name if class_name is not None else ''
                        }
        
            changed_order_data = []
            for order in order_uuids:
                del order['order_uuid']
                if order not in changed_order_data:
                    changed_order_data.append(order)

            self.dialog.status_general_label.setText('Подготавливаем варианты...')
            progress_value += 20
            self.dialog.progress.setValue(progress_value)

            result_variants = {}
            for r in changed_order_data:
                u = r['route_uuid']
                result_variants[u] = result_variants.get(u, {})
                result_variants[u]['route_reg_number'] = r['route_reg_number']
                result_variants[u]['route_number'] = r['route_number']
                result_variants[u]['vehicle_type'] = registry_dict[r['route_uuid']]['name'] if r['route_uuid'] in registry_dict.keys() else ''
                result_variants[u]['vehicle_class_type'] = registry_dict[r['route_uuid']]['class_name'] if r['route_uuid'] in registry_dict.keys() else ''
                result_variants[u]['variants'] = variant_dict.get(u, [])
                result_variants[u]['route_name'] = r.get('route_name', [])

            result = [{'route_uuid': k} | v for k,v in result_variants.items()]
            return result

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
                date_from = self.date_from,
                date_to = self.date_to if self.date_to else self.date_from
            )

            forwards = await card.json

            card.parameters_update(
                route_reg = d.get('uuid'),
                shift = 'обратное',
                date_from = self.date_from,
                date_to = self.date_to if self.date_to else self.date_from
            )

            reverses = await card.json

        return forwards, reverses
    

    async def get_type_payment(self, **d):
        """Получаем инфо из СОБОП по типам оплаты: БК, СК, КОЛ-ВСЕГО"""
        company = 1 if self.company == 'МТА' else 2
        async with self.tkp(self.login_tkp, self.password_tkp) as tkp:
            card = tkp.Card
            await card(3192)
            card.parameters_update (
                date_from = self.date_from,
                date_to = self.date_to if self.date_to else self.date_from,
                route_reg = d.get('array_regs', []),
                group_by = [2, 0, company]
            )
            data = await card.json
        return data


    async def get_zagr_passp(self, **d):
        """"""
        async with self.tkp(self.login_tkp, self.password_tkp) as tkp:
            card = tkp.Card
            await card(3451)

            card.parameters_update (
                date_from = self.date_from,
                date_to = self.date_to if self.date_to else self.date_from,
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
                    date = self.date_from,
                    time_from = f"{time_values[0]}:00",
                    time_to = f"{time_values[1]}:00",
                    occupancy = 0
                )
                data = await card.json
                if len(data) != 0:
                    sobop_data.append(data)
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
                    "description": "",
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


    def update_feature_2(self, variant, geojson, route_type, data_item):
        busstop, coord = variant.get(route_type).get('busstop'), variant.get(route_type).get('coord')
        reg_number = data_item['route_reg_number']
        for i, c in enumerate(coord, 1):
            feature = self.get_feature('LineString')
            feature['geometry']['coordinates'] = c
            feature['properties']['description'] = f'Вариант маршрута {reg_number}'
            feature['properties']['peregon_name'] = f'Перегон: {i}'
            feature['properties']['variant_name'] = variant['name']
            feature['properties']['variant_uuid'] = variant['variant_uuid']
            feature['properties']['route_number'] = data_item['route_number']
            feature['properties']['route_reg_number'] = data_item['route_reg_number']
            feature['properties']['route_name'] = data_item['route_name']
            feature['properties']['route_uuid'] = data_item['route_uuid']
            feature['properties']['date_from'] = str(self.date_from)
            feature['properties']['type'] = data_item['vehicle_type']
            feature['properties']['class_type'] = data_item['vehicle_class_type']
            geojson['features'].append(feature)
        return busstop, geojson
    

    def is_stop_point_in_layer(self, data, point_number):
        for i in data:
            if point_number == int(i['№ остановки']):
                return i
        return None


    def get_points_geojson_layer(self, geojson, stop_point_data):
        if len(stop_point_data) == 0:
            return geojson
        index = 0
        for item in geojson['features']:
            if item['geometry']['type'] == 'Point':
                data = self.is_stop_point_in_layer(stop_point_data, index + 1)
                if data is not None:
                    item['properties']['description'] = f"Номер остановки {index + 1}"
                    item['properties']['Вышло всего'] = data['Вышло всего']
                    item['properties']['Зашло всего'] = data['Зашло всего']
                    item['properties']['Вышло СК'] = data['Вышло СК']
                    item['properties']['Зашло СК'] = data['Зашло СК']
                    item['properties']['Вышло ком'] = data['Вышло ком']
                    item['properties']['Зашло ком'] = data['Зашло ком']   
                else:
                    item['properties']['description'] = f"Номер остановки {index + 1}"
                    item['properties']['Вышло всего'] = 0
                    item['properties']['Зашло всего'] = 0
                    item['properties']['Вышло СК'] = 0
                    item['properties']['Зашло СК'] = 0
                    item['properties']['Вышло ком'] = 0
                    item['properties']['Зашло ком'] = 0
                index += 1
        return geojson
    

    def update_feature_layer_2(self, variant, geojson, route_type, data_item):
        coord = variant.get(route_type).get('coord')
        kol_soc = 0
        kol_kom = 0
        kol_total = 0
        flag = True
        reg_number = data_item['route_reg_number']
        
        feature = self.get_feature('LineString')
        feature['properties']['description'] = f'Вариант маршрута {reg_number}'
        feature['properties']['variant_name'] = f"{variant['name']}-{route_type}"
        feature['properties']['variant_uuid'] = variant['variant_uuid']
        feature['properties']['route_number'] = data_item['route_number']
        feature['properties']['route_reg_number'] = data_item['route_reg_number']
        feature['properties']['route_name'] = data_item['route_name']
        feature['properties']['route_uuid'] = data_item['route_uuid']
        feature['properties']['type'] = data_item['vehicle_type']
        feature['properties']['class_type'] = data_item['vehicle_class_type']
        feature['properties']['date_from'] = str(self.date_from)

        if self.isSOBOP:
            for item in self.sobop_data:
                if str(item['РЕГ НОМЕР']) == str(data_item['route_reg_number']):
                    flag = False
                    kol_soc += item['КОЛ СОЦ'] if item['КОЛ СОЦ'] else 0
                    kol_kom += item['КОЛ КОММ'] if item['КОЛ КОММ'] else 0
                    kol_total += item['КОЛ ВСЕГО'] if item['КОЛ ВСЕГО'] else 0

            if self.date_to is not None:
                feature['properties']['date_to'] = str(self.date_to)

            if flag and self.isSOBOP:
                print(f"{data_item['route_reg_number']} не добавлен! Причина - нет в СОБОП ")
                return geojson
            
            feature['properties']['kol_soc'] = kol_soc
            feature['properties']['kol_kom'] = kol_kom
            feature['properties']['kol_total'] = kol_total

        feature['geometry']['coordinates'] = coord

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
            integer_values = []
            for value in values:
                if value is not None:
                    if type(value) != QVariant:
                        integer_values.append(int(value))

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
                self.variant_pass_count += 1
        else:
            symbol = QgsLineSymbol()
            symbol.setWidth(1.26)
            symbol.setColor(QColor(101, 15, 207))
            layer_renderer = QgsSingleSymbolRenderer(symbol)
            layer.setRenderer(layer_renderer)
            layer.triggerRepaint()
            print(f"Поле '{category_field_name}' не найдено в слое.")

    
    def interpolate_color(self, minval, maxval, val, color_palette):
        """Interpolates a color from a color palette based on a value."""
        val = max(minval, min(maxval, val))
        norm_val = (val - minval) / (maxval - minval)
        idx = int(norm_val * (len(color_palette) - 1))
        return color_palette[idx]


    def get_color_gradient(self):
        """Creates a color gradient from green to red with transparency."""
        color_palette = [QColor(0, 255, 0, 141), QColor(255, 255, 0, 141), QColor(255, 0, 0, 141)]
        gradient = []
        for i in range(101):
            gradient.append(QColor(
                color_palette[0].red() + i * (color_palette[2].red() - color_palette[0].red()) // 100,
                color_palette[0].green() + i * (color_palette[2].green() - color_palette[0].green()) // 100,
                color_palette[0].blue() + i * (color_palette[2].blue() - color_palette[0].blue()) // 100,
                141  # Transparency
            ))
        return gradient
    
    def convert_coordinates(self, lon, lat):
        x = (lon * 20037508.34) / 180
        y = math.log(math.tan(((90 + lat) * math.pi) / 360)) / (math.pi / 180)
        y = (y * 20037508.34) / 180
        return [x, y]


    def get_buffer_points_layer(self, layer, layer_name):
        root = QgsProject.instance().layerTreeRoot()
        group_name = 'Загруженность остановок'
        values = set()
        category_field_names = ['Зашло всего', 'Вышло всего']
        group = next(
            (child for child in root.children() if isinstance(child, QgsLayerTreeGroup) and child.name() == group_name),
            None)

        for feature in layer.getFeatures():
            fields_names = feature.fields().names()
            if all(name in fields_names for name in category_field_names):
                sum_value = float(feature[category_field_names[0]]) + float(feature[category_field_names[1]])
                values.add(sum_value)
        
        if not values:
            return

        buffer_layer = QgsVectorLayer('Polygon?crs=EPSG:3857', layer_name, 'memory')
        provider = buffer_layer.dataProvider()
        provider.addAttributes([
            QgsField('Номер остановки', QVariant.Int),
            QgsField('Зашло', QVariant.Double),
            QgsField('Вышло', QVariant.Double),
            QgsField('Пасспоток', QVariant.Double)
            ])
        
        buffer_layer.updateFields()

        min_value = min(values)
        max_value = max(values)
        stop_point_number = 1

        radius_base = 500
        buffer_features = []
        for feature in layer.getFeatures():
            fields_names = feature.fields().names()
            if all(name in fields_names for name in category_field_names):
                enter = float(feature[category_field_names[0]])
                exit = float(feature[category_field_names[1]])
                sum_value = enter + exit
                point = feature.geometry().asPoint()
                x2,y2 = self.convert_coordinates(point.x(), point.y())
                swapped_point = QgsPointXY(x2, y2)

                geom = QgsGeometry.fromPointXY(swapped_point)
                buffer_geom = geom.buffer(radius_base * ((sum_value - min_value) / (max_value - min_value) + 1), 20)
                buffer_feature = QgsFeature()
                buffer_feature.setGeometry(buffer_geom)
                buffer_feature.setAttributes([stop_point_number, enter, exit, sum_value])
                buffer_features.append((buffer_feature, sum_value))
            stop_point_number += 1
        
        provider.addFeatures([item[0] for item in buffer_features])
        QgsProject.instance().addMapLayer(buffer_layer, False)

        # Create categorized renderer
        categories = []
        for buffer_feature in buffer_features:
            value = buffer_feature[1]
            color = self.interpolate_color(min_value, max_value, value, self.get_color_gradient())
            symbol = QgsFillSymbol.createSimple({'color': color.name(QColor.HexArgb), 'outline_color': '0,0,0,141'})
            category = QgsRendererCategory(value, symbol, str(value))
            categories.append(category)
        
        renderer = QgsCategorizedSymbolRenderer('Пасспоток', categories)
        buffer_layer.setRenderer(renderer)
        buffer_layer.triggerRepaint()

        if group is None:
            group = root.addGroup(group_name)
        
        group.insertChildNode(0, QgsLayerTreeLayer(buffer_layer))


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
            group_name = f'Остановки-{group_name}'
            self.get_buffer_points_layer(new_layer_points, new_layer_points.name())
            group = next(
            (child for child in root.children() if isinstance(child, QgsLayerTreeGroup) and child.name() == group_name),
            None)

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
        layer.addAttribute(QgsField("variant_name", QVariant.String))
        layer.addAttribute(QgsField("variant_uuid", QVariant.String))
        layer.addAttribute(QgsField("route_number", QVariant.String))
        layer.addAttribute(QgsField("route_reg_number", QVariant.String))
        layer.addAttribute(QgsField("route_name", QVariant.String))
        layer.addAttribute(QgsField("route_uuid", QVariant.String))
        layer.addAttribute(QgsField("type", QVariant.String))
        layer.addAttribute(QgsField("class_type", QVariant.String))
        layer.addAttribute(QgsField("date_from", QVariant.String))

        if self.isSOBOP:
            if self.date_to is not None:
                layer.addAttribute(QgsField("date_to", QVariant.String))
            layer.addAttribute(QgsField("kol_soc", QVariant.String))
            layer.addAttribute(QgsField("kol_kom", QVariant.String))
            layer.addAttribute(QgsField("kol_total", QVariant.String))

        for feature_data in geojson_obj["features"]:
            feature = QgsFeature()
            if self.isSOBOP:
                if self.date_to is not None:
                    feature.setAttributes([
                        feature_data["properties"]["description"],
                        feature_data["properties"]["variant_name"],
                        feature_data["properties"]["variant_uuid"],
                        feature_data["properties"]["route_number"],
                        feature_data["properties"]["route_reg_number"],
                        feature_data["properties"]["route_name"],
                        feature_data["properties"]["route_uuid"],
                        feature_data["properties"]["type"],
                        feature_data["properties"]["class_type"],
                        feature_data["properties"]["date_from"],
                        feature_data["properties"]["date_to"],
                        feature_data["properties"]["kol_soc"],
                        feature_data["properties"]["kol_kom"],
                        feature_data["properties"]["kol_total"]
                    ])
                else:
                    feature.setAttributes([
                        feature_data["properties"]["description"],
                        feature_data["properties"]["variant_name"],
                        feature_data["properties"]["variant_uuid"],
                        feature_data["properties"]["route_number"],
                        feature_data["properties"]["route_reg_number"],
                        feature_data["properties"]["route_name"],
                        feature_data["properties"]["route_uuid"],
                        feature_data["properties"]["type"],
                        feature_data["properties"]["class_type"],
                        feature_data["properties"]["date_from"],
                        feature_data["properties"]["kol_soc"],
                        feature_data["properties"]["kol_kom"],
                        feature_data["properties"]["kol_total"]
                    ])                 
            else:
                feature.setAttributes([
                    feature_data["properties"]["description"],
                    feature_data["properties"]["variant_name"],
                    feature_data["properties"]["variant_uuid"],
                    feature_data["properties"]["route_number"],
                    feature_data["properties"]["route_reg_number"],
                    feature_data["properties"]["route_name"],
                    feature_data["properties"]["route_uuid"],
                    feature_data["properties"]["type"],
                    feature_data["properties"]["class_type"],
                    feature_data["properties"]["date_from"],
                ])
        
            geometry = QgsGeometry.fromPolylineXY([
                QgsPointXY(coord[0], coord[1]) for item in feature_data["geometry"]["coordinates"] for coord in item
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

    async def fetch_sobop_by_hour(self, geojson):
        variant_uuid = geojson['features'][0]['properties']['variant_uuid']
        for item in self.sobop_data:
            for variant_data in item:
                if variant_data['UUID варианта маршрута'] == variant_uuid:
                    peregon = variant_data['N перегона'] - 1
                    geojson['features'][peregon]['properties']['passp'] = str(variant_data['Кол-во пассажиров'])
                    geojson['features'][peregon]['properties']['zagr'] = f"{round(int(variant_data['Кол-во пассажиров']) / variant_data['Сидячих мест'] * 100, 2)} %"
                    geojson['features'][peregon]['properties']['kol_soc'] = str(variant_data['Кол-во соц']) if variant_data['Кол-во соц'] is not None else '0'
                    geojson['features'][peregon]['properties']['kol_kom'] = str(variant_data['Кол-во ком']) if variant_data['Кол-во ком'] is not None else '0'


    def get_feature_by_pereon(self, geojson, peregon_number):
        for feature in geojson['features']:
            if feature['geometry']['type'] == 'LineString':
                if feature['properties']['peregon_name'].split(' ')[1] == str(peregon_number):
                    return feature
        return None


    async def fetch_sobop_by_stop_point(self, geojson, type_name):
        uuid = geojson['features'][0]['properties']['variant_uuid']
        data = await self.get_zagr_passp(route_type=type_name, var_uid=uuid)
        peregon_index = 1
        current_passp = 0
        current_soc = 0 
        current_kom = 0

        for i in range(len(data) - 1):
            stop_point_prev = int(data[i]['№ остановки'])
            stop_point_curr = int(data[i+1]['№ остановки'])

            if stop_point_curr - stop_point_prev == 1:
                current_passp += data[i]['Зашло всего'] - data[i]['Вышло всего']
                current_soc += data[i]['Зашло СК'] - data[i]['Вышло СК']
                current_kom += data[i]['Зашло ком'] - data[i]['Вышло ком']

                feature = self.get_feature_by_pereon(geojson, stop_point_curr - 1)
                if feature is not None:
                    feature['properties']['passp'] = current_passp
                    feature['properties']['kol_soc'] = current_soc
                    feature['properties']['kol_kom'] = current_kom
                peregon_index += 1
            else:
                while peregon_index != stop_point_curr:
                    feature = self.get_feature_by_pereon(geojson, peregon_index)
                    
                    if feature is not None:                   
                        feature['properties']['passp'] = current_passp
                        feature['properties']['kol_soc'] = current_soc
                        feature['properties']['kol_kom'] = current_kom
                    peregon_index += 1


    def chunks(self, lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n] 


    def get_result_variant_data(self, routes_count, variants_count):
        if self.isSOBOP:
            total_passp = 0
            total_soc = 0
            total_kom = 0
            for variant in self.downloaded_layers:
                for feature in variant['features']:
                    if feature['geometry']['type'] == 'LineString':
                        if 'passp' in feature['properties'].keys() and 'kol_soc' in feature['properties'].keys() and 'kol_kom' in feature['properties'].keys():
                            passp = feature['properties']['passp']
                            soc = feature['properties']['kol_soc']
                            kom = feature['properties']['kol_kom']

                            if passp is not None and passp != 'None':
                                total_passp += int(passp)
                            if soc is not None and soc != 'None':
                                total_soc += int(soc)
                            if kom is not None and kom != 'None':
                                total_kom += int(kom)
            self.dialog.create_downloaded_layer_info_table('layer', [routes_count, variants_count, self.variant_pass_count, variants_count - self.variant_pass_count, total_passp, total_soc, total_kom])                  
        else:
            self.dialog.create_downloaded_layer_info_table('custom', [routes_count, variants_count])


    def get_result_layer_data(self, routes_count, variants_count):
        if self.isSOBOP:
            total_soc = 0
            total_kom = 0
            total = 0
            for variant in self.downloaded_layers:
                for feature in variant['features']:
                    if feature['geometry']['type'] == 'LineString':
                        soc = feature['properties']['kol_soc']
                        kom = feature['properties']['kol_kom']
                        total_value = feature['properties']['kol_total']

                        if soc != 'None':
                            total_soc += int(soc)
                        if kom != 'None':
                            total_kom += int(kom)
                        if total_value != 'None':
                            total += int(total_value)
                            
            self.dialog.create_downloaded_layer_info_table('network', [routes_count, variants_count, total_soc, total_kom, total])


    def get_result_info_stop_point_data(self, routes_count, variants_count):
        if self.isSOBOP:
            total_soc = 0
            total_kom = 0
            total_passp = 0
            for variant in self.downloaded_layers:
                for feature in variant['features']:
                    if feature['geometry']['type'] == 'LineString':
                        passp = 0
                        soc = 0
                        kom = 0

                        if 'passp' in feature['properties'].keys():
                            passp = feature['properties']['passp']
                        
                        if 'kol_soc' in feature['properties'].keys():
                            soc = feature['properties']['kol_soc']

                        if 'kol_kom' in feature['properties'].keys():
                            kom = feature['properties']['kol_kom']

                        if passp != 'None':
                            total_passp += int(passp)
                        if soc != 'None':
                            total_soc += int(soc)
                        if kom != 'None':
                            total_kom += int(kom)
                    
            self.dialog.create_downloaded_layer_info_table('point', [routes_count, variants_count, total_passp, total_soc, total_kom])
                        
    
    def get_data_reduction(self, busstop_list, variant):
        busstop, features = {}, []
        if len(busstop_list) != 0:
            for obj in busstop_list:
                busstop[variant['variant_uuid']] = busstop.get(variant['variant_uuid'], [])
                if obj not in busstop[str(variant['variant_uuid'])]:
                    busstop[variant['variant_uuid']].append(obj)
            for v in busstop.values():
                for b in v:
                    feature = self.get_feature('Point')
                    feature['geometry']['coordinates'] = b
                    features.append(feature)
        return features

#######################################################################################################################################################


######### TRANSFORM VARIANTS TO DIFFERENT LAYERS #########

    async def distillation(self, variant, data_item):
        number = data_item['route_number']
        name = variant['name']
        reg = data_item['route_reg_number']
        geojson = self.get_geojson()
        busstop, geojson = self.update_feature_2(variant, geojson, 'forward_points', data_item)

        if self.getStopPoint:
            if len(geojson['features']) != 0:
                forward_points_sobop, reverse_points_sobop = await self.get_stop_point_data(uuid=geojson['features'][0]['properties']['variant_uuid'])
            else:
                forward_points_sobop = []
                reverse_points_sobop = []
        else:
            forward_points_sobop = []
            reverse_points_sobop = []
        
        f = self.get_data_reduction(busstop, variant)
        if len(f) > 0:
            geojson['features'].extend(f)

            if self.isSOBOP and self.getStopPoint == False:
                await self.fetch_sobop_by_hour(geojson)
            elif self.getStopPoint:
                await self.fetch_sobop_by_stop_point(geojson, 'прямое')
            self.downloaded_layers.append(geojson)
            self.add_layer_to_project(geojson, f'№{number}-{name}-{reg}-прямое', f'forwards-{self.company}', stop_points=forward_points_sobop)

        geojson = self.get_geojson()
        busstop, geojson = self.update_feature_2(variant, geojson, 'reverse_points', data_item)
        f = self.get_data_reduction(busstop, variant)
        if len(f) > 0:
            geojson['features'].extend(f)
            
            if self.isSOBOP and self.getStopPoint == False:
                await self.fetch_sobop_by_hour(geojson)
            elif self.getStopPoint:
                await self.fetch_sobop_by_stop_point(geojson, 'обратное')
            self.downloaded_layers.append(geojson)
            self.add_layer_to_project(geojson, f'№{number}-{name}-{reg}-обратное', f'reverses-{self.company}', stop_points=reverse_points_sobop)


    async def fetchVariants(self, isStopPoint = False):
        self.downloaded_layers = []
        self.variant_pass_count = 0
        variants_count = 0
        percent = 0
        route_list = await self.get_data_from_outfit_plan(self.array_regs)
        
        if self.isSOBOP and isStopPoint == False:
            self.sobop_data = await self.get_workload_tkp(time=self.time, array_regs=self.array_regs)
        elif isStopPoint:
            self.getStopPoint = True

        for route in route_list:
            self.dialog.status_general_label.setText('Отрисовка геометрии. ..')
            for variant in route['variants']:
                variants_count += 1
                self.dialog.progress.setValue(percent)
                percent += int(100 / len(route['variants']))
                if percent >= len(route['variants']):
                    percent = 0
                await self.distillation(variant, route)
                
        self.dialog.status_general_label.setText(f'Загружено маршрутов: {len(route_list)}')               

        if not isStopPoint:
            self.get_result_variant_data(len(route_list), variants_count)
        else:
            self.get_result_info_stop_point_data(len(route_list), variants_count)

#######################################################################################################################################################


######### TRANSFORM VARIANTS TO ONE LAYER #########

    async def distilation_by_layer(self, geojson, variant, data_item):
        if len(variant['forward_points']['coord']) != 0:
            geojson = self.update_feature_layer_2(variant, geojson, 'forward_points', data_item)
            self.downloaded_layers.append(geojson)
        
        if len(variant['reverse_points']['coord']) != 0:
            geojson = self.update_feature_layer_2(variant, geojson, 'reverse_points', data_item)
            self.downloaded_layers.append(geojson)


    async def fetchLayerVariants(self):
        percent = 0
        variants_count = 0
        self.downloaded_layers = []
        route_list = await self.get_data_from_outfit_plan(self.array_regs)
        if self.isSOBOP:
            self.sobop_data = await self.get_type_payment(array_regs=self.array_regs)

        geojson = self.get_geojson()
        for route in route_list:
            self.dialog.status_general_label.setText('Отрисовка геометрии. ..')
            for variant in route['variants']:
                variants_count += 1
                self.dialog.progress.setValue(percent)
                percent += 100 / len(route['variants'])
                if percent >= len(route['variants']):
                    percent = 0
                await self.distilation_by_layer(geojson, variant, route)
        self.add_one_layer_to_project(geojson)
        self.dialog.status_general_label.setText(f'Загружено маршрутов: {len(route_list)}')
        
        self.get_result_layer_data(len(route_list), variants_count)

    async def fetchMunicRoutes(self):
        percent = 0
        variants_count = 0
        self.downloaded_layers = []
        route_list = await self.get_munic_data_from_outfit_plan()
        print(len(route_list))
        return 
        if self.isSOBOP:
            self.sobop_data = await self.get_type_payment(array_regs=self.array_regs)

        return
        geojson = self.get_geojson()
        for route in route_list:
            self.dialog.status_general_label.setText('Отрисовка геометрии. ..')
            for variant in route['variants']:
                variants_count += 1
                self.dialog.progress.setValue(percent)
                percent += 100 / len(route['variants'])
                if percent >= len(route['variants']):
                    percent = 0
                await self.distilation_by_layer(geojson, variant, route)
        self.add_one_layer_to_project(geojson)
        self.dialog.status_general_label.setText(f'Загружено маршрутов: {len(route_list)}')
        
        self.get_result_layer_data(len(route_list), variants_count)

#######################################################################################################################################################


######### START UI FUNCTIONS #########

    async def progress_bar(self, type=1):
        if type == 1:
            task = asyncio.create_task(self.fetchVariants())
        elif type == 2:
            task = asyncio.create_task(self.fetchLayerVariants())
        elif type == 4:
            task = asyncio.create_task(self.fetchMunicRoutes())
        else:
            task = asyncio.create_task(self.fetchVariants(isStopPoint=True))
        await task


#######################################################################################################################################################