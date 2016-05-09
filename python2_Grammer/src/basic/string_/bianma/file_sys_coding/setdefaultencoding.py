#coding=utf-8
'''
没啥用就算设定了系统的编码格式 读取的时候还是要decode-utf-8
'''
import sys
import chardet

# 得到系统当前编码  
print sys.getdefaultencoding() #系统的默认编码为ascii
a="我"
print chardet.detect(a)


# 更换 setdefaultencoding
# #必须要添加不然  加载不到setdefaultencoding这个方法
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # 改成utf-8
print sys.getdefaultencoding()
a="我"
print chardet.detect(a)





