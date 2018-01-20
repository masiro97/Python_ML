from sklearn import svm, datasets
import numpy as np
import matplotlib.pyplot as plt

iris = datasets.load_iris()

X = iris.data[:,:2]
y = iris.target


C = 1.0
svc = svm.SVC(kernel='linear', C=C).fit(X,y)

x_min, x_max = X[:,0].min()-1, X[:,0].max()+1
y_min, y_max = X[:,1].min()-1, X[:,1].max()+1

xx,yy = np.meshgrid(np.arange(x_min,x_max,0.02),np.arange(y_min,y_max,0.02))

Z= svc.predict(np.c_[xx.ravel(),yy.ravel()])

Z = Z.reshape(xx.shape)

plt.contourf(xx,yy,Z,cmap = plt.cm.coolwarm,alpha = 0.8)

plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.coolwarm)

plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
plt.xticks(())
plt.yticks(())
plt.title('SVM Practice')
plt.show()

