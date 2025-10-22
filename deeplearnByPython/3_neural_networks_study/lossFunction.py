import numpy as np

# 均方误差函数
def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

# 交叉熵误差函数
def cross_entropy_error(y, t):
    delta = 1e-7 # 为了确保不生成log0,导致无穷大产生报错
    return -np.sum(t * np.log(y + delta))

t = [1, 0, 0]
y = [0.9, 0.1, 0.0]
h = cross_entropy_error(np.array(y), np.array(t))
print(h)