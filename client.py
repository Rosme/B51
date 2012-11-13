# -*- coding: ISO-8859-1 -*-
'''
@author David Lebrun
serveur.py
'''

import socket
import pickle
import select

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
		#eventuelle boucle qui envoi continuellement des donnees
		#envoyer donne au serveur
		self.donneesSend = input("Donnnes:")
		self.donneesSend = self.donneesSend.encode()
		self.socket.send(self.donneesSend)

	def updateVue(self):
		pass

	def connecter(self):
		print("Connexion en cours...")
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect(self.adresse)
		print("Connexion etablie avec : ", self.adresse)
		while self.clientOn:
			try:
				self.connexionAccepte, wlist, xlist = select.select([self.socket], [], [], 0.05) #on ecoute les joueur dans la listes des joueur qui sont connectés
				self.donnees = input("Message :")
				self.donnees = self.donnees.encode()
				self.socket.send(self.donnees)
			except select.error:
				pass #tant qu'il ny a pas de clients connecte il passe ici
			else:
				#on parcourt chaque client dans la liste - verification si il ont des donnes a soumettre
				for self.client in self.connexionAccepte:
					self.donneesRecu = pickle.load(self.client.recv(self.buffersize))
					print(":", self.donneesRecu)
					'''self.donneesRecu = self.client.recv(self.buffersize)
					self.donneesRecu = self.donneesRecu.decode()
					print(self.donneesRecu)
					#on veut envoyer le message recu du client aux autres client'''

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
