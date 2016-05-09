#coding=utf-8
'''
Created on 2015年3月17日
@author: asus
'''

import urllib2
import re
import time
import jieba


url="http://www.baidu.com"
html=urllib2.urlopen(url).read()
print html
html=unicode(html,'utf-8')
word=re.findall(ur"[\u4e00-\u9fa5]+",html)

s=""
for w in word:
    s+=w
     
seg_list=jieba.cut(s,cut_all=False)
fenci="/ ".join(seg_list)
print 'get web-->',s
print 'div result-》',fenci
time.sleep(10)