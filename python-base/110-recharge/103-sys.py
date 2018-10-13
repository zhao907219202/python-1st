import sys
import os

print(sys.argv)  # sys.argv 包括传递到Python解释器的参数，包括脚本名称
# sys.exit 可以退出当前程序，如果在try/finally 块中调用，finally子句的内容仍然会执行

print(sys.modules)  # 将模块名映射到实际存在的模块上，它只应用于目前导入的模块
print(sys.platform)  # 正在运行的平台名称

print(os.environ)  # 映射环境变量
print(os.environ['PYTHONPATH'])

# os.system("redis-server") 执行操作系统命令
print(os.sep)  # 用于路径的分隔符
print(os.pathsep)  # 用于分隔路径名
print(os.linesep)  # 用于文本文件的字符串分隔符
