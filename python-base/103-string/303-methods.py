print('With a moo-moo here,and a moo-moo there'.find('moo'))
title = "Monty Python's Flying Circus"
print(str(title.find("Monty")) + " " + repr(title.find('Python')))
print(title.find('Exist'))

subject = '$$$ Get rich now!!! $$$'
# 取头不取尾
print(subject.find('$$$', 0, 10))

# split 逆方法
seq = ['1', '2', '3', '4', '5']
print('+'.join(seq))
dirs = '', 'usr', 'bin', 'env'
print('C:' + '\\'.join(dirs))

title = "  have space  "
print(title.strip())

# translate 需要maketrans转换表 参数是两个等长的字符串
# 第一个字符串中的每个字符都用第二个相同位置的字符替换
subject = 'this is an incredible test'
table = subject.maketrans('cs', 'kz')
print(table)
print(subject.translate(table))

sentence = 'I am a coder'
print(sentence.partition('am'))
