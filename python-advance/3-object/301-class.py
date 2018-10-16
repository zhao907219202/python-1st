"""
1. __init__
    1)__init__方法的第一个参数永远是self，表示创建的实例本身，在__init__方法内部，
    可以把各种属性绑定到self，因为self就指向创建的实例本身。

    2)有了__init__方法，在创建实例的时候，就不能传入空的参数了，
    必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去

2. 访问限制
    1）要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名
    如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

    2) 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
    所以，仍然可以通过_Student__name来访问__name变量

    3）注意： 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
    特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名

3. 错误写法
    # >>> bart = Student('Bart Simpson', 59)
    # >>> bart.get_name()
    # 'Bart Simpson'
    # >>> bart.__name = 'New Name' # 设置__name变量！
    # >>> bart.__name
    # 'New Name'

    表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
    内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量

    # >>> bart.get_name() # get_name()内部返回self.__name
    # 'Bart Simpson'
"""


class Student(object):
    count = 0

    def __init__(self, name, score):
        self.__name = name;
        self.__score = score;
        Student.count += 1

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score


bart = Student("Bart Simpson", 59)
lisa = Student("Lisa Simpson", 87)

print("bart.name =", bart.get_name())
print("bart.score =", bart.get_score())
bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())

print("student count:", Student.count)
