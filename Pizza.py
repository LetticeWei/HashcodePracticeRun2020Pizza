# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 10:07:47 2020

@author: Wei Lai
"""
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random
import math
from sklearn.preprocessing import normalize


def f(x): # x is a np list consists of zeros and ones
    obj=sliceMaxNum-np.dot(x,pizza_spec) #note global variables!
    return obj
fileHandler=open('d_quite_big.in','r')
listOfLines=fileHandler.readlines()
fileHandler.close()
sliceMaxNum,numOfTypes= map(int,(listOfLines[0][:-1]).split())
pizza_spec = np.array(list(map(int,(listOfLines[1][:-1]).split())))
#obj func

x_start=np.zeros(numOfTypes)

x_start[189:]=1.0 #d

#x_start[5750:]=1.0 #e 


#no need for contour plotS
#simulated annealing
# Number of cycles
n = 100
# Number of trials per cycle
m = 50
# Number of accepted solutions
na = 0.0
# Probability of accepting worse solution at the start
p1 = 0.7
# Probability of accepting worse solution at the end
p50 = 0.001
# Initial temperature
t1 = -1.0/math.log(p1)
# Final temperature
t50 = -1.0/math.log(p50)
# Fractional reduction every cycle
frac = (t50/t1)**(1.0/(n-1.0))
#initialise x
x=np.zeros((n+1,numOfTypes))
x[0]=x_start
xi=np.zeros(numOfTypes)
xi=x_start
na=na+1.0
#current best results so far
xc=np.zeros(numOfTypes)
xc=x[0]
fc=f(xc)
fs=np.zeros(n+1)
fs[0]=fc
#current temp
t=t1
#DeltaE Average
DeltaE_avg=0.0

def flip(original_value,p):
    if random.random() > p:
        return original_value
    else:
        if original_value==0.0:
            return 1.0
        else:
            return 0.0
flip_prob_l=sliceMaxNum/pizza_spec/np.linalg.norm(sliceMaxNum/pizza_spec)

for i in range(n):
    print('Cycle: ' + str(i)+ ' with Temperature: '+str(t))
    for j in range(m):
        #generate new trial points
        for k in range(numOfTypes):
            # let the prob of flipping sign be 0.3, can be changed later
            xi[k]=flip(xc[k],flip_prob_l[k])
        DeltaE=abs(f(xi)-fc)
        if (f(xi)>fc):
            # Initialize DeltaE_avg if a worse solution was found
            #   on the first iteration
            if (i==0 and j==0): DeltaE_avg = DeltaE
            # objective function is worse
            # generate probability of acceptance
            p = math.exp(-DeltaE/(DeltaE_avg * t))
            # determine whether to accept worse point
            if (random.random()<p):
                # accept the worse solution
                accept = True
            else:
                # don't accept the worse solution
                accept = False
        else:
            # objective function is lower, automatically accept
            if f(xi)>0.0:
                accept = True
            else:
                accept = False
        if (accept==True):
            # update currently accepted solution
            for k in range(numOfTypes):
                xc[k] = xi[k]
            fc = f(xc)
            # increment number of accepted solutions
            na = na + 1.0
            # update DeltaE_avg
            DeltaE_avg = (DeltaE_avg * (na-1.0) +  DeltaE) / na 
        # Record the best x values at the end of every cycle
    for k in range(numOfTypes):
        x[i+1][k] = xc[k]
    fs[i+1] = fc
    # Lower the temperature for next cycle
    t = frac * t
    
'''
plt.figure()
plt.plot(fs,'r.-')
plt.legend(['Objective'])
'''
print(min(fs))

x_final=x[list(fs).index(min(list(fs)))]
ordered_spec=[k for k in range(numOfTypes) if x_final[k]==1.0]



with open('d_quite_big_try.txt','w') as f:
    f.write("{}\n".format(len(ordered_spec)))
    for item in ordered_spec:
        f.write("{} ".format(item))


'''
for loop in range(50):
    print(main())
'''








