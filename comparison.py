#!/usr/bin/env python
########################################################################
# File name: basic_local_search.py                
# Author: Hector Royo Concepcion                      
# Subject:  Sistemas Inteligentes e Interaccion Persona Computador                    
# Description: Comparison between Local Search and VNS                     
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
n_objects = 250 # Total amount of items to store on containers
maxobject_size = 375 # Maximum size (volume) of objects to be stored
timer = 60 * 5 # Time taken by each metaheuristic to be executed, where "5" is the number of minutes

###	 Creating objects ###
objects_original = [] # Each object is defined by its [Size, Container]. Initially, all objects will be in "-1 container", which means they don't have a container yet.
for i in range(n_objects):
   objects_original.append([randint(1,maxobject_size),-1]);

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

     
##################################################################
######################      VNS     ##############################
##################################################################


n_neighbourhood = 3 # Number of neighbourhoods
max_iteration_n = 8 # Number of iterations per neighbourhood before changing it if no new best solution is found

objects = objects_original[:]
newcontainer_list2 = []
newcontainer_list2 = container_list[:]
new_container_n2 = len(container_list) 
n_zero1 = 0 # Number of Zeros. Each "Zero" stands for a new empty container in the set. Used to control how many empty containers there are
n_zero2 = 0 # Number of Zeros. 

n_active = 1
n_iterator = 0 
i = 0


print "["+strftime("%H:%M:%S")+"] Executing VNS "

timeout = time.time() + timer   # Time control 
while(1):
    if time.time() > timeout: 
      break


    i = 0
    while ( i < n_active ):
      n_zero2 = n_zero1

      item = randint(0,n_objects-1)	
      container = randint(0, new_container_n2-1)

      if (objects[item][0] + newcontainer_list2[container] <= containers_size and newcontainer_list2[container] != 0):
        newcontainer_list2[container] += objects[item][0]
        newcontainer_list2[objects[item][1]] -= objects[item][0]
        objects[item][1] = container
        i += 1
        n_iterator += 1
		     
    if (n_zero1 < newcontainer_list2.count(0)):
       n_zero1 = newcontainer_list2.count(0)
       n_iterator = 0
       print "["+strftime("%H:%M:%S")+"] New best solution (Found at neighbourhood "+str(n_active)+"):  "+ str(new_container_n2 - n_zero2) + " >> " + str(new_container_n2 - n_zero1)

    if (n_iterator > max_iteration_n):
       n_active = ((n_active+1) % (n_neighbourhood))+1
       n_iterator = 0
       	
print "["+strftime("%H:%M:%S")+"]VNS finished, best solution: " + str(new_container_n2 - n_zero1)  + " containers."
#print newcontainer_list
print "Checksum: " + str(sum(newcontainer_list2))
