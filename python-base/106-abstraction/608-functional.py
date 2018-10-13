from functools import reduce

l = map(str, range(10))
print(list(l))


def func(x):
    # 判断是否是由字符和数字组成
    return x.isalnum()


seq = ["foo", "x41", "?!", "***"]
print(list(filter(func, seq)))
print([x for x in seq if x.isalnum()])

f = filter(lambda x: x.isalnum(), seq)
print(list(f))

# reduce函数：它会将序列的前两个元素与给定的函数联合使用，并且将他们的返回值
# 和第三个元素继续联合使用，知道整个序列都处理完毕，得到一个最终结果
numbers = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 32]
r = reduce(lambda x, y: x + y, numbers)
print(r)
