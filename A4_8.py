# Assignment 4
# Problem 8
# Monte Carlo integration

import numpy as np
#-------------- defining equations of nth dimentional spheres ----------------------
def s1(x): # eqation of circle in 1st coordinate
 if x<=1.0:
  return(np.sqrt(1.0-x*x))
 else:
  return(0.0)

def s10(r): # equation of 10 dimentional unit splere in 1st coordinate
 rd=np.dot(r,r)
 if rd<=1.0:
  return(np.sqrt(1.0-rd))
 else: 
  return(0.0)
#-----------------------------------------------------------------------------------

# calculating volume of n dim sphere using Monte-Carlo mean value method
# ------circle---------------
f_mean=0.0
for i in range(10000):
 x=np.random.rand()
 f_mean+=s1(x)
f_mean/=10000
A1=4.0*f_mean # area of unit circle 
#----------------------------
#---- 10 dimentional sphere -----------
f_mean=0.0
for j in range(10**6):
 r=np.random.rand(9) # 10^6 vectors of 9 dimention
 f_mean+=s10(r)
f_mean/=10**6
A10=f_mean*2**10 # volume of 10 d unit sphere
#-------------------------------------
print("Using Monte Carlo ")
print("Area of circle : ",A1)
print("Volume of 10 d sphere : ",A10)
