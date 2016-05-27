# coding=utf-8
'''
Created on 2016年5月6日
@author: 李健博
程序作用：
使用了前向切分和后向切分
找出词典中会被词典里面的词 切分后大于三的词
'''
from __future__ import division
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
from Cut_Sentence.max_waCut_to_wordackward_seg import MaxBackwardSeg
from Cut_Sentence.max_waCut_to_wordorward_seg import MaxForwardSeg

def get_data():
    lis_write = []
    with open(r'new_dict_no_duplicate.txt', 'rb') as somefile:
        for line in somefile:
            line = line.decode('utf-8')
            line = line.strip()  # 去除换行符号
            lis_write.append(line)
    return lis_write
            
            


if __name__ == '__main__':
    lis_write = []
    # 读取的词库文件名
    lis_sen = get_data()
    maxBackSeg = MaxBackwardSeg()
    maxForSeg = MaxForwardSeg()
    for sen in lis_sen:
        lis_for_seg = maxForSeg.seg_forward(sen)
        lis_back_seg = maxBackSeg.seg_backward(sen)
        
        if len(lis_for_seg) >= 3 or len(lis_back_seg) >= 3:
            lis_write.append(sen)
            
    with open(r'1.txt', 'wb') as somefile:
        for line in lis_write:  # 不会自动换行
            line += "\r\n"
            somefile.write(line)
    print "down"
    
         

        
