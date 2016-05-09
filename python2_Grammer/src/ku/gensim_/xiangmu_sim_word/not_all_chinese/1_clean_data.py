#coding=utf-8
'''
Created on 2015年7月25日
@author: Administrator
'''
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

with open(r'comment2.txt','rb') as somefile:
    lis_sen=[]# 存放分割完的句子
    for line in somefile:
        line= line.strip()
        line=line.split("\t")[0]# 得到配评论
#         print line[2]
        seg_gen = jieba.cut(line, cut_all=False,HMM=False)
        sen=" ".join(seg_gen)+"\n"
        lis_sen.append(sen)

with open(r'1.txt','wb') as f:
    for line in lis_sen:
        f.write(line)

        
print "down"
        
