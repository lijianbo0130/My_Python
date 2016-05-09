#coding=utf-8
'''
按目标字符来切分
传统的split不能使用正则表达式
'''
import re

# 按照.!%进行分割 
'''
注意如果符号在最后或者在最前都会分出一个""
通过正则表达式将字符串分离。
如果用括号将正则表达式括起来，那么匹配的字符串也会被列入到list中返回。
''' 

# 分割的字符串不要
# s="a.a!ffff%"
# re_han = re.compile(ur"[.!%]", re.U)
# b=re_han.split(s)
# '''
# 同时.!这些符号都被去掉了
# 注意如果符号在最后或者在最前都会分出一个""
# '''
# print b # ['a', 'a', 'ffff', '']

# 留下分割的字符串 加一个()
# s="a.a!ffff%"
# re_han = re.compile(ur"([.!%])", re.U)
# b=re_han.split(s)
# print b # ['a', '.', 'a', '!', 'ffff', '%', '']
'''
同时.!这些符号都被去掉了
注意如果符号在最后或者在最前都会分出一个""
'''


#多个h分割  用正则
sp=re.compile(u"(?:h+)", re.U)
a = u'hahhhahaaah'
b=sp.split(a)
print b # [u'', u'a', u'a', u'aaa', u'']  前后都为""


#多个中文拆分
# re_han = re.compile(ur"([\u4E00-\u9FA5]+)", re.U)# 如果用括号将正则表达式括起来
# a=u"aa我来到北aa京清华大学aa我来到北aa京清华大学aa我来到北aa京清华大学"
# blocks = re_han.split(a)
# for i in blocks:
#     print i

#只返回中文
# for word in blocks:
#     if re_han.match(word):
#         print word
    
    


#加了r  \t \就不修饰t了 所以不能加
# b='\xe5\xa4\xa7\xe5\xb6\x9d\xe5\xb2\x9b\t118.336702\t24.562202\t0:00\t24:00\t4H'
# b=b.split(r"\t")
# print b






   


    
