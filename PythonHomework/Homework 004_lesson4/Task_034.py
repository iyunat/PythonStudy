# Даны два файла, в каждом из которых находится запись многочлена, 
# приравненного к нулю. Задача - сформировать файл, 
# содержащий сумму многочленов (суммируем подобные слагаемые).

with open('file_034.txt', 'w', encoding='utf-8') as file:
    file.write('2*x**2 + 4*x + 5 = 0')

with open('file2_034.txt', 'w', encoding='utf-8') as file:
    file.write('4*x**2 + 7*x + 9 = 0')

with open('file_034.txt','r') as file:
    str_1 = file.readline()
    list_1 = str_1.split()


with open('file2_034.txt','r') as file:
    str_2 = file.readline()
    list_2 = str_2.split()

print(f'{list_1} + {list_2}')
sum_poly = list_1 + list_2

with open('summa.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_1} + {list_2}')