# 조건 1. diabetes.csv 파일로 부터 데이터 직접 불러오기
# 조건 2. training set과 test set을 직접 기준을 정하여 나누기
# 조건 3. SVM과 Neural Network으로 구현하고 결과 비교해보기
# 조건 4. 각 알고리즘에 PCA 적용해보고 결과 비교해보기

# 6,148,72,35,0,33.6,0.627,50,1
# 1,85,66,29,0,26.6,0.351,31,0
# 8,183,64,0,0,23.3,0.672,32,1
# 1,89,66,23,94,28.1,0.167,21,0
# 0,137,40,35,168,43.1,2.288,33,1

#(768,9)

import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn import svm
from sklearn.decomposition import PCA

xy = np.loadtxt('diabetes.csv',unpack = True, dtype = 'float32', delimiter=',')

x_data = np.transpose(xy[:-1])
y_data = xy[-1]

x_train, x_test = x_data[:600] , x_data[600:]
y_train, y_test = y_data[:600] , y_data[600:]

mlp = MLPClassifier(hidden_layer_sizes=(100,100), solver='sgd',alpha=1e-4,max_iter = 1000)
mlp.fit(x_data,y_data)

print("Nueral_Network")
print("Test set score: %f" % mlp.score(x_test, y_test))

svm1 = svm.SVC(kernel="rbf",gamma=0.01,degree=5)
svm1.fit(x_train,y_train)

print("SVM")
print('Test set score %f' %svm1.score(x_test,y_test))


print("\n-----------------PCA--------------------\n")

pca = PCA(n_components=2)

X_pca = pca.fit(x_data)

X_pca = X_pca.transform(x_data)

x_train, x_test = X_pca[:650] , X_pca[650:]
y_train, y_test = y_data[:650] , y_data[650:]


mlp2 = MLPClassifier(hidden_layer_sizes=(100,100), solver='sgd',alpha=1e-4,max_iter = 1000)
mlp2.fit(x_train,y_train)

print("Nueral_Network")
print("Test set score: %f" % mlp2.score(x_test, y_test))


svm2 = svm.SVC(kernel="rbf",gamma=0.01,degree=5)
svm2.fit(x_train,y_train)
print("SVM")
print('Test set score %f' %svm2.score(x_test,y_test))




