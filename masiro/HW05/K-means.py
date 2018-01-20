#K-Means Clustering
#2017-05-24

import numpy as np
import random
from matplotlib import pyplot as plt
from matplotlib import cm as cm

def getDistance(a,b):
    d = np.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    return d


#num = random.randrange(1,10) #1 이상 10미만

a = np.random.randint(25,85,(40,2))
b = np.random.randint(90,150,(40,2))
C = [] #Centroid
D = [] # distance_of_data

z = np.vstack((a,b))
z = np.float32(z)
U = np.zeros(80)

K = int(input("K값을 입력해주세요 : "))

for k in range(0,K):
    centroid = np.array([random.randrange(25,85), random.randrange(25,85)])
    C.append(centroid)



for iter in range(0,20):

    num = []
    TD = []

    for k in range(0,K):
        t = np.array([0, 0])
        TD.append(t)
        num.append(0)

    for k in range(0,80):
        mind = getDistance(z[k], C[0])
        index = 0
        for x in range(0,K):
            d = getDistance(z[k],C[x])
            D.append(d)
            if d < mind:
                index = x
                mind = d

        U[k] = index
        num[index] = num[index] + 1
        TD[index] = TD[index] + z[k]

    for k in range(0,K):
        if num[k]!= 0:
            temp = [num[k],num[k]]
            C[k] = np.divide(TD[k],temp)

cm = cm.get_cmap('RdYlBu')
colors=[cm(1.*i/20) for i in range(20)]

for k in range (0,80):
    for x in range(0,K):
        if(U[k] == x):
            plt.scatter(z[k][0], z[k][1],c=colors[x])

for k in range(0,K):
    plt.scatter(C[k][0],C[k][1],marker='^',c=colors[k])

plt.show()
