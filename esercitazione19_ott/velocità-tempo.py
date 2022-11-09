import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import integrate
mydata= pd.read_csv('vel_vs_time.csv')
vv=mydata['v']
tt=mydata['t']
plt.plot(tt,vv,color='gainsboro')
plt.xlabel('tempi (s)')
plt.ylabel('velocità')
plt.show()
def spazio (i):
    
    s= integrate.simpson(vv[:i],tt[:i])
    return s
print(spazio(10))
print(spazio(23))
print(spazio(90))
spaces=np.zeros(len(tt))
for i in range (1,len(tt)):
    spaces[i]=spazio(i)
plt.plot(tt,spaces,color='hotpink')
plt.show()

