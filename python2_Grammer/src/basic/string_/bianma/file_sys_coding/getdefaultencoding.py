#coding=utf-8
'''
Created on 2015年6月3日
@author: Administrator
'''

import sys
import chardet
#得到系统当前编码  
print sys.getdefaultencoding() #系统的默认编码为ascii 但是有coding=utf-8 就变成了utf-8
a="我我我"
print chardet.detect(a) #utf-8

