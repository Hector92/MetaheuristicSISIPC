from random import randint
from time import gmtime, strftime
print "BPP"


containers_size = 100
n_objects = 100
maxobject_size = 80

objects = []

for i in range(n_objects):
   objects.append([randint(1,maxobject_size),-1]);

container_list = [0]
j = 0;

for i in range(n_objects):
  j = 0
  while (j != -1):
    if (objects[i][0] + container_list[j] <= containers_size):
      container_list[j] =  container_list[j] + objects[i][0]
      objects[i][1] = j;
      j = -1
    else:
      j = j+1
      if (j == len(container_list)):
		container_list.append((objects[i][0]))
		objects[i][1] = j;
		j = -1
print "Solucion Inicial"
new_container_n = len(container_list) 
print "El numero de contenedores es: " + str(new_container_n)
print container_list
print sum(container_list)
##################################################################
###################### LOCAL SEARCH MOD 1 ########################
##################################################################

newcontainer_list = []
newcontainer_list = container_list
item = [];


nzero1 = 0
nzero2 = 0

while(1):
    
    nzero2 = nzero1
    new_container_n2 = new_container_n
    item = randint(0,n_objects-1)	
    container = randint(0, new_container_n-1)

    if (objects[item][0] + newcontainer_list[container] <= containers_size and newcontainer_list[container] != 0 and newcontainer_list[container] != 100):
      newcontainer_list[container] += objects[item][0]
      newcontainer_list[objects[item][1]] -= objects[item][0]
      objects[item][1] = container
      if (nzero1 < newcontainer_list.count(0)):
        nzero1 = newcontainer_list.count(0)
        print "["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] Mejora encontrada " + str(new_container_n - nzero2) + " >> " + str(new_container_n - nzero1)



     
    
