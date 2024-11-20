#вариант4.1. Найти среднее арифметическое всех целых чисел от a до 200 
#(значения a и b вводятся с клавиатуры; a≤ 200). Решить задачу используя циклическую конструкцию for
a = int(input("Enter a:"))
b = int(input("Enter b:"))

sum = 0
if b < a:
    for element in range(b, a +1):
        sum += element
        average = sum/(a-b+1)
if a < b:
    for element in range(a, b +1):
        sum += element
        average = sum/(b-a+1)  

print(f"Sum of elements from = {sum} (task №4.1)")
print(f"The average of all elements = {average} (task №4.1)")

#вариант4.2. Дана последовательность из n вещественных чисел, 
# начинающаяся с положительного числа. 
# Определить, какое количество положительных чисел записано в начале последовательности. 
# Условный оператор не использовать. Решить задачу используя циклическую конструкцию while

subseqeunce = [1.5, 9.8, 4.6, -2.3, -3.15, 5.43]
n = len(subseqeunce)
count = 0
i = 0
while subseqeunce[i] > 0:
    count += 1
    i += 1
print(f"\nthe subsequence is {subseqeunce} (task №4.2)")
print(f"the number of elements in the subsequence is {n} (task №4.2)")
print(f"number of positive elements at the beginning of the subsequence is {count} (task №4.2)")   