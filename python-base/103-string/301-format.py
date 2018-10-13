import math
from string import Template

# 字符串是不可变的 不能用分片形式进行赋值 [1:3] ='ab'

format = "Hello,%s. %s enough for you?"
values = ('world', 'Hot')
# 如果用列表或其他序列代替元组，那么序列就会被解释为一个值
# 报错 TypeError: not enough arguments for format string
print(format % values)

# 需要使用百分号 则用 %% 进行转义
format = 'Pi with three decimals: %.3f'
values = math.pi
print(format % values)

s = Template('$x.glorious $x')
print(s.substitute(x='python'))

s = Template('It\' is ${x}thon program!')
print(s.substitute(x='py'))

s = Template('Make $$ selling $x')
print(s.substitute(x='python'))

s = Template('A $thing must nerver $action')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
print(s.substitute(d))

# safe_substitute 不会因为缺少值或者不正确使用$字符而出错
