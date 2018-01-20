import numpy as np
import matplotlib.pyplot as plt
import random

def sigmoid(z):
    return 1 / (1+np.exp(-z))

def costFunction(W,X,y):
    m = y.size
    h = sigmoid(np.dot(W,X))
    a = 0.001
    for i in range(0,100000):
        h = sigmoid(np.dot(W,X))
        W = W - (a/m) * (np.dot(h-y,np.transpose(X)))
        grad = (a/m) * sum(np.dot(h-y,np.transpose(X)))
        gradient = (a/m) * (np.dot(h-y,np.transpose(X)))
        if abs(grad) < 0.0005:
            a = a + 0.00001
        if(i % 10000 == 1):
            cost = -(1 / m) * sum(y * np.log(h) + (1 - y) * np.log(1 - h))
            print("cost : %f" %cost)

    return cost,gradient,W

def accuracy(W,X,y):
    cnt = 0
    m = y.size
    for i in range(m):
        h = sigmoid(np.dot(W,[1,X[1,i],X[2,i]]))
        if(h >0.5 and y[i] ==1):
            cnt = cnt + 1
        elif (h<0.5 and y[i] ==0):
            cnt = cnt + 1

    acc = cnt/m
    error = 100 -cnt
    return acc,error
