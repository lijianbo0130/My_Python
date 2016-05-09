#coding=utf-8
'''
Created on 2015年11月3日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


# 等号是指向同一个对象。一个改变两个都变了。
# a=[1,2,3]
# b=a
# a[1]=5
# print b

# 带了：就是深拷贝了是两个不同的对象了
# a=[1,2,3]
# b=a[:]
# a[1]=5
# print b

# 单个:全部拷贝 是新对象 a的改变不会改变b
# a=[1,2,3]
# b=a[:]
# a[1]=5
# print b # [1, 2, 3]

# 带有数字相当于把某一部分替换
# a=[1,2]
# # 在前面插入
# a[:1]=[3,3,3]# 和a[0:1]效果是一样的
# print a # [3, 3, 3, 2] 会把1替换掉

# 数字的意思
a=[1,2,3]
print a[0:] # [1, 2, 3]
print a[1:2] # [2] 第二个元素 下标为1的元素
print a[-1:] # [3] 从最后一个元素向后
print a[3:] # 第三个元素向后 为空集合 []
a[1:]=[2,3]
print a #[1,2,3]
print a[0]
print a[1:]
a[1:3]=[2,3]
print a



