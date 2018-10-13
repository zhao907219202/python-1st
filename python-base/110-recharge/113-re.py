# re.compile 将正则表达式（以字符串书写的）转换为模式对象
# 在调用re.search 和 re.match 时，其内部也会将字符串转换为正则表达式对象
# 使用compile转换过一次之后，在每次使用模式的时候就不用进行转换
# re.search(pat,string) pat 是string类型的正则表达式 等价于 pat.search(string) pat 是compile创建的模式对象
# 经过compile 转换后的正则表达式对象也能用于普通的re函数

# re.search 在字符串中寻找模式 如果存在返回MatchObject 值为True，否则为None 值为False
# re,match 在字符串的开头匹配正则表达式，结果同上，模式的结尾加美元符号，会要求匹配整个字符串
# re.split 根据模式的匹配项来分割字符串
# re.findall  列出字符串中所有的匹配项
# re.sub(pat,repl,string[,count=0] 将字符串中所有pat的匹配项用repl替换
# re.escape(string) 将字符串中所有的特殊正则表达式字符转义

import re

some_text = 'alpha,bata, ,,, ,gama  delta'
print(re.split('[, ]+', some_text))  # 匹配任意长度的逗号和空格
print(re.split("a(m)", "family"))  # ['f', 'm', 'ily'] 小括号的内容会放在中间
print(re.split('[, ]+', some_text, maxsplit=2))  # 最大分隔的部分数

pat = "[a-zA-Z]+"
text = '"Hm...Err -- are you sure?"he said, sounding insecure.'
print(re.findall(pat, text))
pat = r'[.?\-",]+'  # 匹配标点符号 - 需要被转义
print(re.findall(pat, text))

pat = '{name}'
text = "Dear {name}"
print(re.sub(pat, "Mr.Fred", text))

print(re.escape("www.python.org"))
print(re.escape("But where is the ambiguity?"))

# 组的概念： 当找到匹配项的时候，他们都会返回MatchObject对象，这些对象包括匹配模式的子字符串信息，
# 他们还包含了哪个模式匹配了子字符串哪部分信息，这些部分就叫做组
# 组 即圆括号里面的匹配项

# group 获取给定组的匹配项
# start 返回给定组的匹配项的开始位置
# end   返回给定组的匹配项的结束位置，和分片一样，不包括组的结束位置
# span  返回一个组的开始和结束位置
print("########### Group ###########")
m = re.match(r'www\.(.*)\..{3}', "www.python.org")
print(m.group(1))
print(m.start(1))
print(m.end(1))
print(m.span(1))

emphasis_pattern = re.compile(r'''
  \*      # Beginning emphasis tag -- an asterisk
  (       # Bigin group for capturing phrase
  [^\*]+  # Capture anything except asterisk
  )       # End group
  \*      # Ending emphasis tag
''', re.VERBOSE)
print(re.sub(emphasis_pattern, r'<em>\1</em>', "Hello,*world*!"))
emphasis_pattern = re.compile(r'\*(.+)\*')
# 重复运算发默认是贪婪的，尽可能多的匹配，所以下面例子只会匹配一头一尾，解决办法 加个问号
print(re.sub(emphasis_pattern, r'<em>\1</em>', "*Hello*,*world*!"))

emphasis_pattern = re.compile(r'\*(.+?)\*')
print(re.sub(emphasis_pattern, r'<em>\1</em>', "*Hello*,*world*!"))

