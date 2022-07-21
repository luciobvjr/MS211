import numpy as np
from matplotlib import pyplot as plt

def F(y): #y'
    f = y**2
    return f

def Euler_explicito():
    h = float(input('h value = '))
    xbar = float(input('x value = '))
    n = xbar / h 
    n = int(n)
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    x[0] = 0
    y[0] = 3

    for i in np.arange(0,n):
        y[i+1] = y[i] + h * F(y[i])
        x[i+1] = x[i] + h
    
    print('Corresponding y value =',y[-1])
    plt.plot(x,y)
    plt.show()

Euler_explicito()