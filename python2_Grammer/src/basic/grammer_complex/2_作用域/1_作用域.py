#coding=utf-8
'''
Python是基于 LEGB 来进行作用于解析的, 
LEGB 是 Local  函数内部
Enclosing   函数外部的封包函数
Global   全局变量
Built-in 的缩写。
看起来“见文知意”，对吗？实际上，在Python中还有一些需要注意的地方，先看下面一段代码：
'''

'''
案例1
'''
# x = 10
# def foo():
#     #这里会默认为定义一个新的x 所以x这个变量找不到
#     x += 1
#     print x
# 
# foo()

# global 的使用
# x = 10
# def foobar():
#     #这里使用global 把外面的x变量引入
#     global x
#     print x
#     #外界的函数值也被改变
#     x += 1
# foobar()
# print x



'''
案例2
当编译这则代码时，Python碰到给X赋值的语句时认为在这个函数中的任何地方X会被视作一个本地变量名。
但是之后当真正运行这个函数时，执行print语句的时候，赋值语句还没有发生，
这样Python便会报告一个“未定义变量名”的错误。
'''
# x = 99
# b=[0]
# def func():
#     print x
#     x=50
#  
#  
# func()

