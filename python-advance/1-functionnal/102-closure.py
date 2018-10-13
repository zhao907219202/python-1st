"""
返回函数 —————— 闭包

1. 像这种内层函数引用了外层函数的变量（参数也算变量），
然后返回内层函数的情况，称为闭包（Closure）。

2. 闭包的特点是返回的函数还引用了外层函数的局部变量，
所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变.

3. 匿名函数：lambda x: x * x 实际上就是
关键字lambda 表示匿名函数，冒号前面的 x 表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不写return，返回值就是该表达式的结果

>>> myabs = lambda x: -x if x < 0 else x
>>> myabs(-1)
1

"""
from functools import reduce


# 1. return function example
def calc_prod(lst):
    def lazy_prod():
        def multi_product(x, y):
            return x * y

        return reduce(multi_product, lst, 1)

    return lazy_prod


ret_func = calc_prod([1, 2, 3, 4])
print("lazy_prod: " + str(ret_func()))


# 2.  local variable can't change
# 希望一次返回3个函数，分别计算1x1,2x2,3x3:
def count1():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


c1_f1, c1_f2, c1_f3 = count1()
print("count1: " + str(c1_f1()))  # 输出是9，因为局部变量i已经变成了3


# 多包一层函数，局部变量传入，再调用一次返回内部函数，确保不会变
def count2():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j

            return g

        r = f(i)
        fs.append(r)
    return fs


c2_f1, c2_f2, c2_f3 = count2()
print("count2: " + str(c2_f1()))


# 3. 用匿名函数简化
def is_not_empty(s):
    return s and len(s.strip()) > 0


print("normal: :" + str(list(filter(is_not_empty, ['test', None, '', 'str', '  ', 'END']))))
print("lambda: " + str(list(filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END']))))
