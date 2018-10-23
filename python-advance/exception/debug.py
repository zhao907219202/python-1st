"""
调试

    1. logging
        这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
        当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
        这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
        logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件

    2. pdb: python -m pdb 开启命令行的单步调试
        1） 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：
            # (Pdb) l
            #   1     # err.py
            #   2  -> s = '0'
            #   3     n = int(s)
            #   4     print(10 / n)
        2)  输入命令n可以单步执行代码：
            # (Pdb) n
            # > /Users/michael/Github/learn-python3/samples/debug/err.py(3)<module>()
            # -> n = int(s)
            # (Pdb) n
            # > /Users/michael/Github/learn-python3/samples/debug/err.py(4)<module>()
            # -> print(10 / n)
        3)  任何时候都可以输入命令p 变量名来查看变量：
            # (Pdb) p s
            # '0'
        4)  输入命令q结束调试，退出程序：
    3. IDE debug

"""

import logging

logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
