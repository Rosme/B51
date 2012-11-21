import tkinter
import socket
import pickle
import netdata as nd

class MenuConnexion():
    def __init__(self, parent):
        self.parent = parent
        self.nom = ''
        self.menuConnexion(self.nom)
        
    def menuConnexion(self, nomJoueur):
        self.nom = nomJoueur
        self.backgroundImage = tkinter.PhotoImage(file='assets/Image/Prometheus_1.gif',width=1024,height=768)
        self.fondEcran= tkinter.Canvas(self.parent.root,width=1024,height=768)
        self.fondEcran.place(x=0,y=0)
        self.fondEcran.create_image(512,384, image= self.backgroundImage,tags="fondEcran")
                
        self.iplabel = tkinter.Label(self.parent.root, text="connexion: (IP:Port)", width=15)
        self.ipentry = tkinter.Entry(self.parent.root, width="18" )
        self.bouton= tkinter.Button(self.parent.root, text='Debuter', command=self.validerIPort)
        self.boutonRetour= tkinter.Button(self.parent.root, text='Retour',command=self.effacerEcran)
                
        #place les widget
        self.iplabel.place(x=50, y=50)
        self.ipentry.place(x=200, y=50)
        self.bouton.place(x=400,y=400)
        self.boutonRetour.place(x=200,y=400)

    def effacerEcran(self):
        self.iplabel.destroy()
        self.ipentry.destroy()
        self.bouton.destroy()   
        self.boutonRetour.destroy()
        self.fondEcran.destroy()
        
    def debuterPartie(self):
        self.effacerEcran()
        self.parent.parent.enJeu()
    
    def validerIPort(self):
        adresse = self.ipentry.get()

        temp = adresse.split(':')
        adresse = temp[0]
        port = temp[1]
        port = int(port)

        reseau = self.parent.parent.reseau.connecter(adresse, port, self.nom)
        print(reseau.id)

        self.debuterPartie()