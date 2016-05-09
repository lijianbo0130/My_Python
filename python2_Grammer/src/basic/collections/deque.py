#coding=utf-8
'''
Created on 2015年3月19日
@author: asus
'''
import collections as cs

b=cs.deque()
print  b
#末尾加入一个元素
b.append(1)
b.append(2)
print b
#前面插入
b.appendleft(3)
b.appendleft(3)
b.appendleft(3)
print b
#计算出现的次数
print b.count(3) 
#清空
# b.clear()
#长度
print len(b)






