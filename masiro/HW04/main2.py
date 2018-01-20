from pylab import *
from scipy.spatial import distance
from scipy.ndimage import interpolation
import random as pyrandom
from scipy.io import loadmat
from sklearn import svm

def moments(image):
    c0,c1 = mgrid[:image.shape[0],:image.shape[1]]
    m0 = sum(c0*image)/sum(image)
    m1 = sum(c1*image)/sum(image)
    m00 = sum((c0-m0)**2*image)/sum(image)
    m11 = sum((c1-m1)**2*image)/sum(image)
    m01 = sum((c0-m0)*(c1-m1)*image)/sum(image)
    return array([m0,m1]),array([[m00,m01],[m01,m11]])


def deskew(image):
    c,v = moments(image)
    alpha = v[0,1]/v[0,0]
    affine = np.array([[1,0],[alpha,1]])
    ocenter = np.array(image.shape)/2.0
    offset = c-np.dot(affine,ocenter)
    img = interpolation.affine_transform(image,affine,offset=offset)
    return (img - img.min()) / (img.max() - img.min())

def deskewAll(X):
    currents = []
    for i in range(len(X)):
        currents.append(deskew(X[i].reshape(28,28)).flatten())
    return np.array(currents)



mnist_path = "./mnist-original.mat"
mnist_raw = loadmat(mnist_path)

mnist={
    "data":mnist_raw["data"].T,
    "target":mnist_raw["label"][0],
    "COL_NAMES":["label","data"],
    "DESCR":"mldata.org.dataset : mnist-original"
}

x = mnist.get('data') /255.0 -1
y = mnist.get('target')


x_train , x_test = x[:60000],x[60000:]
y_train , y_test = y[:60000],y[60000:]

X_train_deskewed = deskewAll(x_train)
X_test_deskewed = deskewAll(x_test)

print("start")
classifier = svm.SVC(verbose=1,kernel="poly",degree=4,C=5.0,gamma = 0.001,
                     decision_function_shape='ovr')

classifier.fit(X_train_deskewed,y_train)

print('Test set score %f' %classifier.score(X_test_deskewed,y_test))