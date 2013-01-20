# -*- coding: ISO-8859-1 -*-
'''
@author David Lebrun
Classe Client pour se connecter au serveur et communiquer avec les autres clients
client.py
'''

import socket
import select
import pickle
import Netdata as nd

class Client():
	def __init__(self):
		self.host = 'localhost'
		self.port = 43225
		self.address = (self.host, self.port)
		self.buffersize = 4096
		self.id = -1

	def receive(self):
		try:
			bData = self.socket.recv(self.buffersize)
			if bData:
				data = pickle.loads(bData)
				if isinstance(data, nd.ClientId):
					self.id = data.id
					nom = input("Nom > ")
					clientInfo = nd.ClientInfo(self.id, nom)
					self.sendData(clientInfo)
				elif isinstance(data, nd.ListClientInfo):
					for client in data.list:
						print(client.nom)
		except socket.timeout:
			pass
		except socket.error:
			print("Erreur sur la connexion au serveur")

	def connecter(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect(self.address)
		self.socket.settimeout(0.1)

	def sendData(self, data = None):
		if data != None:
			bData = pickle.dumps(data)
			self.socket.send(bData)

c = Client()
c.connecter()
while True:
	c.receive()