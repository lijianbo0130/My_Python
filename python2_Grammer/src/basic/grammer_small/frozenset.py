#coding=utf-8
'''
set是可变的，有add（），remove（）等方法。既然是可变的，所以它不存在哈希值。
frozenset是冻结的集合，它是不可变的，存在哈希值，好处是它可以作为字典的key，
也可以作为其它集合的元素。缺点是一旦创建便不能更改，没有add，remove方法。

'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

