import functools

print(set(range(0, 10)))

a = set([1, 2, 3])
b = {2, 3, 4}
c = a.union(b)
print(c)
print(a | b)
c = a & b
print(c)

print(c <= a)
print(c.issubset(a))
print(c.issuperset(a))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a ^ b)
a.symmetric_difference_update(b)  # 修改 a，去掉重复的元素，添加 b 有 a 没有的元素
print(a)
print(b)

print(a.copy() is a)
print(a.copy() == a)

mySets = []
for i in range(10):
    mySets.append(set(range(i, i + 5)))
result = functools.reduce(set.union, mySets)
print(result)

# 集合是可变的，所以不能作为字典的键
# 集合本身只能包含不可变(可散列)的值，所以不能包含其他集合
# 为了可以使用集合的集合，所以需要使用 frozenset，用于表示不可变(可散列)的集合

a = set()
b = set([1,2])
c = set([3,4])
# a.add(b)  # TypeError: unhashable type: 'set'
a.add(frozenset(b))
a.add(frozenset(c))
print(a)


