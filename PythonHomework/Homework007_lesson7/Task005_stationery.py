#
# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# # Создать экземпляры классов и проверить, что выведет описанный метод 
# для каждого экземпляра

class Stationery:
    def __init__(self,title):
        self.title = title
        print (f"Создали {self.title}")
    
    def draw (self):
        print ("Запуск отрисовки")

class Pen (Stationery):
    def draw (self):
        print ("Ручка, пиши!")

class Pencil (Stationery):
    def draw (self):
        print (f"Карандаш, рисуй!")

class Handle (Stationery):
    def draw (self):
        print (f"Маркер, подчеркивай!")

st = Stationery ("Ручка, карандаш, маркер")
st.draw()
print()

p= Pen ("Ручка BIG")
p.draw()
print()

pen= Pencil ("Карандаш DD")
pen.draw()
print()

h = Handle ("Желтый маркер")
h.draw()
print()