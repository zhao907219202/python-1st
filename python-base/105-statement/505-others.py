from math import sqrt

# python 中空代码块是非法的 所以用pass起到占位符的作用
name = "Howard"
if name == "Ralph":
    print("Welcome")
elif name == "Enid":
    pass
elif name == "Bill Gates":
    print("Access Denied")

x = ["Hello", "World"]
y = x
y[1] = "Python"
del x
# 删除的只是名称，值在Python中时没有办法删除的，解释器负责内存的回收
print(y)

# Python3 exec是函数 不再是语句
exec("print('Hello,world!')")

# 使用exec 要注意命名空间的问题


scope = {}
exec('sqrt=2', scope)
sqrt(4)
print(scope['sqrt'])
# 类似exec 为执行字符串求值语句
print(eval("sqrt*sqrt", scope))
