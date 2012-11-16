import tkinter

class MenuChargerPartie():
    def __init__(self, parent):
        self.parent = parent
        self.menuChargerPartie()
        
    def menuChargerPartie(self):
        self.backgroundImage = tkinter.PhotoImage(file='assets/Image/Prometheus_1.gif',width=1024,height=768)
        self.fondEcran= tkinter.Canvas(self.parent.root,width=1024,height=768)
        self.fondEcran.place(x=0,y=0)
        self.fondEcran.create_image(512,384, image= self.backgroundImage,tags="fondEcran")
                
        self.iplabel = tkinter.Label(self.parent.root, text="connection: ", width=15)
        self.ipentry = tkinter.Entry(self.parent.root, width="18" )
        self.portlabel = tkinter.Label(self.parent.root, text="Port: ", width=15)
        self.portentry = tkinter.Entry(self.parent.root, width="18" )
        self.bouton= tkinter.Button(self.parent.root, text='Debuter', command=self.validerIPort)
        self.boutonRetour= tkinter.Button(self.parent.root, text='Retour',command=self.effacerEcran)
                
        #place les widget
        self.iplabel.place(x=50, y=50)
        self.ipentry.place(x=200, y=50)
        self.portlabel.place(x=50, y=100)
        self.portentry.place(x=200, y=100)
        self.bouton.place(x=400,y=400)
        self.boutonRetour.place(x=200,y=400)
        
    def effacerEcran(self):
        self.iplabel.destroy()
        self.ipentry.destroy()
        self.portlabel.destroy()
        self.portentry.destroy()
        self.bouton.destroy()   
        self.boutonRetour.destroy()
        
    def debuterPartie(self,ip,port):
        
        ## debuter la partie si les informations rentres sont correct 
        #si le no port et ip  sont correct donc on continue
        self.effacerEcran()
        self.txt="Partie debute a l'adresse " +ip+":"+port
        self.debuterPartieTexte= self.fondEcran.create_text(400,200,text=self.txt ,fill='white',font=("Arial","30"),tags="debuter_partie")
        
    def validerIPort(self):
        port=self.portentry.get()
        ip=self.ipentry.get()
        if ip and port:
            print(ip+':'+port)
            self.debuterPartie(ip,port)
        else:
            print("cases vides")
            return False      
        # sinon on redemande de rentrer les info de reseau encore