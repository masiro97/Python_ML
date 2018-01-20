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


x_train , x_test = x[:60000],x[60000:]
y_train , y_test = y[:60000],y[60000:]

classifier = svm.SVC(verbose=1, C = 2.8, kernel="poly",degree=9,gamma=.0073,probability=False)
classifier.fit(x_train,y_train)


print('Training set score %f' %classifier.score(x_train,y_train))
print('Test set score %f' %classifier.score(x_test,y_test))