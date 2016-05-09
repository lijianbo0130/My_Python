#coding=utf-8
'''
Created on 2015年8月26日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

import urllib2

# 构造request对象
request = urllib2.Request("http://www.baidu.com")
# 得到response对象
response = urllib2.urlopen(request)
print response.read()