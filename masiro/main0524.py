#K-Means Clustering
#2017-05-24

import numpy as np
import random
from matplotlib import pyplot as plt

a1 = np.array([0,0])
b1 = np.array([1,1])
def getDistance(a,b):
    d = np.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    return d


#num = random.randrange(1,10) #1 이상 10미만

a = np.random.randint(25,50,(25,2))
b = np.random.randint(55,85,(25,2))

c0 = np.array([random.randrange(25,50), random.randrange(25,50)]) #centroid
c1 = np.array([random.randrange(55,85), random.randrange(55,85)]) #centroid
C = [c0,c1]

z = np.vstack((a,b))
z = np.float32(z)
U = np.zeros(50)

for i in range(0,10):
    num0 = 0
    num1 = 0
    t0 = np.array([0, 0])
    t1 = np.array([0, 0])

    for k in range(0,50):
        d0 = getDistance(z[k],C[0])
        d1 = getDistance(z[k],C[1])
        if(d0 > d1):
            U[k] = 0
            num0 = num0 +  1
            t0 =  t0 + z[k]

        else:
            U[k] = 1
            num1 = num1 + 1
            t1 = t1 + z[k]

    anum0 = [num0,num0]
    anum1 = [num1,num1]
    C[0] = np.divide(t0,anum0)
    C[1] = np.divide(t1,anum1)
    print(C[0])
    print(C[1])


for k in range (0,50):
    if(U[k] == 0):
        plt.scatter(z[k][0], z[k][1], c='red')
    else:
        plt.scatter(z[k][0], z[k][1], c='blue')
plt.scatter(C[0][0],C[0][1],marker='^',c='red')
plt.scatter(C[1][0],C[1][1],marker='^',c='blue')

plt.show()
