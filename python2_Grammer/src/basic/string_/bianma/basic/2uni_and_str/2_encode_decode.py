#coding=utf-8
'''

decode是解码，把(utf8,gbk2312)编码转换成unicode， 
encode是编码，把unicode转换成(utf8,gbk2312)


字符串在Python内部的表示是unicode编码，因此，在做编码转换时，通常需要以unicode作为中间编码，
即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。
'''


import chardet


'''encode 
unicode=> GBK'''
# u = u'汉' # 
# u = u.encode('GBK') # 转成gbk
# print repr(u)  # '\xba\xba'
# print chardet.detect(u)# TIS-620 GBK的一种
# 
# u = u'汉' # 
# u = u.encode('UTF-8') # 转成gbk
# print repr(u)  # '\xba\xba'
# print chardet.detect(u)# windows-1252 UTF-8的一种


'''
decode 
utf-8=>unicode
'''
u="我我我"
print chardet.detect(u)
print repr(u) # '\xe6\xb1\x89'
print isinstance(u, str) # True
u = u.decode('UTF-8')
print repr(u) # u'\u6c49'
print isinstance(u, unicode)# True
print u 









