#3. Найти файл/файлы (указываем полное имя или часть имени) выводит в консоль список найденных файлов (путь к ним)

import os
print("\ntask №3")
def find_files(name, path):
    found_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if name in file:
                found_files.append(os.path.join(root, file))
    return found_files

name = input("Введите имя файла для поиска: ")
path = input("Введите путь для поиска файла: ")

found_files = find_files(name, path)

if found_files:
    for file in found_files:
        print(file)
else:
    print("Файлы не найдены")

#7. Переименовать файл/папку (указываем путь и новое имя) переименование файла / папки 

import os
print("\ntask №7")
# Указываем путь к файлу/папке и его/её новое имя
old_name = input("Введите текущее имя файла/папки: ")
new_name = input("Введите новое имя файла/папки: ")

# Переименовываем файл/папку
os.replace(old_name, new_name)

print("Файл/папка успешно переименован(-а)")

#9. Переместить файл/папку (указываем путь и новый путь) перемещение файла / папки 

import shutil
print("\ntask №9")
# Указываем путь к файлу/папке и его/её новый путь
old_place = input("Введите текущее расположение файла/папки: ")
new_place = input("Введите новое расположение файла/папки: ")

# Перемещаем файл/папку
shutil.move(old_place, new_place)

print("Файл/папка успешно перемещен(-а)")
