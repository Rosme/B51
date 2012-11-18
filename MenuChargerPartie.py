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
        ligne = self.file.readline() 
        i=0  
        while len(ligne) != 0:
            self.nomLabel = self.fondEcran.create_text(300 + i*5,100,text=ligne,fill='white',font=("Arial","20"),tags="nouvelle_partie",activefill='red')
            ligne = self.file.readline() 
            i+=1
            
    def loadChar(self):
        try:
            self.file = open("player.dat", 'r')
            self.menuPerso()
        except IOError as e:
            tkinter.messagebox.showwarning("Aucun Joueur", "Aucune sauvegarde n'a ete trouve", command=self.parent.menuP.menuPrincipal())
    
    def saveChar(self):
        pass
    

    