

def unpack_metro(object_detail_metro, list_params):
    metro_name = ''                      # Название станции метро
    distance = ''                          # Дистанция до метро
    distance_number = ''                          # Число дистанции
    object_detail_metro = object_detail_metro.strip()
    for element in object_detail_metro:
        if element.isalpha():
            metro_name += element
        else:
            break
    list_params.append({'metro_name': metro_name})

    try:
        distance = object_detail_metro[object_detail_metro.index('(') : object_detail_metro.index(')') + 1]
    except ValueError:
        distance = object_detail_metro
    list_params.append({'metro_distance': distance})

    for element in distance:
        if element.isdigit():
            distance_number += element
    list_params.append({'metro_distance_number': distance_number})
    return list_params

def unpack_total_area(total_area, list_params):
    total_area = total_area.strip()
    try:
        square_name, total_square, m = total_area.split(' ')
        list_params.append({'square_name': square_name})
        list_params.append({'total_square': total_square})
    except ValueError:
        square_name, a, total_square, m = total_area.split(' ')
        square_name = f'{square_name} {a}'
        list_params.append({'square_name': square_name})
        list_params.append({'total_square': total_square})
    return list_params

def unpack_living_area(living_area, list_params):
    living_area = living_area.strip()
    try:
        square_name, total_square, m = living_area.split(' ')
        list_params.append({'square_name': square_name})
        list_params.append({'living_square': total_square})
    except ValueError:
        square_name, a, total_square, m = living_area.split(' ')
        square_name = f'{square_name} {a}'
        list_params.append({'square_name': square_name})
        list_params.append({'living_square': total_square})
    return list_params

def unpack_floor_number(floor_number_html, list_params):
    floor_number_html = floor_number_html.strip()
    try:
        floor, floor_numbers = floor_number_html.split()
    except ValueError:
        for element in floor_number_html:
            if element.isdigit():
                index = floor_number_html.index(element)
                break
        floor = floor_number_html[:index]
        floor_numbers = floor_number_html[index:]
    finally:
        floor_number, floor_total = floor_numbers.split('/')  # floor_number - Номер этажа,  floor_tota - Этажей в доме
        list_params.append({'floor_number': floor_number})
        list_params.append({'floor_total': floor_total})
    return list_params

def unpack_room_count(room_count_html, list_params):
    room_count_html = room_count_html.strip()
    try:
        room, count_room = room_count_html.split()
    except ValueError:
        for element in room_count_html:
            if element.isdigit():
                index = room_count_html.index(element)
                break
        room = room_count_html[:index]
        count_room = room_count_html[index:]
    finally:
        list_params.append({'room': room})
        list_params.append({'count_room': count_room})
    return list_params

def unpack_material(material_html, list_params):
    material_html = material_html.strip()
    try:
        material, material_name = material_html.split()
    except ValueError:
        material_name = material_html
    list_params.append({'material': material_name})
    return list_params

def unpack_balcony(balcony_html, list_params):
    balcony_html = balcony_html.strip()
    balcony_type = balcony_html[:13]
    balcony_name = balcony_html[14:]
    list_params.append({'balcony_type': balcony_name})
    return list_params

def unpack_date_update(date_update, list_params):
    date_update = date_update.strip()
    if date_update:
        date, update, date_number = date_update.split()
        date_update = f'{date} {update}'
        year_public = date_number[:4]
        list_params.append({'year_public': year_public})
        month_public = date_number[4:6]
        list_params.append({'month_public': month_public})
        day_public = date_number[6:8]
        list_params.append({'day_public': day_public})
        time_public = date_number[8:]
        list_params.append({'time_public': time_public})
    return list_params

def unpack_id(id_html, list_params):
    id_html = id_html.strip()
    try:
        nom, name, id = id_html.split()
    except ValueError:
        try:
            nom_name, id = id_html.split()
        except ValueError:
            id_revers = ''
            id = ''
            for element in id_html[::-1]:
                if element.isdigit():
                    id_revers += element
                    if len(id_revers) >= 6:
                        break
            for element in id_revers[::-1]:
                id += element
    finally:
        list_params.append({'id': id})
    return list_params

def unpack_price(print_price_print, list_params):
    price_numer = ''
    price_text = ''
    for element in print_price_print:
        if element.isdigit():
            price_numer += element
        else:
            price_text += element
    price_numer = int(price_numer)
    type_text, currency = price_text.split()
    list_params.append({currency: price_numer})
    return list_params

def unpack_address_html(address_html, list_params):
    address_html = address_html.strip()
    try:
        street, house_number, city, area_city = address_html.split(',')
        list_params.append({'street': street})
        list_params.append({'house_number': house_number})
        list_params.append({'city': city})
        list_params.append({'area_city': area_city})
    except ValueError:
        list_params.append({'address': address_html})
    return list_params

def unpack_name_object_html(name_object_html, list_params):
    name_object_html = name_object_html.strip()
    try:
        coun_r_type_object, m, n = name_object_html.split(',')
        coun_r_type_object = coun_r_type_object.strip()
        z, type_object = coun_r_type_object.split()
    except ValueError:
        type_object = name_object_html
    list_params.append({'type_object': type_object})
    return list_params






