#coding=utf-8
'''
Created on 2015年6月11日
@author: Administrator
'''
from __future__ import  division


#  replace() 方法把字符串中的 old（旧字符串） 
# 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
# str.replace(old, new[, max])
# 参数
# old -- 将被替换的子字符串。
# new -- 新字符串，用于替换old子字符串。
# max -- 可选字符串, 替换不超过 max 次


#实例
str1 = "is is is is";
str2= str1.replace("is", "was"); # was was was was
print str2
str3= str1.replace("is", "was", 3); # was was was is
print str3


