#coding=utf-8
'''
Created on 2015年5月7日
@author: Administrator
'''

# a=[[1,2],[3,4],[5,6],[7,8]]
# #得到第一行的最大值
# print max(a[0])
# #得到第一列的最大值
# print max([k for k,v in a])
# #得到最大值的下标
# print [k for k,v in a].index(max([k for k,v in a]))

# for k,v in a:
#     print k,v


#三个参数
list_coefficient=[[1,2,3],[3,4,5],[5,6,7]]
print [k3 for k1,k2,k3 in list_coefficient].index(max([k3 for k1,k2,k3 in list_coefficient]))













