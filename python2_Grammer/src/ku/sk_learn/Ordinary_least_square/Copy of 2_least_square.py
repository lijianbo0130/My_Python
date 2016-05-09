#coding=utf-8
'''
Created on 2015年10月6日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
from sklearn import linear_model
# 数据集
X= [[0, 0], [0, 3]]
y = [1, 3]
# 开始拟合
clf = linear_model.LinearRegression()
clf.fit(X, y)
# 所有的输出

# 参数值
print "W1-Wn的值"
print clf.coef_ # W1-Wn的值
print "W0的值"
print clf.intercept_ # W0的值

# 预测值
x=[3,3]
print "预测x点的值"
print clf.predict([x])# 预测值





