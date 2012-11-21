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

class ClientInfo():
	def __init__(self, conn, address, id):
		self.conn = conn
		self.address = address
		self.id = id

class Serveur():
	def __init__(self, port = 43225):
		self.port = port
		self.statut = "arreter"
		self.listeCommande = {"fermer-serveur":self.arreter, "demarrer-serveur":self.demarrer, "redemarrer-serveur":self.redemarrer, "client-deconnection":self.clientDeconnection}
		self.maxConnect = 10
		self.idConnect = []
		for i in range(self.maxConnect):
			self.idConnect.append(False)

	def demarrer(self, client = None, donnees = None):
		self.statut = "demarrer"
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#création du socket
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
			client.conn.close()			#déconnecte le client à partir de la liste

	def clientDeconnection(self, client, donnees = None):
		print("Client Deconnecte")
		msg = nd.Message("ok-deconnection")
		bMsg = pickle.dumps(msg)			
		client.conn.send(bMsg)					#envoi un message au client pour l'informer que le client c'est bien déconnecté
		self.clients.remove(client)			
		client.conn.close()						#fermeture de sa connexion
	
	def retirerClient(self, client):
		client.conn.close()
		self.clients.remove(client)
		self.idConnect[client.id] = False

	def redemarrer(self, client = None, donnees = None):
		pass

	def updateClients(self):
		incomingConnection, wlist, xlist = select.select([self.socket], [], [], 0.05)

		if len(self.clients) < self.maxConnect:
			for connection in incomingConnection:			#Accepte les connexions et ajoutes les clients dans la liste
				conn, address = self.socket.accept()
				client = ClientInfo(conn, address, len(self.clients)+100)
				self.clients.append(client)

	def update(self):
		pass

	def recevoirMessage(self):
		if self.statut == "demarrer" and self.clients:
			toRead = []
			try:
				listConn = []
				for co in self.clients:
					listConn.append(co.conn)
				toRead, wlist, xlist = select.select(listConn, [], [], 0.05)
			except select.error as serror:
				print("Select error: ", serror)
			else:

				for client in toRead:
					try:
						data = pickle.loads(client.recv(4096))				#desérialise les données reçu
						if isinstance(data, nd.PersoInfo):
							info = self.genererId(data)
							cl = self.obtenirInfoClient(client)
							cl.id = info.id
							bData = pickle.dumps(info)
							client.send(bData)
							print("Nouveau client: " + info.nom + "(" + str(info.id) + ")")
						elif isinstance(data, nd.Message):					#retourne vrai si l'objet est une instance de nd.message
							estCommande, message, donnees = cm.parseCommande(data.message)  #permet de lire si c'est une commande valide envoyé du client au serveur à partir de la méthode parseCommande dans commande.py
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
						print("Erreur sur lecture de client. Deconnection: ", ex)
						client.close()
						self.retirerClient(self.obtenirInfoClient(client))


	def obtenirInfoClient(self, conn):
		for client in self.clients:
			if client.conn == conn:
				return client
		return False

	def envoyerMessage(self):
		message = nd.Message("NO_MESSAGE")
		if self.statut == "arreter":
			message.message = "fermer-serveur"

		if message.message != "NO_MESSAGE":
			bMessage = pickle.dumps(message) #Serialisation du message/données
			for client in self.clients:
				client.conn.send(bMessage)		#envoi message/données
		
	def appliquerCommande(self, action, client, donnees):
		if action in self.listeCommande:
			self.listeCommande[action](client, donnees)


	def genererId(self, info):
		for i in range(len(self.idConnect)):
			if self.idConnect[i] == False:
				info.id = i
				self.idConnect[i] = True
				return info

serveur = Serveur()
serveur.demarrer()

while serveur.statut == "demarrer":
	serveur.updateClients()
	serveur.recevoirMessage()
	serveur.updateClients()
	serveur.envoyerMessage()

serveur.deconnecterClients()
