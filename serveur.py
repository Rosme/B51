# -*- coding: ISO-8859-1 -*-
'''
Par Jean-Sebastien Fauteux
Classe Serveur pour faire tourner le serveur du jeu
serveur.py
'''

import select 
import socket
import pickle
import netdata as nd
import commande as cm

class Serveur():
	def __init__(self, port = 43225):
		self.port = port
		self.statut = "arreter"
		self.listeCommande = {"fermer-serveur":self.arreter, "demarrer-serveur":self.demarrer, "redemarrer-serveur":self.redemarrer, "client-deconnection":self.clientDeconnection}

	def demarrer(self, client = None, donnees = None):
		self.statut = "demarrer"
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#cr�ation du socket
		s.bind(('', self.port))
		s.listen(5)
		self.socket = s
		self.clients = []		
		self.deconnected = []
		print("Demarrage du serveur")

	def arreter(self, client = None, donnees = None):
		self.statut = "arreter"
	
	def deconnecterClients(self):
		for client in self.clients:
			client.close()			#d�connecte le client � partir de la liste

	def clientDeconnection(self, client, donnees = None):
		print("Client Deconnecte")
		msg = nd.Message("ok-deconnection")
		bMsg = pickle.dumps(msg)			
		client.send(bMsg)					#envoi un message au client pour l'informer que le client c'est bien d�connect�
		self.clients.remove(client)			
		client.close()						#fermeture de sa connexion
			

	def redemarrer(self, client = None, donnees = None):
		pass

	def updateClients(self):
		incomingConnection, wlist, xlist = select.select([self.socket], [], [], 0.05)

		for connection in incomingConnection:			#Accepte les connexions et ajoutes les clients dans la liste
			conn, address = self.socket.accept()
			self.clients.append(conn)
			print("Nouveau client")			

	def update(self):
		pass

	def recevoirMessage(self):
		if self.statut == "demarrer" and self.clients:
			toRead = []
			try:
				toRead, wlist, xlist = select.select(self.clients, [], [], 0.05)
			except select.error as serror:
				print("Select error: ", serror)
			else:

				for client in toRead:
					try:
						data = pickle.loads(client.recv(4096))				#des�rialise les donn�es re�u
						if isinstance(data, nd.Message):					#retourne vrai si l'objet est une instance de nd.message
							estCommande, message, donnees = cm.parseCommande(data.message)  #permet de lire si c'est une commande valide envoy� du client au serveur � partir de la m�thode parseCommande dans commande.py
							if estCommande == True:											
								self.appliquerCommande(message, client, donnees)			
							else:
								print(message)
						else:
							print("Type de donnees inconnu")
					except EOFError as eof:
						print("Erreur sur le serveur: ", eof)
						self.clients = []
					except Exception as ex:
						print("Erreur sur lecture de client. Deconnection")
						self.deconnected.append(client)

					
	def envoyerMessage(self):
		message = nd.Message("NO_MESSAGE")
		if self.statut == "arreter":
			message.message = "serveur-shutdown"

		if message.message != "NO_MESSAGE":
			bMessage = pickle.dumps(message) #Serialisation du message/donn�es
			for client in self.clients:
				client.send(bMessage)		#envoi message/donn�es
		
	def appliquerCommande(self, action, client, donnees):
		if action in self.listeCommande:
			self.listeCommande[action](client, donnees)

serveur = Serveur()
serveur.demarrer()

while serveur.statut == "demarrer":
	serveur.updateClients()
	serveur.recevoirMessage()
	serveur.updateClients()
	serveur.envoyerMessage()

serveur.deconnecterClients()