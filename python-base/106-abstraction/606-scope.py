x = 1
scope = vars()
print(scope['x'])


def combine(parameter):
    print(parameter + external)
    print('使用global函数获取全局变量值')
    print(globals()['external'])


external = "World"
combine("Hello ")


def multiplier(factor):
    def multiply_by_factor(number):
        return number * factor

    return multiply_by_factor


print()
# 返回 子函数（及其定义所在的作用域：它的环境）
double = multiplier(2)
print(double(5))


