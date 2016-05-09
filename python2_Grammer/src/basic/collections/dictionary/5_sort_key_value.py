#coding=utf-8
'''
Created on 2015年7月17日
@author: Administrator
'''
from __future__ import  division

def sorted_key1(dic):
    '''
    返回按key升序排序的lis[tuple1,tuple2,tuple3] 
    '''
    items = dic.items()
    # 转成了一个list 里面都是tuple 
    # 默认的sort 是按tuple的第一个(key)从小到大排列
    items.sort()
    return items


def compare(a,b):
    if a>=b :
        return 1
    else:
        return -1

def sorted_value_ascending(dic):
    '''
    返回按value升序排序的lis[tuple1,tuple2,tuple3] 
    '''
    items = dic.items()  
    items.sort(cmp=lambda a,b:compare(a[1],b[1]))# a[1]表示的是用tuple1[1]来排序 
    return items

def sorted_value_descending(dic):
    '''
    返回按value升序排序的lis[tuple1,tuple2,tuple3] 
    '''
    items = dic.items()  
    items.sort(cmp=lambda a,b:compare(b[1],a[1]))# 这里和前面换了位置
    return items
    



dic = {"k1":3.2,"k2":2,"k3":10}
r=sorted_value_descending(dic)
print r # [(k2, 2), (k1, 3), (k3, 10)]