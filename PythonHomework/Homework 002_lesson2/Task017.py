# Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит 
# от количества элементов в списке)  в одной строке одно число.

from random import randint

with open('file.txt', 'w') as data:
    data.write('0\n')
    data.write('1\n')
    data.write('3\n')
    data.write('5\n')
    data.write('7\n')
    
def numbers_rand(n):
    return [randint(-n/2, n) for i in range(-n, n + 1)]

def file_data(path):
    data = open(path, 'r')
    dlist = [int(line.strip()) for line in data]
    data.close()
    return dlist

def multiply_d (num, list_d):
    multi = 1
    for i in list_d:
        multi*= num[i]
    return multi

path = 'file.txt'
n = 7 
list_d = file_data (path)
num = numbers_rand(n)

print(num)
print(list_d)
print(multiply_d(num, list_d))