import requests


def find_district_yandex(address):
    api_key = "894783b2-7817-4c77-be1f-4f6d1f928161"

    geocoder_url = "https://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": api_key,
        "geocode": address,
        "format": "json",
        "kind": "district"
    }
    response = requests.get(geocoder_url, params=geocoder_params)
    if response.status_code == 200:
        geo_data = response.json()
        try:
            district = geo_data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["text"]
            print(f"Район: {district}")
        except IndexError:
            print("Район не найден.")
    else:
        print("Ошибка при запросе геокодера.")


address = input("Введите адрес: ")
find_district_yandex(address)