#coding=utf-8
'''
Created on 2015年6月26日
@author: Administrator
'''
import Image

im = Image.open('1.jpg')
Pixels = im.load()
#得到图片的基本数据
(Width, Height) = im.size
print Width, Height
#得到图片的一个像素
Pixels[0,0]
#若该点接近黑色则将其置为黑色（0），否则置为白色（255）
