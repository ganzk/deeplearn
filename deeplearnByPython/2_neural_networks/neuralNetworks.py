import numpy as np
import math
import activationFunction as af

# 3层神经网络实现
# 第一层
X = np.array([1, 2])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])
A1 = np.dot(X, W1) + B1
Z1 = af.sigmoid(A1)
print(A1)
print(Z1)

# 第二层
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])
A2 = np.dot(Z1, W2) + B2
Z2 = af.sigmoid(A2)
print(A2)
print(Z2)

# 输出层
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])
A3 = np.dot(Z2, W3) + B3
Z3 = af.identity_function(A3)
print(A3)
print(Z3)