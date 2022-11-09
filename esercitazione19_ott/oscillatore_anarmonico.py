import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
xx=np.arange(0,5.05,0.1)
yy=0.6*xx**6
def Periodo(x0):
    zz=1/(np.sqrt(yy[x0]-yy[:x0]))
    T=np.sqrt(8)*integrate.simpson(zz,xx[:x0])
    return T
periodi=np.zeros(len(xx))
for i in range(1,len(xx)):
    print(i,yy[i])
    periodi[i]=Periodo(i)

plt.plot(xx,periodi)
plt.show()
