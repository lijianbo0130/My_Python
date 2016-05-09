#coding=utf-8
'''
出现过的问题
'''

# 如果是数字只存一个 虽然id不同
# a=1
# b=1.0
# print type(a)
# print id(a)
# print id(b)
# print type(b)
# set_t=set()
# set_t.add(a)
# set_t.add(b)
# for i in set_t:
#     print i # 1 只有一个1 虽然类型不一样


# 类的对象就算初始化一样 但是是两个不同的

# class Teacher():
#     def __init__(self,name):
#         self.name = name
#         
# 
# t1=Teacher("a")
# t2=Teacher("a")
# t3=t1
# print t1 is t3 # True
# print t1 is t2 # False
# 
# set_t=set()
# set_t.add(t1)
# set_t.add(t2)
# set_t.add(t3)
# print set_t # 只有两个对象
    
