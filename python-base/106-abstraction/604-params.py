def hello(greeting='Hello', name='world'):
    print('%s, %s' % (greeting, name))


def print_param(*param):
    print(param)


def print_param_2(**param):
    print(param)


def print_param_3(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)


# 使用关键字参数赋默认值
hello(name="zhaoyu")

# 参数前加 * 作为元组传递
print_param("abc", "cba", '123')

# 参数前加 ** 作为字典传递
print_param_2(x=1, y=2, z=3)

# 混合使用
print()
print_param_3(1, 2, 3, 5, 6, 7, foo=1, bar=2)


# 参数反转
def add(a, b):
    print(a + b)


def print_param_4(x, y, z):
    print(x, y, z)


c = (1, 2)
add(*c)

d = {'x': 1, 'y': 2, 'z': 3}
print_param_4(**d)
