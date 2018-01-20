import numpy as np
import module
import random

file = open("bmi.txt","r")

data = file.readlines()

Input = np.array([])
Output = np.array([])

for i in data:
    list = i.split("/")
    value = float(list[0])
    Input = np.append(Input,value)
    list2 = list[1].split("\n")
    progression = float(list2[0])
    Output = np.append(Output,progression)

w = random.randomrange(-5,5)
b = random.randomrange(-5,5)

theta = [b , w] # theta0 = b theta1 = w
alpha = 0.1
temp = theta

for i in range(0,2000):
    theta[0] = module.GradientDescent2(Input,Output,theta,alpha,0)
    theta[1] = module.GradientDescent2(Input,Output,theta,alpha,1)
    if abs(temp[0] - theta[0] < 0.0002 and temp[1] - theta[1] < 0.0002):
        alpha += 0.001
    elif abs(temp[0] - theta[0] > 0.0002 and temp[1] - theta[1] > 0.0002):
        alpha -= 0.001
    else:
        alpha = alpha

while(True):
    print("1 : 입력 0 : 종료 ")
    a = int(input("입력 : "))
    if a == 1:
        bmi = float(input("Please input bmi : "))
        progression = theta[1] * bmi  + theta[0]
        print("progression  = %.2f" %progression)
    else:
        break

