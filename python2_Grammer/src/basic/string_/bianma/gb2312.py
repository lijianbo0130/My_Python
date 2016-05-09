#coding=gb2312
'''
#coding=gb2312 表示的是当前文件的编码格式
'''

import chardet
s='爸爸'
print  chardet.detect(s)   # windows-1252 为GBK的一种
#转unicode
s = s.decode('GBK')
print repr(s) # u'\u7238\u7238'
print s
s = s.encode('utf-8')
#转utf-8
print s
print  chardet.detect(s) 
