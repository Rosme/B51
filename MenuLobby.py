# -*- coding: ISO-8859-1 -*-
import tkinter

class MenuLobby():
    
    def __init__(self,parent):
        self.parent = parent
        self.menuLobby()
        
    def menuLobby(self):
        #Image de fond
        self.backgroundImage = tkinter.PhotoImage(file='assets/Image/Prometheus_1.gif',width=1024,height=768)
        self.fondEcran= tkinter.Canvas(self.parent.root,width=1024,height=768)
        self.fondEcran.place(x=0,y=0)
        self.fondEcran.create_image(512,384, image= self.backgroundImage,tags="fondEcran")
        
        #creation de la fenetre lobby
        self.fenetre = tkinter.Canvas(self.parent.root,width=400, height=400)
        self.fenetre.create_rectangle(0,0,100,100)
        
        #creation de la fenetre nombre de joueurs
        self.fenetreNbJoueurs = tkinter.Canvas(self.parent.root,width=100, height=40)
        self.fenetreNbJoueurs .create_rectangle(0,0,110,50)
        self.fenetreNbJoueurs.place(x=40,y=90)
        self.fondEcran.create_text(140,70,text="Nombre de joueurs :",font=("verdana","12","bold"),fill="red",tags="textIP")
        
        #creation de la fenetre information du joueur
        self.fenetreInfo = tkinter.Canvas(self.parent.root,width=800, height=40)
        self.fenetreInfo.create_rectangle(0,0,820,50)
        self.fenetreInfo.place(x=40,y=200)
        self.fondEcran.create_text(170,180,text="Information sur le joueur :",font=("verdana","12","bold"),fill="red",tags="textIP")
        
        #creation de boutton
        self.boutonDemarrer= tkinter.Button(self.parent.root, text='Demarrer', command=self.debuterPartie)
        self.boutonRetour= tkinter.Button(self.parent.root, text='Retour',command=self.retour)
        #on place les boutons de navigation
        self.boutonDemarrer.place(x=550,y=650)
        self.boutonRetour.place(x=400,y=650)
        
    def debuterPartie(self):
        self.effacerEcran()
        self.parent.parent.enJeu()  
    
    def effacerEcran(self):
        self.boutonDemarrer.destroy()   
        self.boutonRetour.destroy()
        self.fondEcran.destroy()
        
    def retour(self):
        self.effacerEcran()
        self.parent.menuP.menuPrincipal()