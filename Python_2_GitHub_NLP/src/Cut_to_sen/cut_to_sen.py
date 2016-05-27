#coding=utf-8
'''
Created on 2016年3月20日
@author: 李健博
程序作用：
把文章拆分为短句
'''
from __future__ import  division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import re





class Cut_to_sen():
    '''
    用来分割文章的正则表达式
    用分割符号把句子分割成 小段，去除分割符号
    '''
    re_article_seg = re.compile(ur"[,，。！？ ]+", re.U)# 汉字和字母
#     re_article_seg = re.compile(ur"([\u4E00-\u9FD5a-zA-Z0-9+#&\._]+)", re.U)# 汉字和字母
#     re_remain_seg = re.compile(ur"(\r\n|\s)", re.U)# 不符合re_article_seg的交给re_remain_seg
    



    def cut_article(self,article):
        '''
        把长文章按照特定的符号分割成短句
            原文：
        一篇文章市场上厕@所一篇文章市场上厕所一篇文章市场上厕所
        
        分割后：
        一篇文章市场上厕
        @
        所一篇文章市场上厕所一篇文章市场上厕所
        '''
        
        # 对文章进行分割
        blocks = Cut_to_sen.re_article_seg.split(article)
        return blocks

#     def cut_blocks_no_hmm(self,blocks):
#         '''
#         非hmm分词
#         '''
#         for blk in blocks:# 遍历每一个块
#             if not blk:# 如果为空
#                 continue
#             # 可能是aa方芳芳
#             # 如果是符合re_article_seg 就可以用cut_max_prob短句分词
#             if Cut_article.re_article_seg.match(blk):
#                 for word in self.cut_obj.cut_max_prob_ho_hmm(blk):
#                     yield word
#             else:# 可能是@@@%%这种东西
#                 tmp = Cut_article.re_remain_seg.split(blk)# 按照空白符把block分割
#                 for x in tmp:
#                     if Cut_article.re_remain_seg.match(x):# 如果是空白符直接返回
#                         yield x
#                     else :# 如果是其他把里面的字符一个一个分割开来 @@@会被分割成@@@
#                         for xx in x:
#                             yield xx
                                
#     def cut_blocks_hmm(self,sentence):
#         '''
#         hmm分词
#         '''
#         for blk in blocks:# 遍历每一个块
#             if not blk:# 如果为空
#                 continue
#             # 可能是aa方芳芳
#             # 如果是符合re_article_seg 就可以用cut_max_prob短句分词
#             if Cut_article.re_article_seg.match(blk):
#                 for word in self.cut_obj.cut_max_prob(blk):
#                     yield word
#             else:# 可能是@@@%%这种东西
#                 tmp = Cut_article.re_remain_seg.split(blk)# 按照空白符把block分割
#                 for x in tmp:
#                     if Cut_article.re_remain_seg.match(x):# 如果是空白符直接返回
#                         yield x
#                     else :# 如果是其他把里面的字符一个一个分割开来 @@@会被分割成@@@
#                         for xx in x:
#                             yield xx
        
    
    
                            



if __name__ == '__main__':
    '''
    用法 no_hmm
    '''
    sentence=u"一篇文@aaaff章市场,我我"
    cut_article=Cut_to_sen()
    words=cut_article.cut_article(sentence)
    for word in words:
        print word

    
