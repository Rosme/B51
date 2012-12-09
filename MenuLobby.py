# -*- coding: ISO-8859-1 -*-
import tkinter

class MenuLobby():
    
    def __init__(self,parent):
        self.parent = parent
        self.frameMenuLobby = tkinter.Frame(self.parent.root)
        
        #Image de fond
        self.backgroundImage = tkinter.PhotoImage(file='assets/Image/Prometheus_1.gif',width=1024,height=768)
        self.fondEcran= tkinter.Canvas(self.frameMenuLobby,width=1024,height=768)
        self.fondEcran.pack()
        self.fondEcran.create_image(512,384, image= self.backgroundImage,tags="fondEcran")
        
        #creation de la fenetre lobby
        
        self.fenetre = tkinter.Canvas(self.frameMenuLobby,width=400, height=400)
        self.fenetre.create_rectangle(0,0,100,100)
        
        #creation de la fenetre nombre de joueurs
        self.fenetreNbJoueurs = tkinter.Canvas(self.frameMenuLobby,width=100, height=40)
        self.fenetreNbJoueurs .create_rectangle(0,0,110,50)
        self.fenetreNbJoueurs.place(x=40,y=90)
        self.fondEcran.create_text(140,70,text="Nombre de joueurs :",font=("verdana","12","bold"),fill="red",tags="textIP")
        
        #creation de la fenetre information du joueur
        self.fenetreInfo = tkinter.Canvas(self.frameMenuLobby,width=800, height=40)
        self.fenetreInfo.create_rectangle(0,0,820,50)
        self.fenetreInfo.place(x=40,y=200)
        self.fondEcran.create_text(170,180,text="Information sur le joueur :",font=("verdana","12","bold"),fill="red",tags="textIP")
        
        #creation de boutton
        self.boutonDemarrer= tkinter.Button(self.frameMenuLobby, text='Demarrer', command=self.debuterPartie)
        self.boutonRetour= tkinter.Button(self.frameMenuLobby, text='Retour',command=self.retour)
        #on place les boutons de navigation
        self.boutonDemarrer.place(x=550,y=650)
        self.boutonRetour.place(x=400,y=650)
        
    def menuLobby(self):
        self.frameMenuLobby.pack()
        
    def debuterPartie(self):
        self.frameMenuLobby.pack_forget()
        self.parent.parent.enJeu() 
        
    def retour(self):
        self.frameMenuLobby.pack_forget()
        self.parent.menuP.menuPrincipal()