from __future__ import division
import math

print("Hello,world!")
# 求类型
print(type(4))
# 取绝对值
print(abs(1.2))
# 四舍五入
print(round(2.2365, 2))
# 幂函数
print(pow(2, 4))
# 取整
print(math.floor(3.2))
# 开放
print(math.sqrt(4))

# python3 已优化 不再做整除
# python2会进行整除 import division 不会整除
print(2 / 5)
print(10 / 3)
print(5 // 2)
# 返回商和余数
print(divmod(5, 2))
