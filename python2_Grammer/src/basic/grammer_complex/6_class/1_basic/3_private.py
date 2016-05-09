#coding=utf-8
'''
public：public表明该数据成员、成员函数是对所有用户开放的，所有用户都可以直接进行调用 

private：private表示私有，
私有的意思就是除了class自己之外，
任何人都不可以直接使用，私有财产神圣不可侵犯嘛，
即便是子女，朋友，都不可以使用。 
出了类的定义的范围就不能使用

     3、protected：protected对于子女、朋友来说，就是public的，可以自由使用，没有任何限制，而对于其他的外部class，protected就变成private。 
'''
class Father():
    def __init__(self,money,my_chilrd,my_own):
        self.money = money
        self._my_chilrd = my_chilrd
        self.__my_own = my_own
        
class Child(Father):
    
    def say(self):
        print self.__my_own# 在子类中也无法使用__my_own


f=Father(1,2,3)
print f._my_chilrd
# print f.__my_own # 出异常

c=Child(1,2,3)
# c.say() 异常