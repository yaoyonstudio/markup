"""
模块制作
"""
# 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。

# 模块中存在的类型
# 类/函数/全局变量/局部变量

# 模块中希望被引用的部分
# 只针对 from...import*有效
# 添加__all__=['函数名或者全局变量名或者类名']
# 若无限定，则全部可被引用


# 测试模块
# 只在本模块中使用，不被外部引用
# 添加if __name__ == '__main__':测试主函数名(参数）
# 若无判断条件，则不仅在本类中运行，被引用时也会运行


"""
模块引用
"""
# import ...
# 需要把命令放置顶端
# 一个模块只会被导入一次
# 导入模块的所有信息
# 调用格式
# 模块名.函数名 / 模块名.类名 / 模块名.全局变量名


# from ... import ...
# 如果只想导入模块的一个变量或者函数或者类
# 格式：from 模块名 import 全局变量名/函数名/类名
# 调用格式
# 函数名/类名/全局变量名
# 通过这种方式引入，调用函数时只能给出函数名，不能给出模块名，
# 当两个模块中含有相同名称函数的时候，后面一次引入会覆盖前一次引入。


# from ... import *
# 导入一个模块中的所有项目。
# 调用格式
# 函数名/类名/全局变量名


# from ... import ...as 新名字
# 为了防止和本模块中的名字冲突

# 导入模块时的查询定位
# 导入一个模块，Python解析器对模块位置的搜索顺序是：
# 1、当前目录
# 2、如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。
# 3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/
# 4、模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。


"""
包的制作
"""
# 包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
# 由__init__.py和其他模块构成的文件夹

# __init__.py：默认空白
# python3中此文件可删除，python2中不可删除
# 可添加添加__all__=['模块名']，确定可被引用的模块，只针对 from...import*有效


"""
包的引用
"""

# import ...

# from ... import ...

# from ... import *

