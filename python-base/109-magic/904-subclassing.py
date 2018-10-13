class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0

    # 重写__getitem__并非获取用户访问的完全之策，
    # 因为还有其他访问列表内容的途径，比如pop方法
    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)


cl = CounterList(list(range(0, 10)))
print(cl)
x = cl[0]
print(cl.counter)
