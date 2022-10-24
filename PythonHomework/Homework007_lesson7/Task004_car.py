#Реализуйте базовый класс Car. У данного класса должны быть следующие 
# публичные атрибуты: speed, color, name, is_police (булево).
# А также публичные методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).

# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

# Добавьте в базовый класс публичный метод show_speed,
# который должен показывать текущую скорость автомобиля.

# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, color, max_speed, is_police):
        self.name = name
        self.color = color
        self.max_speed = max_speed
        self.is_police = is_police
        print (f"Поздравляем, с конвеера вышла новая машина {self.name} {self.color} цвета с максимальной скоростью {self.max_speed} км/ч!")

    def go (self):
        print (f"Машина {self.name} поехала!")
    
    def stop (self):
        print (f"Машина {self.name} остановилась!")

    def stop (self):
        print (f"Машина {self.name} остановилась!")

    def turn(self, direction):
        print (f"Машина {self.name} повернула {direction}!")

    def show_speed (self, speed):
        self.speed = speed
        print (f"Текущая скорость машины {self.name} составляет: {self.speed} км/ч")


class TownCar (Car):
    def __init__(self, name, color, max_speed, is_police, car_price):
        super().__init__(name, color, max_speed, is_police)

        self.car_price = car_price
        print (f"Стоимость новой городской машины {self.name} {self.color} цвета  составляет {self.car_price} рублей!")

    def show_speed (self, speed):
        self.speed = speed
        self.permissible_speed = 60
        print (f"Текущая скорость {self.speed} км/ч автомобиля {self.name}")
        if self.speed > self.permissible_speed:
            print(f"Внимание, скорость автомобиля {self.name} превышена!")
    


class SportCar (Car):
    def __init__(self, name, color, max_speed, is_police, country_origin):
        super().__init__(name, color, max_speed, is_police)

        self.country_origin = country_origin
        print (f"Страна-производитель машины {self.name} {self.color} цвета - {self.country_origin}!")

class WorkCar (Car):
    def show_speed (self, speed):
        self.speed = speed
        self.permissible_speed = 40
        print (f"Текущая скорость  автомобиля {self.name} {self.speed} км/ч")
        if self.speed > self.permissible_speed:
            print(f"Внимание, скорость автомобиля {self.name} превышена!")


class PoliceCar (Car):
    def __init__(self, name, color, max_speed, is_police):
        super().__init__(name, color, max_speed, is_police)
        print ("Это полиция, уступите дорогу!")


c1 = Car ("Тойота", "красного", 250, False)
c1.go()
c1.stop()
c1.turn ("направо")
c1.show_speed (90)
print()

t1 = TownCar("Хонда", "желтого", 250, False, 500000)
t1.go()
t1.stop()
t1.turn ("налево")
t1.show_speed (80)
print()

s1 = SportCar ("BMV", "зеленого", 270, False, "РОССИЯ")
s1.go()
s1.stop()
s1.turn ("в сторону базы отдыха")
s1.show_speed (80)
print()

w1 = WorkCar ("Кия", "белого", 250, False)
w1.go()
w1.stop()
w1.turn ("направо")
w1.show_speed (100)
print()

p1 = PoliceCar ("Лада", "белого", 250, True)
p1.go()
p1.stop()
p1.turn ("в гараж")
p1.show_speed (130)

