# 卷积层
import numpy as np
from im2ccol import im2col

# 生成4维数据
# x = np.random.randn(10,1,28,28)
# print(x.shape) # 四维数据
# print(x[0].shape) # 三维数据
# print(x[0,0].shape) # 二维数据
# print(x[0,0,0].shape) # 一维数据



# x2 = np.random.rand(2, 2, 4, 4)
x2 = np.random.randint(low=1, high=31, size=(2, 2, 4, 4))
print(x2)
inCol = im2col(x2,2,2,2,0)
print(inCol.shape)
print(inCol)


class Convolution:
    def __init__(self, W, b, stride=1, pad=0):
        self.W = W
        self.b = b
        self.stride = stride
        self.pad = pad
    def forward(self, x):
        FN, C, FH, FW = self.W.shape
        N, C, H, W = x.shape
        out_h = int(1 + (H + 2*self.pad - FH) / self.stride)
        out_w = int(1 + (W + 2*self.pad - FW) / self.stride)
        col = im2col(x, FH, FW, self.stride, self.pad)
        ## 简单展开，也可以用im2col函数，不过乘的是需要取转置
        col_W = self.W.reshape(FN, -1).T # 滤波器的展开
        out = np.dot(col, col_W) + self.b
        # 输出数据，通过reshape和transpose 还原形状
        out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)
        return out
