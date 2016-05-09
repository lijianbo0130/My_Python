#coding=utf-8
'''
浅复制
对于不可变对象和可变对象来说，浅复制都是复制的引用，
只是因为复制不变对象和复制不变对象的引用是等效的（因为对象不可变，当改变时会新建对象重新赋值）。
所以看起来浅复制只复制不可变对象（整数，实数，字符串等），
对于可变对象，浅复制其实是创建了一个对于该对象的引用，
也就是说只是给同一个对象贴上了另一个标签而已。

浅复制的常见使用场景
(1)完全切片操作[:],
(2)利用工厂函数,比如 list(),dict()等,
(3)使用 copy 模块的 copy 函数.

不能copy的有:
class,lis,dict,set,tuple

问题：
但是这些a和b对象的元素的引用是同一个的时候，
所以a或者b更改了它的对象的元素就会影响到另外一个的值
'''

import copy
# a=[1,2,3]
# b=a # b的改变会影响a
# 
# b=copy.copy(a)
# print b is a # Flase b的改变不会影响a a,b为不同对象

# 问题
# a=[1,[2,3],4]
# b=copy.copy(a)
# # a[1]=5# 这样不会影响b 只是生成了一个5对象 然后a[1]指向它
# a[1][0]=3# 这样会影响 b
# print b















