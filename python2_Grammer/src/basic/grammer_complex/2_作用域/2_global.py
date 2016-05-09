#coding=utf-8
'''
如果使用外部变量最好使用global关键字
'''

# 最简单的
# def f():
#     a=x
#     print a
# 
# 
# x=1 # x必须在调用之前定义
# f() # 1

# 在其他函数中定义
# def f():
#     global x
#     x= 5
#     print x
# 
# def xx():
#     print x
#     
# f()
# xx() #可以找到x变量