#coding=utf-8
'''
这个是example不要乱改
'''

#encoding=utf-8
import jieba

'''
全模式  把词典里面有的词全提取出来
'''
# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print "Full Mode:", "/ ".join(seg_list)  
# #我/ 来到/ 北京/ 清华/ 清华大学/ 华大/ 大学  

'''
精确模式 概率最大的切分
'''
seg_generator = jieba.cut("公司的控制权", cut_all=False,HMM=True)
# print "Default Mode:", "/ ".join(seg_generator)  # 我/ 来到/ 北京/ 清华大学
# for word in seg_generator:
#     print word
    
# 返回的是generator 有时候可以转成list 使用 
seg_lis=list(seg_generator)
print seg_lis # [u'\uff0c', u'\u6211', u'\u53eb', u'aaa', u'\u674e\u5065\u535a']

'''
默认的格式
默认的HMM为True HMM=True
精确切分 cut_all=False
def cut(self, sentence, cut_all=False, HMM=True):
'''



# 搜索引擎模式 和全模差不多 把大于3的词再切分一遍
# seg_list = jieba.cut_for_search("我来到北京清华大学")  # 搜索引擎模式
# print ", ".join(seg_list)
