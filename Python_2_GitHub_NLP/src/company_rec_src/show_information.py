# coding=utf-8
'''
Created on 2016年5月19日
@author: 李健博
程序作用：
输出标注中的各种模式的数量和正确比例
'''
from __future__ import division
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

'''
key=flag value=[y的个数,n的个数]
'''
dict_info={}
with open(r'company_rec.txt','rb') as somefile: 
    for index,line in enumerate(somefile):
        if index ==0:
            continue
        line = line.decode('utf-8')
        line= line.strip() # 去除换行符号
        line_split =line.split("\t")# 按照空格分开 
        rec_flag=line_split[1]
        is_company=line_split[5]
#         print rec_flag,is_company
        if rec_flag not in dict_info:
            dict_info[rec_flag]=[0,0]
        if is_company=="y":
            dict_info[rec_flag][0]+=1
        else:
            dict_info[rec_flag][1]+=1


# 显示
with open(r'1.txt','wb') as somefile:
    for flag in dict_info: # 不会自动换行
        num_y=dict_info[flag][0]
        num_n=dict_info[flag][1]
        num_total=num_y+num_n
        line=flag+"\t"+str(num_y)+"\t"+str(num_n)+"\t"+str(num_total)+"\t"+str(num_y/num_total)
        line+="\r\n"
        somefile.write(line)
        

print "down"
        

        


         

        

         

        

