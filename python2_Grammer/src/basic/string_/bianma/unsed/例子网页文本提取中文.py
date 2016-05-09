#coding=utf-8
'''
Created on 2015年3月17日
@author: asus
'''
import urllib2
import re
import time
import jieba

f1=open(r'C:\Users\asus\Desktop\data\2.xml','r')
#read  全部读出来
a=f1.read()
print(a)


# url="http://www.baidu.com"
# html=urllib2.urlopen(url).read()
# print html
html=unicode(a,'utf-8')
word=re.findall(ur"[\u4e00-\u9fa5]+",html)

s=""
for w in word:
    s+=w
     
seg_list=jieba.cut(s,cut_all=False)
fenci="/ ".join(seg_list)
print 'get web-->',s
print 'div result-》',fenci
time.sleep(10)