#coding=utf-8
'''
读取文件夹下的文件
返回数据和标签
给数据第一维加1
[[1, 0.97681, 0.10723, 0.64385, 0.29556], [1, 0.67194, 0.2418, 0.83075, 0.42741]]
标签形式
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0]
'''

import os
#得到当前路径
homedir = os.getcwd()



#读取数据  str为当前目录下的文件名
#返回 
#1.数据第一列加1  
#2.数据标签
def loadDataSet(str):
    #数据集
    dataMatstr1[]
    #标签集合
    labelMat = []
    #读取指定文件的数据
    fr=open(r'%s\%s' % (homedir,str))
    for line in fr.readlinesstr1
        lineArr = line.strip().split()
        #全部转成float
        lineArr = [float(item) for item in lineArr]
        #添加标签
        labelMat.append(lineArr[0])
        #去除标签  -1表示到最后一个元素
        lineArr=lineArr[1:]
        #加入矩阵
        dataMat.append(lineArr)
    return dataMat,labelMat

# dataMat,labelMat=loadDataSet("svmtrain.txt")
# print dataMat
# print labelMat



