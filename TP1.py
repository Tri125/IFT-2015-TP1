
import random, time, copy 
from Mot import Mot
from Liste import Liste
from ListeTriee import ListeTriee
from Dictionnaire import Dictionnaire

#start_time = time.time()
# code
#elapsed_time = time.time() - start_time

wordList = []

myList = Liste()
myOrderedList = ListeTriee()
myDictionnary = Dictionnaire()

SEED = 7256
SIZE = 10000
TimeListInsert= 0
TimeOrderedListInsert = 0
TimeDictionnaryInsert = 0

TimeListSearch= 0
TimeOrderedListSearch = 0
TimeDictionnarySearch = 0

TimeListDelete= 0
TimeOrderedListDelete = 0
TimeDictionnaryDelete = 0


def generate_RndCompte():
				length = random.randrange(2,15) #mot de 2 à 14 lettres 
				alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
				list_mot = []
				for x in range(length):
					lettre = random.randrange(len(alphabet))
					list_mot.append(alphabet[lettre])
				return ''.join(list_mot)

random.seed(SEED)			
for x in range(0, SIZE):
	wordList.append(generate_RndCompte())

#Insertion				
for x in range(0, SIZE):
	start_time = time.time()
	myList.inserer(wordList[x])
	TimeListInsert += time.time() - start_time

for x in range(0, SIZE):
	start_time = time.time()
	myOrderedList.inserer(wordList[x])
	TimeOrderedListInsert += time.time() - start_time
	
for x in range(0, SIZE):
	start_time = time.time()
	myDictionnary.inserer(wordList[x])
	TimeDictionnaryInsert += time.time() - start_time
	
	
#Recherche
random.seed(SEED)
for x in range(0, SIZE):
	index = random.randrange(len(wordList))
	start_time = time.time()
	myList.trouver(wordList[index])
	TimeListSearch += time.time() - start_time

random.seed(SEED)
for x in range(0, SIZE):
	index = random.randrange(len(wordList))
	start_time = time.time()
	myOrderedList.trouver(wordList[index])
	TimeOrderedListSearch += time.time() - start_time
	
random.seed(SEED)
for x in range(0, SIZE):
	index = random.randrange(len(wordList))
	start_time = time.time()
	myDictionnary.trouver(wordList[index])
	TimeDictionnarySearch += time.time() - start_time
	
	
	
#Supression
random.seed(SEED)
for x in range(0, SIZE):
	start_time = time.time()
	myList.supprimer(wordList[index])
	TimeListDelete += time.time() - start_time

random.seed(SEED)
for x in range(0, SIZE):
	start_time = time.time()
	myOrderedList.supprimer(wordList[index])
	TimeOrderedListDelete += time.time() - start_time
	
random.seed(SEED)
for x in range(0, SIZE):
	start_time = time.time()
	myDictionnary.supprimer(wordList[index])
	TimeDictionnaryDelete += time.time() - start_time
	
	

#print("Liste: ", myList)
#print("ListeTriee: ", myOrderedList)
#print("Dictionnaire: ", myDictionnary)
print("Temps d'insertion de Liste: ", TimeListInsert, "Temps d'insertion de ListeTriee: ", TimeOrderedListInsert, "Temps d'insertion de Dictionnaire: ", TimeDictionnaryInsert)
print("Temps de recherche de Liste: ", TimeListSearch, "Temps de recherche de ListeTriee: ", TimeOrderedListSearch, "Temps de recherche de Dictionnaire: ", TimeDictionnarySearch)
print("Temps de supression de Liste: ", TimeListDelete, "Temps de supression de ListeTriee: ", TimeOrderedListDelete, "Temps de supression de Dictionnaire: ", TimeDictionnaryDelete)



