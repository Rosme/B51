# -*- coding: ISO-8859-1 -*-
import tkinter
import Netdata as nd

class MenuLobby():
    def __init__(self,parent):
        self.parent = parent
        self.network = self.parent.parent.network
        self.frameMenuLobby = tkinter.Frame(self.parent.root)
        self.inLobby = True

        #Image de fond
        self.fondEcran= tkinter.Canvas(self.frameMenuLobby,width=1024,height=768)
        self.fondEcran.pack()
        self.fondEcran.create_image(512,384, image= self.parent.getImage("backgroundImage"),tags="fondEcran")
        
        #creation de la fenetre lobby
        
        self.fenetre = tkinter.Canvas(self.frameMenuLobby,width=400, height=400)
        self.fenetre.create_rectangle(0,0,100,100)
        
        self.fondEcran.create_text(140,70,text="Nombre de joueurs :",font=("verdana","12","bold"),fill="red",tags="nbPlayer")
        

        #creation de boutton
        self.boutonDemarrer= tkinter.Button(self.frameMenuLobby, text='Demarrer', command=self.lancerSignal)
        self.boutonRetour= tkinter.Button(self.frameMenuLobby, text='Retour',command=self.retour)
        #on place les boutons de navigation
        self.boutonDemarrer.place(x=550,y=650)
        self.boutonRetour.place(x=400,y=650)
        
    def menuLobby(self):
        self.inLobby = True
        self.frameMenuLobby.pack()
        
    def lancerSignal(self):
        self.network.sendData(nd.StartGameMsg())

    def debuterPartie(self, playerList):
        for player in playerList:
            self.parent.parent.nouveauJoueur(player.id, player.race, player.nom)
        self.inLobby = False
        self.frameMenuLobby.pack_forget()
        self.parent.parent.enJeu() 
        
    def retour(self):
        self.inLobby = False
        self.network.disconnect()
        self.frameMenuLobby.pack_forget()
        self.parent.menuP.menuPrincipal()

    def update(self, clientList):
        nb = "Nombre de joueurs : " + str(len(clientList))
        self.fondEcran.delete("nbPlayer")
        self.fondEcran.create_text(140,70,text=nb,font=("verdana","12","bold"),fill="red",tags="nbPlayer")
        
        i=0
        for client in clientList:
            txt= str(client.id)+ "                  " + client.nom +"                " + client.race
        
            self.fondEcran.create_text(270,200+i*50,font=("verdana","12","bold"), text=txt, fill='red', tags="nbplayer")
            i+=1

    def updateClientList(self):
        self.network.recevoirDonnees()

        if self.inLobby:
            self.parent.root.after(100, self.updateClientList)