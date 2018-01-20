import numpy as np
import matplotlib.pyplot as plt
import random
import functions as ft

xy = np.loadtxt('ex2data1.txt',unpack = True, dtype = 'float32', delimiter=',')

x_data = xy[:-1]
y_data = xy[-1]

w0 = random.uniform(-1.0,1.0)
w1 = random.uniform(-1.0,1.0)
w2 = random.uniform(-1.0,1.0)

W = [w0,w1,w2]

n , m = x_data.shape
x_data = np.vstack((np.ones(m),x_data))

cost, grad, W = ft.costFunction(W,x_data,y_data)

print("---------------------------------------")
print("cost : %f" %cost)
print("grad : [%f , %f, %f]" %(grad[0],grad[1],grad[2]))
print("W : [%f %f %f]" %(W[0],W[1],W[2]))
pos = np.where(y_data ==1)
neg = np.where(y_data ==0)

t1 = plt.plot(x_data[1,pos],x_data[2,pos],'bo')
t2 = plt.plot(x_data[1,neg],x_data[2,neg],'rx')
plt.xlabel('Midterm Score')
plt.ylabel('Finterm Score')
plt.legend([t1[0],t2[0]],['Pass','Fail'])
plt.xlim([25,105])
plt.ylim([25,105])
x1 = np.arange(0,100)
x2 = -(W[0] + W[1]*x1) / W[2]
plt.plot(x1,x2)
plt.show()
