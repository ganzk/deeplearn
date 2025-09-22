import matplotlib.pyplot as plt
import numpy as np
import math
import activationFunction as af

# 阶跃函数
# x = np.arange(-5.0, 5.0, 0.1)
# y = af.step_function_numpy(x)

# sigmoid 函数
# x = np.arange(-10, 10)
# y = af.sigmoid(x)

# ReLU函数
x = np.arange(-10, 10)
y = af.relu(x)

# softmax 函数
# x = np.arange(-10, 10)
# y = af.softmax(x)

# 函数图像
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # 指定y轴的范围
plt.show()


