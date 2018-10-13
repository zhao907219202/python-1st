class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    # Python 3 用 __next__代替nexr
    # 用内建函数next(it) 代替原it.next()
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


# 一个实现了__iter__方法的对象说明其是可迭代的
# 一个实现了__next__方法的对象说明其是一个迭代器
# 推荐迭代器实现自己的__iter__方法，这样就可以直接在for循环中迭代其本身了

fibs = Fibs()
# 循环开始时调用iter方法获取迭代器，后每次循环调用next方法获取下一个值s
for f in fibs:
    if f > 1000:
        print(f)
        break

it = iter([1, 2, 3])
print(next(it))
print(next(it))
