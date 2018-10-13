edward = ['Edward Gumby', 25]
john = ['John Smith', 50]
database = [edward, john]
print(database)

greeting = 'Hello'
print(greeting[0])
print(greeting[-1])

tag = '<a href="http://www.python.org">Python web site</a>'
# 取头不取尾
print(tag[9:30])
print(tag[32:-4])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[-3:0])  # [] :左边索引要是比右边索引晚出现 则返回空序列
print(numbers[-3:])
print(numbers[:3])

# 步长
print(numbers[::2])  # [1, 3, 5, 7, 9]
print(numbers[8:3:-1])  # [9, 8, 7, 6, 5]  步长不能为0 为负代表从右往左截取
print(numbers[::-2])  # [10, 8, 6, 4, 2]
print(numbers[5::-2])  # [6, 4, 2]
print(numbers[:5:-2])  # [10, 8]

# print([1, 2, 3] + 'string')
print(['a', 'b'] * 5)  # ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
