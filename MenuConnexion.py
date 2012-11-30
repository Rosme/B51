import tkinter

class MenuConnexion():
    def __init__(self, parent):
        self.parent = parent
        self.frameMenuConnexion=tkinter.Frame(self.parent.root)
        self.backgroundImage = tkinter.PhotoImage(file='assets/Image/Prometheus_1.gif',width=1024,height=768)
        self.fondEcran= tkinter.Canvas(self.frameMenuConnexion,width=1024,height=768)
        self.fondEcran.pack()
        self.fondEcran.create_image(512,384, image= self.backgroundImage,tags="fondEcran")
        self.fondEcran.create_text(100,60,text="Adresse IP :",font=("Arial","15"),fill="white",tags="textIP")
        self.ipentry = tkinter.Entry(self.frameMenuConnexion, width="14" )
        self.boutonConnexion= tkinter.Button(self.frameMenuConnexion, text='Debuter', command=self.validerIPort)
        self.boutonRetour= tkinter.Button(self.frameMenuConnexion, text='Retour',command=self.retour)
                
        #place les widget
        self.ipentry.place(x=200, y=50)
        self.boutonConnexion.place(x=550,y=650)
        self.boutonRetour.place(x=400,y=650)
        self.menuConnexion()
        
    def menuConnexion(self):
        self.frameMenuConnexion.pack()
        
    def effacerEcran(self):
        self.frameMenuConnexion.pack_forget()
        
    def retour(self):
        self.effacerEcran()
        self.parent.menuP.menuPrincipal()
        
    def debuterPartie(self):
        self.effacerEcran()
        self.parent.parent.enJeu()
        
    def validerIPort(self):
        self.debuterPartie()
       
    '''
    def validerIPort(self):
        adresse = self.ipentry.get()

        temp = adresse.split(':')
        adresse = temp[0]
        port = temp[1]
        temp = adresse.split('.')
        
        if len(temp) != 4:
            return False
        
        adresse = []    
        for i in range(4):
            adresse.append(temp[i])
        
        try:
            ip = []
            for i in adresse:
                ip.append(int(i))
        
            port = int(port)
            
            for i in range(4):
                if ip[i] > 255 or ip[i]< 0:
                    return False
        
            if port <= 1024 or port >= 49551:
                return False
                    
        except ValueError:
            return False
        # sinon on redemande de rentrer les info de reseau encore
    '''