import numpy as np
from scipy import optimize
from scipy import integrate
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('fit_data.csv')

xd=np.array(data['x'])
yd=np.array(data['y'])

    
x = xd
y = yd
print(y)

ey1= np.sqrt(y)


plt.errorbar(x,y, yerr=ey1, fmt='o' )
plt.xlabel('X')
plt.ylabel('Y')


plt.show()
