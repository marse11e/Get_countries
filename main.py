import requests

def get_countries():
    # API endpoint для получения списка стран
    url = "https://restcountries.com/v2/all"

    # Отправляем GET-запрос и получаем ответ
    response = requests.get(url)

    # Проверяем статус ответа
    if response.status_code == 200:
        # Парсим ответ в JSON
        countries = response.json()
        # Создаем словарь для стран
        country_dict = {}
        # Перебираем страны и добавляем их в словарь
        for country in countries:
            country_dict[country["alpha3Code"]] = country["name"]
        # Возвращаем словарь стран
        return country_dict
    else:
        # Если статус ответа не 200, возвращаем None
        print("Error:", response.status_code)
        return None

def print_country_names(country_dict):
    # Перебираем страны и выводим их названия
    for code, name in country_dict.items():
        print(f"{code}: {name}")

country_dict = get_countries()
if country_dict:
    print_country_names(country_dict)


# В этом коде функция get_countries() использует библиотеку requests для отправки GET-запроса к API списка стран. 
# Затем она парсит ответ в формате JSON и создает словарь стран, 
# где ключом является код страны, а значением ее название.
# После этого функция возвращает сложенный словарь стран. Если статус ответа не 200 (OK), 
# то функция возвращает None. Функция print_country_names(country_dict) 
# перебирает страны из словаря и выводит их код и название. 
# В конце код вызывает функцию get_countries() и если полученный словарь стран не None, 
# то вызывает функцию print_country_names(country_dict).
