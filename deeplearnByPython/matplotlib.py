import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0, 10)

# y = 1 / (1 + math.e ** (-x))
# y = x ** 2
y =  2 * x

plt.plot(x, y)

plt.show()