import matplotlib.pyplot as plt
import numpy as np
import random
import module
Input = np.array([0,1,2,3,4,5])
Output = np.array([1,2,3,4,5,6])

w = random.randomrange(-5,5)
b = random.randomrange(-5,5)

theta = [b , w] # theta0 = b theta1 = w
alpha = 0.1
for i in range(0,1000):
    theta[0] = module.GradientDescent2(Input,Output,theta,alpha,0)
    theta[1] = module.GradientDescent2(Input,Output,theta,alpha,1)

print(theta[0])
print(theta[1])

h = module.hypothesis(theta[1],theta[0],Input)
plt.plot(Input,Output,'or-')
plt.plot(Input,h,'ob-')
plt.show()

