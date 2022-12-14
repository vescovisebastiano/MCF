import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tab1 = pd.read_csv('tab.csv')

ax1 = gg
ay1=tem
ay2 =mmp

plt.plot(ax1,ay1, label='temperatura')
plt.plot(ax1,ay2, label='mm pioggia')

plt.xlabel('giorni')
plt.ylabel('y')

plt.show()
