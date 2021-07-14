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
class EngineV1:
    def __init__(self):
        self.volume = '2.4'


class EngineV2:
    def __init__(self):
        self.volume = '4'


class Car:
    def __init__(self, en):
        self.engine = en

    def get_volume(self):
        return self.engine.volume

car_obj = Car(en=EngineV2())
print(car_obj.get_volume())

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

class Shape:
    def area(self):
        raise NotImplementedError('Implement area method')

    def perimeter(self):
        raise NotImplementedError('Implement perimeter method')

# area, perimeter
class Circle(Shape):
    def area(self):
        pass

    def perimeter(self):
        pass

class Triangle(Shape):
    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Shape):
    def area(self):
        pass

    def perimeter(self):
        pass

c = Circle()
c.area()
c.perimeter()

s = Square()
s.area()
s.perimeter()

t = Triangle()
t.area()
t.perimeter()
