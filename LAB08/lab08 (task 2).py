#вариант3, задание 1. Используя библиотеки requests и beautifulsoup4 произвести скрейпинг страниц сайта https://worldathletics.org.
#- Перейти в раздел https://worldathletics.org/records/toplists
#- Проанализировать закономерности изменения адресов страниц при смене года, пола спортсмена и дисциплины
#- Проанализировать код страницы (найти теги, отвечающие за представление информации о результате, имени спортсмена, стране и дате соревнования)
#Получить информацию о лучших результатах (топ-1) у мужчин и женщин в дисциплинах прыжок в высоту, прыжок с шестом, прыжок в длину, тройной прыжок за 2001-2024 годы. 
# Данные (год, имя спортсмена, страна, высота/длина, дата соревнования) сохранить в файле top_results.csv

import requests
from bs4 import BeautifulSoup
import csv

# Функция для получения html-кода страницы
def get_html(url):
    response = requests.get(url)
    response.raise_for_status()  # Проверка на наличие ошибок
    return response.text

# Функция для получения списка лучших результатов
def get_top_results(year, gender, event):
    base_url = f"https://worldathletics.org/records/toplists"
    url = f"{base_url}/jumps/{event}/all/{gender}/senior/{year}"
    
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    results = []
    
    # Находим таблицу с результатами
    table = soup.find(class_ ='records-table')
    if table:
        # Ищем все строки с результатами
        rows = table.find_all('tr')[1:]  # Пропускаем заголовок

        for row in rows:
            columns = row.find_all('td')
            if len(columns) > 4:  # Проверяем, что есть достаточное количество колонок
                # Извлекаем нужную информацию
                athlete_name = columns[1].get_text(strip=True)
                country = columns[2].get_text(strip=True)
                result = columns[3].get_text(strip=True)
                date = columns[4].get_text(strip=True)

                results.append({
                    'year': year,
                    'athlete_name': athlete_name,
                    'country': country,
                    'result': result,
                    'date': date
                })
    
    return results

# Список дисциплин и пола
events = ['high-jump', 'pole-vault', 'long-jump', 'triple-jump']
genders = ['men', 'women']
years = range(2001, 2025)

top_results = []

# Сбор данных
for event in events:
    for gender in genders:
        for year in years:
            results = get_top_results(year, gender, event)
            if results:
                top_results.append(results[0])  # Берем только топ-1

# Сохранение данных в файл

with open('top_results.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['year', 'athlete_name', 'country', 'result', 'date'])
    writer.writeheader()
    writer.writerows(top_results)

print("Данные успешно собраны и сохранены в top_results.csv")
