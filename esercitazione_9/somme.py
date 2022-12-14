import numpy as np

def sn(n):
    a=0
    for i in range (0, n+1):
        a=a+i
    return a

def srad(n):
    a=0
    for i in range (0, n+1):
        a=a+np.sqrt(i)
    return a

