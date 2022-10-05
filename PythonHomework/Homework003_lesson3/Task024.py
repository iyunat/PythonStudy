# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: o [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_nums = [1.1, 1.2, 3.1, 5, 10.01]
print ("Список ", list_nums)
modul_list = []

for i in list_nums:
    modul = round(i%1,2)
    modul_list.append(modul)
print (modul_list)

max= modul_list[0]
for i in modul_list:
    if max < i:
        max=i
print (f"Максимальное значение дробной части равно {max}")

min=modul_list[0]
for i in modul_list:
    if min > i:
        min=i
print (f"Минимальное значение дробной части равно {min}")
difference = max - min
print (f"Разница между максимальным и минимальным значением дробной части элементов равна", difference)