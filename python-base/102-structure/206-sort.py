a = [5, 1, 3, 6, 7, 4, 2]
# 排序列表
a.sort()
print(a)
# 保留原列表排序
a.reverse()
b = sorted(a)
print(a)
print(b)

# 高级排序
x = ['ab', 'bba', 'edd', 'opsa', 'sa']
x.sort(key=max, reverse=True)
print(x)
