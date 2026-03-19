import numpy as np
import math


S=3     # 序列长度
Dq=2    # q向量维度
Dk=2    # k向量维度
Dv=3    # v向量维度
Dx=4    # 词向量维度

def softmax(x, axis=None):
    """数值稳定的 Softmax 实现"""
    e_x = np.exp(x - np.max(x, axis=axis, keepdims=True))  # 减去最大值避免溢出
    return e_x / e_x.sum(axis=axis, keepdims=True)


# 初始化输入词向量矩阵，以及Wq、Wk、Wv三个权重矩阵
X=np.array([[0.312, 0.395, -1.343, 2.102],
       [1.232, 2.567, -0.123, 0.838],
       [2.134, -3.123, 0.123, -0.271]])
Wq=np.random.rand(Dx, Dq)
Wk=np.random.rand(Dx, Dk)
Wv=np.random.rand(Dx, Dv)

def self_attention(X):
    # 计算序列X的self_attention
    # 第一步，计算Q、K、V
    Q=np.dot(X,Wq)
    print("=====Q=====")
    print(Q)
    K=np.dot(X,Wk)
    print("=====K=====")
    print(K)
    V=np.dot(X,Wv)
    print("=====V=====")
    print(V)
    # 第二步，计算注意力权重
    A=np.dot(Q,K.T)/math.sqrt(Dq)
    print("=====A=====")
    print(A)
    # 第三步，归一化注意力权重
    AA=softmax(A, axis=1)
    print("=====AA=====")
    print(AA)
    # 第四步，计算v向量加权和
    O=np.dot(AA, V)
    return O

O=self_attention(X)
print(O)