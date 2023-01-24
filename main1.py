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

def get_cities(country_dict):
    # Создаем словарь для городов
    city_dict = {}
    # Перебираем страны и запрашиваем города
    for code, name in country_dict.items():
        url = f"https://restcountries.com/v2/alpha/{code}?fields=capital"
        response = requests.get(url)
        if response.status_code == 200:
            city = response.json()["capital"]
            city_dict.setdefault(name, []).append(city)
        else:
            print("Error:", response.status_code)
    # Возвращаем словарь городов
    return city_dict

country_dict = get_countries()
if country_dict:
    print_country_names(country_dict)
    city_dict = get_cities(country_dict)
    print(city_dict)



# В этом коде добавлена функция get_cities(country_dict), 
# которая принимает словарь стран и возвращает словарь городов. 
# Функция перебирает страны из словаря и для каждой страны отправляет 
# GET-запрос к API с запросом на получение информации о столице. 
# Если ответ со статусом 200 (OK), то из ответа извлекается название столицы и 
# добавляется в словарь городов с соответствующим ключом - названием страны.

# В конце кода вызывается функция get_cities(country_dict), 
# которая принимает словарь стран и возвращает словарь городов. 
# После этого словарь городов выводится на экран.

# Обратите внимание, что в этом коде не реализована обработка ошибок и проверка наличия столицы у страны. 
# Это может привести к ошибкам в работе кода и необходимо их учесть при разработке.
