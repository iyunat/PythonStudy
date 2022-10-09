# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.

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


print(f"ответ: {che_list(list_1, lst_2)}")