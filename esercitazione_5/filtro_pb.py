from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

def Vin1(t):
    if (int(t)%2==0):
        return 1
    else:
        return -1

def fpb(Vout, t, RC):
    return (1/RC)*(Vin1(t)-Vout)

mydf = pd.DataFrame( columns=['t', 'Vin(t)', 'Vout(t,RC1)','Vout(t,RC2)', 'Vout(t,RC3)' ])

voutsol={}
tsol={}
RC1=[1, 0.1, 0.05]
Vin=np.array([])
h=0.1 #passo dell'asse dei tempi

tt = np.arange(0,10,h)


x=tt
y=np.array([])
for i in x:
    k=Vin1(i)
    y=np.append(y, k)
    
plt.plot(x, y)
plt.show()

xo=0 #definisco xo

for i in RC1:

    Voo = np.empty(0)
    Voo = integrate.odeint(fpb, y0=xo, t=tt, args=(i,))
    voutsol.update({i : Voo})
    tsol.update({i : tt})
   
    

mydf['t'] = tt
mydf['Vin(t)'] =y
mydf['Vout(t,RC1)']=voutsol[RC1[0]]
mydf['Vout(t,RC2)']=voutsol[RC1[1]]
mydf['Vout(t,RC3)']=voutsol[RC1[2]]


#plot
fig,ax = plt.subplots(figsize=(9,6))
plt.title('scipy.integrate.odeint ', color='red', fontsize=14)

for i in RC1:
    plt.plot(tsol[i],voutsol[i], label='{:4f} punti'.format(i))

    

mydf.to_csv('mydf.csv', index=True)

plt.xlabel('t')
plt.ylabel('Vout')
plt.legend( fontsize=14)
plt.show()
