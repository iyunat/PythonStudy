# Задание 2.

# Каждое из слов «class», «function», «method» записать в байтовом формате
# без преобразования в последовательность кодов
# не используя!!! методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.

# Подсказки:
# --- b'class' - используйте маркировку b''
# --- используйте списки и циклы, не дублируйте функции

prog_1= [b'class', b'function', b'method']

for i in prog_1:
    
    print ('Tип переменной:{}'.format(type(i)))
    print('Cодержание переменной:{}'.format(i))
    print('Длина переменной: {}'.format (len(i)))
    print()

