#вариант3, задание 1. Используя библиотеку requests и сторонний API получить данные о странах, 
# говорящих на испанском, португальском и немецком языках с площадью более 100000 квадратных киллометров. 
# (справка для получения адреса api https://restcountries.com/#endpoints-language) 
# -Сохранить данные об именах стран, столицах, площади и численности населения в файл results.json (https://restcountries.com/#endpoints-filter-response для справки). 
# -Для каждого из языков вывести в консоль страну с наибольшей площадью. 
# -.png флаги каждой из 3 стран сохранить отдельными файлами

import requests
import json

# Базовый URL для API
base_url = "https://restcountries.com/v3.1"

# Языки и критерий площади
languages = ["spanish", "portuguese", "german"]
min_area = 100000

# Результаты для сохранения в файл
results = []

# Функция для сохранения флагов
def save_flag(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

# Для хранения стран с наибольшей площадью для каждого языка
largest_countries = {}

# Обработка для каждого языка
for language in languages:
    response = requests.get(f"{base_url}/lang/{language}")
    if response.status_code == 200:
        countries = response.json()

        # Вывод количества стран по каждому языку
        print(f"Для языка {language.capitalize()} количество стран: {len(countries)}")
        
        # Фильтрация стран по площади
        filtered_countries = [
            {
                "name": country["name"]["common"],
                "capital": country.get("capital", ["No capital"])[0],
                "area": country["area"],
                "population": country["population"],
                "flag": country["flags"]["png"]
            }
            for country in countries if country["area"] > min_area
        ]

        # Добавление в общий список результатов
        results.extend(filtered_countries)

        # Поиск страны с наибольшей площадью для текущего языка
        if filtered_countries:
            largest_country = max(filtered_countries, key=lambda x: x["area"])
            largest_countries[language] = largest_country

            # Сохранение флага страны с наибольшей площадью
            save_flag(largest_country["flag"], f"{language}_largest_flag.png")

# Сохранение результатов в файл results.json
with open("results.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4, ensure_ascii=False)

# Вывод стран с наибольшей площадью для каждого языка
for language, country in largest_countries.items():
    print(f"Для языка {language.capitalize()} страна с наибольшей площадью: {country['name']} ({country['area']} км²)")
