#coding=utf-8
'''
2.添加詞典：
开发者可以指定自己自定义的词典，以便包含 jieba 词库里没有的词。
虽然 jieba 有新词识别能力，但是自行添加新词可以保证更高的正确率
用法： jieba.load_userdict(file_name) # file_name 为自定义词典的路径
词典格式和dict.txt一样，一个词占一行；每一行分三部分，
一部分为词语，另一部分为词频，最后为词性（可省略），用空格隔开
前两个部分必须有 
第二个部分后面要加空格

如：
云计算 5
李小福 2 nr
创新办 3 i
easy_install 3 eng
好用 300
韩玉赏鉴 3 nz

自己测试词典:======================================================
中国 3
中国人民 3
中国人名解放军 3
解放军 3
人民 3

会追加到原来词的后面 不会出现不使用原来词库的问题
如果想强制分词 最好使用50000000
'''


import sys
import jieba
sys.path.append("../")
jieba.load_userdict("user.txt")


seg_list = jieba.cut("李健博中国人民解放军来了魅力漂亮可爱", cut_all=False,HMM=False)
print  "/ ".join(seg_list)  # 全模式





