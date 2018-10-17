"""
1. 多态：
    概念与java 一致，区别在于Python为动态语言，传入的对象有要执行的方法即可。
    区别于Java 编译时要求一定传入Animal类型，Python只需要保证传入的对象有一个run()方法就可以了

2. 对象信息
    1）type()
        # >>> import types
        # >>> def fn():
        # ...     pass
        # ...
        # >>> type(fn)==types.FunctionType
        # True
        # >>> type(abs)==types.BuiltinFunctionType
        # True
        # >>> type(lambda x: x)==types.LambdaType
        # True
        # >>> type((x for x in range(10)))==types.GeneratorType
        # True

    2) isinstance()
        还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
        优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽

        # >>> isinstance([1, 2, 3], (list, tuple))
        # True
        # >>> isinstance((1, 2, 3), (list, tuple))
        # True
    3) dir()
        如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，
        比如，获得一个str对象的所有属性和方法：

        # >>> dir('ABC')
        # ['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']

        类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，
        如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
"""


# 1. inherit
class Animal(object):
    def run(self):
        print("Animal is running...")


class Dog(Animal):
    def run(self):
        print("Dog is running...")


class Cat(Animal):
    def run(self):
        print("Cat is runnung...")


def run_twice(animal):
    animal.run()


a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)
print()


# 2. 特殊方法
class Example(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = Example()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x'))  # 有属性'x'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
setattr(obj, 'y', 19)  # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y'))  # 获取属性'y'
print('obj.y =', obj.y)  # 获取属性'y'

print('getattr(obj, \'z\') =', getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404

f = getattr(obj, 'power')  # 获取属性'power'
print("power function:", f)
print("power execution:", f())
