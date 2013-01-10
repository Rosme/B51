# -*- coding: ISO-8859-1 -*-
'''
Par Jean-Sebastien Fauteux
Classe Serveur pour faire tourner le serveur du jeu
serveur.py
'''

import socket
import select
import pickle
import Netdata as nd
from time import sleep

#Classe Wrapper pour les connexions clientes
class Client():
	def __init__(self, conn, address, id):
		self.conn = conn
		self.address = address
		self.id = id
		self.nom = ""
		self.race = ""

#Classe Wrapper pour les Joueurs
class Joueur():
	def __init__(self, client = Client(None, None, None), events = list()):
		self.client = client
		self.events = events

#Classe Serveur
class Serveur():
	def __init__(self, port = 43225):
		self.port = port
		self.restart()

		#Cr?ation du socket pour les connexions, ainsi que son param?trage
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind(('', self.port))
		s.listen(5)
		self.socket = s

	def recevoirConnexion(self):
		#On va accepter les connexions uniquement si on est en-dessous du nombre de joueur maximal ou la partie n'est pas commenc?
		if self.qteConnect < self.maxConnect and self.statut == "demarrer":
			incoming, wlist, xlist = select.select([self.socket], [], [], 0.05) #Obtention de connexion
			for connection in incoming:
				conn, address = self.socket.accept()
				client = Client(conn, address, self.generateId())
				self.clients.append(client)

				#Envoi du Id au joueur
				clientId = nd.ClientId(client.id)
				bClientId = pickle.dumps(clientId)
				client.conn.send(bClientId)
		if self.statut == "jeu":
			if self.qteConnect == 0:
				self.restart()

	def restart(self):
		self.statut = "demarrer" #Le statut repr?sente l'?tat du serveur. demarrer(attend les connexions des joueurs), jeu(refuse les connexions)
		self.maxConnect = 8
		self.clients = [] #Maximum de 8, contient chaque client connect? au serveur
		self.qteConnect = len(self.clients)
		self.newClient = False
		self.listIdClient = nd.ListClientInfo()
		self.msgQueue = nd.MsgQueue()
		self.eventQueue = []
		self.treatedQueue = {}

		#Liste de bool?en pour les id des joueurs
		#Mis ? False par d?faut pour pouvoir les attribuer
		self.boolIdConnect = []
		for i in range(self.maxConnect):
			self.boolIdConnect.append(False)

	def generateId(self):
		for i in range(self.maxConnect):
			if self.boolIdConnect[i] == False:
				self.boolIdConnect[i] = True
				return i
		return -1 #Aucun ID Disponible

	#Met ? jour le nombre de clients et les id dans la liste
	def updateQteClients(self):
		self.qteConnect = self.boolIdConnect.count(True)
		self.newClient = True
		self.listIdClient = nd.ListClientInfo()
		for client in self.clients:
			self.listIdClient.list.append(nd.ClientInfo(client.id, client.nom, client.race))

	def sendData(self):
		#On est pas encore dans le jeu, la seule chose qu'on envoie c'est la liste des clients
		if self.statut == "demarrer":
			if self.newClient == True:
				bListClient = pickle.dumps(self.listIdClient)
				for client in self.clients:
					client.conn.send(bListClient)
			self.newClient = False
		elif self.statut == "starting":
			bListMsg = pickle.dumps(self.msgQueue)
			for client in self.clients:
				client.conn.send(bListMsg)
			self.msgQueue.msg = []
			self.statut = "jeu"
		elif self.statut == "jeu":
			bEvents = pickle.dumps(self.treatedQueue)
			'''
			for frame in self.treatedQueue:
				item = self.treatedQueue[frame]
				print(item)
				sleep(1)
			'''
			for client in self.clients:
				'''
				for event in self.treatedQueue:
					bEvent = pickle.dumps(event)
					client.conn.send(bEvent)
				'''
				client.conn.send(bEvents)
				'''
				for event in self.treatedQueue:
					for cl in self.treatedQueue[event]:
						print(cl.events)
				'''

			self.treatedQueue = {}


	def getListConn(self):
		listConn = []
		for client in self.clients:
			listConn.append(client.conn)
		return listConn

	def findClientByConnection(self, conn):
		for client in self.clients:
			if client.conn == conn:
				return client
		return None

	def removeClient(self, conn):
		client = self.findClientByConnection(conn)
		self.boolIdConnect[client.id] = False
		self.clients.remove(client)
		self.updateQteClients()

	def recvData(self):
		if self.clients:
			toRead = []
			try:
				listConn = self.getListConn()
				toRead, wlist, xlist = select.select(listConn, [], [], 0.05)
			except select.error as serror:
				print("Select error: ", serror)
			else:
				for conn in toRead:
					try:
						bData = conn.recv(4096)
						if bData:
							data = pickle.loads(bData)
							if isinstance(data, nd.ClientInfo): #R?cup?ration des infos du joueur
								print("New client: " + str(data.nom) + " / " + str(data.race))
								client = self.findClientByConnection(conn)
								client.nom = data.nom
								client.race = data.race
								self.updateQteClients()
							elif isinstance(data, nd.ClientDisconnect):
								print("Client disconnected")
								bDisco = pickle.dumps(nd.ClientDisconnect(data.id))
								conn.send(bDisco)
								self.removeClient(conn)
							elif isinstance(data, nd.StartGameMsg):
								self.statut = "starting"
								self.msgQueue.msg.append(data)
							elif isinstance(data, nd.ClientTickInfo):
								self.eventQueue.append(data)
					except Exception as ex:
						print("Erreur sur lecture de client. Deconnection: ")
						self.removeClient(conn)

	def updateFrames(self):
		if self.statut == "jeu":
			for event in self.eventQueue:
				self.treatedQueue[event.tick+5] = []

			for event in self.eventQueue:
				self.treatedQueue[event.tick+5].append(nd.ClientTickData(event.id, event.events))
			
			'''
			for frame in self.treatedQueue:
				events = self.treatedQueue[frame]
				for data in events:
					print(data.id, data.events)
			'''
			sleep(0.05)
			#sleep(1)

			self.eventQueue = []


