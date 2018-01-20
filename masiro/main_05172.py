from sklearn import svm, datasets
import numpy as np

digits = datasets.load_digits()


data = digits.images.reshape((len(digits.images),-1))
target = digits.target
train_len = int(len(data)/2)

X_train, X_test = data[:train_len], data[train_len:]
y_train, y_test = target[:train_len], target[train_len:]

C = 1.0
svc = svm.SVC(kernel='linear', C=C).fit(X_train,y_train)

accuracy = svc.score(X_test,y_test)

print(accuracy)