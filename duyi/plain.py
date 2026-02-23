import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data_path = r'data.csv'

pd = pd.read_csv('data.csv')


# 数据预处理


# 激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 激活函数导数
def sigmoid_derivative(x):
    return x * (1 - x)

# 损失函数
def loss(y, y_hat):
    return ((y - y_hat) ** 2) * 0.5

# 损失函数导数
def loss_derivative(y, y_hat):
    return y_hat - y




# 权重预处理
def weight_init(input_size, output_size):
    w = np.random.randn(input_size, output_size) * 0.01
    return w

# 偏置预处理
def bias_init(output_size):
    b = np.zeros(output_size)
    return b
# 前向传播
def forward(x, w, b):
    y_hat = np.dot(x, w) + b
    return y_hat
# 反向传播
def backward(x, y, y_hat, w, b):
    m = x.shape[0]
    dz = (1 / m) * (y_hat - y)
    dw = np.dot(x.T, dz)
    db = np.sum(dz)
    return dw, db
# 更新权重
def update(w, b, dw, db, lr):
    w = w - lr * dw
    b = b - lr * db
    return w, b
# 训练
def train(x, y, w, b, lr, epochs):
    for i in range(epochs):
        y_hat = forward(x, w, b)
        dw, db = backward(x, y, y_hat, w, b)
        w, b = update(w, b, dw, db, lr)
        if i % 100 == 0:
            print('epoch: {}, loss: {}'.format(i, loss(y, y_hat)))
    return w, b
# 预测
def predict(x, w, b):
    y_hat = forward(x, w, b)
    return y_hat