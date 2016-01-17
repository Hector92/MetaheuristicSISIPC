#!/usr/bin/env python
########################################################################
# File name: taboo_search_timer.py                
# Author: Hector Royo Concepcion                      
# Subject:  Sistemas Inteligentes e Interaccion Persona Computador                    
# Description:  Taboo Search. Allows one bad movement when no
# new best solution has been found in a certain period      
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
print container_list
print sum(container_list)

##################################################################
###################### TABOO SEARCH TIMER ##############################
##################################################################
newcontainer_list = []
newcontainer_list = container_list[:]
item = [];

nzero1 = 0
nzero2 = 0
print "["+strftime("%H:%M:%S")+"] Executing Taboo Search "

timeout = time.time() + timer   # 5 minutes from now
now = time.time()
allow_bad_move = 1
while(1):
    if time.time() > timeout: 
      break
        
    nzero2 = nzero1

    item = randint(0,n_objects-1)	
    container = randint(0, new_container_n-1)
    
    if (time.time() - now > 0.20 * timer and allow_bad_move == 1): # If no new solution found in 20% of executing time, one bad movement is allowed
      objects[item][1] = len(newcontainer_list)
      newcontainer_list.append(objects[item][0])
      new_container_n += 1
      print "["+strftime("%H:%M:%S")+"] Taboo Movement " + str(new_container_n- 1 - nzero1) + " >> " + str(new_container_n - nzero1)   
      now = time.time()
      allow_bad_move = 0
    if (objects[item][0] + newcontainer_list[container] <= containers_size and newcontainer_list[container] != 0):
      newcontainer_list[container] += objects[item][0]
      newcontainer_list[objects[item][1]] -= objects[item][0]
      objects[item][1] = container
      if (nzero1 < newcontainer_list.count(0)):
        nzero1 = newcontainer_list.count(0)
        t0 = 0;
        now = time.time()
        allow_bad_move = 1
        print "["+strftime("%H:%M:%S")+"] New best solution " + str(new_container_n - nzero2) + " >> " + str(new_container_n - nzero1)   

print "["+strftime("%H:%M:%S")+"] Taboo Search finished, best solution: " + str(new_container_n - nzero1)  + " containers."

     
    
