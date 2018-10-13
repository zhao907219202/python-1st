import copy

print(dir(copy))  # dir 查看模块包含的内容，它将模块的所有特性列出
li = [n for n in dir(copy) if not n.startswith('_')]
print(li)

print(copy.__all__)
# 使用 all 以外的函数，要么显示的实现，或者导入copy，用全名或短名
# 在编写模块的时候，设置 __all__ 这样的技术是相当有用的，过滤了很多其他程序不需要的变量
# 如果没有 __all__ 用import * 语句默认将会输出模块中所有不以下划线开头的全局名称

# 交互编辑器可以使用help
help(copy.copy)
print("####################")
# 文档
print(copy.copy.__doc__)
print(range.__doc__)

print("###################")
# 使用源代码
print(copy.__file__)

# 一些模块不包含任何源代码，可能融入了解释器，或者可能是C语言编写的
