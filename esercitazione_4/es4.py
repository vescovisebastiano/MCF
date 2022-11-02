import numpy as np
from scipy import optimize
from scipy import integrate
import matplotlib.pyplot as plt
import pandas as pd

#definizione funzione, definisca una funzione lognormale da usare per il fit dei dati;

def lognorm(x,s,m,h):
    return h*(np.exp(-((np.log(x)-m)/s)**2))

data = pd.read_csv('fit_data.csv')

xd=np.array(data['x'])
yd=np.array(data['y'])

    
x = xd
y = yd
ey1= np.sqrt(y)

pstart = np.array([1, 1, 1])
params, params_covariance = optimize.curve_fit(lognorm, x, y, p0=[pstart])

print('params', params )
print('params_cov', params_covariance)
print('errori params', np.sqrt(params_covariance.diagonal()))

ytest = lognorm(x, params[0], params[1], params[2])

plt.errorbar(x,y, yerr=ey1, fmt='o')
plt.plot(x, ytest, color='red')
plt.xscale('log') #lo vedo logaritmico
plt.xlabel('X')
plt.ylabel('Y')

chi=0
for i in range(len(y)):
    chi=chi+(ytest[i]-y[i])**2/ytest[i]

print('chi square= ' , chi)

plt.show()
