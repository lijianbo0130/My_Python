#coding=utf-8
'''
Created on 2015年3月19日
@author: asus
'''

from time import time 

'''
Python 字典中使用了 hash table，
因此查找操作的复杂度为 O(1)，而 list 实际是个数组，
在 list 中，查找需要遍历整个 list，其复杂度为 O(n)，
因此对成员的查找访问等操作字典要比 list 更快。
'''

t = time() 
list = ['a','b','is','python','jason','hello','hill','with','phone','test', 
'dfdf','apple','pddf','ind','basic','none','baecr','var','bana','dd','wrd'] 
# list = dict.fromkeys(list,True)   #不注释是dict 注释是list
print list 
filter = [] 
for i in range (1000000): 
    for find in ['is','hat','new','list','old','.']: 
        if find not in list: 
            filter.append(find) 
print "total run time:"
print time()-t





