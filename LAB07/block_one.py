#вариант4.1. Создать словарь в котором хранятся семь пар ключ значение следующего типа: 
# Фильмы ( str ) и их сборы в 6 различных странах dict 
# - Вывести на экран список всех фильмов и их суммарные сборы 
# - Вывести на экран фильмы с максимальными и минимальными суммарными сборами. 
# - Вывести на экран фильмы превосходящие по суммарным сборам более чем на 25% от минимальный по сборам фильм. 
# - Выделить все фильмы, сборы которых в Китае меньше их сборов в Индии. 
# Полученный словарь сохранить в бинарный файл data.pickle c использованием модуля pickle. 
# Предусмотреть возможность чтения бинарного файла и сохранение его данных в объект словаря

import pickle

# Создание словаря с данными о фильмах и их сборах в странах
films = {
    "Film1": {"USA": 1000000, "UK": 500000, "China": 1000000, "India": 1500000, "Russia": 800000, "Brazil": 700000},
    "Film2": {"USA": 1500000, "UK": 700000, "China": 1800000, "India": 1200000, "Russia": 600000, "Brazil": 500000},
    "Film3": {"USA": 1200000, "UK": 800000, "China": 1600000, "India": 1800000, "Russia": 500000, "Brazil": 400000},
    "Film4": {"USA": 800000, "UK": 400000, "China": 1400000, "India": 900000, "Russia": 400000, "Brazil": 300000},
    "Film5": {"USA": 1100000, "UK": 600000, "China": 1700000, "India": 1300000, "Russia": 700000, "Brazil": 600000},
    "Film6": {"USA": 1300000, "UK": 900000, "China": 1900000, "India": 2100000, "Russia": 900000, "Brazil": 800000},
    "Film7": {"USA": 1400000, "UK": 1000000, "China": 2100000, "India": 1600000, "Russia": 1000000, "Brazil": 900000}
}

# Сохранение словаря в бинарный файл с помощью pickle
with open("data.pickle", "wb") as file:
    pickle.dump(films, file)

# Чтение данных из бинарного файла и сохранение их в объект словаря
with open("data.pickle", "rb") as file:
    films = pickle.load(file)

# Вывод списка всех фильмов и их суммарных сборов
total_revenue = {}
print("Total receipts for films: (task №4.1)")
for film, countries in films.items():
    total = sum(countries.values())
    total_revenue[film] = total
    print(f"{film}: {total}")

# Вывод фильмов с максимальными и минимальными суммарными сборами
max_revenue = max(total_revenue, key=total_revenue.get)
min_revenue = min(total_revenue, key=total_revenue.get)
print(f"\nFilm with maximum fees: {max_revenue} (task №4.1)")
print(f"Film with minimum fees: {min_revenue} (task №4.1)")

# Вывод фильмов, превосходящих по суммарным сборам более чем на 25% от минимального по сборам фильма
threshold = total_revenue[min_revenue] * 1.25
print("\nfilms that exceed the total fees by more than 25% of the minimum film fees: (task №4.1)")
for film, revenue in total_revenue.items():
    if revenue > threshold and film != min_revenue:
        print(film)

# Выделение всех фильмов, сборы которых в Китае меньше их сборов в Индии
print("\nFilms, fees in China are less than fees in India: (task №4.1)")
for film, countries in films.items():
    if countries["China"] < countries["India"]:
        print(film)

#вариант4.2. В каждой строке текстового файла (input.txt) перевести все слова в верхний регистр. 
# Записать результат выполнения в другой текстовый файл (output.txt)
print ("\n(task №4.2)")
with open('input.txt', 'r') as file:
    with open('output.txt', 'w') as output_file:
        for line in file:
            output_file.write(line.upper())
           