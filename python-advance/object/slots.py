"""
1. 动态给实例绑定属性和方法，给一个实例绑定的方法，对另一个实例是不起作用的
   但也可以动态给类绑定方法

2. 想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
   为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，
   来限制该class实例能添加的属性

注意：
   __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
   除非在子类中也定义__slots__，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
"""
from types import MethodType
from object.clazz import Student


# 1. 动态绑定
def set_gender(self, gender):
    self.gender = gender


def set_hometown(self, hometown):
    self.hometown = hometown


s = Student("Fred Simpson", 75)
s.age = 22
print("set age property:", s.age)

s.set_gender = MethodType(set_gender, s)
s.set_gender("F")
print("set gender instance function:", s.gender)

Student.set_hometown = set_hometown
s.set_hometown("New York")
print("set hometown class function:", s.hometown)

print()


# 2. __slots__
class GraduateStudent(Student):
    __slots__ = ('name', 'score')

    def __init__(self, name):
        super(GraduateStudent, self).__init__(name, 0)


g = GraduateStudent("Susan Simpson")
# g.grade = 7   # AttributeError: 'GraduateStudent' object has no attribute 'grade'
# print("set grade error:", g.grade)
print("GraduateStudent Name:", g.get_name(), ",Score:", g.get_score())
