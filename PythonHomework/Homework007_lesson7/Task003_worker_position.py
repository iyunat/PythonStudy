# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
#  В классе Position реализовать публичные методы
# получения полного имени сотрудника (get_full_name) и 
# дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, 
# передать данные, # проверить значения атрибутов, вызвать методы экземпляров).
# П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
# __str__(self) - вызывается функциями str, print и format. 
#Возвращает строковое представление объекта.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self. _income = {"wage": wage, "bonus": bonus}



class Position (Worker):
    def get_full_name (self):
        print (f"Имя: {self.name}, фамилия: {self.surname}, должность: {self.position}")

    def get_total_income (self):
         return self._income["wage"] + self._income["bonus"]



p1 = Position ("Николай", "Бочкин", "юрист", 3000, 1000)

p1.get_full_name()
p1.get_total_income()
print (f"Доход с учетом премии у {p1.name} {p1.surname} составляет: {p1.get_total_income()}")