# 这几个值作为布尔表达式时 会被解释成假
# False None 0 "" () [] {}
print(bool(None))
print(True == 1)

name = "Maris"
if name.endswith("Howard"):
    print("Hello")
else:
    print("World")

num = 15
if num > 0:
    print("The number is  positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

# print(1 > 'a')  TypeError: '>' not supported between instances of 'int' and 'str'
print("aa" == "bb")

# 字符串比较大小 是根据ord函数返回结果依次比较
print(ord('a'))
print(chr(97))
print("Abc" > "abc")

# 序列比较
print([1, 2] > [2, 1])
print([2, [1, 4]] < [2, [1, 5]])

# bool运算符  and or
num = 5
if 0 < num < 10:
    print("Hello")

# 断言
age = 10
assert 0 < age < 10
