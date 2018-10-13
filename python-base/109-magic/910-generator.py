ln = [[1, 2], [3, 4], [5]]


# 任何包含yield语句的函数成为生成器
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


# yield不是像return那样返回值，而是每次产生多个值
# 每次产生一个值（使用yield语句），函数就会被冻结，即函数停在那里等待被激活。
# 函数被激活后就从停止的那点开始执行。

generator = flatten(ln)
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())

# 生成器表达式
g = ((i + 2) * 2 for i in range(2, 10))
print(g.__next__())
print(g.__next__())

print(sum((i + 1) * 5 for i in range(1, 5)))
