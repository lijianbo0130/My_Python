#coding=utf-8
'''
Created on 2015年6月3日
@author: Administrator
'''

#返回一个list 但是迭代的时候才生成
# def f(lis):
#     for num in lis:
#         yield num
# 
# lis=[1,2,3,4]
# 
# 
# for num in f(lis):
#     print num, #1 2 3 4

#不能和return 同时使用
# def f(lis):
#     for num in lis:
#         yield num
#     return "s"
#  
# lis=[1,2,3,4]
# gen,s=f(lis)
# print gen,s

