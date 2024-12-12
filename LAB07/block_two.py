#вариант11.1. Прочитать и проанализировать содержимое файла 11.сsv. 
# Вывести его содержимое в консоль в формате Ключ → Значение. 
# Написать функции для вычисления минимального/максимального значения по некоторому столбцу, 
# суммы или количества (зависит от данных) подходящих значений по подходящему столбцу, 
# среднего значения по подходящему столбцу

import csv
print("task №11.1")
# открывает CSV файл и читает данные из него, затем возвращает список словарей данных
def read_csv_file(file):
    data = []
    with open("11.csv", 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    
    return data
# выводит данные из списка словарей в удобочитаемом формате
def print_data(data):
    for row in data:
        for key, value in row.items():
            print(f"{key} → {value}")
        print()
# находит минимальное значение в указанной колонке
def find_min(data, column_name):
    values = [float(row[column_name]) for row in data]
    return min(values)
# находит максимальное значение в указанной колонке
def find_max(data, column_name):
    values = [float(row[column_name]) for row in data]
    return max(values)
# считает сумму значений в указанной колонке
def find_sum(data, column_name):
    values = [float(row[column_name]) for row in data]
    return sum(values)
# вычисляет среднее значение в указанной колонке
def find_avg(data, column_name):
    values = [float(row[column_name]) for row in data]
    return sum(values) / len(values)

# чтение данных из файла
data = read_csv_file("11.csv")

print_data(data)

#вариант11.2. Прочитать и проанализировать содержимое файла lab.json. 
# Содержимое передать в словарь python. 
# Написать функцию для поиска пользователей по языку и передачи отфильтрованных данных в файл out.json

print("\n(task №11.2)")
import json
# Функция для чтения данных из JSON файла
def read_json(file):
    with open('lab.json', 'r') as file:
        data = json.load(file)
    return data
# Функция для записи данных в JSON файл
def write_json(data, file):
    with open('out.json', 'w') as file:
        json.dump(data, file, indent=4)
# Функция для нахождения пользователей с определенным языком
def find_users_by_language(data, language):
# Фильтруем данные и находим пользователей с определенным языком
    filtered_data = [user for user in data if user.get("language") == language]
    return filtered_data

data = read_json("lab.json")
language = "Uyghur"
filtered_data = find_users_by_language(data, language)
write_json(filtered_data, "out.json")
