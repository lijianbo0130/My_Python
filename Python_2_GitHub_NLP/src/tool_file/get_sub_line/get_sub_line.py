# coding=utf-8
'''
Created on 2016年4月20日
@author: 李健博
程序作用：
从origin_fine中截取前max_index行 
写入new_file中

'''
from __future__ import division
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

def get_sub_file(origin_fine, new_file, max_index):
    lis_write = []
    with open(origin_fine, 'rb') as somefile:
        for index, line in enumerate(somefile):
            if (index >= max_index):
                break
            line = line.decode('utf-8')
            line = line.strip()  # 去除换行符号
            lis_write.append(line)
    
    with open(new_file, 'wb') as somefile:
        for line in lis_write:  # 不会自动换行
            line += "\r\n"
            somefile.write(line)

if __name__ == '__main__':
    max_index = 100000
    origin_fine = ""
    new_file = ""
    get_sub_file(origin_fine, new_file, max_index)

print "down"

        


         

        
