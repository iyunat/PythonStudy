# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k и приравняйте его к нулю.
#Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
max_val=100
k = 2
# коэфф. при старшей степени не должен быть равен 0
koeff=[randint(0,max_val) for i in range(k)]+[randint(1,max_val)]
poly='+'.join([f'{(j,"")[j==1]}x**{i}' for i, j in enumerate(koeff) if j][::-1])
# Поиск и замены:
poly=poly.replace('x**1+', 'x+')
poly=poly.replace('x**0', '')
poly+=('','1')[poly[-1]=='+']
poly=(poly, poly[:-2])[poly[-2:]=='**1']
print(poly,'=', 0)

with open('file_033.txt', 'w') as data:
    data.write(poly + '= 0')