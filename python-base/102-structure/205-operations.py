# 改变列表 元素赋值
x = [1, 1, 1]
x[1] = 2
print(x)

names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print(names)

letters = list('Perl')
print(letters)
# 不等长序列分片替换
letters[1:] = list('Python'[1:])
print(letters)

numbers = [1, 5]
# 插入新的元素
numbers[1:1] = [2, 3, 4]
print(numbers)
# 删除元素 等同于 del numbers[1:4]
numbers[1:4] = []
print(numbers)
# 追加元素
numbers.append(6)
print(numbers)

# 统计某个元素在列表中出现的次数
count = ['a', 'b', 'c', 'a', 'd'].count('a')
print(count)

# 用新列表扩展原有列表
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)  # a + b 会返回一个全新的列表
print(a)
# 找出某个值第一个匹配的索引位置
print(a.index(4))
# 将对象插入到列表中
a.insert(3, 0)
print(a)
# 移除列表中的一个元素（默认是最后一个）
b = a.pop()
print(b)
print(a)
# 删除某个元素（必须已经存在于列表中）
a.remove(1)
print(a)
# 倒序列表
a.reverse()
print(a)
