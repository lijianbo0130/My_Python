# coding=utf-8
'''
Created on 2016年5月6日
@author: 李健博
程序作用：
把文件合并成一个文件
fileone 为开始文件
已经验证：
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
    lis_write = []  # lis保存所有数据
    # 读取第一个文件
    with open(file_one, 'rb') as somefile:
        for line in somefile:
            line = line.decode('utf-8')
            line = line.strip()  # 去除换行符号
            lis_write.append(line)
            
    # 读取第二个文件
    with open(file_two, 'rb') as somefile:
        for line in somefile:
            line = line.decode('utf-8')
            line = line.strip()  # 去除换行符号
            lis_write.append(line)
            
    # 写入目标文件
    with open(merge_file_name, 'wb') as somefile:
        for line in lis_write:  # 不会自动换行
            line += "\r\n"
            somefile.write(line)
            

    
if __name__ == '__main__':

    file_one = "sougou.txt"
    file_two = "zb_basic.txt"
    merge_file_name = "new_dict.txt"
    merge_file(file_one, file_two, merge_file_name)
    print "down"

