import tkinter

class MenuConnexion():
    def __init__(self, parent):
        self.parent = parent
        self.menuConnexion()
        
    def menuConnexion(self):
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