serveur = Serveur()
while True:
	serveur.recevoirConnexion()
	serveur.sendData()
	serveur.recvData()
	serveur.updateFrames()

'''
import select 
import socket
import pickle
import Netdata as nd
import Commande as cm

class ClientInfo():
	def __init__(self, conn, address, id):
		self.conn = conn
		self.nom = None
		self.address = address
		self.id = id

class Serveur():
	def __init__(self, port = 43225):
		self.port = port
		self.statut = "arreter"
		self.listeCommande = {"fermer-serveur":self.arreter, "demarrer-serveur":self.demarrer, "client-deconnection":self.clientDeconnection, "demarrer-partie":self.demarrerPartie}
		self.maxConnect = 8
		self.etatPartie = False
		self.idConnect = []
		for i in range(self.maxConnect):
			self.idConnect.append(False)

	def demarrer(self, client = None, donnees = None):
		self.statut = "demarrer"
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#cr?ation du socket
		s.bind(('', self.port))
		s.listen(5)
		self.socket = s
		self.clients = []		
		self.deconnected = []
		self.queueEnvoie = []
		self.clientsEvents = []
		print("Demarrage du serveur")

	def arreter(self, client = None, donnees = None):
		self.statut = "arreter"
	
	def deconnecterClients(self):
		for client in self.clients:
			client.conn.close()			#d?connecte le client ? partir de la liste

	def clientDeconnection(self, client, donnees = None):
		print("Client Deconnecte")
		msg = nd.Message("ok-deconnection")
		bMsg = pickle.dumps(msg)			
		client.send(bMsg)					#envoi un message au client pour l'informer que le client c'est bien d?connect?
		infoClient = self.obtenirInfoClient(client)
		self.idConnect[infoClient.id] = False
		self.clients.remove(infoClient)
		client.close()						#fermeture de sa connexion
		self.queueEnvoie.append(nd.ClientDecoMsg(infoClient.id))
	
	def retirerClient(self, client):
		if client:
			client.conn.close()

			self.clients.remove(client)
			self.idConnect[client.id] = False 

	def demarrerPartie(self, client = None, donnees = None):
		self.etatPartie = True

	def updateClients(self):
		incomingConnection, wlist, xlist = select.select([self.socket], [], [], 0.05)

		if self.etatPartie == False and len(self.clients) < self.maxConnect:
			for connection in incomingConnection:			#Accepte les connexions et ajoutes les clients dans la liste
				conn, address = self.socket.accept()
				client = ClientInfo(conn, address, len(self.clients)+100)
				self.clients.append(client)

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
						data = pickle.loads(client.recv(4096))				#des?rialise les donn?es re?u
						if isinstance(data, nd.PersoInfo):
							info = self.genererId(data)
							cl = self.obtenirInfoClient(client)
							cl.id = info.id
							cl.nom = info.nom
							bData = pickle.dumps(info)
							client.send(bData)
							print("Nouveau client: " + info.nom + "(" + str(info.id) + ")")
							self.queueEnvoie.append(info)
						elif isinstance(data, nd.ClientData):
							self.clientsEvents.append(data)
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
		for msg in self.queueEnvoie:
			bMsg = pickle.dumps(msg)
			for client in self.clients:
				client.conn.send(bMsg)

		self.queueEnvoie = []
		
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
'''