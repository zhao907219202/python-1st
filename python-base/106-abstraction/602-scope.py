def try_to_change(n):
    n = "Mr Fred"


def change(n):
    n[0] = 'Mr Gumby'


name = "Mrs Carrie"
try_to_change(name)
print(name)

names = ["Mr Fred", "Mrs Skler"]
change(names)
print(names)

n = names[:]
print(n is names)  # False
print(n == names)  # True




