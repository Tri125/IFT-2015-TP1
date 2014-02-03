
import random, time, copy 
from Mot import Mot
from Liste import Liste
from ListeTriee import ListeTriee
from Dictionnaire import Dictionnaire

#start_time = time.time()
# code
#elapsed_time = time.time() - start_time


myList = Liste()
myOrderedList = ListeTriee()
myDictionnary = Dictionnaire()

insertList = []

for x in range(0,100000):
	tmp = Mot()
	insertList.append(Mot())

ListeTotal = 0
ListeTrieeTotal = 0
DictionnaireTotal = 0

for x in insertList:
	a = copy.deepcopy(x)
	b = copy.deepcopy(x)
	c = copy.deepcopy(x)
	
	start_time = time.time()
	myList.inserer(a)
	elapsed_time = time.time() - start_time
	ListeTotal += elapsed_time
	
	start_time = time.time()
	myOrderedList.inserer(b)
	elapsed_time = time.time() - start_time
	ListeTrieeTotal += elapsed_time
	
	start_time = time.time()
	myDictionnary.inserer(c)
	elapsed_time = time.time() - start_time
	DictionnaireTotal += elapsed_time

print("Liste: ", myList)
print("ListeTriee: ", myOrderedList)
print("Dictionnaire: ", myDictionnary)
print("Temps d'insertion de Liste: ", ListeTotal, "Temps d'insertion de ListeTriee: ", ListeTrieeTotal, "Temps d'insertion de Dictionnaire: ", DictionnaireTotal)



