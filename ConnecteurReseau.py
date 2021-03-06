# -*- coding: ISO-8859-1 -*-
import socket
import pickle
import Netdata as nd
from time import sleep
import random

class ConnecteurReseau():
    def __init__(self, parent):
        self.parent = parent
        self.port = None
        self.adresse = None
        self.id = -1
        self.socket = None
        self.nom = None
        self.race = None
        self.playerList = None
        
    def connecter(self, adresse, port):
        #Mise à jour des informations du client
        self.adresse = adresse
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((adresse, port))
        self.socket.settimeout(1)

    def recevoirDonnees(self):
        try:
            bData = self.socket.recv(4096)
            if bData:
                data = pickle.loads(bData)
                if isinstance(data, nd.ClientId):
                    self.id = data.id
                    clientInfo = nd.ClientInfo(self.id, self.nom, self.race)
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
                            self.parent.app.menuL.debuterPartie(self.playerList)
                elif isinstance(data,nd.Seed):
                    random.seed(data.seed)
                elif isinstance(data, nd.ClientDisconnect):
                    '''
                    for id in data.listId:
                        self.parent.jeu.updateQteClients(id)
                    '''
                    pass
                else:
                    '''
                    for event in data:
                        li = data[event]
                        for cl in li:
                            print(event, cl.events)
                            #sleep()
                    '''
                    self.parent.totalEventQueue.append(data)
        except socket.timeout:
            return None
        except socket.error as ex:
            print("Erreur sur la connexion au serveur: ", ex)

    def sendData(self, data = None):
        if data != None:
            bData = pickle.dumps(data)
            self.socket.send(bData)

    def disconnect(self):
        self.sendData(nd.ClientDisconnect(self.id))