class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


# 父类Filter
class SPAM_Filter(Filter):
    def init(self):
        self.blocked = ['SPAM']


s = SPAM_Filter()
s.init()
l = s.filter(['SPAM', "SPAM", 'eggs', "bacon", 'SPAM'])
print(l)

print(issubclass(SPAM_Filter, Filter))
print(SPAM_Filter.__bases__)
print(isinstance(SPAM_Filter(), Filter))
# 查看class属性
print(SPAM_Filter().__class__)
print()


# -------多继承-------
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print("Hi,my value is", self.value)


class TalkingCalculator(Calculator, Talker):
    pass


tc = TalkingCalculator()
tc.calculate('1+2+3')
tc.talk()

# 如果两个超类具有相同名字的两个不同方法：
# 在class语句中，先继承的类中的方法会重写后继承的类中的方法。
# 如果超类们共享一个超类，那么在查找给定方法或者特性时访问超
# 类的顺序（MRO，Method Resolution Order）所使用的十分复杂，不需过多关系
print(hasattr(tc, 'talk'))
print(callable(getattr(tc, 'talk')))
setattr(tc, 'name', 'Mr Fred')
print(tc.name)
# 查看对象内所有存储的值
print(tc.__dict__)
