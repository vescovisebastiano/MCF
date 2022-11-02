"""
 Distanza percorsa in funzine del tempo
il file di dati vel_vs_time.csv contiene dei valori di velocitÃƒÂ  in funzione del tempo;
creare uno script python che:
legga il file scaricato;
produca un grafico della velocitÃƒÂ  in funzione del tempo;
calcoli la distanza percorsa in funzopne del tempo (utilizzando scipy.integrate.simpson);
produca il grafico della distanza percorsa in funzione del tempo.
"""
import numpy as np
from scipy import optimize
from scipy import integrate
import matplotlib.pyplot as plt
import pandas as pd

velotem = pd.read_csv('vel_vs_time.csv')

vel=np.array(velotem['v'])
tem=np.array(velotem['t'])

    
ax = tem
ay = vel

plt.plot(ax,ay)
plt.xlabel('t')
plt.ylabel('v')

plt.show()

print(integrate.simps(vel, tem)) #calcolo l'integrale

spa=np.array([0])
for i in range(1, len(vel), 1):
    spa=np.append(spa,integrate.simps(vel[:i], tem[:i])) #dal primo termire all'i_esimo

print(spa)

ax = tem
ay = spa

plt.plot(ax,ay)
plt.xlabel('t')
plt.ylabel('s')

plt.show()





