#coding=utf-8
'''
Created on 2015年5月15日
@author: Administrator
'''
import re

# # 数字提取
# s1="30cac0040"
# # 取出最后两位的数字  
# match=re.search("\d\d$", s1)
# print match.group()
# # 取出最后三位的数字  
# match=re.search("\d{3}$", s1)
# print match.group()
# # 取出最后的所有数字
# match=re.search("\d+$", s1)
# print match.group()


# # 统一空格数量  变成"a b c d"
# a="a   b c  d"
# p = re.compile("\s+") 
# date = p.sub(' ', a)
# print date

#判断s是否由纯数字组成
# s1="12345678"
# s2="123s45678"
# m=re.match("\d+", s1)
# if m is not None:
#     print "是数字"
# 
# m=re.match("^\d+$", s2)
# if m is not None:
#     print m.group()




