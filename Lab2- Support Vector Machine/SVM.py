import numpy as np
import random
import math
from scipy.optimize import minimize
import matplotlib.pyplot as plt


# Data sample generations
np.random.seed(100)
classA = np.concatenate((np.random.randn(10, 2) * 0.6 + [1.5, 0.5], np.random.randn(5, 2) * 0.3 + [-1.5, 0.5], np.random.randn(5, 2) * 0.7 + [0.5, -1.0],))
classB = np.random.randn(20, 2) * 0.3 + [0.0, -0.5]
inputs = np.concatenate((classA, classB))
targets = np.concatenate((np.ones(classA.shape[0]), -np.ones(classB.shape[0])))
N = inputs.shape[0] # Number of rows (samples)
permute = list(range(N))
random.shuffle(permute)
inputs = inputs[permute, :]
targets = targets[permute]

def linear_kernel(x, y):
    return np.dot(x, y)

def polynomial_kernel(x, y, p=3):
    return np.power((np.dot(x, y) + 1), p)

def RBF(x, y, smoothness=2):
    return np.exp(-math.pow(np.linalg.norm(x-y), 2)/(2*smoothness**2))

def objective(alpha):
    return (1/2) * np.dot(alpha, np.dot(alpha, P)) - np.sum(alpha)

def zerofun(alpha):
    return np.dot(alpha, targets)

cur_kernel = RBF

P = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        P[i,j] = targets[i] * targets[j] * cur_kernel(inputs[i], inputs[j])

def calc_b(support_vectors):
    b = 0
    s = support_vectors[0]
    for ai, xi, ti in support_vectors:
        b += ai * ti * cur_kernel(xi, s[1])
    b -= s[2]
    return b
        
def indicator(s, support_vectors, b):
    ind = 0
    for ai, xi, ti in support_vectors:
        ind += ai * ti * cur_kernel(s, xi)
    ind -= b
    return ind

C = 1
XC={'type':'eq', 'fun':zerofun}
B = [(0, C) for b in range(N)]
start = np.zeros(N)

ret = minimize(objective, start, bounds=B, constraints=XC)
alpha = ret['x']


# # Plotting
# plt.plot([p[0] for p in classA], [p[1] for p in classA], 'b.')
# plt.plot([p[0] for p in classB], [p[1] for p in classB], 'r.')
# plt.axis('equal') # Force same scale on both axes
# plt.savefig('svmplot.pdf')# Save a copy in a file
# plt.show() # Show the plot on the screen


#Extract the non-zero alpha values
threshold = 1e-5 #10^-5
# support_vectors = [(alpha[i], inputs[i], targets[i]) for i in range(N) if abs(alpha[i]) > threshold]
support_vectors = []

for i, a in enumerate(alpha):
    if threshold < a < C:
        support_vectors.append((a, inputs[i], targets[i]))




b = calc_b(support_vectors)



xgrid = np.linspace(-5, 5)
ygrid = np.linspace(-4, 4)
grid = np.array([[indicator([x, y], support_vectors, b) for x in xgrid] for y in ygrid])
plt.plot([p[0] for p in classA], [p[1] for p in classA], 'b.')
plt.plot([p[0] for p in classB], [p[1] for p in classB], 'r.')
plt.contour(xgrid, ygrid, grid, (-1.0, 0.0, 1.0), colors=('red', 'black', 'blue'), linewidths=(1, 3, 1))
plt.title("Polynomial kernel (degree 3)")
plt.show()