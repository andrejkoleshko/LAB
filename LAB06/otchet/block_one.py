#вариант11. Дано три числа. Найти количество положительных чисел среди них

a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

count = 0

if a > 0:
    count += 1
if b > 0:
    count += 1
if c > 0:
    count += 1

print(f"Count of positive = {count}")