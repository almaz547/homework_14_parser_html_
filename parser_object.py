import requests
from bs4 import BeautifulSoup
from function_unpack_object import *


domain = 'https://anflat.ru'
def get_params_object(detail_url, dict_elements):
    url_element = f'{domain}{detail_url}'
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url_element, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    list_params = []
    # print(f'{detail_url}--> list_params = [] -->  {list_params}')      # Тест принт


    try:
        object_detail_metro = soup.find('div', class_='object-detail__metro').text
    except AttributeError:
        pass
    else:
        list_params = unpack_metro(object_detail_metro, list_params)
    # print(f'{detail_url}--> list_params = unpack_metro() -->  {list_params}')     # Тест принт


    try:
        total_area = soup.find('li', class_="total_area").text
    except AttributeError:
        pass
    else:
        list_params = unpack_total_area(total_area, list_params)
    try:
        living_area = soup.find('li', class_="living_area").text
    except AttributeError:
        pass
    else:
        list_params = unpack_living_area(living_area, list_params)
    # print(f'{detail_url}--> list_params = unpack_total_area() -->  {list_params}')     # Тест принт


    try:
        floor_number_html = soup.find('li', class_="floor_number").text
    except AttributeError:
        pass
    else:
        list_params = unpack_floor_number(floor_number_html, list_params)
    # print(f'{detail_url}--> list_params = unpack_floor_number() -->  {list_params}')   # Тест принт


    room_count_html = soup.find('li', class_="room_count").text
    list_params = unpack_room_count(room_count_html, list_params)
    # print(f'{detail_url}--> list_params = unpack_room_count() -->  {list_params}')   # Тест принт


    try:
        material_html = soup.find('li', class_="material").text
    except AttributeError:
        pass
    else:
        list_params = unpack_material(material_html, list_params)
    try:
        material_html = soup.find('li', class_="wall_material").text
    except AttributeError:
        pass
    else:
        list_params = unpack_material(material_html, list_params)
    # print(f'{detail_url}--> list_params = unpack_material() -->  {list_params}')    # Тест принт


    try:
        balcony_html = soup.find('li', class_="balcony").text
    except AttributeError:
        pass
    else:
        list_params = unpack_balcony(balcony_html, list_params)
    # print(f'{detail_url}--> list_params = unpack_balcony() -->  {list_params}')   # Тест принт


    try:
        is_home_appliances = soup.find('li', class_="is_home_appliances").text
    except AttributeError:
        pass
    else:
        list_params.append({'is_home_appliances': is_home_appliances})
    # print(f'{detail_url}--> "is_home_appliances": is_home_appliances" -->  {list_params}')   # Тест принт


    try:
        is_furniture = soup.find('li', class_="is_furniture").text
    except AttributeError:
        pass
    else:
        list_params.append({'is_furniture': is_furniture})
    try:
        is_single = soup.find('li', class_="single").text
    except AttributeError:
        pass
    else:
        list_params.append({'is_single': is_single})
    # print(f'{detail_url}--> list_params = "is_furniture": is_furniture -->  {list_params}')   # Тест принт


    try:
        date_update = soup.find('li', class_="date_update").text
    except AttributeError:
        pass
    else:
        list_params = unpack_date_update(date_update, list_params)
    # print(f'{detail_url}--> list_params = unpack_date_update() -->  {list_params}')  # Тест принт


    id_html = soup.find('li', class_="id").text
    list_params = unpack_id(id_html, list_params)
    # print(f'{detail_url}--> list_object = unpack_id() -->  {list_params}')    # Тест принт


    print_price_print = soup.find('div', class_="print-price print").text
    list_params = unpack_price(print_price_print, list_params)
    # print(f'{detail_url}--> list_params = unpack_price() -->  {list_params}')   # Тест принт


    address_html = soup.find('div', class_="address").text
    list_params = unpack_address_html(address_html, list_params)
    # print(f'{detail_url}--> list_params = unpack_address_html() -->  {list_params}')    # Тест принт


    name_object_html = soup.find('h1', class_="name").text
    list_params = unpack_name_object_html(name_object_html, list_params)
    # print(f'{detail_url}--> list_params = unpack_name_object_html() -->  {list_params}')    # Тест принт



    dict_elements[detail_url] = list_params
    # print(f'dict_elements -->  {dict_elements}')                          #  Тест принт
    # print(f'len(dict_elements) -->  {len(dict_elements)}')                #  Тест принт

    return dict_elements


