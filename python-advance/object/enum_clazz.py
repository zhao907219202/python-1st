"""
枚举类

    1.example:
        from enum import Enum

        Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
        for name, member in Month.__members__.items():
            print(name, '=>', member, ',', member.value)

        # Jan => Month.Jan , 1
        # Feb => Month.Feb , 2
        # ...
        # Nov => Month.Nov , 11
        # Dec => Month.Dec , 12

    2. example

        from enum import Enum, unique
        # @unique装饰器可以帮助我们检查保证没有重复值。
        @unique
        class Weekday(Enum):
            Sun = 0 # Sun的value被设定为0
            Mon = 1
            Tue = 2
            Wed = 3
            Thu = 4
            Fri = 5
            Sat = 6

        # >>> day1 = Weekday.Mon
        # >>> print(day1)
        # Weekday.Mon
        # >>> print(Weekday.Tue)
        # Weekday.Tue
        # >>> print(Weekday['Tue'])
        # Weekday.Tue
        # >>> print(Weekday.Tue.value)
        # 2
        # >>> print(day1 == Weekday.Mon)
        # True
        # >>> print(day1 == Weekday.Tue)
        # False
        # >>> print(Weekday(1))
        # Weekday.Mon
        # >>> print(day1 == Weekday(1))
        # True
        # >>> Weekday(7)
        # Traceback (most recent call last):
        #   ...
        # ValueError: 7 is not a valid Weekday

        # >>> for name, member in Weekday.__members__.items():
        #         print(name, '=>', member)
        # ...
        # Sun => Weekday.Sun
        # Mon => Weekday.Mon
        # Tue => Weekday.Tue
        # Wed => Weekday.Wed
        # Thu => Weekday.Thu
        # Fri => Weekday.Fri
        # Sat => Weekday.Sat

"""

from enum import Enum, unique


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


def print_info():
    bart = Student('Bart', Gender.Male)
    if bart.gender == Gender.Male:
        print('测试通过!')
    else:
        print('测试失败!')


print_info()
