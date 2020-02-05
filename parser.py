import requests
import json
from parser_object import get_params_object
from menu_parser import menu


def get_element():
    mode = menu()
    dict_elements = {}
    object_count = 1  # Количество объектов (квартир)
    empty_page_count = 0
    page_number = 1  # Номер страницы каталога

    while empty_page_count <= 4 and page_number <= 3:
        settings = {'rent': {
            'url': f'https://anflat.ru/api/catalog/rent/apartments/?limit_delta=0&filter%5Bobject_type%5D=apartments&filter%5Blocality%5D=kazan&order=1&page={page_number}&lang=ru',
            'file_name': 'dict_rent_apartments.json'},
            'sale': {
                'url': f'https://anflat.ru/api/catalog/sale/apartments/?limit_delta=0^&filter^%^5Bobject_type^%^5D=apartments^&filter^%^5Blocality^%^5D=kazan^&order=1^&page={page_number}^&lang=ru',
                'file_name': 'dict_sale_apartments.json'}}
        url = settings[mode]['url']
        # print(url)                                             # Тест принт
        requests.packages.urllib3.disable_warnings()
        result = requests.get(url, verify=False).json()
        data = result['data']
        if data:
            empty_page_count = 0
            for element in data:
                detail_url = element['detail_url']
                # print(detail_url)                                             # Тест принт
                # print(mode)                                                   # Тест принт
                # print(page_number)                                           # Тест принт
                if detail_url in dict_elements:
                    print(f'Повтор ! ! !  {detail_url} ')
                else:
                    dict_elements = get_params_object(detail_url, dict_elements)
                    object_count += 1
            page_number += 1
        else:
            empty_page_count += 1
            print('Данных на странице нет !')
    print(f'len(dict_elements) -->  {len(dict_elements)}')

    record = input('Записать в файл:   yes   ,если нет:   no ')
    if record == 'yes':
        with open(f'{settings[mode]["file_name"]}', 'w') as f:
            json.dump({settings[mode]['file_name']: dict_elements}, f)

    return dict_elements


get_element()

