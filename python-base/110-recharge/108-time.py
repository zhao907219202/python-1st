import time

time_tuple = (2018, 1, 25, 15, 5, 14, 3, 25, 0)
print(time.asctime())
print(time.localtime(time.time()))  # 本地时间
print(time.gmtime())  # 世界时间
print(time.mktime(time_tuple))  # 时间元组转时间戳
# time.sleep(1)            # 线程休眠
print(time.time())  # 打印时间戳
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 把时间数组格式化
print(time.strptime("2018-01-25 15:17:12", "%Y-%m-%d %H:%M:%S"))  # 根据格式化的字符串转换为时间数组
