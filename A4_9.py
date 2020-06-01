# Assignment 4
# problem 9
# MCMC uniform distribution (3,7)

import matplotlib.pyplot as pt
from random import random 
from random import uniform

# disired probability distribution
def f(x):
 if x>3 and x<7:
  return(1.0)
 else:
  return(0.0)

# proposal PDF is choosen to be uniform in range [-1,1]
x0=5.0 # initial sample
sample=[5]
n=[0]

# creating samples which follow distribution proportional to f(x)
for i in range(1000):
 x1=x0+uniform(-1.0,1.0) # new sample
 r=random()
 if f(x1)/f(x0)>r:
  x0=x1
 sample+=[x0]
 n+=[i+1]

# plotting result
pt.subplot(2,1,1)
pt.plot(n,sample,c='c',ls='--',marker='3',mec='m')
pt.title("Markov chain")
pt.xlabel("sequence");pt.ylabel("sample value")
pt.subplot(2,1,2)
pt.hist(sample,range=(1,10),bins=40,density=True,label="histogram")
pt.plot([1,3,3,7,7,10],[0,0,0.25,0.25,0,0],'r--',label="Distribution function")
pt.xlabel("bins");pt.ylabel("number density");pt.title("Histogram plot");pt.legend();pt.tight_layout()
pt.show()
