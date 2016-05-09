'''
返回排序后的下标
'''

import numpy as np

# 一维数组  
x = np.array([3, 1, 2])
a=np.argsort(x)
print(a)


# 二维数组
x = np.array([[0, 3], [2, 1]]) 
a=np.argsort(x, axis=0) #按列排序
print(a)

 
a=np.argsort(x, axis=1) #按行排序
print(a)

