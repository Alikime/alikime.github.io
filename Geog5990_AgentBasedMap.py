# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 01:23:45 2019

@author: Baba Gana Modu
@version: 001

Required Function: distance_between
"""
import random
import matplotlib.pyplot
from distance_between import distance_between

#This defines the number of agents we have 
num_of_agents = 20 
num_of_iterations = 100 
agents = []

# Make the agents.
for i in range(num_of_agents):
    #created a list with num_of_agents coordinates 
        agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
    #This iterations moves our agent's coordinates based on the number of times defined
for j in range(num_of_iterations):
        for i in range(num_of_agents):

            if random.random() < 0.5:
            #make our agent coordinations change an arbitrary number of times.
                agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100


answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)



# Change location of agent.
if random.random() < 0.5:
        agents[i][0] += 1
else:
        agents[i][0] -= 1
# Check the location of agent and adjust if off edge.
if agents[i][0] < 0:
        agents[i][0] = 0
if agents[i][1] < 0:
        agents[i][0] = 0
if agents[i][0] > 99:
        agents[i][0] = 99
if agents[i][1] > 99:
        agents[i][0] = 99
    
if random.random() < 0.5:
        agents[i][0] = (agents[i][0] + 1) % 100
else:
        agents[i][0] = (agents[i][0] - 1) % 100
    
distance = distance_between(agents[0], agents[1])
matplotlib.pyplot.show()
    #To plot multiple agent coordinates
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
        matplotlib.pyplot.show()
