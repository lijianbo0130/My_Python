#coding=utf-8
'''
字符串不是str就是unicode
str和unicode都是basestring的子类
'''
 
s1="aa" # ascii
s2=u"我我"


print isinstance(s1, basestring) # True
print isinstance(s2, basestring) # True

#判断是否为一个字符
print isinstance(s1, basestring)

