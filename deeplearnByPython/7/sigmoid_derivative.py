import numpy as np
import matplotlib.pyplot as plt
import math

def sigmoid(x):
    return 1 / (1 + math.e ** (-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

# 绘制 sigmoid 函数及其导数
x = np.linspace(-10, 10, 1000)
y_sigmoid = sigmoid(x)
y_deriv = sigmoid_derivative(x)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x, y_sigmoid, 'b-', linewidth=2, label='Sigmoid')
plt.xlabel('x')
plt.ylabel('σ(x)')
plt.title('Sigmoid 函数')
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, y_deriv, 'r-', linewidth=2, label="Sigmoid'")
plt.xlabel('x')
plt.ylabel("σ'(x)")
plt.title('Sigmoid 导数')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()