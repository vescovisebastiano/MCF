import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import constants, fft, optimize

data1 = pd.read_csv('data_sample1.csv')
data2 = pd.read_csv('data_sample2.csv')
data3 = pd.read_csv('data_sample3.csv')


freq1=np.array(data1['meas'])
tem=np.array(data1['time'])
freq2=data2['meas'].values #fa la stessa cosa dell'altro comando
freq3=np.array(data3['meas'])

plt.plot(tem, freq1, color='grey')
plt.plot(tem, freq2, color='pink')
plt.plot(tem, freq3,  color='red')

plt.xlabel('t')
plt.ylabel('freq')

plt.show()

#fare trasformata e freq

a=0.5 #quando uso la tf reale devo fare *0.5 (non mio caso)
tf1=fft.fft(freq1)
tf2=fft.fft(freq2)
tf3=fft.fft(freq3)
ftf1 = fft.fftfreq(len(tf1), d=1)
ftf2 = fft.fftfreq(len(tf1), d=1)
ftf3 = fft.fftfreq(len(tf1), d=1)

#Grafico spettro di potenza (modulo quadro)
y1=[()]
y1=np.absolute(tf1[:tf1.size//2])**2
y2=[()]
y2=np.absolute(tf2[:tf2.size//2])**2
y3=[()]
y3=np.absolute(tf3[:tf3.size//2])**2

x1=ftf1[:len(ftf1)//2] #il primo è zero

plt.plot(x1,y1, 'o', markersize=4, color='grey') #prendo solo la prima metà dei dati, la seconda è speculare
plt.plot(x1,y2, 'o', markersize=4, color='pink')
plt.plot(x1,y3, 'o', markersize=4, color='red')
plt.xscale('log')
plt.yscale('log')
plt.show()

#fare fit

def fpow(x, b, c):
    return  b/(x**c)

x1=x1[50:]
y1=y1[50:]
y2=y2[50:]
y3=y3[50:]

pstart = np.array([1, 1])
params1, params_covariance1 = optimize.curve_fit(fpow, x1, y1, p0=[pstart])
print('params1', params1 )

params2, params_covariance2 = optimize.curve_fit(fpow, x1, y2, p0=[pstart])
print('params2', params2 )

params3, params_covariance3 = optimize.curve_fit(fpow, x1, y3, p0=[pstart])
print('params3', params3 )

yteste1=fpow(x1,params1[0], params1[1])
yteste2=fpow(x1,params2[0], params2[1])
yteste3=fpow(x1,params3[0], params3[1])

plt.plot(x1, yteste1, color='grey')
plt.plot(x1, yteste2, color='pink')
plt.plot(x1, yteste3, color='red')
plt.xscale('log')
plt.yscale('log')

plt.show()



        
