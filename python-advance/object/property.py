"""
1. @Property
    @property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，
    只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，
    负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作

    class Student(object):

        @property
        def score(self):
            return self._score

        @score.setter
        def score(self, value):
            if not isinstance(value, int):
                raise ValueError('score must be an integer!')
            if value < 0 or value > 100:
                raise ValueError('score must between 0 ~ 100!')
            self._score = value
"""


# 1. 利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
# 单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用“from xxx import *”而导入
class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height


def test():
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')


test()
