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
a=np.array([[1,0,0],[0,2,0],[0,0,3]])
i_value,i_vector=np.linalg.eig(a)
print i_value
print i_vector
