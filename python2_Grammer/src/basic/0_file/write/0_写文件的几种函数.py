#coding=utf-8
'''
Created on 2015年4月13日
@author: Administrator
write  一次写入一行
没有writeline
确保文件存在，则会首先清空，然后写入。
writelines():
'''



#write 写入一个字符串没有换行
# a=["ssssss","sdsdws","sdsaaadws"]
# with open(r'1.txt','wb') as f:
#     for line in a:
#         f.write(line)
        
       

#writelines 传入的是一个list
#写入的是一行 如果要多行  [‘write date\n’,’to 3.txt\n’,’finish\n’]
# a=["ssssss","sdsdws","sdsaaadws"]
# with open(r'1.txt','w') as f:
#     f.writelines(a)

#关于generator  在write里面无法使用
# def f(x):
#     yield x
# a=[]  
# x1=f("对对对")
# x2=f("对对对")
# x3=f("对对对")
# a.append(x1)
# a.append(x2)
# a.append(x3)
# with open(r'1.txt','w') as f:
#     f.writelines(a)


    