# -*- coding: ISO-8859-1 -*-
import socket
import pickle
import Netdata as nd


class ConnecteurReseau():
	def __init__(self):
		self.port = None
		self.adresse = None
		self.id = -1
		self.socket = None
		self.nom = None

	def connecter(self, adresse, port, nom):
		#Mise à jour des informations du client
		self.adresse = adresse
		self.port = port
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((adresse, port))
		self.socket.settimeout(0.01)

		self.nom = nom

		'''
		#On envoie les informations de connection pour générer un ID et avoir une connection
		infoJoueur = nd.PersoInfo(nom)
		infoBinaire = pickle.dumps(infoJoueur)
		self.socket.send(infoBinaire)

		#On reçoit les données du serveur, et on s'ajuste ainsi
		infoBinaire = self.socket.recv(4096)
		infoJoueur = pickle.loads(infoBinaire)
		self.id = infoJoueur.id

		return infoJoueur
		'''

	'''
	def deconnecter(self):
		cmd = nd.Message("/quit")
		cmdBinaire = pickle.dumps(cmd)
		self.socket.send(cmdBinaire)
		self.socket.close()

	def envoyerDonnees(self, donnees):
		bin = pickle.dumps(donnees)
		self.socket.send(bin)

	'''

	def recevoirDonnees(self):
		try:
			bData = self.socket.recv(4096)
			if bData:
				data = pickle.loads(bData)
				if isinstance(data, nd.ClientId):
					self.id = data.id
					clientInfo = nd.ClientInfo(self.id, self.nom)
					self.sendData(clientInfo)
					return True
				elif isinstance(data, nd.ListClientInfo):
					for client in data.list:
						print(client.nom)
				elif isinstance(data, nd.ClientDisconnect):
					self.socket.close()
		except socket.timeout:
			return None
		except socket.error:
			print("Erreur sur la connexion au serveur")

	def sendData(self, data = None):
		if data != None:
			bData = pickle.dumps(data)
			self.socket.send(bData)

	def disconnect(self):
		self.sendData(nd.ClientDisconnect(self.id))