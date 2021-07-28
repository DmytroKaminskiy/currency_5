# has is

# IS
# class Human:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def info(self):
#         return f'{self.first_name} {self.last_name}'
#
# class Student(Human):
#     def __init__(self, grade, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.grade = grade
#
#     def info(self):
#         human_info = super().info()
#         return f'{human_info} {self.grade}'
#
# h1 = Human(first_name='Dima', last_name='Kaminskyi')
# s1 = Student(first_name='Alex', last_name='R', grade='Python Dev')
#
# print(h1.info())
# print(s1.info())

# has
# class EngineV1:
#     def __init__(self):
#         self.volume = '2.4'
#
#
# class EngineV2:
#     def __init__(self):
#         self.volume = '4'
#
#
# class Car:
#     def __init__(self, en):
#         self.engine = en
#
#     def get_volume(self):
#         return self.engine.volume
#
# car_obj = Car(en=EngineV2())
# print(car_obj.get_volume())

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __hash__(self):
#         return 1
#
#     def __eq__(self, other):
#         print(self)
#         print(other)
#         return True
#
# c1 = Cat('Alisa')
# c2 = Cat('Not Alisa')
#
# c1 == c2
#
# dct = {
#     c1: '11',
#     c2: '22',
# }
# print(dct)

# class Shape:
#     def area(self):
#         raise NotImplementedError('Implement area method')
#
#     def perimeter(self):
#         raise NotImplementedError('Implement perimeter method')
#
# # area, perimeter
# class Circle(Shape):
#     def area(self):
#         pass
#
#     def perimeter(self):
#         pass
#
# class Triangle(Shape):
#     def area(self):
#         pass
#
#     def perimeter(self):
#         pass
#
# class Square(Shape):
#     def area(self):
#         pass
#
#     def perimeter(self):
#         pass
#
# c = Circle()
# c.area()
# c.perimeter()
#
# s = Square()
# s.area()
# s.perimeter()
#
# t = Triangle()
# t.area()
# t.perimeter()

'''
Lesson10
Формы

1. Создать модель Source с полями
   id
   source_url = string(255)
   name = string(64)
2. Показать список всех объектов Source
3. Создать форму для создания и редактирования модели Source (create/update)
4. Показать детали объекта Source (details)
5. Добавить удаление объекта Source (delete)
'''

from datetime import date

# class Human:
#     def __init__(self, first_name, last_name, date_of_birth):
#         self.first_name = first_name  # attribute
#         self.last_name = last_name  # attribute
#         self.date_of_birth = date_of_birth
#         # self.full_name = f"{first_name} {last_name}"
#
#     def get_age(self):
#         return int((date.today() - self.date_of_birth).days / 365)
#
#     @property
#     def age(self):
#         return int((date.today() - self.date_of_birth).days / 365)
#
#     @property
#     def full_name(self):
#         return f'{self.last_name} {self.first_name}'
#
#
# h1 = Human('Dmytro', 'Kaminskyi', date(1992, 1, 23))
# # print(h1.get_age())
# print(h1.age)


# class Human:
#     def __init__(self, first_name):
#         self._first_name = first_name.capitalize()
#
#     @property
#     def first_name(self):  # getter
#         return self._first_name
#
#     @first_name.setter
#     def first_name(self, value):  # setter
#         self._first_name = value.capitalize()
#
#     @first_name.deleter
#     def first_name(self):  # deleter
#         self._first_name = None
#
# h1 = Human('dmytro')
# print(h1.first_name)
# h1.first_name = 'alEX'
# print(h1.first_name)
#
# del h1.first_name
# print(h1.first_name)


# class TemplateView:
#     def get_context_data(self, **kwargs):
#         context = {
#             'message': 'Hello',
#         }
#         return context
#
#
# class GeneratePasswordView(TemplateView):
#     template_name = 'generate_password.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context = {}
#         return context
#
#
# gp = GeneratePasswordView()
# print(gp.get_context_data())

'''
1. CRUD операции для модели Source создать на основе class based views.
2. Создать модуль urls.py в приложении currency и подключить в settings/urls.py
3. Все линки в шаблонах должны быть сгенерированы с помощью тега {% url '...' %}
4. Все линки в python коде должны быть сгенерированы с помощью функции reverse или reverse_lazy
'''

# from functools import reduce

def add(x, y):
    return x + y

print(add(2, 3))
print(add.__call__(2, 3))

# print(reduce(add, [1, 2, 3]))
# print(reduce(lambda x, y: x + y, [1, 2, 3]))

add2 = lambda x, y: x + y
print(add2(2, 3))
print(add2.__call__(2, 3))

# class Foo:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __call__(self, *args, **kwargs):
#         return self.x + self.y
#
# f = Foo(3, 6)
# print(f())
