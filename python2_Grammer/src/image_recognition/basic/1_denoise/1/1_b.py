#coding=utf-8
'''
最基本的去噪
'''

import Image


def Binarized(Picture):
    '''用二分法做判别'''
    Pixels = Picture.load()
    (Width, Height) = Picture.size
  
    Threshold = 100    # 阈值
  
    for i in xrange(Width):
        for j in xrange(Height):
            if Pixels[i, j] > Threshold: # 大于阈值的置为背景色，否则置为前景色（文字的颜色）
                Pixels[i, j] = 255 # 白色
            else:
                Pixels[i, j] = 0 # 黑色
    return Picture

def Enhance(Picture):
    '''强去噪使用
    分离有效信息和干扰信息'''
    Pixels = Picture.load()
    Result = Picture.copy()
    ResultPixels = Result.load()
    (Width, Height) = Picture.size
  
    xx = [1, 0, -1, 0, 1, -1, 1, -1]
    yy = [0, 1, 0, -1, -1, 1, 1, -1]
      
    Threshold = 100
      
    Window = []
    for i in xrange(Width):
        for j in xrange(Height):
            Window = [i, j]
            for k in xrange(8):  # 取3*3窗口中像素值存在Window中
                if 0 <= i + xx[k] < Width and 0 <= j + yy[k] < Height:
                    Window.append((i + xx[k], j + yy[k]))
            Window.sort()
            (x, y) = Window[len(Window) / 2]
            if (abs(Pixels[x, y] - Pixels[i, j]) < Threshold):    # 若差值小于阈值则进行“强化”
                if Pixels[i, j] < 255 - Pixels[i,j]:   # 若该点接近黑色则将其置为黑色（0），否则置为白色（255）
                    ResultPixels[i, j] = 0
                else:
                    ResultPixels[i, j] = 255
            else:
                ResultPixels[i, j] = Pixels[i, j]
    return Result

def Smooth(Picture):
    '''平滑降噪'''
    Pixels = Picture.load()
    (Width, Height) = Picture.size
  
    xx = [1, 0, -1, 0]
    yy = [0, 1, 0, -1]
  
    for i in xrange(Width):
        for j in xrange(Height):
            if Pixels[i, j] != 0:
                Count = 0
                for k in xrange(4):
                    try:
                        if Pixels[i + xx[k], j + yy[k]] == 0:
                            Count += 1
                    except IndexError: # 忽略访问越界的情况
                        pass
                if Count > 3:
                    Pixels[i, j] = 0
    return Picture

def mySmooth(Picture):
    '''去除噪点9个那种'''
    Pixels = Picture.load() #用Pixels 得到数据  用Pixels[1,1]
    (Width, Height) = Picture.size #得到宽和长
    print Pixels[35,2]
    print Pixels[34,2]
    #开始去噪
    for w in range(1,Width):
        for h in range(1,Height):
            #如果中心点为黑色
            if Pixels[w,h]==BLACK:
                #判断的标识  默认为要修改
                flag=True
                for w2 in range(-1,2):
                    for h2 in range(-1,2):
#                         print w2,h2
                        #如果为原点就不计算
                        if w2==0 and h2==0:
#                             print w2,h2
                            continue
                        #如果有黑点 就跳出
                        if Pixels[w+w2,h+h2]==BLACK:
                            flag=False
                            break;
                    #如果有黑点就没必要判断
                    if flag==False:
                        break
                
                if flag==True:
                    print flag
                    for w2 in range(-1,2):
                        for h2 in range(-1,2):
                            Pixels[w+w2,h+h2]=WRITE
    return Picture
                            
    
def remove_bound(Picture):
    '''去除边界所有的黑点'''
    (Width, Height) = Picture.size
    Pixels = Picture.load()
    for i in range(Width):
        Pixels[i,0]=WRITE
        Pixels[i,Height-1]=WRITE
        
    for i in range(Height):
        Pixels[0,i]=WRITE
        Pixels[Width-1,i]=WRITE
    return Picture
        
    
    
    
                   
         
         
    


BLACK=0
WRITE=255


img = Image.open('2.png') # 读入图片
img = img.convert("L") # 转换颜色的模式 L表示灰度图像
img=Binarized(img) # 
# img.show()
img= remove_bound(img)#边界去除
# img.show()
img=mySmooth(img)
# img.show()
img.save("new_1.bmp")





# #变成黑白
# threshold = 90
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
#  
# out = img.point(table,'1')
# out.show()










#二值化
# for y in xrange(img.size[1]):
#     for x in xrange(img.size[0]):
#         if pixdata[x, y][0] < 90:
#             pixdata[x, y] = (0, 0, 0, 255)
# for y in xrange(img.size[1]):
#     for x in xrange(img.size[0]):
#         if pixdata[x, y][1] < 136:
#             pixdata[x, y] = (0, 0, 0, 255)
# for y in xrange(img.size[1]):
#     for x in xrange(img.size[0]):
#         if pixdata[x, y][2] > 0:
#             pixdata[x, y] = (255, 255, 255, 255)

# img.show()
# img.save("input-black.gif", "GIF")
# #放大图像 方便识别
# im_orig = Image.open('input-black.gif')
# big = im_orig.resize((1000, 500), Image.NEAREST)
