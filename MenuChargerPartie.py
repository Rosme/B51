import tkinter
import tkinter.messagebox
import pickle

class MenuChargerPartie():
    def __init__(self, parent):
        self.parent = parent
        self.loadChar()
    
    '''def menuValiderNom(self):
        self.backgroundImage = tkinter.PhotoImage(file='assets/Image/Prometheus_1.gif',width=1024,height=768)
        self.fondEcran= tkinter.Canvas(self.parent.root,width=1024,height=768)
        self.fondEcran.place(x=0,y=0)
        self.fondEcran.create_image(512,384, image= self.backgroundImage,tags="fondEcran")      
        self.iplabel = tkinter.Label(self.parent.root, text = "Entrer votre nom ", width=15)
        self.ipentry = tkinter.Entry(self.parent.root,width="18" )
        self.bouton= tkinter.Button(self.parent.root, text='Valider', command=self.loadChar)
        self.boutonRetour= tkinter.Button(self.parent.root, text='Retour',command=None)
        #place les widget
        self.iplabel.place(x=50, y=50)
        self.ipentry.place(x=200, y=50)
        self.bouton.place(x=400,y=400)
        self.boutonRetour.place(x=200,y=400)'''
        
    def menuPerso(self):
        self.joueur = []
        self.backgroundImage = tkinter.PhotoImage(file='assets/Image/Prometheus_1.gif',width=1024,height=768)
        self.fondEcran= tkinter.Canvas(self.parent.root,width=1024,height=768)
        self.fondEcran.place(x=0,y=0)
        self.fondEcran.create_image(512,384, image= self.backgroundImage,tags="fondEcran")      
        for i in self.file.readlines():
            self.joueur[i] = self.file.readlines()
            self.nomLabel = self.fondEcran.create_text(512 + i*5,250,text=self.joueur[i],fill='white',font=("Arial","30"),tags="nouvelle_partie",activefill='red')
            
    def loadChar(self):
        try:
            self.file = open("player.dat", 'a')
            self.menuPerso()
        except IOError as e:
            tkinter.messagebox.showwarning("Aucun Joueur", "Aucune sauvegarde n'a ete trouve", command=self.parent.menuP.menuPrincipal())
    
    def saveChar(self):
        pass
    

    