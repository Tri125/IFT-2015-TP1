
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

SEED = 42
SIZE = 10000
TimeListInsert= 0
TimeOrderedListInsert = 0
TimeDictionnaryInsert = 0


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
	start_time = time.time()
	myList.inserer(generate_RndCompte())
	TimeListInsert += time.time() - start_time

random.seed(SEED)
for x in range(0, SIZE):
	start_time = time.time()
	myOrderedList.inserer(Mot(generate_RndCompte()))
	TimeOrderedListInsert += time.time() - start_time
	
random.seed(SEED)
for x in range(0, SIZE):
	start_time = time.time()
	myDictionnary.inserer(Mot(generate_RndCompte()))
	TimeDictionnaryInsert += time.time() - start_time
	
	

print("Liste: ", myList)
print("ListeTriee: ", myOrderedList)
print("Dictionnaire: ", myDictionnary)
print("Temps d'insertion de Liste: ", TimeListInsert, "Temps d'insertion de ListeTriee: ", TimeOrderedListInsert, "Temps d'insertion de Dictionnaire: ", TimeDictionnaryInsert)



