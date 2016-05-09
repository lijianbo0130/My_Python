#coding=utf-8
'''
Created on 2015年7月25日
@author: Administrator
'''
import sys
import jieba
sys.path.append("../")
jieba.load_userdict("spot_name.txt")
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import toolkit.data as dt



with open(r'data_comment2.txt','rb') as somefile:
    lis_sen=[]# 存放分割完的句子
    for line in somefile:
        sen_lis=[]
        line= line.strip()
        line=line.split("\t")[0]# 得到配评论
#         print line[2]
        seg_gen = jieba.cut(line, cut_all=False,HMM=True)
        for word in seg_gen:
            for word in dt.get_chinese_word(word)[0]:
                sen_lis.append(word)
            
        lis_sen.append(" ".join(sen_lis)+"\n")

with open(r'data_chinese_sen.txt','wb') as f:
    for line in lis_sen:
        f.write(line)
 
         
print "down"
        
