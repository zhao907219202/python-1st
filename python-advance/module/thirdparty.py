"""
1. 安装第三方库
    Mac或Linux，安装pip本身这个步骤就可以跳过
    Windows，请参考安装Python一节的内容，确保安装时勾选了pip和Add python.exe to Path

    一般来说，第三方库都会在Python官方的pypi.python.org网站注册，
    要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，
    比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：

    # pip install Pillow

2. 模块搜索路径
    默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，
    搜索路径存放在sys模块的path变量中：

    1）直接修改sys.path，添加要搜索的目录：运行时修改，运行结束后失效
    # >>> import sys
    # >>> sys.path.append('/Users/michael/my_py_scripts')

    2）设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到
    模块搜索路径中。设置方式与设置Path环境变量类似。
    注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响

"""