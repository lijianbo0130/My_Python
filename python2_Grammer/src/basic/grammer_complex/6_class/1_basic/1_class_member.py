#coding=utf-8
'''
给成员变量赋值
'''

class Peo():
    s="123"
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        # 可以这样调用
        self.dd=self.sex
        
# 实例对象调用
s=Peo(1,2,3)
print s.age
print s.dd

# 类直接调用
# print Peo().age# 会报错因为没有初始化
print Peo(1,2,3).age

#是否可以不会成员赋值  不可以
# class Peoo():
#     s="123"
#     def __init__(self):
#         self.name
#         
# 
# s=Peoo()
# s.name="bb"
# print s.name