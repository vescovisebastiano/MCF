import numpy as np
import pandas as pd

gg=np.linspace(1, 30, 30)
temp=np.random.rand(30)
tem=temp*10+20
errtemp=np.random.rand(30)
errtem=errtemp*2+1
mm=np.random.rand(30)
mmp=mm*5
errmmp=np.random.rand(30)


tab = pd.DataFrame( columns=['giorni', 'temperatura', 'err temperatura', 'mmp', 'err mmp'])

tab['giorni'] = gg
tab['temperatura']  = tem
tab['err temperatura']  = errtem
tab['mmp']=mmp
tab['err mmp']=errmmp

print(tab)

esercitazione.py_csv('tab.csv', index=False)




