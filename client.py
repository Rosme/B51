# -*- coding: ISO-8859-1 -*-
'''
@author David Lebrun
Classe Client pour se connecter au serveur et communiquer avec les autres clients
client.py
'''

import socket
import select
import pickle

class Client():
	def __init__(self):
		self.host = 'localhost'
		self.port = 43225
		self.address = (self.host, self.port)
		self.buffersize = 4096

	def receive(self):
		try:
			bData = self.socket.recv(self.buffersize)
			if bData:
				data = pickle.loads(bData)
				print(data)
		except socket.timeout:
			pass
		except socket.error:
			print("Erreur sur la connexion au serveur")

	def connecter(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect(self.address)
		self.socket.settimeout(0.1)

c = Client()
c.connecter()
while True:
	c.receive()

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
		try:
			bMessage = self.socket.recv(self.buffersize)
			if bMessage:
				donnees = pickle.loads(bMessage) 	#On desérialise le binaire en objet
				if isinstance(donnees, nd.Message):		#Vérification, retourne vrai si l'objet est un instance de nd.message, sinon retourne faux
					if donnees.message == "ok-deconnection":
						self.deconnecter()
					else:
						print(donnees.message)
		except socket.timeout:
			pass
		except socket.error:
			print("La connexion avec le serveur est impossible")
			self.deconnecter()
			

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
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#création du socket
		self.socket.connect(self.adresse)								#connexion au serveur
		self.socket.settimeout(0.1)										#maximum de 0.1 ms pour le timeout, déclenche une exception si le délai c'est écoulé
				
	def deconnecter(self):
		print("Deconnexion en cours...")
		#On déconnecte le client
		self.socket.close()
		self.clientOn = False
	
	def update(self):
		pass

	def appliquerCommande(self):
		pass
'''
''' MAIN '''
'''
if __name__ == "__main__":
	j = Client()
	j.connecter()
	while j.clientOn:
		j.envoyerMessage()
		j.recevoirMessage()
'''