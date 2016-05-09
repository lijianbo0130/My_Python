#coding=utf-8
'''
#coding=utf-8  表示的是用什么格式对当前文件(指的是写代码的这个文件)进行编码  
相当于property里面的  text file coding
'''



import chardet
#设置了 coding=utf-8
a="我我我"
print chardet.detect(a) #utf-8

a="a"
print chardet.detect(a) #utf-8
