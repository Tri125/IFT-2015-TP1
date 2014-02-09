
import random

class Mot(object):

	def __init__(self, cle = None):
				if ( (cle == None) or (not cle)):
						self.cle = self.generate_RndCompte()
				else:
						self.cle = cle
				self.compte = 1

	def generate_RndCompte(self):
				length = random.randrange(2,15) #mot de 2 à 14 lettres 
				alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
				list_mot = []
				for x in range(length):
					lettre = random.randrange(len(alphabet))
					list_mot.append(alphabet[lettre])
				return ''.join(list_mot)
				
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.cle == other.cle
		else:
			return False
			
	def __ne__(self, other):
		return not self.__eq__(other)

	def __lt__(self, other):
		if not isinstance(other, self.__class__):
			return NotImplemented
		return self.cle < other.cle
	
	def __gt__(self, other):
		if not isinstance(other, self.__class__):
			return NotImplemented
		return self.cle > other.cle


	def get_compte(self):
		return self.compte

	def get_cle(self):
		return self.cle

	def incrementer(self):
		self.compte+= 1

	def decrementer(self):
		self.compte-= 1

