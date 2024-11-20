#вариант5.1. Даны две дроби A/B и C/D (А, В, С, D — натуральные числа). 
# Составить программу вычитания из первой дроби второй. Ответ должен быть несократимой дробью. 
# Использовать подпрограмму алгоритма Евклида для определения НОД

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def subtract_fractions(A, B, C, D):
    numerator = A * D - B * C
    denominator = B * D
    common_divisor = gcd(numerator, denominator)
    
    numerator //= common_divisor
    denominator //= common_divisor
    
    return numerator, denominator

# Пример использования
A = int(input("Enter A (task №5.1): "))
B = int(input("Enter B (task №5.1): "))
C = int(input("Enter C (task №5.1): "))
D = int(input("Enter D (task №5.1): "))

result_numerator, result_denominator = subtract_fractions(A, B, C, D)
print(f"the result of the subtraction: {result_numerator}/{result_denominator} (task №5.1)")
print("\n(task №5.2)")

#вариант5.2. Написать рекурсивную функцию для перевода числа из десятичной системы счисления в двоичную

def decToBin(n):
    if n > 1:
        decToBin(n // 2)
    print(n % 2, end='')

# Пример использования
decimal_num = int(input("Enter number:"))
decToBin(decimal_num)      