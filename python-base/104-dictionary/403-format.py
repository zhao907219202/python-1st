phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# 利用字典进行格式化 %(key)s
description = "Cecil's phone number is %(Cecil)s" % (phonebook)
print(description)

template = '''<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>
'''
data = {'title': 'My Home Page', 'text': 'Welcome to my home page'}
print(template % data)
