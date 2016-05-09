#coding=utf-8
'''
Created on 2015年11月22日
@author: Administrator
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import numpy as np
a=[1,2,3,4,5,6,7]
a=np.array(a)
# 减去平均数
a=a-np.mean(a)# [-3. -2. -1.  0.  1.  2.  3.]
# 除以标准差
a=np.divide(a,np.sqrt(np.sum(np.power(a,2)/len(a))))

