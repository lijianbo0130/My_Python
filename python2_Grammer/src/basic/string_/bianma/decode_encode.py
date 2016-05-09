#coding=utf-8
'''
在做编码转换时，
通常需要以unicode作为中间编码，即先将其他编码的字符串解码（decode）成unicode，
再从unicode编码（encode）成另一种编码。 

decode的作用是将其他编码的字符串转换成unicode编码，
如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。 

encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，
表示将unicode编码的字符串str2转换成gb2312编码。 
'''
import chardet

#转成unicode 一般先尝试 utf-8 在尝试 unicode

#转成utf-8
a="我的"
print  chardet.detect(a) 
a = a.decode('utf-8')
print repr(a) #u'\u6211\u7684'


