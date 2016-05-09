#coding=utf-8
'''
figure对象
'''
import matplotlib.pyplot as plt
'''matplotlib的图像都位于Figure对象中。你可以用plt.figure创建一个新的Figure
接下来调用figure创建一个绘图对象，并且使它成为当前的绘图对象。
也可以不创建绘图对象直接调用接下来的plot函数直接绘图，
matplotlib会为我们自动创建一个绘图对象。
如果需要同时绘制多幅图表的话，可以是给figure传递一个整数参数指定图标的序号，
如果所指定序号的绘图对象已经存在的话，将不创建新的对象，而只是让它成为当前绘图对象。'''

plt.figure(figsize=(8,4))

