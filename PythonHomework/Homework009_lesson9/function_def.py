# Функция №1:
 
list_1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
print(f"список: {list_1}")
lst_2 = input("Введите искомый элемент: ")

def che_list(list_1, lst_2):
    count = 0
    for i in range(len(list_1)):
        if list_1[i] == lst_2:
            count += 1
            if count == 2:
                return i
    else:
        return -1

# Функция №2:

# def input_n(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите количество конфет в диапазоне от 1 до 28: "))
#     return x

# Функция №3:

# def decimal_binary (decimal_nums):
#     binary_nums= 0
#     multiply = 1

#     while decimal_nums != 0:
#         binary_nums = binary_nums + decimal_nums % 2 * multiply
#         decimal_nums //=2
#         multiply *=10
#     return binary_nums

# Функция №4:

# def interSection(arr1, arr2): 
#    out = list(filter(lambda it: it in arr1, arr2))
#    return out