class MyClass:
    @staticmethod
    def smeth():
        print("This is a static method")

    # smeth = staticmethod(smeth)
    # 手动包装比较麻烦，使用装饰器更加便捷

    @classmethod
    def cmeth(cls):
        print("This is a class method of ", cls)
    # cmeth = classmethod(cmeth)


MyClass.smeth()
MyClass.cmeth()
