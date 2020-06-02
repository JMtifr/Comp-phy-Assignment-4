# Assignment 4
# problem 10
# data fitting

import numpy as np
from scipy.optimize import minimize
import emcee
import corner
import matplotlib.pyplot as pt


# reading data from file
index,x,y,sigma_y =np.loadtxt("/media/jibak/Data/JIBAK/GS/Computational physics/aSSIGNMENT 4/data.txt", delimiter='&',usecols=(0,1,2,3),unpack=True)

# defining useful functions
def log_likelihood(theta, x, y, yerr): # Gaussian likehood
 a,b,c = theta
 model = a*x*x+b*x+c
 sigma2 = yerr**2
 return 0.5 * np.sum((y - model) ** 2 / sigma2 + np.log(2 * np.pi * sigma2))

def log_prior(theta): # uniform prior
 a,b,c=theta
 if -100.0 < a < 100.0 and -500.0 < b < 500.0 and -1000<c<1000: 
  return 0.0
 else:
  return -np.inf

def log_probability(theta, x, y, yerr): # probability function for emcee.EnsembleSampler
 lp = log_prior(theta)
 if not np.isfinite(lp):
  return -np.inf
 return lp - log_likelihood(theta, x, y, yerr)

# taking initial a,b,c after optimizing likehood
guess = (1.0, 1.0,1.0)
soln = minimize(log_likelihood,guess,args=(x, y, sigma_y))

# MCMC using 50 Markov chain of 4000 steps using emcee library
nwalkers, ndim = 50,3
pos = soln.x + 1e-4 * np.random.randn(nwalkers, ndim) # initialising Markov chains near optimized a,b,c
sampler = emcee.EnsembleSampler(nwalkers,ndim,log_probability,args=(x, y, sigma_y))
sampler.run_mcmc(pos,4000) # running MCMC of 4000 steps
samples = sampler.get_chain() # samples array has shape(4000,50,3)
labels=["a","b","c"]

# Median and 1-sigma uncertainty of a,b,c from MCMC samples
# best fit model is the [0]th element of sampler got from minimize()
medians = np.median(samples, axis=0)
sigma1=medians-np.percentile(samples,84,axis=0)
sigma2=np.percentile(samples,16,axis=0)
print("Best fit parameter values with one-sigma uncertainty :-\n","========================================================\n")

for i in range(3):
 print("Parameter value : ",labels[i]," = ",medians[0][i]," | 1-sigma + = (",sigma1[0][i],") ,1-sigma - = (",sigma2[0][i],")")
 print("_________________________________________________________________________________________________________________")

# plotting Markov chains
f1,(ax1,ax2,ax3)=pt.subplots(nrows=3, ncols=1, sharex=True,tight_layout=True)
f1.suptitle("Markov chains")
ax1.semilogx(samples[:, :, 0]) # a values
ax1.set_ylabel("a")
ax2.semilogx(samples[:, :, 1]) # b values
ax2.set_ylabel("b")
ax3.semilogx(samples[:,:,2]) # c values
ax3.set_ylabel("c")
ax3.set_xlabel("steps")
pt.show()

# plotting posterior PDFs using corner library
a_true=medians[0][0]; b_true=medians[0][1]; c_true=medians[0][2]
flat_samples = sampler.get_chain(flat=True)
f2 = corner.corner(flat_samples,labels=labels,truths=[a_true, b_true, c_true])
f2.suptitle("Posterior PDFs")
pt.show()

# Plotting best fit and 200 models
x0=np.linspace(47,287,101)
inds = np.random.randint(len(flat_samples), size=200)
f3,ax=pt.subplots(nrows=1,ncols=1,tight_layout=True)
for i in inds:
    sample = flat_samples[i]
    ax.plot(x0,sample[0]*x0*x0+sample[1]*x0+sample[2],'y-')
ax.plot(x0,sample[0]*x0*x0+sample[1]*x0+sample[2],'y-',label="Model")
ax.plot(x0,a_true*x0*x0+b_true*x0+c_true,'k-',label="Best fit")
ax.errorbar(x,y,yerr=sigma_y,fmt='.k')
ax.set_title("Fitting curves")
pt.legend()
pt.show()
