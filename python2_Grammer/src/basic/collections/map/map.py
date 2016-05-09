#coding=utf-8
'''
对整个列表进行操作
不改变原来的列表
对可迭代函数'iterable'中的每一个元素应用‘function’方法，将结果作为list返回。 
'''

#基本  把s中所有的数加10
# s=[1,2,3,4,5,6]
# b=map(lambda x:x+10, s)
# print s #[1, 2, 3, 4, 5, 6]
# print b #[11, 12, 13, 14, 15, 16]

#提高
# b=map(pow, [1,2],[2,3])
# print b #1**2 2**3

#多个参数
l1 = [1,2,3] 
l2 = [4,5,6] 
l3 = [7,8,9] 
a=map(lambda x,y,z:x+y+z,l1,l2,l3) 
print a






