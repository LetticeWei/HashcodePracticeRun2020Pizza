# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:46:06 2020

@author: Wei Lai
"""
import numpy as np

fileHandler=open('d_quite_big.in','r')
listOfLines=fileHandler.readlines()
fileHandler.close()
sliceMaxNum,numOfTypes= map(int,(listOfLines[0][:-1]).split())
pizza_spec = np.array(list(map(int,(listOfLines[1][:-1]).split())))

# A Dynamic Programming based Python Program for 0-1 Knapsack problem 
# Returns the maximum value that can be put in a knapsack of capacity W 
def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 
  
# Driver program to test above function 
val = pizza_spec
wt = pizza_spec
W = sliceMaxNum
n = numOfTypes
print(knapSack(W, wt, val, n)) 
  