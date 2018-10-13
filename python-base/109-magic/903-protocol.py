def checkIndex(key):
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class CustomSequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        checkIndex(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value


s = CustomSequence(1, 2)
print(s[4])
s[4] = 2
print(s[4], s[5])
# 由于没有定义 __delitem__，删除元素会抛出异常
# del s[4] AttributeError: __delitem__
# __len__ 返回集合中所含项目的个数


