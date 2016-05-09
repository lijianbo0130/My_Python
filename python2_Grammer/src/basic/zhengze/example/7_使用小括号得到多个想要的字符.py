#coding=utf-8
'''
Created on 2015年8月26日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

'''
要把content里面的 两队中文找到
'''
content='''
<a>我的1</a>
<b>你的</b>
<a>我的2</a>
<b>你的</b>
'''
import re
# 加了.*? ?表示非贪婪模式
pattern = re.compile('<a>(.*?)</a>.*?<b>(.*?)</b>',re.S)
items = re.findall(pattern,content)
for item in items:
    print item[0],item[1]

