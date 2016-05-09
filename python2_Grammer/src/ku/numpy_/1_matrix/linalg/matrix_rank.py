'''
#矩阵的轶
'''
import numpy as np
#矩阵的轶
a=np.mat([[1,2,3],[4,5,6],[7,8,9]])
b=np.linalg.matrix_rank(a)
print(a)
print(b)