import perceptron as pt

x1,x2 = 0, 1
print(pt.AND(pt.NON(pt.AND(x1, x2)), pt.OR(x1, x2)))
