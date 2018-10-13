class FooBar:
    def __init__(self):  # 构造方法
        self.some_var = 42


# python还有一个析构方法 __del__,尽力避免使用该方法
f = FooBar()
print(f.some_var)


class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("Aaaah...")
            self.hungry = False
        else:
            print("No,thanks")


class SongBird(Bird):
    def __init__(self):
        self.sound = "Squawk"

    def sing(self):
        print(self.sound)


sb = SongBird()
sb.sing()
# sb.eat() AttributeError: 'SongBird' object has no attribute 'hungry'
