"""
元类
    class Hello(object):
        def hello(self, name='world'):
            print('Hello, %s.' % name)

    # >>> from hello import Hello
    # >>> h = Hello()
    # >>> h.hello()
    # Hello, world.
    # >>> print(type(Hello))
    # <class 'type'>
    # >>> print(type(h))
    # <class 'hello.Hello'>

    1. type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
    2. type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，
        而无需通过class Hello(object)...的定义：

        # >>> def fn(self, name='world'): # 先定义函数
        #         print('Hello, %s.' % name)
        # >>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
        # >>> h = Hello()
        # >>> h.hello()
        # Hello, world.
        # >>> print(type(Hello))
        # <class 'type'>
        # >>> print(type(h))
        # <class '__main__.Hello'>

        要创建一个class对象，type()函数依次传入3个参数：
        1） class的名称；
        2）继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
        3）class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

        通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
        仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。


    3. metaclass:
        先定义metaclass，就可以创建类，最后创建实例。
        metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

"""

# type 动态创建类
Hello = type('Hello', (object,), dict())
h = Hello()


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class CustomList(list, metaclass=ListMetaclass):
    pass


"""
当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，
要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

__new__()方法接收到的参数依次是：
1) 当前准备创建的类的对象；
2) 类的名字；
3) 类继承的父类集合；
4) 类的方法集合。

"""


def print_info():
    print('type create class:', type(h))

    custom_list = CustomList()
    custom_list.add(1)
    print('metaclass define add method:', custom_list)


print_info()
