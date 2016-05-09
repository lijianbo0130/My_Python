#coding=utf-8
'''
读取指定文件夹下的文件
读取目录f1下的所有文件 0_0.txt到9_88.txt
写到f2中
@author: asus
'''
import os

#目标文件夹
obrf_dir=r'C:\Users\asus\Desktop\dataset\trainingDigits'
obwf=r'C:\Users\asus\Desktop\dataset\writefile.txt'
#把目录下的所有文件变成一个列表
trainingFileList = os.listdir(obrf_dir)
#得到文件的长度
m=len(trainingFileList)   
#装入所有文件的数组
all_file=[]
for i in range(m):
    #得到第i个文件的文件名
        fileNameStr = trainingFileList[i]
        f1=open(r'%s\%s' % (obrf_dir,fileNameStr))
        text=f1.read()
        all_file.append(text)
        f1.close

f2=open(obwf,'w')
#white 函数只能写string
for i in all_file:
    f2.write(i) 

f2.flush()    
f2.close()
print("done")
    
    