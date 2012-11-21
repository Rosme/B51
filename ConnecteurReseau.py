# -*- coding: ISO-8859-1 -*-
import socket
import pickle
import netdata as nd

class ConnecteurReseau():
	def __init__(self):
		self.port = None
		self.adresse = None
		self.id = -1
		self.socket = None

	def connecter(self, adresse, port, nom):
		#Mise à jour des informations du client
		self.adresse = adresse
		self.port = port
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.bind((adresse, port))

		#On envoie les informations de connection pour générer un ID et avoir une connection
		infoJoueur = nd.PersoInfo(nom)
		infoBinaire = pickle.dumps(infoJoueur)
		self.socket.send(infoBinaire)

		#On reçoit les données du serveur, et on s'ajuste ainsi
		infoBinaire = self.socket.recv(4096)
		infoJoueur = pickle.loads(infoBinaire)
		self.id = infoJoueur.id

		self.socket.settimeout(0.1)

	def deconnecter(self):
		cmd = nd.Message("/quit")
		cmdBinaire = pickle.dumps(cmd)
		self.socket.send(cmdBinaire)
		self.socket.close()

	def envoyerDonnees(self, donnees):
		bin = pickle.dumps(donnees)
		self.socket.send(bin)

	def recevoirDonnees(self):
		try:
			bin = self.socket.recv(4096)
			if bin:
				donnees = pickle.loads(bin)
				return donnees
		except socket.timeout:
			return None
