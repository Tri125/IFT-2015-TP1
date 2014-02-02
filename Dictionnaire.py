
import filecmp
from Mot import Mot

class Dictionnaire:
	
	def __init__(self):
		self.mots = dict()
		
	def __str__(self):
		tmp = []
		for key, value in self.mots.items():
			tuple = (key, value)
			tmp.append( (tuple) )
		return '[' + ', '.join(str(v) for v in tmp) + ']'
		
	def inserer(self, element):
		if isinstance(element, Mot):
			if element.get_cle() not in self.mots:
				element.incrementer()
				self.mots[element.get_cle()] = element.get_compte()
			else:
				self.mots[element.get_cle()] += 1
		else:
			return NotImplemented
		
	def supprimer(self, element):
		if isinstance(element, Mot):
			if element.get_cle() in self.mots:
				if self.mots[element.get_cle()] > 1:
					self.mots[element.get_cle()] -= 1  
				else: 
					self.mots.pop(element.get_cle(), None)
		else:
			return NotImplemented
		
	def trouver(self, element):
		if isinstance(element, Mot):
			return element.get_cle() in self.mots
		
	def get_mot(self, element):
		if isinstance(element, Mot):
		 return self.mots[element.get_compte()] if element.get_cle() in self.mots  else None

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










