import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dati=pd.read_csv('oscilloscope.csv')
fig,ax=plt.subplots(1,2, figsize=(12,6))
ax[0].plot(dati['time'],dati['signal1'], color='crimson')                                  
ax[1].plot(dati['time'],dati['signal2'], color='royalblue')
plt.show()
