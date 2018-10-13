try:
    1 / 1
except NameError:
    print("Unknown variable")
else:
    print("That went well")
finally:
    print("Cleaning up..")


def describe_person(person):
    print("Description of ", person['name'])
    print("Age:", person['age'])
    try:
        # 这里使用加号而不是逗号，否则字符串'Occupation'在异常引发之前就会被输出
        print("Occupation:" + person['ocupation'])
    except KeyError:
        pass


describe_person({'name': "Fred", 'age': 24})
