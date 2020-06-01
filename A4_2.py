# Assignment 4
# numpy.random.rand()
import numpy as np
import matplotlib.pyplot as pt
import time

x=[]
t1=time.perf_counter()
for i in range(10000):
 x+=[np.random.rand()]
t2=time.perf_counter()
print("Total time taken to generate 10000 random numbers : ",t2-t1)

pt.hist(x,range=(0,1.0),density=True,label="histogram")
pt.plot([0,1],[1,1],'r--',label="distribution")
pt.xlabel("bins");pt.ylabel("Normalised number of random numbers")
pt.title("numpy.random.rand()")
pt.legend()
pt.show()
