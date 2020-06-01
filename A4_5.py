#Assignment 4
# problem 5
# box muller method

import numpy as np
import matplotlib.pyplot as pt

def f(x): #  Gaussian distribution with mean 0 and variance 1
 return(np.exp(-x*x/2.0)/np.sqrt(2.0*np.pi))

# x1 & x2 are uniform random numbers in [0,1)
# y1 & y2 will be random numbers with Gaussian distribution

n=10000
x1=np.random.rand(n)
x2=np.random.rand(n)
y1=np.sqrt(-2.0*np.log(x1))*np.cos(2.0*np.pi*x2)
y2=np.sqrt(-2.0*np.log(x1))*np.sin(2.0*np.pi*x2)

x=np.linspace(-4.0,4.0,50)
pt.subplot(1,2,1)
pt.hist(y1,range=(-4,4),density=True, bins=20,label="histogram")
pt.plot(x,f(x),'r--',label="distribution")
pt.xlabel("bins");pt.ylabel("normalised random number density");pt.title("y1")
pt.legend()
pt.subplot(1,2,2)
pt.hist(y2,range=(-4,4),density=True, bins=20,label="histogram")
pt.xlabel("bins");pt.ylabel("normalised random number density");pt.title("y2")
pt.plot(x,f(x),'r--',label="distribution")
pt.legend()
pt.tight_layout()
pt.show()
