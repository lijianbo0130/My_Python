#coding=utf-8
'''
Created on 2015年3月19日
@author: asus
'''

# sort
# L.sort(cmp=None, key=None, reverse=False) 排序


# (1)
# cmp 接受一个函数，定义比较规则函数
# def f(a,b):
#     return a-b  # 函数返回大于0 表示按 a,b排序
# l=[1,2,9,8,5]
# l.sort(cmp=f, key=None, reverse=False)
# print l # [1, 2, 5, 8, 9]

# 如果有小数
# def f(a,b):
#     if a-b>0:
#         return 1
#     else:
#         return -1
#     return a-b  # 函数返回大于0 表示按 a,b排序
# l=[1.1,2.1,0.1]
# l.sort(cmp=f, key=None, reverse=False)
# print l # [0.1, 1.1, 2.1]

# (2) 
# key 定义排序的数据
# l=["a","aasss","aaa"]
# l.sort(key=len)# 用数据的长度来排列
# print l # ['a', 'aaa', 'aasss']

# (3)
# reverse  一般默认的是升序  reverse 设置是否反过来排列
# l=[1,2,9,8,5]
# l.sort(reverse=True)
# print l


# sorted函数
# sorted函数是内建函数，他接受一个序列，返回有序的副本
# 他与sort的唯一区别就是会返回副本
# 第一个是要被排序的对象
# b=sorted(students, key=lambda student : student[2],reverse=False) 









