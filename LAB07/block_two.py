#вариант11.1. Прочитать и проанализировать содержимое файла 11.сsv. 
# Вывести его содержимое в консоль в формате Ключ → Значение. 
# Написать функции для вычисления минимального/максимального значения по некоторому столбцу, 
# суммы или количества (зависит от данных) подходящих значений по подходящему столбцу, 
# среднего значения по подходящему столбцу

import csv
print("task №11.1")
def read_csv_file(file):
    data = []
    with open("11.csv", 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    
    return data

def print_data(data):
    for row in data:
        for key, value in row.items():
            print(f"{key} → {value}")
        print()

def find_min(data, column_name):
    values = [float(row[column_name]) for row in data]
    return min(values)

def find_max(data, column_name):
    values = [float(row[column_name]) for row in data]
    return max(values)

def find_sum(data, column_name):
    values = [float(row[column_name]) for row in data]
    return sum(values)

def find_avg(data, column_name):
    values = [float(row[column_name]) for row in data]
    return sum(values) / len(values)


data = read_csv_file("11.csv")

print_data(data)

#вариант11.2. Прочитать и проанализировать содержимое файла lab.json. 
# Содержимое передать в словарь python. 
# Написать функцию для поиска пользователей по языку и передачи отфильтрованных данных в файл out.json

print("\n(task №11.2)")
import json

def read_json(file):
    with open('lab.json', 'r') as file:
        data = json.load(file)
    return data

def write_json(data, file):
    with open('out.json', 'w') as file:
        json.dump(data, file, indent=4)

def find_users_by_language(data, language):
    filtered_data = [user for user in data if user.get("language") == language]
    return filtered_data

data = read_json("lab.json")
language = "Uyghur"
filtered_data = find_users_by_language(data, language)
write_json(filtered_data, "out.json")
