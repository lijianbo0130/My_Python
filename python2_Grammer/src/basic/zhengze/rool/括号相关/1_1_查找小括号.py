# coding=utf-8
'''
Created on 2016年4月11日
@author: 李健博
程序作用：
使用转意字符才能查找小括号
'''
from __future__ import division
from __future__ import unicode_literals

import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


# 常用小括号非贪婪
lis=re.findall(u"\(\)", ur"()aaaa()")
print lis  # [u'()', u'()']