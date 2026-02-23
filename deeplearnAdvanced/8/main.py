import numpy as np

N, T, H = 10, 5, 4
hs = np.random.randn(N, T, H)
a = np.random.randn(N, T)
ar = a.reshape(N, T, 1).repeat(H, axis=2)
# ar = a.reshape(N, T, 1) # 使用广播

t = hs * ar # 加权

print(t.shape)
# (10, 5, 4)
c = np.sum(t, axis=1) # 求和
print(c.shape)
# (10, 4)