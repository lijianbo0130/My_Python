#coding=gb2312
'''
#coding=gb2312 ��ʾ���ǵ�ǰ�ļ��ı����ʽ
'''

import chardet
s='�ְ�'
print  chardet.detect(s)   # windows-1252 ΪGBK��һ��
#תunicode
s = s.decode('GBK')
print repr(s) # u'\u7238\u7238'
print s
s = s.encode('utf-8')
#תutf-8
print s
print  chardet.detect(s) 
