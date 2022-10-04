#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: o [2, 3, 4, 5, 6] => [12, 15, 16]; o [2, 3, 5, 6] => [12, 15]

list_numers = [2, 3, 4, 5, 6]
new_list = []
for i in range ((len (list_numers) +1) //2):
    new_list.append (list_numers [i]* list_numers [len (list_numers)-1-i])

print (new_list)
