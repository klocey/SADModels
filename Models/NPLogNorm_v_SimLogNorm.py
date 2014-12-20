import numpy as np
from random import randrange
import matplotlib.pyplot as plt
import sys
import os

mydir = os.path.expanduser("~Nathan_Hillis/SADModels/") # put the path to the repo here (e.g. Ken's desktop has a directory named "repos")

sys.path.append(mydir + "tools") # put a more explicit path here
import pln

sys.path.append(mydir + "Analysis")
from AverageShape import AvgShape



"""
    

"""

def SimLogNorm(N, S, sample_size):
    
    RACs = []  # 'sample' is a function. You don't want to give variables the same name as a function 
    
    while len(RACs) < sample_size:
        RAC = [N] #Initial 
        
        while len(RAC) < S:
            ind = randrange(len(RAC))
            v = RAC.pop(ind) # Removes randomly selected number from list RAC
            v1 = int(round(0.75 * v)) # split 75:25
            v2 = v - v1  # force all abundances to be integers 
            
            if v1 < 1 or v2 < 1: break # force min(RAC) to be > 1
                                            
            RAC.extend([v1, v2]) # add new values to RAC, increaseing len(RAC) by 1
            
        if len(RAC) == S and sum(RAC) == N: # When conditions are met sort and append
            RAC.sort()
            RAC.reverse()
            RACs.append(RAC)
            print len(RACs)
            
    return RACs
    
''' Going from mean to S and N:
    e^(mean) = e^(log(n/s))
    e^(mean) = N/S
    e^(mean) * S = N'''
def npLogNorm(mean, variance, S, sample_size):#will need to change log(ab) to ab
    RACs=[]
    while RACs < sample_size:
        np.random.lognoramal(mean=10, sigma = 1, size =S)
        
    
    
    
sample_size = 25
N = 10000
S = 50
RACs = SimLogNorm(N, S, sample_size)
RAC = AvgShape(RACs) # you (nathan) were leaving this out

MLE = get_LogNormMLE(RAC) #Finding MLE for log-normal for a given N and S (does not return N)

N = sum(MLE)
print 'N =',N,', S =', S

sample_size = 100
RACs = SimLogNorm(N, S, sample_size)

SimLogNorm = AvgShape(RACs) # you (nathan) were leaving this out

x = []
y = []

for RAC in RACs: #Placing SLN RAC values into lists
    y.extend(np.log(RAC))
    x.extend(range(len(RAC)))
    

print len(MLE), sum(MLE), len(RAC), sum(RAC)

plt.hexbin(x, y, mincnt=1, gridsize = 20, bins = 'log', cmap=plt.cm.jet) # Generating Heat Map

plt.plot(np.log(MLE), color='0.3', lw=3, label='MLE: N='+str(N)+', S='+str(S)) # Plot the MLE 

plt.plot(np.log(SimLogNorm), color='Lime', lw=3, label='Simulated N='+str(N)+', S='+str(S)) # Plot the simulated form

leg = plt.legend(loc=1,prop={'size':13}) # plot a legend
leg.draw_frame(False) # don't plot the legend's frame
    

plt.xlim(0, S + 5)
plt.xlabel('Rank in abundance', fontsize=16)
plt.ylabel('log(abundance)', fontsize=16)

plt.savefig('/Users/Nathan_Hillis/SADModels/figures/Debug_Figs/Ploting_MLE_RACs/logNormal_MLEs_RACs_N='+str(N)+'_S='+str(S)+'.png', dpi=600, bbox_inches = 'tight', pad_inches=0.03)
plt.show()