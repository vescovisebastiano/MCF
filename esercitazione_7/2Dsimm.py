#random walk in 2 dimensioni

import sys
import numpy as np
import scipy 
import matplotlib.pyplot as plt

def ran_walk (n, s):
    walk=np.random.uniform(low=0, high=2*np.pi, size=n)
    x=np.array([0])
    y=np.array([0])
    xtot=0
    ytot=0
    for i in walk:
        xtot=xtot+s*np.cos(i)
        x=np.append(x, xtot)
        ytot=ytot+s*np.sin(i)
        y=np.append(y, ytot)
        xy=np.array([x, y])
    return xy


st=1
num=1000
for i in range(6):
     cam=ran_walk(num, st)
     plt.plot(cam[0], cam[1])
plt.show()

passi=np.array([10, 100, 1000])
ax=np.array([0])
ay=np.array([0])
for i in range(100): 
        cam=ran_walk(num, st)
        ax=np.append(ax, cam[0][9])
        ax=np.append(ax, cam[0][99])
        ax=np.append(ax, cam[0][999])
        ay=np.append(ay, cam[1][9])
        ay=np.append(ay, cam[1][99])
        ay=np.append(ay, cam[1][999])

plt.plot(ax, ay, 'o')
        
plt.xlabel('x')
plt.ylabel('y')
plt.show()
    
    
    
    
    
