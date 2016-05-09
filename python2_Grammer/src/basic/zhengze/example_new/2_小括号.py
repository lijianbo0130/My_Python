# coding=utf-8
'''
Created on 2016年4月11日
@author: 李健博
程序作用：

'''
from __future__ import division
from __future__ import unicode_literals

import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

# 常用小括号非贪婪 .*?表示非贪婪
lis=re.findall(u"\(.*?\)", ur"(123)dd(8896)()(")
print lis  # [u'(123)', u'(8896)', u'()']
 
# 中文括号
pattern=re.compile(u"（.*?）")