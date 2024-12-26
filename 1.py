import requests

def show_stadiums_map():
    # Определяем местоположения стадионов
    stadiums_location = {
        "Лужники": "37.554191,55.715551",
        "Спартак": "37.440262,55.818015",
        "Динамо": "37.559809,55.791540"
    }

    # Формируем метки для карты
    markers = "~".join([f"{coords},pm2rdm" for coords in stadiums_location.values()])

    # Создаем URL для запроса
    map_url = "https://static-maps.yandex.ru/1.x/"
    params = {
        "l": "map",
        "size": "600,400",
        "pt": markers
    }

    # Отправляем запрос
    response = requests.get(map_url, params=params)

    # Обрабатываем ответ
    if response.status_code == 200:
        with open("stadiums_map.html", "w") as file:
            html_content = f"""
            <html>
                <body>
                    <h3>Карта с метками стадионов</h3>
                    <img src="{response.url}" alt="Карта с метками">
                </body>
            </html>
            """
            file.write(html_content)
        print("Карта сохранена в файле 'stadiums_map.html'")
    else:
        print("Ошибка при загрузке карты.")

# Вызов функции
show_stadiums_map()
