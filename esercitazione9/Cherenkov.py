import numpy as np 
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import reco as r


dati0=pd.read_csv('hit_times_M0.csv')
dati1=pd.read_csv('hit_times_M1.csv')
dati2=pd.read_csv('hit_times_M2.csv')
dati3=pd.read_csv('hit_times_M3.csv')

plt.hist(dati0['hit_time'], bins=100)
plt.show()

deltaT=np.diff(dati0['hit_time'].values)
mask=deltaT>0
logdelta=np.log10(deltaT[mask])
plt.hist(logdelta ,bins=100)
plt.show()

def insiemehit(mod,sens,time):
    ii=(len(time))
    hits=np.empty(0)
    hits=np.append(hits,[r.Hit(mod[i],sens[i],time[i]) for i in range(ii)])
    return hits

hits0=insiemehit(dati0['mod_id'].values,dati0['det_id'].values,dati0['hit_time'].values)
hits1=insiemehit(dati1['mod_id'].values,dati1['det_id'].values,dati1['hit_time'].values)
hits2=insiemehit(dati2['mod_id'].values,dati2['det_id'].values,dati2['hit_time'].values)
hits3=insiemehit(dati3['mod_id'].values,dati3['det_id'].values,dati3['hit_time'].values)


hits=np.append(hits0,hits1)
hits=np.append(hits,hits2)
hits=np.append(hits,hits3)

hits=np.sort(hits)

deltatimes=np.diff(hits).astype(np.float64)
mask2=deltatimes>0
logdelta=np.log10(deltatimes[mask2])
plt.hist(logdelta,bins =50)
plt.show()

def insieme_eventi(array_hit):
    totale=np.empty(0)
    deltat=10**3
    deltas=np.diff(array_hit).astype(np.float64)
    maske=deltas>0
    logdeltas=np.log10(deltas[maske])
    ris=np.empty(0)
    for j in range(len(array_hit)):
        if (logdeltas[j]<deltat):
            ris=np.append(ris,array_hit[j])
            evento=r.Event(len(ris),ris[0].timestamp,ris[len(ris)-1].timestamp,ris[len(ris)-1].timestamp-ris[0].timestamp,ris)
            totale=np.append(totale,evento)
    return totale

insieme=insieme_eventi(hits)
for i in range (10):
    print(insieme[i])





            
        
