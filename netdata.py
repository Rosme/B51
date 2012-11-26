# -*- coding: ISO-8859-1 -*-
'''
Classe englobante pour le transfert de donnees sur le reseau
Par Jean-Sebastien Fauteux
netdata.py
'''

class PersoInfo():
	def __init__(self, nom):
		self.nom = nom
		self.id = -1

class Message():
	def __init__(self, message):
		self.message = message

class ClientDecoMsg(Message):
	def __init__(self, id):
		Message.__init__(self, "Client deconnecte: " + str(id))
		self.id = id
