#coding=utf-8
'''
正弦和余弦函数
'''




from pylab import *
# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
figure(figsize=(8,6), dpi=80)
# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
subplot(1,1,1)
# '''X 是一个 numpy 数组，包含了从 −π 到 +π 等间隔的 256 个值。
# C 和 S 则分别是这 256 个值对应的余弦和正弦函数值组成的 numpy 数组。'''
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
plot(X, C, color="blue", linewidth=1.0, linestyle="-")
# 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
plot(X, S, color="green", linewidth=1.0, linestyle="-")
# 设置横轴的上下限
xlim(-4.0,4.0)
# 设置横轴记号  X上显示 -4 -3 -2 -1 0 1 2 3 4  9个数字
xticks(np.linspace(-4,4,9,endpoint=True))
# 设置纵轴的上下限
ylim(-1.0,1.0)
# 设置纵轴记号
yticks(np.linspace(-1,1,5,endpoint=True))
# 以分辨率 72 来保存图片
# savefig("exercice_2.png",dpi=72)
# 在屏幕上显示
show()