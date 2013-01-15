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
        self.listClientGone = []

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
                print("REDEMARRAGE DU SERVEUR")
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

        print("****** DEMARRAGE DU SERVEUR ******")
        print("******     PORT: " + str(self.port) + "      ******")
        print("******   MAX JOUEUR : " + str(self.maxConnect) + "     ******")

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
            print("****** DEMARRAGE D'UNE PARTIE ******")
        elif self.statut == "jeu":
            '''
            if len(self.listClientGone) == 0:
                clientsGone = nd.ClientDisconnect(self.listClientGone)
                bList = pickle.dumps(clientsGone)
                for client in self.clients:
                    client.conn.send(bList)
                self.listClientGone = []
            '''
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
                try:
                    client.conn.send(bEvents)
                except:
                    print("Erreur sur Envoie de client. Deconnection: ")
                    self.removeClient(client.conn)
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
        self.listClientGone.append(client.id)
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
                            elif isinstance(data, nd.ClientTireInfo):
                                print("works")
                                pass
                    except Exception as ex:
                        print("Erreur sur lecture de client. Deconnection: ")
                        self.removeClient(conn)

    def updateFrames(self):
        if self.statut == "jeu":
            for event in self.eventQueue:
                self.treatedQueue[event.tick+3] = []

            for event in self.eventQueue:
                self.treatedQueue[event.tick+3].append(nd.ClientTickData(event.id, event.events))
            
            '''
            for frame in self.treatedQueue:
                events = self.treatedQueue[frame]
                for data in events:
                    print(data.id, data.events)
            '''
            sleep(0.05)

            self.eventQueue = []


serveur = Serveur()
while True:
    serveur.recevoirConnexion()
    serveur.sendData()
    serveur.recvData()
    serveur.updateFrames()