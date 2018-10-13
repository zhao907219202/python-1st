import math

x = 1
y = math.sqrt
print(callable(x))
print(callable(y))


def hello(name):
    """ function doc with help() to print it
    """
    print('Hello', name)


def fibs(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result


hello("Howard")
print(fibs(10))
help(hello)
