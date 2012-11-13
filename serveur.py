# -*- coding: ISO-8859-1 -*-
'''
Par Jean-Sebastien Fauteux
Classe Serveur pour faire tourner le serveur du jeu
'''

import select 
import socket

class Serveur():
	def __init__(self, port = 43225):
		self.port = port
		self.statut = "arreter"

	def demarrer(self):
		self.statut = "demarrer"
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind(('', self.port))
		s.listen(5)
		self.socket = s
		self.clients = []
		self.deconnected = []
		print("Serveur demarré")

	def arreter(self):
		self.statut = "arreter"
		for client in self.clients:
			client.close()
		

	def redemarrer(self):
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

	def update(self):
		pass

	def recevoirMessage(self):
		if self.statut == "demarrer" and self.clients:
			toRead = []
			try:
				toRead, wlist, xlist = select.select(self.clients, [], [], 0.05)
			except select.error:
				print(select.error)
			else:
				for client in toRead:
					received = client.recv(1024)
					received = received.decode()
					received = received.split("\r")[0]
					print("{}".format(received))
					if received == "/quit":
						self.deconnected.append(client)
					elif received == "/shutdown":
						self.arreter()

	def envoyerMessage(self):
		pass
		
	def appliquerCommande(self):
		pass


serveur = Serveur()
serveur.demarrer()

while serveur.statut == "demarrer":
	serveur.updateClients()
	serveur.recevoirMessage()
	serveur.envoyerMessage()