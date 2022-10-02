#Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.

num = int (input ("Введите положительное число "))
def sum_sequence (num):
    return [round((1+1/i)**i,2) for i in range (1, num+1)]

nums = sum_sequence (num)
print (nums)
print (f'Последовательность: {nums}\nСумма чисел последовательности: {round(sum(nums), 2)}')

