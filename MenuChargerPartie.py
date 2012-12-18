import tkinter
import tkinter.messagebox
import pickle

class MenuChargerPartie():
    def __init__(self, parent):
        self.parent = parent
        self.loadChar()
        
    def menuPerso(self):
        self.frameMenuChargerPartie=tkinter.Frame(self.parent.root)
        self.fondEcran= tkinter.Canvas(self.frameMenuChargerPartie,width=1024,height=768)
        self.fondEcran.pack()
        self.fondEcran.create_image(512,384, image= self.parent.getImage("backgroundImage"),tags="fondEcran")
        self.boutonConnexion= tkinter.Button(self.fondEcran, text='Continuer',command=self.getPlayer)
        self.boutonRetour= tkinter.Button(self.fondEcran, text='Retour',command=self.effacerEcran)
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
        
        self.menuChargerPartie()
    
    def menuChargerPartie(self):
        self.frameMenuChargerPartie.pack()
    
    def effacerEcran(self):
        self.frameMenuChargerPartie.pack_forget()    
    
    def loadChar(self):
        try:
            self.file = open("player.dat", 'r')
            self.menuPerso()
        except IOError as e:
            tkinter.messagebox.showwarning("Aucun Joueur", "Aucune sauvegarde n'a ete trouve", command=self.parent.menuP.menuPrincipal())

    def getPlayer(self):
        self.player = self.v.get()
        self.effacerEcran()
        self.parent.menuConnexion()

    