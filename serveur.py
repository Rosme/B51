# -*- coding: ISO-8859-1 -*-
'''
@author David Lebrun
serveur.py
'''

import socket 

class creationServeur(): #le nom des classes et des méthodes sont à revoir
    
    def __init__(self):
        self.host = "localhost"
        self.port = 12800
        self.adresse = (self.host, self.port)
        self.buffer = 4096
        self.maxconnexion = 5
        self.clientConnecter = ()
    
    def setSocket(self):
        #Creation d'une connexion TCP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.adresse)
        self.socket.listen(self.maxconnexion)
        print("********************************************************")
        print("DÉMARRAGE DU SERVEUR : Area B51 Multiplayer game")
        print("INFORMATIONS SERVEUR : " , self.adresse)
        print("********************************************************")
    
    def acceptConnexion(self):
        #on ajoute le client accepter dans la liste
        self.connexion_client, self.adresse_client = self.socket.accept()
        #self.clientConnecter.append(self.adresse_client) a revoir
        print("Le client :" ,self.adresse_client ,"vient de se connecter")  
        
    def gestionDataRecv(self):
        while 1:
            self.data = self.connexion_client.recv(self.buffer)
            #self.client = self.socket.getpeername() a revoir
            self.data.decode()
            if not self.data:
                break
            print("\nLe serveur à reçu le message suivant :")
            print("Client :" ) #self.client
            print("Message :" , self.data)
            print("\nFIN DU MESSAGE \n#######################")
        #maintenant on doit envoyer le message au autres client
        #vérification des clients connectés
        for i in self.clientConnecter:
            if self.clientConnecter.count(i) != self.adresse_client:
                #on encode les données avant des envoyés
                self.data.encode()
                #on envoi le message au autres clients
                self.socket.sendto(self.data, self.clientConnecter(i))
                self.connexion_client.close()


if __name__ == "__main__":
    j = creationServeur()
    j.setSocket()
    j.acceptConnexion()
    j.gestionDataRecv()
    