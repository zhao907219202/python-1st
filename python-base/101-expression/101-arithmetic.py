# coding:utf-8
"""
请计算: 19+2*4-8/2
"""
a = 19 + 2 * 4 - 8 / 2
print(a)

b = 101
# print("Hello," + b)  TypeError: must be str, not int
print("Hello," + str(b))
print("World," + repr(b))

