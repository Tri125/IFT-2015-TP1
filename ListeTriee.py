
import filecmp
from Mot import Mot

class ListeTriee:

	def __init__(self):
		self.mots = []
		
	def __str__(self):
		tmp = []
		for value in self.mots:
			tuple = (value.get_cle(), value.get_compte())
			tmp.append( (tuple) )
		return '[' + ', '.join(str(v) for v in tmp) + ']'
		
	def inserer(self, element):
		if isinstance(element, Mot):
			if (not self.trouver(element) ):
				element.incrementer()
				self.mots.append(element)
				self.mots.sort()
			else:
				next(value for value in self.mots if value == element).incrementer()
		else:
			return NotImplemented
		
		
	def supprimer(self, element):
		if isinstance(element, Mot):
			if (self.trouver(element)):
				index = self.recherche_binaire_index(self.mots, element, 0, len(self.mots))
				if (self.mots[index].get_compte() == 1):
					del self.mots[index]
				else:
					self.mots[index].decrementer()
		else:
			return NotImplemented
		
	def trouver(self, element):
		if isinstance(element, Mot):
			return  self.recherche_binaire(self.mots, element, 0, len(self.mots)-1)
		else:
			return NotImplemented
		
	def get_mot(self, element):
		if isinstance(element, Mot):
			if (self.trouver(element)):
				index = self.recherche_binaire_index(self.mots, element, 0, len(self.mots)-1)
				return mots[index]
			else:
				return None
		else:
			return NotImplemented

		
		
		
	def recherche_binaire(self, data, cible, min, max, profondeur = 0 ):
		#print( profondeur * ' ', 'recherche_binaire(', data, ',', cible, ',', min, ',', max, ',' ')' )
		if min > max:
			return False #interval vide, pas de match
		else:
			milieu = (min + max) // 2
			if cible == data[milieu]:
				return True
			elif cible < data[milieu]:
				#on cherche dans la portion gauche de la liste
				return self.recherche_binaire( data, cible, min, milieu-1, profondeur+1 )
			else:
				#on cherche dans la portion droite de la liste
				return self.recherche_binaire( data, cible, milieu+1, max, profondeur+1 )
				
	def recherche_binaire_index(self, data, cible, min, max, profondeur = 0 ):
		#print( profondeur * ' ', 'recherche_binaire_index(', data, ',', cible, ',', min, ',', max, ',', ')', )
		if min > max:
			return None #interval vide, pas de match
		else:
			milieu = (min + max) // 2
			if cible == data[milieu]:
				return milieu
			elif cible < data[milieu]:
				#on cherche dans la portion gauche de la liste
				return self.recherche_binaire_index( data, cible, min, milieu-1, profondeur+1 )
			else:
				#on cherche dans la portion droite de la liste
				return self.recherche_binaire_index( data, cible, milieu+1, max, profondeur+1 )



if __name__ == '__main__':
	
	"""Validation de la classe (unit testing)"""
	
	liste = ListeTriee()
	with open('text1.txt') as texte:
		for ligne in texte:
			liste_mots_ligne = ligne.split()
			for mot_brut in liste_mots_ligne:
				mot_strip = mot_brut.strip('!?%(),;:\'".')
				liste.inserer(mot_strip)
			
	liste.supprimer("and")
	liste.supprimer("to")
	liste.supprimer("fragments")
	liste.supprimer("qwerty")
	
	if not liste.trouver("and"):
		print("Une erreur s'est produite...")
	elif not liste.trouver("to"):
		print("Une erreur s'est produite...")
	elif liste.trouver("fragments"):
		print("Une erreur s'est produite...")
	elif liste.trouver("qwerty"):
		print("Une erreur s'est produite...")
	elif liste.get_mot("and").get_compte() != 6:
		print("Une erreur s'est produite...")
	elif liste.get_mot("to").get_compte() != 1:
		print("Une erreur s'est produite...")
	elif liste.get_mot("fragments") != None:
		print("Une erreur s'est produite...")
	elif liste.get_mot("qwerty") != None:
		print("Une erreur s'est produite...")
	
	with open('text1_ListeTriee_test.txt', 'w') as test:
		print(liste, file = test)
	
	if filecmp.cmp("text1_ListeTriee.txt", "text1_ListeTriee_test.txt"):
		print("Aucun bug détecté.")
	else:
		print("Il y a un bug...")
		print("Alors que l'objet devrait s'imprimer ainsi :")
		print()
		print(open("text1_ListeTriee.txt").read())
		print("Il s'imprime plutôt ainsi :")
		print()
		print(liste)










