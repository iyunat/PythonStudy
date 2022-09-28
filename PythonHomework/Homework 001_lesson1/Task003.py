# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

coordinate_X = int (input ("Введите координату Х: "))
coordinate_Y = int (input ("Введите координату Y: "))
print ("X =", coordinate_X, ",", "Y =", coordinate_Y)
if coordinate_X >0 and coordinate_Y >0:
    print ("Точка с координатами X =", coordinate_X, ";", "Y =", coordinate_Y, "лежит в первой четверти.")
elif coordinate_X <0 and coordinate_Y >0:
    print ("Точка с координатами X =", coordinate_X, ";", "Y =", coordinate_Y, "лежит во второй четверти.")
elif coordinate_X <0 and coordinate_Y <0:
    print ("Точка с координатами X =", coordinate_X, ";", "Y =", coordinate_Y, "лежит в третьей четверти.")
elif coordinate_X >0 and coordinate_Y <0:
    print ("Точка с координатами X =", coordinate_X, ";", "Y =", coordinate_Y, "лежит в четвертой четверти.")
else:
    print ("Ошибка, координаты точки (X,Y) не должны быть равны нулю!")