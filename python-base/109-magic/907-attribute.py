class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    # 当试图给特性name赋值时被自动调用
    # 涉及的特性不是size时该方法也会被调用，
    # 为了避免死循环（该方法再次被调用），使用__dict__进行赋值
    def __setattr__(self, name, value):
        if name == "size":
            self.width, self.height = value

        else:
            self.__dict__[name] = value

    # 当特性name被访问且对象没有相应的特性时被自动调用
    def __getattr__(self, name):
        if name == "size":
            return self.width, self.height
        else:
            raise AttributeError

# __getattribute__(self,name) 当特性name被访问时自动被调用
# 死循环：getattribute 会拦截所有特性的访问，也拦截__dict__的访问，
# 访问__getattribute__中与self相关的特性时，使用超类的__getattribute__方法（super函数）是唯一安全的途径

# __delattr__(self,name) 删除时自动被调用
