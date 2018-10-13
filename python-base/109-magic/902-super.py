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
        # Bird.__init__(self) 使用未绑定的超类构造方法
        # 使用super函数 python3 可以不传参给super直接调用
        super(SongBird, self).__init__()
        self.sound = "Squawk"

    def sing(self):
        print(self.sound)


sb = SongBird()
sb.sing()
sb.eat()
