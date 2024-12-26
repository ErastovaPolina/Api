import random
import requests
from PIL import Image
from io import BytesIO

cities = [
    {"name": "Москва", "coords": [55.7558, 37.6173]},
    {"name": "Париж", "coords": [48.8566, 2.3522]},
    {"name": "Нью-Йорк", "coords": [40.7128, -74.0060]},
    {"name": "Токио", "coords": [35.6895, 139.6917]}
]


def get_city_map_yandex(city, zoom, map_type, api_key="894783b2-7817-4c77-be1f-4f6d1f928161"):
    base_url = "https://static-maps.yandex.ru/1.x/"
    params = {
        "ll": f"{city['coords'][1]},{city['coords'][0]}",
        "z": zoom,
        "size": "600,400",
        "l": map_type
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.content
    else:
        print("Не удалось загрузить карту.")
        return None


city = random.choice(cities)
zoom = random.randint(13, 15)
map_type = random.choice(["sat", "map"])

image_data = get_city_map_yandex(city, zoom, map_type)
if image_data:
    image = Image.open(BytesIO(image_data))
    image.show()
else:
    print("Ошибка при получении изображения.")