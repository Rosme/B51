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
		try:
			bMessage = self.socket.recv(self.buffersize)
			if bMessage:
				donnees = pickle.loads(bMessage) #On desirialise le binaire en objet
				if isinstance(donnees, nd.Message):
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
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect(self.adresse)
		self.socket.settimeout(0.1)
				
	def deconnecter(self):
		print("Deconnexion en cours...")
		#On déconnecte le client
		self.socket.close()
		self.clientOn = False
	
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
