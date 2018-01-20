# from sklearn.decomposition import PCA
#
# # X = 데이터
# #
# # pca = PCA(n_components=2)
# # X_pca = pca.fit(X)
# # X_pca = X_pca.transform(X_pca)

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

iris = datasets.load_iris()

X = iris.data
y = iris.target

target_names = iris.target_names

pca = PCA(n_components=2)
X_pca = pca.fit(X)
X_pca = X_pca.transform(X)
print(y)
# y = np.choose(y,[1,2,0]).astype(np.float)
# fig = plt.figure(1,figsize=(4,3))
# plt.clf()
#
# ax = Axes3D(fig,rect = [0,0,.95,1], elev=48, azim=134)
# ax.scatter(X[:,0], X[:,1],c=y,cmap=plt.cm.spectral)

plt.scatter(X_pca[:,0],X_pca[:,1],c=y)
plt.show()


