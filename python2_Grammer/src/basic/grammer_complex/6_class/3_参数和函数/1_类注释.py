#coding=utf-8
'''
使用类注释
'''
class peo:
    #下面是类的__doc__注释 '''''', 和'' ,''''都行
    '''get c2c'''
    def __init__(self,name):
        self.Name = name
        
p=peo("ss")
print p.__doc__# get c2c

#     #__str__()这个方法告诉python在打印(print)一个对象时,具体显示什么内容
#     def __str__(self):
#         msg='my name is: ' +self.Name
#         return msg
# 
# zhangsan=peo("zhangsan")
# print zhangsan




    