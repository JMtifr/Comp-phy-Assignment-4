# Assignment 4
# Problem 7
# Chi square test
import numpy as np
from scipy.stats import chi2 

# scores and expected values of dice roll
o1=[4,10,10,13,20,18,18,11,13,14,13] # set 1
o2=[3,7,11,15,19,24,21,17,13,9,5] # set 2
nps=np.array([1/36.0,2/36.0,3/36.0,4/36.0,5/36.0,6/36.0,5/36.0,4/36.0,3/36.0,2/36.0,1/36.0])*np.sum(o1) # expectation values
# applying chi square test
v1=0;v2=0
for i in range(11):
 v1=(o1[i]-nps[i])**2/nps[i]+v1
 v2=(o2[i]-nps[i])**2/nps[i]+v2
c1=1.0-chi2.cdf(v1,10)
c2=1.0-chi2.cdf(v2,10)

# result of chi-square test
def result(x):
 if x<1.0 or x>99.0:
  return("not sufficiently random")
 elif (x>=1.0 and x<5.0) or (x>95.0 and x<=99.0):
  return("suspect")
 elif (x>=5.0 and x<10.0) or (x<=5.0 and x>90.0):
  return("almost suspect")
 else:
  return("sufficiently random")
print("Random numbers in simulation 1 are ::",result(c1*100))
print("Random numbers in simulation 2 are ::",result(c2*100))
