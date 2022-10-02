# Реализуйте алгоритм перемешивания списка

import random

list_1 = [3, 5, 9, 1, 45, 17]
list_2 = list_1.copy ()
random.shuffle (list_2)

print ("Первоначальный список: ", list_1 )
print ("Измененный список: ", list_2 )