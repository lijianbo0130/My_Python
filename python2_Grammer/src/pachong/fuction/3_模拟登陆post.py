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
import urllib

values = {"username":"lijianbo0130@qq.com","password":"85640890"}
data = urllib.urlencode(values) 
urlmy="http://passport.csdn.net/account/login;jsessionid=CEC6D294A7F907A24F2781E0CA4A866F.tomcat1?from=http://my.csdn.net/my/mycsdn"
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(urlmy,data)
response = urllib2.urlopen(request)
print response.read()
