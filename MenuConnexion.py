import tkinter

class MenuConnexion():
    def __init__(self, parent):
        self.parent = parent
        self.frameMenuConnexion=tkinter.Frame(self.parent.root)
        
        self.fondEcran= tkinter.Canvas(self.frameMenuConnexion,width=1024,height=768)
        self.fondEcran.pack()
        self.fondEcran.create_image(512,384, image= self.parent.getImage("backgroundImage"),tags="fondEcran")
        self.fondEcran.create_text(100,60,text="Adresse IP :",font=("Arial","15"),fill="white",tags="textIP")
        self.ipentry = tkinter.Entry(self.frameMenuConnexion, width="14" )
        self.boutonNouveauServeur = tkinter.Button(self.frameMenuConnexion, text='Nouveau serveur', command=self.nouveauServeur)
        self.boutonRejoindre= tkinter.Button(self.frameMenuConnexion, text='Rejoindre une partie', command=self.validerIPort)
        self.boutonRetour= tkinter.Button(self.frameMenuConnexion, text='Retour',command=self.retour)
                
        #place les widget
        self.ipentry.place(x=200, y=50)
        self.boutonNouveauServeur.place(x=700,y=650)
        self.boutonRejoindre.place(x=550,y=650)
        self.boutonRetour.place(x=400,y=650)
        
    def menuConnexion(self):
        self.frameMenuConnexion.pack()
        
    def retour(self):
        self.frameMenuConnexion.pack_forget()
        self.parent.menuPrincipal()
     
    def rejoindreUnePartie(self):
        self.frameMenuConnexion.pack_forget()
        self.parent.menuLobby()
        
    def nouveauServeur(self):
        self.frameMenuConnexion.pack_forget()
        self.parent.menuLobby()
        
    def validerIPort(self):
        self.rejoindreUnePartie()

        '''
        adresse = self.ipentry.get()

        temp = adresse.split(':')
        adresse = temp[0]
        port = temp[1]
        port = int(port)

        self.parent.parent.reseau.connecter(adresse, port, self.nom)

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
