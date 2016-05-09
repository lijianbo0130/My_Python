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
import urllib2  

url = 'http://www.zhihu.com/#signin'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'  
values = {'username' : '307508861@qq.com',  'password' : '85640890' }  
headers = { 'User-Agent' : user_agent ,
           'Referer':'http://www.zhihu.com/articles'}  
data = urllib.urlencode(values)  
request = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(request)  
page = response.read() 