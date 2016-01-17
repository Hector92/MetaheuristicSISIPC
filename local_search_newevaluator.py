#!/usr/bin/env python
########################################################################
# File name: basic_local_search.py                
# Author: Hector Royo Concepcion                      
# Subject:  Sistemas Inteligentes e Interaccion Persona Computador                    
# Description: Local Search Implementation with variable number of
# objects, objects size and containers size. This program
# executes for a certain period of time, specified by the user  
# The local change of this algorithm is just an object movement from 
# from their original container to any other container where it fits. 
# This version includes 2 evaluators:
# First evaluator consider one solution better than other when containers
# are almost full or empty.
# The other consider one solution better than other when it has more
# empty containers than the other.
########################################################################
from random import randint
from time import gmtime, strftime
import time
import os

clear = lambda: os.system('clear')
clear()
########################################################################

print "BPP: Bin Packing Problem"

containers_size = 500 # Size of each container
n_objects = 500 # Total amount of items to store on containers
maxobject_size = 300 # Maximum size (volume) of objects to be stored
timer = 60 * 5 # Time taken by each metaheuristic to be executed, where "5" is the number of minutes

###	 Creating objects ###
objects_original = [] # Each object is defined by its [Size, Container]. Initially, all objects will be in "-1 container", which means they don't have a container yet.
for i in range(n_objects):
   objects_original.append([randint(maxobject_size*0.3,maxobject_size),-1]);

### Generating initial solution, random solution ###
container_list = [0] # List of containers used
for i in range(n_objects):
  j = 0
  while (j != -1):
    if (objects_original[i][0] + container_list[j] <= containers_size): # Each item is asigned to the first container they fit in.
      container_list[j] =  container_list[j] + objects_original[i][0]
      objects_original[i][1] = j; # Objects are located at all time
      j = -1
    else:
      j = j+1
      if (j == len(container_list)):
		container_list.append((objects_original[i][0]))
		objects_original[i][1] = j;
		j = -1
		
print "Initial Solution"
new_container_n = len(container_list) 
print "Number of Containers: " + str(new_container_n)
print container_list
print sum(container_list)

##################################################################
####### LOCAL SEARCH WITH EVALUATOR AlmostFull/AlmostEmpty #######
##################################################################

newcontainer_list = []
newcontainer_list = container_list[:]
newcontainer_list2 = newcontainer_list[:]
objects = objects_original[:]

nzero1 = 0 # Number of Zeros. Each "Zero" stands for a new empty container in the set. Used to control how many empty containers there are
nzero2 = 0 # Number of Zeros. 

iterator = 0
almost_fullorempty = 0

for i in newcontainer_list:	
    if (i != 0 and (i > 0.9 * containers_size) or (i < (0.1 * containers_size))):
     almost_fullorempty += 1

print str(almost_fullorempty*100/(len(container_list))) + "% of containers are almost full or empty"
     



print "["+strftime("%H:%M:%S")+"] Executing Local Search "

timeout = time.time() + timer   # Time control 
while(1):
    if time.time() > timeout: 
      break
      
    if (iterator == 1):
     almost_fullorempty = almost_fullorempty2
    
     newcontainer_list = newcontainer_list2[:]
     iterator = 0
    iterator += 1   
    almost_fullorempty2 = almost_fullorempty
    nzero2 = nzero1

    item = randint(0,n_objects-1)	
    container = randint(0, new_container_n-1)

    if (objects[item][0] + newcontainer_list[container] <= containers_size and newcontainer_list[container] != 0):
      newcontainer_list[container] += objects[item][0]
      newcontainer_list[objects[item][1]] -= objects[item][0]
      objects[item][1] = container
      
    almost_fullorempty = 0  
    for i in newcontainer_list:
      if (i != 0 and (i > 0.9 * containers_size) or (i < (0.1 * containers_size))):  # Almost full : >= 90%, Almost Empty <= 10%
       almost_fullorempty += 1
  
        
    if (nzero1 < newcontainer_list.count(0) or almost_fullorempty2 <= almost_fullorempty ):
        newcontainer_list2 = newcontainer_list[:] 
        
        if (nzero1 < newcontainer_list.count(0)):     
         nzero1 = newcontainer_list.count(0)
         print "["+strftime("%H:%M:%S")+"] New best solution " + str(new_container_n - nzero2) + " >> " + str(new_container_n - nzero1)
         print str(almost_fullorempty*100/(new_container_n - nzero1)) + "% of containers are almost full or empty" 

        
print "["+strftime("%H:%M:%S")+"]Local search finished, best solution: " + str(new_container_n - nzero1)  + " containers."

     
##################################################################
###################### LOCAL SEARCH ##############################
##################################################################

newcontainer_list = []
newcontainer_list = container_list[:]
objects = objects_original[:]

nzero1 = 0 # Number of Zeros. Each "Zero" stands for a new empty container in the set. Used to control how many empty containers there are
nzero2 = 0 # Number of Zeros. 

print "["+strftime("%H:%M:%S")+"] Executing Local Search "

timeout = time.time() + timer   # Time control 
while(1):
    if time.time() > timeout: 
      break
    nzero2 = nzero1

    item = randint(0,n_objects-1)	
    container = randint(0, new_container_n-1)

    if (objects[item][0] + newcontainer_list[container] <= containers_size and newcontainer_list[container] != 0):
      newcontainer_list[container] += objects[item][0]
      newcontainer_list[objects[item][1]] -= objects[item][0]
      objects[item][1] = container
      if (nzero1 < newcontainer_list.count(0)):
        nzero1 = newcontainer_list.count(0)
        print "["+strftime("%H:%M:%S")+"] New best solution " + str(new_container_n - nzero2) + " >> " + str(new_container_n - nzero1)   

print "["+strftime("%H:%M:%S")+"]Local search finished, best solution: " + str(new_container_n - nzero1)  + " containers."
    
almost_fullorempty = 0    
for i in newcontainer_list:	
    if (i != 0 and (i > 0.9 * containers_size) or (i < (0.1 * containers_size))):
     almost_fullorempty += 1

print str(almost_fullorempty*100/(len(container_list))) + "% of containers are almost full or empty"
   
