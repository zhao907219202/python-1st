import random
import time

# random 伪随机，是以一个可预测的系统作为基础

print(random.random())  # 返回 0 <= n <= 1 的随机实数
print(random.getrandbits(5))  # 以长整型形式返回n个随机位
print(random.uniform(1, 2))  # 返回 a <= n <= b 的随机实数
print(random.randrange(0, 10, 2))  # 返回range(start,stop,step中的随机数
print(random.choice([1, 2, 3, 4]))  # 从序列seq中返回随意元素
li = [1, 2, 3, 4]
random.shuffle(li)
print(li)  # 原地混乱序列
print(random.sample(li, 2))  # 从序列中选择n个随机且独立的元素

date1 = (2008, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = time.mktime(date1)
date2 = (2009, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = time.mktime(date2)
random_time = random.uniform(time1, time2)
print(time.asctime(time.localtime(random_time)))

num = input("How many dice?")
sides = input("How many sides per die?")
sum = 0
for i in range(int(num)):
    sum += random.randrange(int(sides)) + 1
print("The result is", sum)
