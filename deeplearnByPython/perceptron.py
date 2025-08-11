# 感知机
import numpy as np

# 与门
def AND(x1, x2):
    w1, w2, theta = 1, 1, 2
    if x1 * w1 + x2 * w2 >= theta:
        return 1
    else:
        return 0


# 非门
def NON(x):
    return 1-x

# 或门
def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, -0.2
    if theta + x1 * w1 + x2 * w2 >= 0:
        return 1
    else:
        return 0