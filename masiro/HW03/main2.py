import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

xy = np.loadtxt('ex2data1.txt',unpack = True, dtype = 'float32', delimiter=',')

x_data = xy[:-1]
y_data = xy[-1]

logreg = linear_model.LogisticRegression(C=1e5)
logreg.fit(np.transpose(x_data),y_data)
w = logreg.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(25,105)
yy = a * xx - (logreg.intercept_[0]) / w[1]

plt.plot(xx,yy)

pos = np.where(y_data ==1)
neg = np.where(y_data ==0)
t1 = plt.plot(x_data[0,pos],x_data[1,pos],'bo')
t2 = plt.plot(x_data[0,neg],x_data[1,neg],'rx')
plt.xlabel('Midterm Score')
plt.ylabel('Finterm Score')
plt.legend([t1[0],t2[0]],['Pass','Fail'])
plt.show()