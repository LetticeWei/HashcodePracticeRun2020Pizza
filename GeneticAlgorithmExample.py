# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:58:24 2020

@author: Wei Lai
"""
#import Pizza
import random
import numpy as np
#Select parents from population
fileHandler=open('c_medium.in','r')
listOfLines=fileHandler.readlines()
fileHandler.close()
global numOfTypes
sliceMaxNum,numOfTypes= map(int,(listOfLines[0][:-1]).split())
pizza_spec = np.array(list(map(int,(listOfLines[1][:-1]).split())))
print(sliceMaxNum)
print(numOfTypes) #len(pizza_spec)=numOfTypes
print(pizza_spec)

pop_size=int(numOfTypes/10)

population=np.zeros((pop_size,numOfTypes))

for i in range(pop_size):
    for j in range(numOfTypes):
        population[i,j]=random.randint(0.0,1.0)

'''
population=Pizza.main()[int(-1*pop_size):]
'''

#Determine fitness of population
def mate(par1,par2,prob_mut):
    child=np.zeros(numOfTypes)
    for k in range(numOfTypes):
        rand_prob=random.random()
        if rand_prob<(1-prob_mut)*0.5: # prob of taking parent1's gene
            child[k]=par1[k]
        elif rand_prob<1-prob_mut: # prob of taking parent2's gene
            child[k]=par2[k]
        else: # chance of mutation prob_mut
            child[k]=random.randint(0.0,1.0)
    return child

#Untill convergence repeat this genetic selection: 
generation=1
max_ite=100
prob_mut=0.10
old_fitness=sliceMaxNum-pizza_spec.dot(population[0])
while generation<max_ite: # ite will be changed later
    #select parents from population
    fitness_l=sliceMaxNum-pizza_spec.dot(np.transpose(population))
    population_with_fitness=list(zip(population, fitness_l))
    sorted_population_with_fitness=sorted(population_with_fitness,key=lambda population_with_fitness:population_with_fitness[1])
    if sorted_population_with_fitness[0][1] ==0: 
        
        x_final=sorted_population_with_fitness[0][0]
        ordered_spec=[k for k in range(numOfTypes) if x_final[k]==1.0]
        print(ordered_spec)
        with open('d_quite_big_genetic.txt','w') as f:
            f.write("{}\n".format(len(ordered_spec)))
            for item in ordered_spec:
                f.write("{} ".format(item))
        break
    # Otherwise generate new offsprings for new generation 
    new_generation = [] 
    # Perform Elitism, that mean elite (default 10%) of fittest population 
    # goes to the next generation 
    elite=generation/max_ite/10
    newbie=0.0
    s = int(pop_size*elite)
    for k in range(s):
        new_generation.append(sorted_population_with_fitness[k][0]) 
    # From gamma (default is 50%) of fittest population, Individuals  
    # will mate to produce offspring 
    gamma=0.5
    s = int(pop_size*(1-elite-newbie))
    '''
    if old_fitness-fitness_l[0]<-100:
        prob_mut*=1.2
    elif old_fitness-fitness_l[0]<100:
        
        prob_mut*=1.1
    elif old_fitness-fitness_l[0]>10000:
        prob_mut*=0.9
    prob_mut=min(0.7,max(prob_mut,0.05))
    '''
    print(prob_mut)
    for _ in range(s):
        parent1 = random.choice(sorted_population_with_fitness[:int(pop_size*gamma)])[0]
        parent2 = random.choice(sorted_population_with_fitness[:int(pop_size*gamma)])[0]
        child = mate(parent1,parent2,prob_mut)
        while sliceMaxNum-pizza_spec.dot(child)<0:
            parent1 = random.choice(sorted_population_with_fitness[:int(pop_size*gamma)])[0]
            parent2 = random.choice(sorted_population_with_fitness[:int(pop_size*gamma)])[0]
            child = mate(parent1,parent2,prob_mut)
        new_generation.append(child)
    newbie_population=np.zeros((int(pop_size*newbie),numOfTypes))
    for i in range(int(pop_size*newbie)):
        for j in range(numOfTypes):
            newbie_population[i,j]=random.randint(0.0,1.0)
    new_generation.extend(newbie_population)
    
    population=new_generation
    print("Generation: {} : Fitness: {}".format(generation,fitness_l[0])) 
    generation += 1
    old_fitness=fitness_l[0]










