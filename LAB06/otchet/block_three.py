#вариант3. В строке удалить символ точку (.) и подсчитать количество удаленных символов

string = "Hello world. You're nice."
count = 0

for char in string:
    if char == ".":
        count += 1
        string = string.replace(".", "", count)
print(f"deleted {count} symbols (.)")
print(f"the changed string: {string}")
