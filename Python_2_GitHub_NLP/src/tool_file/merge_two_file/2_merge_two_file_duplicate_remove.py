# coding=utf-8
'''
Created on 2016年5月6日
@author: 李健博
程序作用：
把文件合并成一个文件
fileone 为开始文件
同时去重，两个文件可能有重复的数据
同时保存文件的顺序，不能用set保存，这样不能保存顺序
'''
from __future__ import division
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

def merge_file(file_one, file_two, merge_file_name):
    '''
    把file_one，file_two合并成一个文件，名字为merge_file_name
    '''
    set_only = set()  # lis保存所有数据
    lis_write=[]
    # 读取第一个文件
    with open(file_one, 'rb') as somefile:
        for line in somefile:
            line = line.decode('utf-8')
            line = line.strip()  # 去除换行符号
            if line not in set_only: # 不在set中才加入
                lis_write.append(line)
            set_only.add(line)
            
    # 读取第二个文件
    with open(file_two, 'rb') as somefile:
        for line in somefile:
            line = line.decode('utf-8')
            line = line.strip()  # 去除换行符号
            if line not in set_only:
                lis_write.append(line)
            set_only.add(line)
            
    # 写入目标文件
    with open(merge_file_name, 'wb') as somefile:
        for line in lis_write:  # 不会自动换行
            line += "\r\n"
            somefile.write(line)
            

    
if __name__ == '__main__':

    file_one = "sougou.txt"
    file_two = "zb_basic.txt"
    merge_file_name = "new_dict_no_duplicate.txt"
    merge_file(file_one, file_two, merge_file_name)
    print "down"

