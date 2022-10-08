# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#70 = 2*5*7 => [2, 5, 7], 140 = 2*2*5*7 => [2, 2, 5, 7]

numers = int(input("Введите натуральное число: "))
i = 2 # первое простое число
multiplier = []
new = numers
while i <= numers:
    if numers % i == 0:
        multiplier.append(i)
        numers //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {new}: {multiplier}")