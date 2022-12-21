import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import corner
import emcee
from scipy.optimize import minimize


dati=pd.read_csv("absorption_line.csv")

print(dati)

plt.errorbar(dati["E"],dati["f"],yerr=dati["ferr"])
plt.show()

def funzione_teorica(params, E):
    m,b,alpha,mu,sigma =params
    f=m*E + b + alpha*np.exp(-(E-mu)**2/(2*(sigma**2)))
    return f
m0=-0.2
b0=10
mu0=4.5
alpha0=-5
sigma0=0.5
valori_iniziali=(m0,b0,alpha0,mu0,sigma0)

plt.plot(dati["E"],funzione_teorica(valori_iniziali, dati["E"]))
plt.errorbar(dati["E"],dati["f"],yerr=dati["ferr"])
plt.show()


def loglike_teor(params, E, f,ferr):
    return -0.5*np.sum(((f-funzione_teorica(params,E))/ferr)**2)
def lnprior_teor(params):
    m,b,alpha,mu,sigma=params
    if(-10 < m < 0 and 0<b<20 and 0<mu<10 and -10<alpha<-0 and 0<sigma<2):
        return 0.0
    return -np.inf
def lnprob_teor(params,E,f,ferr):
    lp=lnprior_teor(params)
    lg=loglike_teor(params,E,f,ferr)
    if (np.isfinite(lp) and np.isfinite(lg)):
        return lp+lg
    return -np.inf

                    
nw = 64
valori_partenza=np.array([-1,15,-2,6,1.5])
ndim_teor=len(valori_partenza)
p0=np.array(valori_partenza)+0.01*np.random.randn(nw, ndim_teor)

sampler_teor=emcee.EnsembleSampler(nw,ndim_teor, lnprob_teor, args=(dati["E"].values,dati["f"].values,dati["ferr"].values))

print("Running production...")
sampler_teor.run_mcmc(p0,2000,progress=True)
fig,axes=plt.subplots(ndim_teor, figsize=(11,10),sharex=True)
samples_teor=sampler_teor.get_chain()
labels=["m","b","alpha","mu","sigma"]
for i in range(ndim_teor):
    ax=axes[i]
    ax.plot(samples_teor[:,:,i], "k",alpha=0.3)
    ax.set_ylabel(labels[i])
    ax.set_xlim(0,len(samples_teor))

plt.show()

flat_samples_teor=sampler_teor.get_chain(discard=500,thin=15,flat=True)
plt.errorbar(dati["E"],dati["f"],yerr=dati["ferr"])
for s in flat_samples_teor[np.random.randint(len(flat_samples_teor),size=50)]:
    plt.plot(dati["E"],funzione_teorica(s,dati["E"].values),alpha=0.3)
plt.show()
fig=corner.corner(flat_samples_teor,labels=labels,truths=valori_iniziali)
plt.show()
