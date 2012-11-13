# -*- coding: ISO-8859-1 -*-
'''
@author David Lebrun
serveur.py
'''

import socket
import pickle		
import select
import sys

class Client():

	def __init__(self):
		self.host = 'localhost' #L'adresse IP que le client va entrer dans la fenêtre client
		self.port = 43225 #Le # du port par défaut, le client peut le change si désirer
		self.adresse = (self.host, self.port)
		self.buffersize = 4096
		self.clientOn = True

	def recevoirMessage(self):
		#eventuelle boucle qui reçoit continuellement des donnees
		self.data = self.socket.recv(self.buffersize)
		if self.data:
			self.donneesRecv = self.socket.recv(self.buffersize)
			self.donneesRecv = self.donneesRecv.decode()
			print(self.donneesRecv)
		else:
			print("Aucune donnees recu")

	def envoyerMessage(self):
		try:
			donnees = b""
			donnees = input("Message :") #on met le message dans une variables
			donnees = donnees.encode() 	 #on encode le message
			self.socket.send(donnees)    #on envoi le message
		except socket.error:
			print("Les données n'ont pas pu être envoyées. Impossible de rejoindre le serveur.")
			print("Tentative de reconnexion...")
			self.connecter()

	def updateVue(self):
		pass

	def connecter(self):
		print("Connexion en cours...")
		try:
			self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error:
			print("Une erreur inconnue est survenue.")
		
		try:
			self.socket.connect(self.adresse)
			print("Connexion etablie avec : ", self.adresse)
		except socket.gaierror:
			print("Impossible de rejoindre l'hôte. Veuillez recommencer")
		except socket.error:
			print("Un problème de connexion est survenue. ")
			
		while self.clientOn:
			try:
				self.connexionAccepte, wlist, xlist = select.select([self.socket], [], [], 0.05) #on ecoute les joueur dans la listes des joueur qui sont connectés
				self.envoyerMessage() #on entre dans la méthode envoyerMessage
				
			except select.error:
				pass
			else:
				pass
				#on parcourt chaque client dans la liste - verification si il ont des donnes a soumettre
				#ici on doit appeler la méthode recevoirMessage() pour permettre la réception des messages du serveur
				
	def deconnecter(self):
		print("Déconnexion en cours...")
		#On déconnecte le client
		self.connexion.close()
	
	def update(self):
		pass

	def appliquerCommande(self):
		pass

''' MAIN '''
if __name__ == "__main__":
	j = Client()
	j.connecter()
