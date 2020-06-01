# Assignment 4
# Rejection method
import numpy as np
import matplotlib.pyplot as pt

def p(x): # intended probability distribution function
 return(np.sqrt(2.0/np.pi)*np.exp(-x*x/2.0))
def f(x): # comparison function
 return(1.0/np.cosh(x))
def F(x): # solution of dx/dy=f(y)
 return(np.arcsinh(np.tan(x)))

# rejection method-------------------------------
x=np.random.rand(10000)  # uniform daviate [0,1)
X=F(np.pi/2.0*x) # random numbers with distribution F(x)
y=np.random.rand(10000)
y=y*f(X)
XP=[]
for i in range(len(y)):
 if y[i]<=p(X[i]):
  XP+=[X[i]] #XP is distributed as p(x)
#------------------------------------------------

xx=np.linspace(0,5,51)
pt.hist(XP,bins=30,range=(0,5),density=True,label="histogram")
pt.plot(xx,p(xx),'r--',label="probability distribution")
pt.xlabel("bins");pt.ylabel("number density");pt.title("rejection method")
pt.legend()
pt.show()
