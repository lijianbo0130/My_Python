#coding=utf-8
'''
对龚兵给的图像进行强去噪
'''

import Image


def Binarized(Picture,Threshold = 100):
    '''用二分法做判别
    Threshold 为阀值
    '''
    Pixels = Picture.load()
    (Width, Height) = Picture.size
    for i in xrange(Width):
        for j in xrange(Height):
            if Pixels[i, j] > Threshold: # 大于阈值的置为背景色，否则置为前景色（文字的颜色）
                Pixels[i, j] = 255 # 白色
            else:
                Pixels[i, j] = 0 # 黑色
    return Picture






def Smooth_9(Picture):
    '''去除噪点9个那种'''
    Pixels = Picture.load() #用Pixels 得到数据  用Pixels[1,1]
    (Width, Height) = Picture.size #得到宽和长
    #开始去噪
    for w in range(1,Width-1):
        for h in range(1,Height-1):
            if Pixels[w,h]==BLACK:#如果中心点为黑色
                flag=True #判断的标识  默认为要修改
                for w2 in range(-1,2):
                    for h2 in range(-1,2):
                        if w2==0 and h2==0:continue# 如果为原点就不计算        
                        if Pixels[w+w2,h+h2]==BLACK: #如果有黑点 就跳出
                            flag=False;break;
                    if flag==False:break #如果有黑点就没必要判断
                
                if flag==True: # 如果需要改变 就改变
                    for w2 in range(-1,2):
                        for h2 in range(-1,2):
                            Pixels[w+w2,h+h2]=WRITE
    return Picture

def Smooth_12(Picture):
    '''去除噪点12个那种
    一次去除横的 一次去除竖的
    调用两次子函数
    '''
    Picture=Smooth_12_sub(Picture)
    Picture = Picture.transpose(Image.ROTATE_90)# 旋转90度
    Picture=Smooth_12_sub(Picture)
    Picture = Picture.transpose(Image.ROTATE_270)# 旋转270度  这样就还原了   
    return Picture  

def Smooth_12_sub(Picture): 
    '''
    width一个像素,height两个像素
    '''
    Pixels = Picture.load() #用Pixels 得到数据  用Pixels[1,1]
    (Width, Height) = Picture.size #得到宽和长
    #开始去噪
    for w in range(1,Width-1):# width 为1个像素
        for h in range(1,Height-2):# height 为2个像素
            if Pixels[w,h]==BLACK and Pixels[w,h+1]==BLACK:#如果中心点为黑色
                print w,h
                flag=True #判断的标识  默认为要修改
                for w2 in range(-1,2):
                    for h2 in range(-1,3):
                        if flag==False:break #如果有黑点就没必要判断
                        if (w2==0 and h2==0) or (w2==0 and h2==1):continue# 如果为原点就不计算        
                        if Pixels[w+w2,h+h2]==BLACK: #如果有黑点 就跳出
                            flag=False;break;
                    
                
                if flag==True: # 如果需要改变 就改变
                    for w2 in range(-1,2):
                        for h2 in range(-1,3):
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
        
def brush(Picture,b_height,e_height):
    (Width, Height) = Picture.size
    Pixels = Picture.load()
    for h in range(b_height,e_height):
        for w in range(Width):
            Pixels[w,h]=WRITE
    return Picture
    

    
    
                   
         
         
    


BLACK=0
WRITE=255

img = Image.open('5.png') # 读入图片
img = img.convert("L") # 转换颜色的模式 L表示灰度图像
img=Binarized(img) # 
img=brush(img,18,24) # 涂白
# img.show()
img= remove_bound(img)#边界去除
# img.show()
img=Smooth_9(img)
img=Smooth_12(img)
# img.show()
img.save("new_5.bmp")
print "down"
