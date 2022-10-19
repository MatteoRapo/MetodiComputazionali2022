import matplotlib.pyplot as plt
import numpy as np
xx= np.arange(0, 100, 0.01)
def f(x):
    return x**np.sin(x)
yy=f(xx)

plt.plot(xx,yy)
plt.xlabel('x')
plt.ylabel('x^sinx')
plt.show()
