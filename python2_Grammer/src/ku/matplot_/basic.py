# coding=utf-8
'''
画图相关的函数
'''


#引入包
import matplotlib.pyplot as plt 
import numpy as np


# 
# '''线'''
# # plt.plot([1,2,3])
# #matplotlib的图像都位于Figure对象中。你可以用plt.figure创建一个新的Figure
# fig=plt.figure()
# #必须用add_subplot创建一个或多个subplot才行
# #这条代码的意思是：图像应该是2,1的，且当前选中的是4个subplot中的第一个（编号从1开始）
# ax = fig.add_subplot(2,1,1)
# #(0,0)到(5,10)
# # plot a line from (0, 0) to (5, 10)
# plt.plot([0, 5], [0, 10]) 
# plt.show()
# 
# 
# 
# '''点'''
# # plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# # plt.plot(x[i][0],x[i][1],'ob')
# # x1 = [1, 2, 3, 4, 5, 6]
# # y1 = [1, 4, 16, 18, 10, 12]
# # x2 = [1, 2, 3, 4, 5, 6]
# # y2 = [3, 4, 15, 18, 13, 12]
# # plt.plot(x1, y1, '*')
# # plt.plot(x2, y2, 'o')
# 
# 
# ''''函数图像'''
# # x到y的函数图像
# # x=np.arange(0,10)
# # y=x*x
# # plt.plot(x,y)
# 
# 
# 
#   
# #标题
# # plt.title('picture')
# # plt.xlabel('x value')
# # plt.ylabel('y value')
# # plt.xlim(0.0, 7.0)
# # #plt.ylim(0.0, 20.0)
# # plt.axis([-4, 4, -4, 4])
# # '''总的长宽'''
# # plt.show()
# # '''画出来'''