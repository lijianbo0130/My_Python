#coding=utf-8
'''
在 python 中，字符串本身是不可修改的。
如果函数修改字符串，那么都是生成会返回一个新的字符串对象。
'''

s="a"
print id(s)
print id("a") # 5227392
print id(s+"s") # 36133608 生成了一个新的对象
