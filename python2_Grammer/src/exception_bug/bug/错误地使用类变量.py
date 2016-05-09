#coding=utf-8
'''
在Python中，类变量在内部当做字典来处理，
其遵循常被引用的方法解析顺序（MRO）。
所以在上面的代码中，由于class C中的x属性没有找到，
它会向上找它的基类（尽管Python支持多重继承，但上面的例子中只有A）。
换句话说，class C中没有它自己的x属性，其独立于A。因此，C.x事实上是A.x的引用。
'''
class A(object):
    x = 1

class B(A):
    pass

class C(A):
    pass

print A.x, B.x, C.x # 1 1 1
B.x = 2
print A.x, B.x, C.x # 1 2 1
#我们只改了A.x，为什么C.x也改了
A.x = 3
print A.x, B.x, C.x # 3 2 3
