# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

coordinate_Xa = int (input ("Введите координату Х точки А: "))
coordinate_Ya = int (input ("Введите координату Y точки А: "))
coordinate_Xb = int (input ("Введите координату Х точки В: "))
coordinate_Yb = int (input ("Введите координату Y точки В: "))
print ("Координаты точки А:(X =", coordinate_Xa, ";", "Y =", coordinate_Ya, ")")
print ("Координаты точки B:(X =", coordinate_Xb, ";", "Y =", coordinate_Yb, ")")
distance = ((coordinate_Xb -coordinate_Xa)**2 +(coordinate_Yb - coordinate_Ya)**2)**0.5
print ("Расстояние между точками А и В =", distance)