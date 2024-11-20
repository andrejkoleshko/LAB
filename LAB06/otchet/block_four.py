#вариант12.1. Найти наименьший нечетный элемент списка и вывести его на экран

L = [5, 9, 4, -2, 6, 3, -1]

min_odd = 0
for num in L:
    if num % 2 != 0:
        if min_odd == 0 or num < min_odd:
            min_odd = num
print(f"the list is: {L} (task №12.1)")
if min_odd != 0:
    print(f"the smallest odd number in the list is: {min_odd} (task №12.1)")
else:
    print("there are no odd numbers in the list (task №12.1)")

#вариант12.2. Даны массивы A и B одинакового размера 10. 
# Поменять местами их содержимое и вывести вначале элементы преобразованного массива A, 
# а затем — элементы преобразованного массива B

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Меняем местами содержимое массивов A и B
for i in range(len(A)):
    A[i], B[i] = B[i], A[i]

# Выводим элементы преобразованного массива A
print("\nThe elements of array A after the exchange: (task №12.2)")
for elem in A:
    print(elem,  end=" ")

# Выводим элементы преобразованного массива B
print("\nThe elements of array B after the exchange: (task №12.2)")
for elem in B:
    print(elem, end=" ")
    