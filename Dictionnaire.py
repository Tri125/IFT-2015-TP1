
import filecmp
from Mot import Mot

class Dictionnaire:
	
	def __init__(self):
		self.mots = dict()
		
	def __str__(self):
		tmp = []
		for key, value in self.mots.items():
			tuple = (value.get_cle(), value.get_compte())
			tmp.append( (tuple) )
		return '[' + ', '.join(str(v) for v in tmp) + ']'
		
	def inserer(self, element):
		if element not in self.mots:
			self.mots[element] = Mot(element)
		else:
			self.mots[element].incrementer()
		
	def supprimer(self, element):
		if element in self.mots:
			if self.mots[element].get_compte() > 1:
				self.mots[element].decrementer()  
			else: 
				self.mots.pop(element, None)
		
	def trouver(self, element):
		return element in self.mots
		
	def get_mot(self, element):
		return self.mots[element] if element in self.mots  else None

if __name__ == '__main__':
	
	"""Validation de la classe (unit testing)"""
	
	liste = Dictionnaire()
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
	else:
		print("Auncun bug détecté.")










