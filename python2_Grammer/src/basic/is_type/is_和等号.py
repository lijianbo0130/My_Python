#coding=utf-8
'''
==是值是否相等 
is是否是相等的对象
id函数获得对象的内存地址
如果内存地址相等就是同一个对象
(ob1 is ob2) 等价于 (id(ob1) == id(ob2))
'''


a = 1
b = 1.0
print a is b # False
print a == b # True
print id(a) # 两个id不等
print id(b)

# 值相同但是不是同一个对象
L = []
L.append(1)
if L == [1]:  #相同的值
    print 'OK'

# 用is判断不相等
if L is [1]: #相同的对象
    print 'Yay!'
