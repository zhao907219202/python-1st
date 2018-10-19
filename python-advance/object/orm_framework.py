"""
元类应用 —— orm 框架
    1. 当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass，如果没有找到，
    就继续在父类Model中查找metaclass，找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类，
    也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。

    2. 在ModelMetaclass中，一共做了几件事情：
        1) 排除掉对Model类的修改；
        2) 在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，
            同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性），也就是说只有当实
            例中属性不存在时才会调用getattr，从而返回dict中的value，否则是直接返回Field实例对象的
        3) 把表名保存到__table__中，这里简化为表名默认为类名。

    3. 在Model类中，就可以定义各种操作数据库的方法，比如save()，delete()，find()，update等等。
    我们实现了save()方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句。
"""


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s,%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    """
    1. 定义类的属性到列的映射：
    2. 类定义后，即使不创建对象，也会打印出metaclass中的found语句
        # Found model: User
        # Found mapping: id ==> <IntegerField,id>
        # Found mapping: name ==> <StringField,username>
        # Found mapping: email ==> <StringField,email>
        # Found mapping: password ==> <StringField,password>
    """
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


print()
# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
