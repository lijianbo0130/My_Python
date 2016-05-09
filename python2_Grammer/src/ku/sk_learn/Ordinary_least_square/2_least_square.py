#coding=utf-8
'''
Created on 2015年10月6日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import numpy as np
from sklearn import linear_model
# 数据集
train_x= np.array([[0, 0], [1, 1], [2, 2],[50,50]])
print  train_x # n个数据就有n行
train_y = np.array([0, 1.1, 2.5,59])
print train_y
# 开始拟合
clf = linear_model.LinearRegression()
clf.fit(train_x, train_y)
# 所有的输出

# 参数值
print "W1-Wn的值"
print clf.coef_ # W1-Wn的值
print "W0的值"
print clf.intercept_ # W0的值

# 预测值
test_x=[[3,3],[4,4]]
test_y=[1,2]
print "预测x点的值"
print clf.predict(test_x)# 预测值

# LinearRegression( normalize=True)

# The mean square error 输出平均误差
import numpy as np
print "输出平均误差" # 把每一个误差平方之后除以n
print np.mean((clf.predict(test_x) - test_y) ** 2)





