#coding=utf-8
'''
ascii utf-8 unicode 都是str
'''

#默认的是ascii
a="我我"
print repr(a) #'\xe6\x88\x91\xe6\x88\x91'
print len(a) # 6
a="a"
print repr(a) #'\xe6\x88\x91\xe6\x88\x91'
b=u""
if a==b:
    print True
    
    
#汉字
print repr(a) #'\xe6\x88\x91\xe6\x88\x91'