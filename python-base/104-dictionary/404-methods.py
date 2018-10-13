from copy import deepcopy

phoneBook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(phoneBook.clear())
print(phoneBook)

x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
# 浅拷贝
y = x.copy()
y['username'] = 'guest'
y['machines'].remove('bar')
print(y)
print(x)

# 深浅拷贝比较
d = dict({})
d['name'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['name'].append('Clive')
print(c)
print(dc)

# fromKeys 方法使用给定的键建立新的字典，默认的值位None
print({}.fromkeys(['name', 'age']))
print(dict.fromkeys(['name', 'age']))
print(dict.fromkeys(['name', 'age'], 'unknown'))

# get 找不到不会报错误
d = {}
# print(d['name']) KeyError: 'name'
print(d.get('name'))
print(d.get('name', 'N/A'))  # 添加默认值
# print(d.has_key('name')) python3没有该方法

d = {'username': 'guest', 'machines': ['foo', 'baz']}
print(d.items())
print(d.keys())
print(d.values())

# 用一个字典更新另一个字典
x = {'title': 'info'}
print(d.update(x))
print(d)

# pop 获得给定键的值 并删除键值对
print(d.pop('title'))
print(d)

# popitem 弹出随机的项
print(d.popitem())
print(d)

d = {}
# setdefault 返回当前字典中的值 默认为None
print(d.setdefault('name', 'N/A'))
d['name'] = 'Fred'
print(d.setdefault('name', 'N/A'))
print(d)
