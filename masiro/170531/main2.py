import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.decomposition import PCA
import time

start = time.time()

from scipy.io import loadmat
from sklearn import svm

mnist_path = "./mnist-original.mat"
mnist_raw = loadmat(mnist_path)

mnist={
    "data":mnist_raw["data"].T,
    "target":mnist_raw["label"][0],
    "COL_NAMES":["label","data"],
    "DESCR":"mldata.org.dataset : mnist-original"
}

x = mnist.get('data')/255.0*2 -1
y = mnist.get('target')

pca = PCA(n_components=20)
X_pca = pca.fit(x)
X_pca = X_pca.transform(x)


x_train , x_test = X_pca[:60000],X_pca[60000:]
y_train , y_test = y[:60000],y[60000:]


classifier = svm.SVC(random_state=42, verbose=1, C=2.8, gamma= 0.073, kernel='poly', degree = 4)

classifier.fit(x_train,y_train)

print('Test set score %f' %classifier.score(x_test,y_test))

end = time.time()
print(int(end-start))