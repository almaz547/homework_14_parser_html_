

def menu():
    mode = 5
    while mode != '1' and mode != '2':
        mode = input('Аренда -   1   ,или  Продажи -   2  ')
    if mode == '1':
        mode = 'rent'
    if mode == '2':
        mode = 'sale'
    return mode

# def get_url(mode, page_number):
#     if mode == '1':
#         url = f'https://anflat.ru/api/catalog/rent/apartments/?limit_delta=0&filter%5Bobject_type%5D=apartments&filter%5Blocality%5D=kazan&order=1&page={page_number}&lang=ru'
#     else:
#         url = f'https://anflat.ru/api/catalog/sale/apartments/?limit_delta=0^&filter^%^5Bobject_type^%^5D=apartments^&filter^%^5Blocality^%^5D=kazan^&order=1^&page={page_number}^&lang=ru'
#     return url

# settings = {'rent': {'url': f'https://anflat.ru/api/catalog/rent/apartments/?limit_delta=0&filter%5Bobject_type%5D=apartments&filter%5Blocality%5D=kazan&order=1&page={page_number}&lang=ru',
#                      'file_name': 'dict_rent_apartments.json'},
#             'sale': {'url': f'https://anflat.ru/api/catalog/sale/apartments/?limit_delta=0^&filter^%^5Bobject_type^%^5D=apartments^&filter^%^5Blocality^%^5D=kazan^&order=1^&page={page_number}^&lang=ru',
#                      'file_name': 'dict_sale_apartments.json'}}