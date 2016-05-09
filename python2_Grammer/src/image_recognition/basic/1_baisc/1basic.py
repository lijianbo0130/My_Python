#coding=utf-8
'''
Created on 2015年6月26日
@author: Administrator
'''
import Image
#载入图片
im = Image.open('1.jpg')
# print im  打印出一个对象

#得到数据
(Width, Height) = im.size
# im = im.load()

#图像翻转
# im.show()
# im = im.transpose(Image.ROTATE_90)# 旋转90度

#裁切图片
region = (0,0,20,20)
region2 = (20,0,40,20)
cropImg = im.crop(region)
cropImg.show()
cropImg = im.crop(region2)
cropImg.show()

#显示图片
im.show()

# #保存图片
im.save('new.bmp') 


