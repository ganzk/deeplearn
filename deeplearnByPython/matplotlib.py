import matplotlib.pyplot as plt
import numpy as np
import math

arr = np.arange(1, 100000)
reciprocals = [1/x for x in arr]
# y = 1 / (1 + math.e ** (-x))
# y = x ** 2
# y =  2 * x
y = np.sin(reciprocals)

plt.plot(reciprocals, y)

plt.show()