import tkinter
import tkinter.messagebox
import pickle

class MenuChargerPartie():
    def __init__(self, parent):
        self.parent = parent
        self.loadChar()
        
    def menuPerso(self):
        self.backgroundImage = tkinter.PhotoImage(file='assets/Image/Prometheus_1.gif',width=1024,height=768)
        self.fondEcran= tkinter.Canvas(self.parent.root,width=1024,height=768)
        self.fondEcran.place(x=0,y=0)
        self.fondEcran.create_image(512,384, image= self.backgroundImage,tags="fondEcran")
        self.boutonConnexion= tkinter.Button(self.fondEcran, text='Continuer',command=self.getPlayer)
        self.boutonRetour= tkinter.Button(self.fondEcran, text='Retour',command=self.retour)
        self.boutonConnexion.place(x=550,y=650)
        self.boutonRetour.place(x=400,y=650)   
        
        self.listePartie=tkinter.Canvas(self.fondEcran,width=200,height=500,bg="black")
        self.listePartie.place(x=300,y=100)
        ligne = self.file.readline() 
        i=0 
        self.boutonListe = []
        sauvegardeListe = []
        self.v=tkinter.StringVar()
        self.v.set("")
        while len(ligne) != 0:
            sauvegardeListe.append(ligne)
            self.boutonListe.append(tkinter.Radiobutton(self.listePartie, text=ligne,variable=self.v, value=sauvegardeListe[i]))
            self.boutonListe[i].place(x=0, y=i*25)
            ligne = self.file.readline()
            i+=1
        self.boutonListe[0].select()
            
    def loadChar(self):
        try:
            self.file = open("player.dat", 'r')
            self.menuPerso()
        except IOError as e:
            tkinter.messagebox.showwarning("Aucun Joueur", "Aucune sauvegarde n'a ete trouve", command=self.parent.menuP.menuPrincipal())
    
    def saveChar(self):
        pass
    
    def retour(self): 
        self.effacerEcran()
        self.parent.menuP.menuPrincipal()
    
    def effacerEcran(self):
        self.fondEcran.destroy()
    
    def getPlayer(self):
        self.player = self.v.get()
        self.parent.menuConnexion()

    