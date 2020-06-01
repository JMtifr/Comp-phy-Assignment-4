# Assignment 4
# linear congruential random number generator
import matplotlib.pyplot as pt
import time

a=321
c=123
x0=1
m=56789
x=[]
# generating 10000 random number
t1=time.perf_counter()
for i in range(10000):
 x1=(a*x0+c)%m # linear congruential method
 x0=x1
 x+=[x1/(m-1)] # divided by m-1 to make number <=1
t2=time.perf_counter()
print("Total time taken to generate 10000 random numbers : ",t2-t1)
pt.hist(x,bins=10, range=(0.0, 1.0), density=True,label="histogram")
pt.plot([0,1],[1,1],'r--',label="distribution")
pt.xlabel("bins");pt.ylabel("normalised number of random numbers")
pt.title("Linear congruential method")
pt.legend()
pt.show()
