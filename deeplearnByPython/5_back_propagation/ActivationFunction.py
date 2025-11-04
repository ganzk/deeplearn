import numpy as np

# 激活层
class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        return dx


class Sigmoid:
    def __init__(self):
        self.out = None

    # 前向传播
    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        return out

    # 反向传播
    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out
        return dx


# Affine层  加权求和