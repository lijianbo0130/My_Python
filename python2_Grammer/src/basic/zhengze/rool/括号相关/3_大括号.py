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
{m} 表示汽配前一个字符m词
{m,n}表示匹配前一个字符m至n词
'''

# 匹配a出现4次后面接b
# sen='''aaabaaaab'''
# lis=re.findall("a{4}b", sen) # 
# print lis # ['aaaab']

# 匹配a出现3次或4次后面接b
# sen='''aaabaaaab'''
# lis=re.findall("a{3,4}b", sen) # 
# print lis #['aaab', 'aaaab']

# 如果为{n,m} 默认的按大的匹配 贪婪模式
# sen='''aaaab'''
# lis=re.findall("a{3,5}b", sen) # 
# print lis #['aaaab']

# n个以上
# 如果为{n,} 默认的按大的匹配 贪婪模式
# sen='''aaaab'''
# lis=re.findall("a{3,5}b", sen) # 
# print lis #['aaaab']

