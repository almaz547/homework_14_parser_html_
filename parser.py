import requests
import json
from parser_object import get_params_object
from menu_parser import menu, get_url





def get_element():
    mode = menu()
    dict_elements = {}
    x = 1  # Количество объектов (квартир)
    z = 0
    i = 1  # Номер страницы каталога

    while z <= 4:
        url = get_url(mode, i)
        i += 1
        requests.packages.urllib3.disable_warnings()
        result = requests.get(url, verify=False).json()
        data = result['data']
        if data:
            z = 0
            for element in data:
                detail_url = element['detail_url']
                # print(detail_url)                                             # Тест принт
                if detail_url in dict_elements:
                    print(f'Повтор ! ! !  {detail_url} ')
                else:
                    dict_elements = get_params_object(detail_url, dict_elements)
                    x += 1
        else:
            z += 1
            print('Данных на странице нет !')
    print(f'len(dict_elements) -->  {len(dict_elements)}')

    record = input('Записать в файл:   yes   ,если нет:   no ')
    if record == 'yes':
        if mode == '1':
            with open('dict_rent_apartments.json', 'w') as rent:
                json.dump({'dict_rent_apartments': dict_elements}, rent)
        else:
            with open('dict_sale_apartments.json', 'w') as sale:
                json.dump({'dict_sale_apartments': dict_elements}, sale)
    return dict_elements


get_element()
