def flatten(nested):
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


# 不应该在flatten函数中对类似于字符串的对象进行迭代
# 1 字符串要作为原子值 不可展开
# 2 会导致无穷递归，因为一个字符串的第一个元素是另一个长度为1的字符串，
# 而长度为1的字符串的第一个元素就是字符串本身

li = list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8]))
print(li)


# 函数被调用时，在函数体中的代码不会被执行，而会返回一个迭代器。
# 每次请求一个值，就会执行生成器中的代码，直到遇到一个yield 或 return，
# yield语句意味着应该生成一个值

# 生成器包含两个部分：1 生成器的函数（包含yield的函数） 2. 生成器的迭代器（返回的部分）
