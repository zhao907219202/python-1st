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


"""

import os

print(os.path.isdir(r'/data/resource/python'))
print(os.path.isfile(r'/data/resource/python/test.txt'))
