from random import choice

x = choice(["Hello,world!", [1, 2, 'e', 'e', 4]])
print(x.count('e'))

# 使用新类 或者 指定类的子类为object 效果一致
# python3 中默认继承object 所以都是新类
_metaclass_ = type


class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello,world! I am %s." % self.name)


foo = Person()
bar = Person()
foo.set_name("Luke SkyWalker")
bar.set_name("Ain SkyWalker")
foo.greet()
bar.greet()

bar.name = "Yoda"
bar.greet()


class Class:
    def method(self):
        print("I have a self")


def func():
    print("I don't have a self")


instance = Class()
instance.method()
instance.method = func
instance.method()


class Bird:
    song = "Squawk"

    def sing(self):
        print(self.song)


bird = Bird()
bird.sing()

bird_song = bird.sing
bird_song()
