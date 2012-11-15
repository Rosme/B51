# -*- coding: ISO-8859-1 -*-
'''
@author David Lebrun
client.py
'''

import socket	
import select
import sys
import pickle
import netdata as nd

class Client():

	def __init__(self):
		self.host = 'localhost' #L'adresse IP que le client va entrer dans la fenêtre client
		self.port = 43225 #Le # du port par défaut, le client peut le change si désirer
		self.adresse = (self.host, self.port)
		self.buffersize = 4096
		self.clientOn = True
		self.id = -1

	def recevoirMessage(self):
		#eventuelle boucle qui reçoit continuellement des donnees
		bMessage = self.socket.recv(self.buffersize)
		donnees = pickle.loads(bMessage) #On desirialise le binaire en objet
		if isinstance(donnees, nd.Message):
			if donnees.message == "serveur-shutdown":
				print("Le serveur est fermer")
				self.clientOn = False
			elif donnees.message == "/quit":
				print("Deconnection reussi")
				self.clientOn = False
			else:
				print(donnees.message)

	def envoyerMessage(self):
		try:
			message = nd.Message(input("Message: "))
			
			bMessage = pickle.dumps(message) #On dump en binaire le message
			self.socket.send(bMessage)    #on envoi le message

		except socket.error:
			print("Les donnees n'ont pas pu etre envoyees. Impossible de rejoindre le serveur.")

	def updateVue(self):
		pass

	def connecter(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect(self.adresse)

		#Test pour générer un id "unique" au joueur avec une connexion, basé sur son nom
		nom = input("Nom: ")
		info = nd.PersoInfo(nom)
		bData = pickle.dumps(info)
		self.socket.send(bData)

		rData = self.socket.recv(4096)
		data = pickle.loads(rData) #Load les donnees binaire
		if isinstance(data, nd.PersoInfo):
			self.id = data.id
		
		'''
		print("Connexion en cours...")
		try:
			self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error:
			print("Une erreur inconnue est survenue.")
		
		try:
			self.socket.connect(self.adresse)
			print("Connexion etablie avec : ", self.adresse)
		except socket.gaierror:
			print("Impossible de rejoindre l'hote. Veuillez recommencer")
		except socket.error:
			print("Un probleme de connexion est survenue. ")
			
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
		'''
				
	def deconnecter(self):
		print("Deconnexion en cours...")
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
	while j.clientOn:
		j.envoyerMessage()
		j.recevoirMessage()
