phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(phonebook['Beth'])

# 可以通过其他映射（比如其他字典）或者（键值）这样的序列对建立字典
items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print(d)

d = dict(name='Howard', age=24)
print(d)

# 字典的键可以是任何不可变类型
x = []
# x[42] = 'name' IndexError: list assignment index out of range
x = {}
x[42] = 'name'
print(x)
