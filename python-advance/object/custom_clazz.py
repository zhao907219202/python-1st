"""
定制类

    1. __str__  print对象时调用 类似 java 中的 toString

    2. __repr__ 在交互式命令行下面输出时调用
        # >>> s = Student('Michael')
        # >>> s
        # <__main__.Student object at 0x109afb310>

    3. __iter__ 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
        该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
        直到遇到StopIteration错误时退出循环

    4. __getitem__ 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
        1）下面的例子没有对step参数作处理，也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
        2）此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
        3）与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
        4）总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这
        完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

    5. __getattr__ 调用不存在的属性时，比如score，Python解释器会试图调用 __getattr__(self, 'score')
        来尝试获得属性，这样，我们就有机会返回score的值,也可以返回函数
        1) 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误

    6. __call__ 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
        能不能直接在实例本身上调用呢？在Python中，答案是肯定的。任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用

        1) __call__() 还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，
            所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
        2) 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，
            这么一来，我们就模糊了对象和函数的界限。那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，
            我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
"""


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

        if attr == 'age':
            return lambda: 25

        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    def __call__(self):
        return 'My name is %s.' % self.name


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self;

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


def print_info():
    s = Student('Michael')
    print(s)

    f = Fib()
    for n in f:
        print('iteration Fib seq:', n)

    print('get_item index', 5, ':', f[5])
    print('get_item slice [2:6]:', f[2:6])

    print('get_attr score:', s.score)
    print('get_attr age function:', s.age())

    print('call s():', s())
    print('callable Student:', callable(s))


print_info()
