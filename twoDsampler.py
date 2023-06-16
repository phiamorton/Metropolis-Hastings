import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand
from tqdm import tqdm

'''assumptions:
Inputs:
2D probability distribution
 
 the initial point, 2D
 number of steps to take (time/length of chain), integer
 maximum step size in each direction

 Outputs:
 chain of x,y values that the sampler walked through, a 2D arrray
'''

def twoDsamplefromGaussian(function, maxstep1, maxstep2, initialpoint, numsteps):
    #make output chain array 2D
    outputchain=np.zeros((numsteps,len(initialpoint)))

    #start at initial point 2D
    outputchain[0][:]=initialpoint

    #for each time step: propose a step at time t/next step
    for time in tqdm(range(1,numsteps)):
        #do I need a maximum step size? yes
        
        #proposed is a 2D location
        proposed=outputchain[time-1]+[rand.uniform(-maxstep1,maxstep1),rand.uniform(-maxstep2,maxstep2)]

        #check if step point is higher probability, function takes 2D input
        if function(proposed) > function(outputchain[time-1]):
            outputchain[time]=proposed
        else:
            #if not, draw from uniform y~[0,1] in 2D and if y<p1/po move if y>p1/p0 dont move
            #store this xvalue in the output chain array
            y=[(rand.uniform()),(rand.uniform())]
            if y[0] < (function(proposed)) - (function(outputchain[time-1])):
                outputchain[time]=proposed
            else: 
                outputchain[time]=outputchain[time-1]


#store this xvalue in the output chain array
    #return the outputchain
    return outputchain
