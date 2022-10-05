# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: o 45 -> 101101  o 3 -> 11 o 2 -> 10

def decimal_binary (decimal_nums):
    binary_nums= 0
    multiply = 1

    while decimal_nums != 0:
        binary_nums = binary_nums + decimal_nums % 2 * multiply
        decimal_nums //=2
        multiply *=10
    return binary_nums

print (decimal_binary (45))
print (decimal_binary (3))
print (decimal_binary (2))