#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
import sk_learn.sk_svm.LoadData1 as ld

#0代表的是0  1代表其他
def cleanData(labelMat):
    m=len(labelMat)
    print m
    for i in range(m):
        if labelMat[i]==0:
            labelMat[i]=0
        else:
            labelMat[i]=1


dataMat,labelMat=ld.loadDataSet("svmtrain.txt")
# print dataMat
# print labelMat

cleanData(labelMat)
dataMat=np.mat(dataMat)
labelMat=np.array(labelMat)

X =dataMat   # we only take the first two features. We could
                      # avoid this ugly slicing by using a two-dim dataset
# print X
y = labelMat
# print y
#x,y都是矩阵
h = .02  # step size in the mesh
print type(X)
print type(y)

# we create an instance of SVM and fit out data. We do not scale our
# data since we want to plot the support vectors
C = 1  # SVM regularization parameter
# svc = SVC(kernel='linear', C=C).fit(X, y)
rbf_svc = SVC(kernel='rbf', gamma=8, C=C).fit(X, y)
# poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, y)
# lin_svc = svm.LinearSVC(C=C).fit(X, y)

# create a mesh to plot in 创建一个网格来画画
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))





i=0
clf=rbf_svc
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
# plt.subplot(2, 2, i + 1)
# plt.subplots_adjust(wspace=0.4, hspace=0.4)

# Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
# 
# 
#     # Put the result into a color plot
# Z = Z.reshape(xx.shape)
# plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
#     # Plot also the training points
# plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
# plt.xlabel('Sepal length')
# plt.ylabel('Sepal width')
# plt.xlim(xx.min(), xx.max())
# plt.ylim(yy.min(), yy.max())
# plt.xticks(())
# plt.yticks(())
# plt.show()


#Index of support vectors.  support vectors的下标
for i in  clf.support_:
    print i

#support vectors  
for i in  clf.support_vectors_:
    print i

#number of support vector for each class  每一类支撑向量的数量
print clf.n_support_

#
for i in  clf.dual_coef_:
    print i








