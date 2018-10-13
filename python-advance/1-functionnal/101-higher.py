"""
高阶函数

1. map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，
并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。

2. reduce()函数也是Python内置的一个高阶函数。reduce()函数接收的参数和 map()类似，
一个函数 f，一个list，但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，
reduce()对list的每个元素反复调用函数f，并返回最终结果值。

3. filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个
函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，
filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。

4. Python内置的 sorted()函数可对list进行排序：但 sorted()也是一个高阶函数，
它可以接收一个比较函数来实现自定义排序，比较函数的定义是，传入两个待比较的元素 x, y，
如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。
如果 x 和 y 相等，返回 0。 Python3 中取消了函数参数，所以需用 cmp_to_key 解决

"""
import math
from functools import reduce
from functools import cmp_to_key


# 1. add example
def add(x, y, f):
    return f(x) + f(y)


print("Add: " + str(add(-5, 9, abs)))


# 2. map example
def format_name(s):
    return s[0].upper() + s[1:].lower()


print("Map: " + str(list(map(format_name, ['adam', 'LISA', 'barT']))))


# 3. reduce example
def multi_product(x, y):
    return x * y


print("Reduce: " + str(reduce(multi_product, [1, 2, 3, 4, 5], 10)))


# 4. filter example
def is_sqrt(x):
    r = int(math.sqrt(x))
    return r * r == x


print("Filter: " + str(list(filter(is_sqrt, range(1, 101)))))


# 5. sorted example

def ignore_case_cmp(x, y):
    lx = x.lower()
    ly = y.lower()
    if lx > ly:
        return 1
    elif lx < ly:
        return -1
    else:
        return 0


print("Sorted: " + str(list(sorted(['bob', 'about', 'Zoo', 'Credit'], key=cmp_to_key(ignore_case_cmp)))))
