#coding=utf-8
'''
Created on 2015年3月17日
@author: asus
'''

import jieba as jb

asdddd='''<postdata>视频加载中，请稍候...自动播放<img width="120" height="90"
 src="http://p.v.iask.com/774/86/135453387_1.jpg" alt="李考察中国铁
 路总公司" /> play李考察中国铁路总公司向前向后<img src="http://i0.sinaimg.
 cn/dy/c/2014-08-24/U11347P1T1D30735825F21DT20140824210029.jpg" alt="
 李克强考察中国铁路总公司" title="李克强考察中国铁路总公司" /> 李克强考察中国
 铁路总公司 　　李克强指出，投资对稳增长、调结构具有关键作用，要深化投融资
 体制改革，加快投资审批制度改革，最大限度取消或简化前置审批，推进审批流程透明化
 和投资便利化，为各类市场主体自主决策和投资创造良好环境。加快铁路建设不能只靠国
 家投资“单打独斗”，要拿出市场前景好的项目和竞争性业务吸引民间资本共同参与，通过
 创新融资方式、丰富多元投资主体，为铁路发展注入新动力。 　　李克强说，高铁等中国
 装备具有性价比高等竞争优势，推动中国装备走向国际市场是扩大开放的重要之举，对提
 升我国对外合作水平、优化外贸结构意义重大，这反过来又会促进国内产业转型升级。要
 继续深化改革，充分用好对外合作平台，创造有利于企业和装备走出去的环境。企业要抢
 抓机遇，优势互补，形成拳头，为中国装备在世界市场赢得良好声誉。 　　马凯、杨晶、
 周小川参加上述活动。 (原标题：李克强考察铁路总公司：不断增</postdata>'''
 


# s = jb.cut(a,cut_all=False)
# for i in s:
#     print i
b="今a天a天气a真好的的的"
 
s = jb.cut(b,cut_all=False)
for i in s:
    print i,
print

import re 

# 提取中文 
b=unicode(b,'utf-8')
# 返回一个sen的list
sen_chinese_lis=re.findall(ur"[\u4e00-\u9fa5]+",b)

# 结果
# for word in word_lis:
#     print word
#===============================================================================
# 今
# 天
# 天气
# 真好的的的
#===============================================================================

# 分词
import jieba
words=""
for sen in sen_chinese_lis:
    seg_list = jieba.cut(sen, cut_all=False,HMM=False) 
    for word in seg_list:
        words+=word+" "

print words
