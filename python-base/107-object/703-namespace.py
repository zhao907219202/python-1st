# 此例用于证明类定义语句也可以用于执行
class C:
    print("Class c being defined")


class MemberCounter:
    members = 0

    def init(self):
        MemberCounter.members += 1


m1 = MemberCounter()
m1.init()
print(MemberCounter.members)
m2 = MemberCounter()
m2.init()
print(MemberCounter.members)

# 类作用域中的变量也可以被所有实例访问
print(m1.members, m2.members)
# 重新绑定（类似于局部变量的覆盖屏蔽）
m1.members = "Two"
print(m1.members, m2.members)
