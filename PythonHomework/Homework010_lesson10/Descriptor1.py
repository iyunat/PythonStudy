#Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ
# Дескриптор №1:

class PositiveNumber:
    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

       
    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    length = PositiveNumber()
    width = PositiveNumber()
    weight_square_meter = PositiveNumber()
    thickness_canvas = PositiveNumber()

    def __init__(self, length, width, weight_square_meter, thickness_canvas ):
        self.length = length
        self.width = width
        self.weight_square_meter = weight_square_meter
        self.thickness_canvas = thickness_canvas
        
    def asphalt_mass (self):
        print (self.length * self.width * self.weight_square_meter * self.thickness_canvas)

r1 = Road (20, 5000, 25, 0.05)

r1.asphalt_mass()