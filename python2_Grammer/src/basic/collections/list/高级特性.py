#coding=utf-8
'''
把列表中所有的元素相加
'''
def sumtree(L):
    tot=0
    for x in L:
        if not isinstance(x,list):
            tot=tot+x
        else:
            tot=tot+sumtree(x)
    return tot

b=sumtree([1,3,4,5,[4,5,6,8,7,[8,9]]])
print b
