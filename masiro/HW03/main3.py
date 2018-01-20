import numpy as np
import random
import functions as ft

xy = np.loadtxt('ex2data1.txt',unpack = True, dtype = 'float32', delimiter=',')

x_data = xy[:-1]
y_data = xy[-1]

n, m = x_data.shape
x_data = np.vstack((np.ones(m), x_data))

w0 = random.uniform(-1.0, 1.0)
w1 = random.uniform(-1.0, 1.0)
w2 = random.uniform(-1.0, 1.0)

W = [w0, w1, w2]

cost, grad, W = ft.costFunction(W, x_data, y_data)

x1 = np.arange(0, 100)
x2 = -(W[0] + W[1] * x1) / W[2]

accuracy, error = ft.accuracy(W, x_data, y_data)

print("총 테스트 개수 : %d" % m)
print("오류 개수 : %d" % error)
print("정확도  : %f" % accuracy)
print("Logistic Regression을 이용한 예측 프로그램\n")

while(True):

    score1 = float(input("Score 1 점수 입력 : "))
    score2 = float(input("Score 2 점수 입력 : "))

    if(score1 ==0 and score2 ==0):
        break
    h = W[0] + W[1] * score1 + W[2] * score2

    if(h >0):
        print("합격")
    else:
        print("불합격")

    progress = int(input("\n계속하시겠습니까? (1/0) "))
    print("\n")
    if(progress == 0):
        break