#coding=utf-8
'''
这里探讨is None 和== None

Comparisons to singletons like None should always be done 
with 'is' or 'is not', never the equality operators
用is 而不要用=
'''


# 例子1
class Foo:
    def __eq__(self,x):
        return True
foo1=Foo()
foo2=Foo()
print foo1

#这里的None表示 foo1里面没有数据
print foo1==None
# True
 
print foo1 is None 
# False

if foo1==foo2:
    print True #True

if foo1 is foo2:
    print True #flase



# class Zero(): # a class that is zero
#     def __nonzero__(self):
#         return False
# 
# class Len0(): # a class with zero length
#     def __len__(self):
#         return 0
# 
# class Equal(): # a class that is equal to everything
#     def __eq__(self, other):
#         return True
# 
# stuff = [None, False, 0, 0L, 0.0, 0j, 
#          (), [], {}, set(), '', float('NaN'), float('inf'), 
#          Zero(), Len0(), Equal()]
# 
# for x in stuff:
#     if x is None: print " %r is None " % x
#     if x==None: print " %r == None " % x

#  None is None 
#  None == None 


