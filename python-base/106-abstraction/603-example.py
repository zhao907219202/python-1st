# 为什么我想要修改参数
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def look_up(data, label, name):
    return data[label].get(name)


def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = look_up(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


MyNames = dict({})
init(MyNames)
store(MyNames, "Fred Yu")
print(look_up(MyNames, "first", 'Fred'))

store(MyNames, "Wang Li Kun")
print(look_up(MyNames, "middle", "Li"))
