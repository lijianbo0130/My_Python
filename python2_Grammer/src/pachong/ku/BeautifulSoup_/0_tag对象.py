#coding=utf-8
'''
Created on 2015年8月26日
@author: Administrator
'''
from __future__ import  division
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 创建 beautifulsoup 对象
soup = BeautifulSoup(html)
# 格式化输出 整个soup对象
# print soup.prettify()

'''
tag对象  HTML 中的一个个标签 打印出一个同名的标签
'''
# print  soup.title #<title>The Dormouse's story</title>
# print soup.head #<head><title>The Dormouse's story</title></head>
# print soup.a # <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
# print soup.p  # <p class="title" name="dromouse"><b>The Dormouse's story</b></p>

'''
对于 Tag，它有两个重要的属性  name 和 attrs
soup 对象本身比较特殊，它的 name 即为 [document]，
对于其他内部标签，输出的值便为标签本身的名称。
'''
# print soup.name #[document]
# print soup.head.name # head

'''
attrs
在这里，我们把 p 标签的所有属性打印输出了出来，
得到的类型是一个字典
'''
print soup.p.attrs
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# {u'class': [u'title'], u'name': u'dromouse'}

'''
NavigableString
获取标签内部的文字
用 .string 
'''
print soup.p
print  soup.p.string
