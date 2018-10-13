import math

x = 1
while x <= 5:
    print(x)
    x += 1

words = ['a', 'b', 'c', 'd', 'e']
for word in words:
    print(word)

for num in range(0, 5):
    print(num)

d = {'x': 1, 'y': 2}
for key, value in d.items():
    print(key, 'correspond to', value)

names = ['Fred', 'Carry', 'Howard', 'Wade']
ages = [20, 22, 25, 21]
for i in range(len(names)):
    print(names[i], 'is', ages[i], 'years old')

print('==========分隔符===========')

for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')

# 循环中else 语句
for n in range(99, 81, -1):
    root = math.sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    # 如果不 break 则进入else
    print("Do not find it!")

# 列表推导式 -- 轻量级的循环
# 使用普通的圆括号而不是方括号不会得到"元组推导器"，而是得到一个生成器
print([x * x for x in range(10) if x % 3 == 0])
print([(x, y) for x in range(3) for y in range(3)])
