import requests
import math


def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000
    a_lon, a_lat = a
    b_lon, b_lat = b

    radians_latitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_latitude)

    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    distance = math.sqrt(dx ** 2 + dy ** 2)
    return distance


def get_coordinates(address, api_key="894783b2-7817-4c77-be1f-4f6d1f928161"):
    geocoder_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": api_key,
        "geocode": address,
        "format": "json"
    }
    response = requests.get(geocoder_url, params=params)
    if response.status_code == 200:
        geo_data = response.json()
        try:
            coords = geo_data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
            lon, lat = map(float, coords.split())
            return lon, lat
        except IndexError:
            print(f"Не удалось найти координаты для адреса: {address}")
            return None
    else:
        print(f"Ошибка при запросе геокодера для адреса: {address}")
        return None


def main():
    api_key = "894783b2-7817-4c77-be1f-4f6d1f928161"

    home_address = input("Введите адрес вашего дома: ")
    university_address = input("Введите адрес университета: ")

    home_coords = get_coordinates(home_address, api_key)
    university_coords = get_coordinates(university_address, api_key)

    if home_coords and university_coords:
        distance = lonlat_distance(home_coords, university_coords)
        print(f"Расстояние от дома до университета: {distance:.2f} метров")
    else:
        print("Не удалось вычислить расстояние.")


if __name__ == "__main__":
    main()