import numpy as np
import matplotlib.pyplot as plt

N = 1000
xTrue = np.linspace(1, 1000, N)
yTrue = 0.5 * xTrue
xData = xTrue + np.random.normal(0, 150, N)
yData = yTrue + np.random.normal(0, 150, N)
xData = np.reshape(xData, (N, 1))
yData = np.reshape(yData, (N, 1))
data = np.hstack((xData, yData))

mu = data.mean(axis=0)
data = data - mu
eigenvectors, eigenvalues, V = np.linalg.svd(data.T, full_matrices=False)


fig, ax = plt.subplots()
ax.scatter(xData, yData)

start, end = mu, mu + eigenvalues[0] * eigenvectors[0] / 15
ax.annotate(
    '', xy=end, xycoords='data',
    xytext=start, textcoords='data',
    arrowprops=dict(facecolor='red', width=1.0))


start, end = mu, mu + eigenvalues[1] * eigenvectors[1] / 15

ax.annotate(
    '', xy=end, xycoords='data',
    xytext=start, textcoords='data',
    arrowprops=dict(facecolor='red', width=1.0))

ax.set_aspect('equal')
plt.grid()
plt.show()
