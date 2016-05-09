#coding=utf-8
'''
python 默认的是贪婪 
当有一个或者多个的时候
默认匹配最多
如果不需要贪婪 比如 :
(李健博)是(李健博)  希望提取两个()中的就能不能使用贪婪模式
用贪婪的话第一个(和最后一个)匹配
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import re

# 非贪婪 在*或者+后面加一个? 一般为在+后面用 因为在*后面使用任何东西都能匹配中0次
lis=re.findall("\d+?", "1s11s6")
print lis  # ['1', '1', '1', '6']

# 贪婪
# lis=re.findall("\d+", "1s11s6")
# print lis  # ['1', '11', '6']

# 常用小括号非贪婪
lis=re.findall(u"\(.*?\)", ur"(123)dd(8896)()(")
print lis  # [u'(123)', u'(8896)', u'()']