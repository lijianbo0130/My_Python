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


# 找到4个及其以上的空格
lis=re.findall(u" {4,}", ur"    a  a       ")
print lis  # [u'    ', u'       ']

