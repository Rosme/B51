# -*- coding: ISO-8859-1 -*-
'''
Classe de base pour les items
'''
class Item():
	def __init__(self, id, poids, nom, description):
		self.id = id
		self.poids = poids
		self.nom = nom
		self.description = description


'''
Classe pour les items qui sert aux upgrades
'''
class Upgradable(Item):
	def __init__(self, id, nom, description):
		#Definition d'un poids de zero pour les stack a l'infini
		Item.__init__(self, id, 0, nom, description)


'''
Classe pour les choses divers(nourriture, stim pack, etc.)
Les items de divers s'applique uniquement au joueur
'''
class Divers(Item):
	def __init__(self, id, poids, nom, description, qualite):
		Item.__init__(self, id, poids, nom, description)
		self.qualite = qualite

	#Augmente la vie du joueur
	def utiliser(self, joueur):
		joueur.vie += self.qualite

'''
Arme
'''
class Arme(Item):
	def __init__(self, id, poids, nom, description, force, energie, cout, vitesseRecharge):
		Item.__init__(self, id, poids, nom, description)
		self.force = force
		self.max_energie = energie
		self.energie = energie
		self.cout = cout
		self.vitesseRecharge = vitesseRecharge

	def utiliser(self):
		self.energie -= self.cout

	def recharge(self):
		self.energie += self.vitesseRecharge

'''
Armure
'''
class Armure(Item):
	def __init__(self, id, poids, nom, description, defense, energie, vitesseRecharge):
		Item.__init__(self, id, poids, nom, description)
		self.defense = defense
		self.max_energie = energie
		self.energie = energie
		self.vitesseRecharge = vitesseRecharge

	def subit(self, degat):
		self.energie -= degat

	def recharge(self):
		self.energie += self.vitesseRecharge

'''
Classe d'Inventaire
'''
class Inventaire():
	def __init__(self, poidsLimite):
		self.poids = 0
		self.poidsLimite = poidsLimite
		self.items = []

	'''
	tente de rajouter l'item a l'Inventaire
	Si on peut, il le fait et retourne True
	Sinon retourne False
	'''
	def ajouterItem(self, item):
		if self.poids+item.poids > self.poidsLimite:
			return False
		else:
			self.items.append(item)
			self.poids += item.poids
			return True

	'''
	Va retirer l'item de la liste
	S'il ne se trouve pas dans la liste, rien ne se passe
	Sinon la fonction va l'enlever et enlever le poids a l'inventaire
	'''
	def retirerItem(self, item):
		if item in self.items:
			self.items.remove(item)
			self.poids -= item.poids
			
'''
Classe du Coffre
'''
class Coffre():
	def __init__(self):
		self.items = []

	'''
	Rajout d'un item au coffre
	'''
	def ajouterItem(self, item):
		self.items.append(item)

	'''
	Va retirer l'item de la liste
	S'il ne se trouve pas dans la liste, rien ne se passe
	Sinon la fonction va l'enlever du coffre
	'''
	def retirerItem(self, item):
		if item in self.items:
			self.items.remove(item)
			
'''
Classe des Sac
'''
class Sac():
	def __init__(self):
		self.items = []

	'''
	Va retirer l'item de la liste
	S'il ne se trouve pas dans la liste, rien ne se passe
	Sinon la fonction va l'enlever du coffre
	'''
	def retirerItem(self, item):
		if item in self.items:
			self.items.remove(item)