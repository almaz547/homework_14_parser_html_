

def menu():
    mode = 5
    while mode != '1' and mode != '2':
        mode = input('Аренда -   1   ,или  Продажи -   2  ')
    return mode

def get_url(mode, i):
    if mode == '1':
        url = f'https://anflat.ru/api/catalog/rent/apartments/?limit_delta=0&filter%5Bobject_type%5D=apartments&filter%5Blocality%5D=kazan&order=1&page={i}&lang=ru'
    else:
        url = f'https://anflat.ru/api/catalog/sale/apartments/?limit_delta=0^&filter^%^5Bobject_type^%^5D=apartments^&filter^%^5Blocality^%^5D=kazan^&order=1^&page={i}^&lang=ru'
    return url

