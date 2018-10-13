# 序列解包需要等号 左右边变量数量完全一致
x, y, z = 1, 2, 3
print(x, y)
x, y = y, x
print(x, y)

scoundrel = {'name': 'Robin', 'girlfriend': "Marion"}
key, value = scoundrel.popitem()
print(key, value)

# 链式赋值
x = y = 1
print(x, y)
