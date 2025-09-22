import math
import numpy as np

# 激活函数  最重要的是权重 偏置   权重 偏置是通过训练得到的数据
# 关心重要信息，以及重要的程度

# 阶跃函数
# 这种写法不接受numpy数组,k > 5是一个数组，不是一个布尔值
def step_function(k):
    if k > 5:
        return 1
    else:
        return 0
def step_function_numpy(k):
    # 对于numpy广播功能，如果在标量和NumPy数组之间进行运算，则标量会和NumPy数组的各个元素进行运算
    z = k > 0
    return z.astype(int)


# sigmoid 函数
def sigmoid(x):
    return 1 / (1 + math.e ** (-x))


# ReLU函数
def relu(x):
    return np.maximum(0, x)


# 恒等函数
def identity_function(x):
    return x


# softmax函数   输出总和为1是softmax函数的一个重要性质
# 因为和为1 每个输出值代表该神经元对应类别的概率。
# 单调递增函数
# 所以 索引 x 的大小影响这y大小,如果只是输出一个最大概率，其实只看x里面最大的数值就行，这种情况输出层这个函数可以省略
def softmax(x):
    # 防止数值过大
    c = np.max(x)
    exp_x = np.exp(x-c)
    sum_exp_a = np.sum(exp_x)
    y = exp_x / sum_exp_a
    return y