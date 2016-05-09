#coding=utf-8
'''
Created on 2015年8月4日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import re

'''
.表示的是任意字符 如果想找到字符串中的. 就需要转意字符
转意符号 \.
'''


# 错误的用法 加r没有用 r对\n\t才有用  希望的输出是a.w
# s="aaa.waasw"
# lis=re.findall(r"a.w", s)
# print lis # ['a.w', 'asw']


# 正确的用法 希望的输出是a.w
# s="aaa.waasw"
# lis=re.findall(r"a\.w", s)
# print lis # ['a.w']

# 想要匹配\
s="aaa\waasw"
s="\\\\"
print s
print s
lis=re.findall(r"\\", s)
print lis # 


# #[*]
# s="[img:01-02-2015050720-nqMRz2]"
# lis=re.findall("\[.*\]", s)
# print lis
# 
# #【*】
# s=u"【img:01-02-2015050720-nqMRz2】"
# lis=re.findall(u"\【.*\】", s)
# print lis


# replacedStr = re.sub(u"\[.*\]", " ", s)
# print replacedStr+"aa"
