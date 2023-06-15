import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand

'''assumptions:
Inputs:
 a Gaussian function in 1D 
 an array of x values (my grid) over which the probability distribution can be evaluated, 
 this should be large enough to encapsulate all possibilities of x the sampler may walk to
 the initial point, in this case a value of x within the bounds of the x values array
 number of steps to take (time/length of chain), integer

 Outputs:
 chain of x values that the sampler walked, an arrray

'''

def samplefromGaussian(function, xvalues, initialpoint, numsteps):
    #evaluate gaussian at each x point
    probabilities=function(xvalues)
    #make output chain array
    outputchain=np.zeros(numsteps)

    #start at initial point
    outputchain[0]=initialpoint

    #for each time step: propose a step at time t/next step
    for time in range(1,numsteps):
        proposed=outputchain[time-1]+np.rand.uniform(-maxstep,maxstep)


    #check if step point is higher probability

    #if not, draw from uniform y~[0,1] and if y<p1/po move if y>p1/p0 dont move

    #store this xvalue in the output chain array

    #set the x point from this step as the starting point for the next step

    #return the outputchain
    return outputchain
