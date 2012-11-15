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
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
			client.close()

	def clientDeconnection(self, client, donnees = None):
		print("Client Deconnecte")
		msg = nd.Message("/quit")
		bMsg = pickle.dumps(msg)
		client.send(bMsg)
		self.deconnected.append(client)

	def redemarrer(self, client = None, donnees = None):
		pass

	def updateClients(self):
		incomingConnection, wlist, xlist = select.select([self.socket], [], [], 0.05)
		
		for deco in self.deconnected:
			self.clients.remove(deco)
			deco.close()
		self.deconnected = []
		

		for connection in incomingConnection:
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
						data = pickle.loads(client.recv(4096))
						if isinstance(data, nd.Message):
							estCommande, message, donnees = cm.parseCommande(data.message)
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
		message = nd.Message("")
		if self.statut == "arreter":
			message.message = "serveur-shutdown"

		if message.message != "":
			bMessage = pickle.dumps(message) #Serialisation
			for client in self.clients:
				client.send(bMessage)
		
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
