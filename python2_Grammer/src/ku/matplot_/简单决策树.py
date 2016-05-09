'''
Created on 2015年1月26日
@author: asus
'''

'''
画图
'''
import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")


def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt,  xycoords='axes fraction',
             xytext=centerPt, textcoords='axes fraction',
             va="center", ha="center", bbox=nodeType, arrowprops=arrow_args )


def createPlot():
#     创建一个figure  1=一个 facecolor=背景色
    fig = plt.figure(1, facecolor='white')
#     plt.plot([0, 5], [0, 10]) 
#     清除当前  figure 防止画有东西
    fig.clf()
# frameon 是否绘制图框架
    createPlot.ax1 = plt.subplot(111, frameon=True)
    plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()

createPlot()