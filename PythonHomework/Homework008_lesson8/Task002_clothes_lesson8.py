#Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Единственный класс этого проекта — одежда (класс Clothes).
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: 
# для пальто (v/6.5 + 0.5), # для костюма (2*h + 0.3). 
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать
# абстрактный класс для единственного класса проекта,
# проверить на практике работу декоратора @property
# Пример:
# Расход ткани на пальто = 1.27
# Расход ткани на костюм = 20.30
# Общий расход ткани = 21.57
# Два класса: абстрактный и Clothes


from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, param):
        self.param = param


    @abstractmethod
    def manufactured_product(self):
        pass
 
    @property
    def total_fabric_consumption(self):
        total = c.fabric_consumption_coat + s.fabric_consumption_suit
        return total

    

class Coat (Clothes):
    def manufactured_product(self):
        print ("Пальто сшито")
    
    @property
    def fabric_consumption_coat(self):
        return self.param // 6.5 + 0.5

   
class Suit (Clothes):
    def manufactured_product(self):
        print ("Костюм сшит")
    
    @property
    def fabric_consumption_suit(self):
        return self.param * 2 + 0.3


c = Coat (44) 
s = Suit (155)
c.manufactured_product()
s.manufactured_product()
print(f"Расход ткани на пальто {c.fabric_consumption_coat}")
print(f"Расход ткани на костюм {s.fabric_consumption_suit}")
print(f"Общий расход ткани {c.total_fabric_consumption}")
print(f"Общий расход ткани {s.total_fabric_consumption}")