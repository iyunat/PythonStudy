#Напишите программу, которая принимает на вход число N и выдает набор 
# произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

nums = int (input ("Введите положительное число: "))
#nums = abs (int (nums))
print ("Вы ввели число =", nums)
multiply = 1
for i in range (1, nums+1):
    if nums > 0:
        multiply = multiply * i
        #i+=1
        print (multiply, end=' ')

if nums <= 0:    
    print ('Число должно быть больше нуля')

