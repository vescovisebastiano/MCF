import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

M0=pd.read_csv('hit_times_M0.csv')

plt.hist(M0['hit_time'], 100)

plt.show()

a=M0['hit_time'].values
b=np.diff(a)
print(np.sort(b))
mask= b>0
c=np.log10(b[mask])
plt.hist(c, bins=50)
plt.show()
