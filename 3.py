import requests


def save_satellite_image(coords, zoom=16, filename="satellite_image.png"):
    base_url = "https://static-maps.yandex.ru/1.x/"
    params = {
        "ll": f"{coords[1]},{coords[0]}",
        "z": zoom,
        "l": "sat",
        "size": "600,400"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Снимок сохранён в файл {filename}")
    else:
        print(f"Не удалось получить снимок: {response.status_code}")
        print("Ответ сервера:", response.text)

if __name__ == "__main__":
    try:
        lat = float(input("Введите широту объекта: "))
        lon = float(input("Введите долготу объекта: "))
        save_satellite_image([lat, lon])
    except ValueError:
        print("Ошибка ввода! Введите координаты в виде десятичных чисел.")


# Пример использования
# save_satellite_image([55.7558, 37.6173])