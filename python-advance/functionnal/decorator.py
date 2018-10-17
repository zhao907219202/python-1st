"""
装饰器

1. Python的 decorator 本质上就是一个高阶函数，它接收一个函数作为参数，返回一个新函数。
使用 decorator 用Python提供的 @ 语法，这样可以避免手动编写 f = decorate(f) 这样的代码
example：
    def log(f):
        def fn(x):
            print('call ' + f.__name__ + '()...')
            return f(x)
        return fn

    @log
    def factorial(n):
        return reduce(lambda x,y: x*y, range(1, n+1))

@log 只支持参数是一个的函数，任意多个参数 需要把上面的 x 替换成 *args, **kw


2. 对于被装饰的函数，log打印的语句是不能变的（除了函数名）。

如果有的函数非常重要，希望打印出'[INFO] call xxx()...'，
有的函数不太重要，希望打印出'[DEBUG] call xxx()...'，
这时，log函数本身就需要传入'INFO'或'DEBUG'这样的参数

example：

    def log(prefix):
        def log_decorator(f):
            def wrapper(*args, **kw):
                print '[%s] %s()...' % (prefix, f.__name__)
                return f(*args, **kw)
            return wrapper
        return log_decorator

    @log('DEBUG')
    def test():
        pass
    print(test())


3. 经过@decorator“改造”后的函数，和原函数相比__name__、__doc__等其它属性被改变

example：
    def log(f):
        def wrapper(*args, **kw):
            print 'call...'
            return f(*args, **kw)
        return wrapper

    @log
    def f2(x):
        pass
    print(f2.__name__)

    输出： wrapper


解决方案：

1）手动复制
    def log(f):
        def wrapper(*args, **kw):
            print 'call...'
            return f(*args, **kw)
        wrapper.__name__ = f.__name__
        wrapper.__doc__ = f.__doc__
        return wrapper

2）内置的functools可以用来自动化完成这个“复制”的任务

    import functools
    def log(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            print 'call...'
            return f(*args, **kw)
        return wrapper

但是函数的签名一定会变，因为参数列表变成了*args, **kw。即使是固定的参数个数，参数名也未必一致。



"""

from functools import reduce
from functools import wraps
import time


# 1. 编写一个@performance，它可以打印出函数调用的时间。
def performance1(f):
    def fn(*args, **kw):
        start = time.time()
        result = f(*args, **kw)
        print("call %s() cost %fs " % (f.__name__, time.time() - start))
        return result

    return fn


@performance1
def factorial1(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print("Performance1 decorator: " + str(factorial1(10)))
print()


# 2. 给 @performance 增加一个参数，允许传入's'或'ms'
def performance2(unit):
    def decorator(f):
        def wrapper(*args, **kw):
            start = time.time()
            result = f(*args, **kw)
            cost = time.time() - start
            print("call %s() cost %f%s " % (f.__name__, cost * 1000 if unit == "ms" else cost, unit))
            return result

        return wrapper

    return decorator


@performance2("ms")
def factorial2(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print("Performance1 decorator: " + str(factorial2(10)))
print()


# 3. 给performance 添加 @functools.wraps
def performance3(unit):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            start = time.time()
            result = f(*args, **kw)
            cost = time.time() - start
            print("call %s() cost %f%s " % (f.__name__, cost * 1000 if unit == "ms" else cost, unit))
            return result

        return wrapper

    return decorator


@performance3("ms")
def factorial3(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print("Performance3 factorial Name: " + factorial3.__name__)
