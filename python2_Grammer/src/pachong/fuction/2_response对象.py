#coding=utf-8
'''
Created on 2015年8月26日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


import urllib
url=r"http://tu.duowan.com/m/bxgif/"

# 得到response对象
web_obj = urllib.urlopen(url)

# response对象有一个read方法，可以返回获取到的网页内容 再次读取为空
# print web_obj.read()

#得到返回码
print web_obj.code
#返回头信息
print web_obj.headers
print web_obj.headers.values()