#random walk asimmetrico

import sys
import numpy as np
import scipy 
import matplotlib.pyplot as plt

def cum_fi(x):
    return 1/2*(1-np.cos(x/2))                                                   

def cuminv_fi(y):
    return 2*np.arccos(1-2*y)

yy=np.random.random(10000) #distribuzione randomica di valori

plt.hist(cuminv_fi(yy), bins=1000, range=(0,6.3), color='orange') #viene come un seno
plt.show()

def ran_walk (n, s):
    walk=np.random.uniform(low=0, high=1, size=n) #è la probabilità, deve variare tra 0 e 1
    x=np.array([0])
    y=np.array([0])
    xtot=0
    ytot=0
    for i in walk:
        xtot=xtot+s*np.cos(cuminv_fi(i))
#al posto di i gli do la cumulativa, così che i risultati seguano quella probabilità
        x=np.append(x, xtot)
        ytot=ytot+s*np.sin(cuminv_fi(i))
        y=np.append(y, ytot)
        xy=np.array([x, y])
    return xy

st=1
num=1000
for i in range(6):
     cam=ran_walk(num, st)
     plt.plot(cam[0], cam[1])
plt.show()

