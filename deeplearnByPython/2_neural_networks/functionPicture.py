import matplotlib.pyplot as plt
import numpy as np
import math
import activationFunction as af

arr = np.arange(0, 10)
# reciprocals = [1/x for x in arr]
reciprocals = [2.0, 1.0, 0.1]
# y = 1 / (1 + math.e ** (-x))
# y = x ** 2
# y =  2 * x
# y = np.sin(reciprocals)
fun = af.softmax(reciprocals)
print(fun)
y = fun

plt.plot(reciprocals, y)

plt.show()