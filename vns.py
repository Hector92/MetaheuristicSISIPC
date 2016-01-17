#!/usr/bin/env python
########################################################################
# File name: basic_local_search.py                
# Author: Hector Royo Concepcion                      
# Subject:  Sistemas Inteligentes e Interaccion Persona Computador                    
# Description: VNS. Neighborhoods define by number of movements              
########################################################################
from random import randint
from time import gmtime, strftime
import time
import os

clear = lambda: os.system('clear')
clear()
########################################################################

print "BPP: Bin Packing Problem"

containers_size = 300 # Size of each container
n_objects = 200 # Total amount of items to store on containers
maxobject_size = 250 # Maximum size (volume) of objects to be stored
timer = 60 * 5 # Time taken by each metaheuristic to be executed, where "5" is the number of minutes

n_neighbourhood = 3 # Number of neighbourhoods
max_iteration_n = 8 # Number of iterations per neighbourhood before changing it if no new best solution is found

###	 Creating objects ###
objects = [] # Each object is defined by its [Size, Container]. Initially, all objects will be in "-1 container", which means they don't have a container yet.
for i in range(n_objects):
   objects.append([randint(1,maxobject_size),-1]);

### Generating initial solution, random solution ###
container_list = [0] # List of containers used
for i in range(n_objects):
  j = 0
  while (j != -1):
    if (objects[i][0] + container_list[j] <= containers_size): # Each item is asigned to the first container they fit in.
      container_list[j] =  container_list[j] + objects[i][0]
      objects[i][1] = j; # Objects are located at all time
      j = -1
    else:
      j = j+1
      if (j == len(container_list)):
		container_list.append((objects[i][0]))
		objects[i][1] = j;
		j = -1
		
print "Initial Solution"
new_container_n = len(container_list) 
print "Number of Containers: " + str(new_container_n)
#print container_list
print "Checksum: " + str(sum(container_list))

##################################################################
######################      VNS     ##############################
##################################################################

newcontainer_list = []
newcontainer_list = container_list[:]
item = [];

nzero1 = 0 # Number of Zeros. Each "Zero" stands for a new empty container in the set. Used to control how many empty containers there are
nzero2 = 0 # Number of Zeros. 

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
      nzero2 = nzero1

      item = randint(0,n_objects-1)	
      container = randint(0, new_container_n-1)

      if (objects[item][0] + newcontainer_list[container] <= containers_size and newcontainer_list[container] != 0):
        newcontainer_list[container] += objects[item][0]
        newcontainer_list[objects[item][1]] -= objects[item][0]
        objects[item][1] = container
        i += 1
        n_iterator += 1
		     
    if (nzero1 < newcontainer_list.count(0)):
       nzero1 = newcontainer_list.count(0)
       n_iterator = 0
       print "["+strftime("%H:%M:%S")+"] New best solution (Found at neighbourhood "+str(n_active)+"):  "+ str(new_container_n - nzero2) + " >> " + str(new_container_n - nzero1)

    if (n_iterator > max_iteration_n):
       n_active = ((n_active+1) % (n_neighbourhood))+1
       n_iterator = 0
       	
print "["+strftime("%H:%M:%S")+"]VNS, best solution: " + str(new_container_n - nzero1)  + " containers."
#print newcontainer_list
print "Checksum: " + str(sum(newcontainer_list))
     
    
