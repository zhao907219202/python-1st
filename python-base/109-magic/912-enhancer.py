def gen(x):
    count = x
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1


f = gen(5)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print('====================')
print(f.send(9))  # 发送数字9给生成器
print(f.__next__())
print(f.__next__())

# f.throw(RuntimeError) RuntimeError
f.close()  # 停止生成器


# print(f.__next__())  StopIteration


# 模拟生成器
def flatten(nested):
    result = []
    try:
        nested + ''
    except TypeError:
        pass
    else:
        raise TypeError
    try:
        for sublist in nested:
            for element in flatten(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result
