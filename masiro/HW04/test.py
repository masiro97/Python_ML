from scipy.io import loadmat
import numpy as np
from sklearn.neural_network import MLPClassifier


mnist_path = "./mnist-original.mat"
mnist_raw = loadmat(mnist_path)

mnist={
    "data":mnist_raw["data"].T,
    "target":mnist_raw["label"][0],
    "COL_NAMES":["label","data"],
    "DESCR":"mldata.org.dataset : mnist-original"
}

x,y = mnist.get('data')/255., mnist.get('target')

x_train, x_test = x[:60000], x[60000:]
y_train, y_test = y[:60000], y[60000:]

print(np.shape(x_train))