#coding=utf-8
'''
实现类的一个方法
'''
class PEO():
    # 静态变量
    s="aaa"
    def __init__(self,name):# 初始化方法
        self.Name = name

    #自己的方法      
    def speak(self):
        print "my name" + self.Name
    
    def change_name(self):
        self.Name="aaa"
    

zhangsan=PEO("zhangsan")
zhangsan.speak()

#也可以直接调用
PEO("ss").speak()
#
print PEO.s
# 不初始化实例不能调用方法
# peo.change_name()
# peo.speak()




    