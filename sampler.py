import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand
from tqdm import tqdm

'''assumptions:
Inputs:
 a Gaussian function in 1D 
 the initial point
 number of steps to take (time/length of chain), integer
 maximum step size?

 Outputs:
 chain of x values that the sampler walked, an arrray

'''

def samplefromGaussian(function, maxstep, initialpoint, numsteps):
    #make output chain array
    outputchain=np.zeros(numsteps)

    #start at initial point
    outputchain[0]=initialpoint

    #for each time step: propose a step at time t/next step
    for time in tqdm(range(1,numsteps)):
        #do I need a maximum step size?
        proposed=outputchain[time-1]+rand.uniform(-maxstep,maxstep)

        #check if step point is higher probability
        if np.log(function(proposed)) > np.log(function(outputchain[time-1])):
            outputchain[time]=proposed
        else:
            #if not, draw from uniform y~[0,1] and if y<p1/po move if y>p1/p0 dont move
            #store this xvalue in the output chain array
            y=np.log(rand.uniform())
            if y < np.log(function(proposed)) - np.log(function(outputchain[time-1])):
                outputchain[time]=proposed
            else: 
                outputchain[time]=outputchain[time-1]


#store this xvalue in the output chain array
    #return the outputchain
    return outputchain
