#Создать метакласс для паттерна Синглтон 

# class Singleton(type):
#     def __call__(self, *args, **kwargs):
#         """ Вызов класса создает новый объект. """
#         # Перво-наперво создадим сам объект...
#         print(self)  # <class '__main__.MyClass'>
#         print('вызываем')
#         obj = type.__call__(self, *args)  # -> <__main__.MyClass object at 0x000001F4A446C6C8>
#         print(obj)
#         # ...и добавим ему переданные в вызове аргументы в качестве атрибутов.
#         for name in kwargs:
#             setattr(obj, name, kwargs[name])
#             # вернем готовый объект
#         return obj


# # Теперь создадим класс, использующий новый метакласс
# class MyClass(metaclass=Singleton):
#     pass


# # Теперь создадим класс, использующий новый метакласс
# class MyClass2(metaclass=Singleton):
#     pass


# # Ура!!!

# MC = MyClass(param_1=100, param_2=200)
# print(MC.param_2)

class MetaSingleton(type):
    _instances = {}
    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(MetaSingleton, self).__call__(*args, **kwargs)
        return self._instances[self]


class SingletonTema(metaclass=MetaSingleton):
    pass


sing1 = SingletonTema()
sing2 = SingletonTema()
print(sing1 == sing2)



