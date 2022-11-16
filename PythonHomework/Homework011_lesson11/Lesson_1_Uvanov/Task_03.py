# import os
# import chardet

prog_1= ['attribute', 'класс', 'функция', 'type']



for i in prog_1:
    try:
        print(i,type(i),i.encode('ascii'), " - в байтовом типе")
        print()
    except UnicodeEncodeError:
        print(i,type(i),"- невозможно записать в байтовом типе с помощью маркировки b")
        print()