# не работает
import requests


def find_nearest_pharmacy_yandex(address):
    api_key = "894783b2-7817-4c77-be1f-4f6d1f928161"  # Вставьте ваш API-ключ

    # Определяем координаты адреса через геокодер
    geocoder_url = "https://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": api_key,
        "geocode": address,
        "format": "json"
    }
    response = requests.get(geocoder_url, params=geocoder_params)

    if response.status_code == 200:
        geo_data = response.json()
        try:
            coords = geo_data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
            lon, lat = map(float, coords.split())
        except IndexError:
            print("Адрес не найден.")
            return
    else:
        print("Ошибка при запросе геокодера.")
        return

    # Ищем ближайшую аптеку
    search_url = "https://search-maps.yandex.ru/v1/"
    search_params = {
        "apikey": api_key,
        "text": "аптека",
        "lang": "ru_RU",
        "ll": f"{lon},{lat}",
        "type": "biz",
        "results": 1
    }
    search_response = requests.get(search_url, params=search_params)

    if search_response.status_code == 200:
        search_data = search_response.json()
        try:
            pharmacy = search_data["features"][0]
            name = pharmacy["properties"]["name"]
            address = pharmacy["properties"]["CompanyMetaData"]["address"]
            print(f"Ближайшая аптека: {name}, адрес: {address}")
        except (IndexError, KeyError):
            print("Аптеки поблизости не найдены.")
    else:
        print(f"Ошибка при поиске аптеки. Код ответа: {search_response.status_code}")
        print("Ответ сервера:", search_response.text)

# Ввод адреса
address = input("Введите адрес: ")
find_nearest_pharmacy_yandex(address)