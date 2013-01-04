# -*- coding: ISO-8859-1 -*-
import socket
import pickle
import Netdata as nd


class ConnecteurReseau():
	def __init__(self, parent):
		self.parent = parent
		self.port = None
		self.adresse = None
		self.id = -1
		self.socket = None
		self.nom = None
		self.playerList = None

	def connecter(self, adresse, port, nom):
		#Mise à jour des informations du client
		self.adresse = adresse
		self.port = port
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((adresse, port))
		self.socket.settimeout(0.01)

		self.nom = nom

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
					self.playerList = data.list
					self.parent.app.menuL.update(self.playerList)
					for client in data.list:
						print(client.nom)
				elif isinstance(data, nd.ClientDisconnect):
					self.socket.close()
				elif isinstance(data, nd.MsgQueue):
					for msg in data.msg:
						if isinstance(msg, nd.StartGameMsg):
							self.parent.app.menuL.debuterPartie()
				elif isinstance(data, nd.ClientTickData):
					if data.id == self.id:
						for event in data.events:
							if event == "MOVE_UP":
								self.parent.jeu.mouvement[0] = True
							if event == "MOVE_RIGHT":
								self.parent.jeu.mouvement[1] = True
							if event == "MOVE_DOWN":
								self.parent.jeu.mouvement[2] = True
							if event == "MOVE_LEFT":
								self.parent.jeu.mouvement[3] = True
							if event == "NO_UP":
								self.parent.jeu.mouvement[0] = False
							if event == "NO_RIGHT":
								self.parent.jeu.mouvement[1] = False
							if event == "NO_DOWN":
								self.parent.jeu.mouvement[2] = False
							if event == "NO_LEFT":
								self.parent.jeu.mouvement[3] = False
				else:
					self.parent.totalEventQueue.append(data)
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