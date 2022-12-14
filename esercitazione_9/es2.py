import sys, os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

sys.path.append('/home/sv010007/MCF/esercitazione_9')

import eco

M0=pd.read_csv('hit_times_M0.csv')
M1=pd.read_csv('hit_times_M1.csv')
M2=pd.read_csv('hit_times_M2.csv')
M3=pd.read_csv('hit_times_M3.csv')
def leggi_e_crea_hit(file):
    t=file['hit_time'].values
    d=file['det_id'].values
    m=file['mod_id'].values
    a0=np.empty(0)
    for i in range(0, np.size(t)):
       a0=np.append(a0, np.array([eco.hit(m[i], d[i], t[i])]))
    return a0
#creazione array di hit
hit1=leggi_e_crea_hit(M0)
hit2=leggi_e_crea_hit(M1)
hit3=leggi_e_crea_hit(M2)
hit4=leggi_e_crea_hit(M3)

#ordinare hit in base al tempo
hitot=np.concatenate((hit1,hit2,hit3,hit4))
hitot.sort(kind='mergesort')
print(hitot)

'''Produca un istogramma dei deltat() fra reco.Hit consecutivi
Come stabilire la finestra temporale da applicare ai deltat che permetta di raggruppare gli Hit dello stesso evento ma sepaari quelii apparteneti ad eventi differenti?'''
for i in hitot
temtot=([])
for i in hitot:
    temtot=np.append(temtot, i.time)

a=np.diff(temtot)
mask= c>0
c=np.log10(b[mask])
plt.hist(c, bins=50)
plt.show()



