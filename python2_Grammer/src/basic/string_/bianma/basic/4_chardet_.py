#coding=utf-8
'''

confidence，是置信度，就是有80%多的概率，它是一个Utf8编码
判断 字符编码要下载 chardet库   chardet.detect(str1)

经常不准不建议使用
'''
import chardet
#用法
s="a"
print  chardet.detect(s)  # 打印编码格式
