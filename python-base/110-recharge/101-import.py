# 导入模块的时候，会有新文件产生，后缀为.pyc，如果稍后导入同一个模块，
# Python 会导入.pyc文件而不是.py文件，除非 .py文件已改变
# 导入并不意味着执行某些操作，他们主要用于定义，比如变量、函数，所以只需要定义一次，导入多次和导入一次是一样的

import sys
import pprint
import imported

pprint.pprint(sys.path)

# 你不需要使用 PYTHON_PATH(环境变量)来更改sys.path
# 路径配置文件(扩展名.pth)可以实现，为了执行路径配置文件，
# 需要将其放置在可以找到的地方

# import drawing                # 包名
# import drawing.colors         # 模块名，必须用全名使用
# from drawing import shaped    # 可以用短名
