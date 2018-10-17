"""
偏函数

1. functools.partial可以把一个参数多的函数变成一个参数少的新函数，
少的参数需要在创建时指定默认值，这样，新函数调用的难度就降低了。

# >>> int('12345', base=8)
# 5349

# def int2(x, base=2):
#     return int(x, base)

# >>> int2('1000000')
# 64

# >>> import functools
# >>> int2 = functools.partial(int, base=2)
# >>> int2('1000000')
# 64

"""

import functools

sorted_ignore_case = functools.partial(sorted, key=functools.cmp_to_key(
    lambda x, y: 1 if x.lower() > y.lower() else (-1 if x.lower() < y.lower() else 0)))

print("Partial: " + str(list(sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']))))
