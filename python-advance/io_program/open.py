"""
    1. 标示符'r'表示读，这样，我们就成功地打开了一个文件
    2. 调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
    3. 可以反复调用read(size)方法，每次最多读取size个字节的内容。
    4. 调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
    5. 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
        除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
        StringIO就是在内存中创建的file-like Object，常用作临时缓冲

    由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
    所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：

    6.  f = open('/Users/michael/test.jpg', 'rb')   # 读二进制文件
    7. f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')  # 默认UTF编码，指定编码读取
    8. f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')  # 遇到有些编码不规范的文件，
        你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，
        open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
    9. 写文件和读一直，把 r 换成 w 即可
"""

try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('/path/to/file', 'r') as f:
    print(f.read())
