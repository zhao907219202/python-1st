import shelve

# Python3 数据处理模块shelve会自动为文件添加扩展名
s = shelve.open("./file/test")
s['x'] = ["a", "b", "c"]
s['x'].append("d")
print(s['x'])

# 存储的d到哪里去了呢？其实很简单，d没有写回，你把['a', 'b', 'c']存到了x，当你再次读取s['x']的时候，
# s['x']只是一个拷贝，而你没有将拷贝写回，所以当你再次读取s['x']的时候，它又从源中读取了一个拷贝，
# 所以，你新修改的内容并不会出现在拷贝中，解决的办法就是，第一个是利用一个缓存的变量，如下所示

temp = s['x']
temp.append("d")
s['x'] = temp
print(s['x'])

# 除了上面说的方法，可以把open函数的 writeback 参数设为true
