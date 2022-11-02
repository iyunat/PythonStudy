# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# 1) Вывод всего справочника
# 2) Добавление нового номера
# 3) Поиск по номеру
# 4) Удаление номера* (необязательно)

telephone_directory = {
    "Иванов С.В.": 4256,
    "Ушаков Н.Р.": 8523,
    "Звонорев Л.Э.": 5479
}

for key, value in telephone_directory.items():
    print (key, value)

print ()

# with open("telephone.txt","w") as data:
#     for key,value in telephone_directory.items():
#         data.write("{}:{}\n".format(key,value))
     

# telephone_directory["Петров К.Н."] = 6541
# for key, value in telephone_directory.items():
#     print (key, value)
    
# print ()

# поиск по номеру:

# def my_key(telephone_directory, value):
#     for k, v in telephone_directory.items():
#         if v == value:
#             return k

# print(my_key(telephone_directory, 4256))

# print()

# # удаление номера
# del telephone_directory ["Петров К.Н."]
# for key, value in telephone_directory.items():
#     print (key, value)
