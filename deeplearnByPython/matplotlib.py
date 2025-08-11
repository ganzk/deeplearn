import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0, 1)

y = 1 / (1 + math.e ** (-x))

plt.plot(x, y)

plt.show()