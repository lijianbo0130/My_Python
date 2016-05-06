#coding=utf-8
'''
这个是example不要乱改
'''

#encoding=utf-8
import jieba

# 全模式
# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print "Full Mode:", "/ ".join(seg_list)  # 全模式  把词典里面有的词全提取出来
#我/ 来到/ 北京/ 清华/ 清华大学/ 华大/ 大学  

# 精确模式
seg_list = jieba.cut("我来到北京清华大学。我叫李健博", cut_all=False)
# print "Default Mode:", "/ ".join(seg_list)  # 我/ 来到/ 北京/ 清华大学
for word in seg_list:
    print word


#HMM 默认的HMM为True
# def cut(self, sentence, cut_all=False, HMM=True):

# 默认是精确模式
# seg_list = jieba.cut("我来自大武汉")  # 默认是精确模式
# for word in  seg_list:
#     print word

# 搜索引擎模式 和全模差不多
# seg_list = jieba.cut_for_search("我来到北京清华大学")  # 搜索引擎模式
# print ", ".join(seg_list)
