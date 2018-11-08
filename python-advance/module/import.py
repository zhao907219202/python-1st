"""
1. 导入
    如果遇到名字冲突怎么办？比如math模块有一个log函数，logging模块也有一个log函数，
    如果同时使用，如何解决名字冲突？

    如果使用import导入模块名，由于必须通过模块名引用函数名，因此不存在冲突：

    import math, logging
    print math.log(10)                      # 调用的是math的log函数
    logging.log(10, 'something')            # 调用的是logging的log函数

    如果使用 from...import 导入 log 函数，势必引起冲突。可以给函数起个“别名”来避免冲突：

    from math import log
    from logging import log as logger       # logging的log现在变成了logger
    print log(10)                           # 调用的是math的log
    logger(10, 'import from logging')       # 调用的是logging的log

2. 动态导入
    利用ImportError错误，我们经常在Python中动态导入模块：
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO

    注意: Python 3 中没有 StringIO 和 cStringIO 只有 io_program

3. __future__
    Python的新版本会引入新的功能，但是，实际上这些功能在上一个老版本中就已经存在了。
    要“试用”某一新的特性，就可以通过导入__future__模块的某些功能来实现

    要在Python 2.7中引入3.x的除法规则，导入__future__的division：
    # >>> from __future__ import division
    # >>> print 10 / 3
    # 3.3333333333333335


"""
from __future__ import unicode_literals
import os

print("os.path.isdir: " + str(os.path.isdir(r'/data/resource/python')))
print("os.path.isfile: " + str(os.path.isfile(r'/data/resource/python/test.txt')))

# 在Python 3.x中，字符串统一为unicode，不需要加前缀 u，而以字节存储的str则必须加前缀 b
# 使用from __future__ import unicode_literals将把Python 3.x的unicode规则带入Python 2.7中。
s = 'am I an unicode?'
print("unicode_literals: " + str(isinstance(s, str)))
