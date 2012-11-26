import tkinter

class MenuConnexion():
    def __init__(self, parent, nom):
        self.parent = parent
        self.menuConnexion()
        self.nom = nom
        
    def menuConnexion(self):
        self.backgroundImage = tkinter.PhotoImage(file='assets/Image/Prometheus_1.gif',width=1024,height=768)
        self.fondEcran= tkinter.Canvas(self.parent.root,width=1024,height=768)
        self.fondEcran.place(x=0,y=0)
        self.fondEcran.create_image(512,384, image= self.backgroundImage,tags="fondEcran")
        
        self.fondEcran.create_text(100,60,text="Adresse IP :",font=("Arial","15"),fill="white",tags="textIP")
        self.ipentry = tkinter.Entry(self.parent.root, width="14" )
        self.boutonConnexion= tkinter.Button(self.parent.root, text='Debuter', command=self.validerIPort)
        self.boutonRetour= tkinter.Button(self.parent.root, text='Retour',command=self.retour)
                
        #place les widget
        self.ipentry.place(x=200, y=50)
        self.boutonConnexion.place(x=550,y=650)
        self.boutonRetour.place(x=400,y=650)

    def effacerEcran(self):
        self.ipentry.destroy()
        self.boutonConnexion.destroy()   
        self.boutonRetour.destroy()
        self.fondEcran.destroy()
        
    def retour(self):
        self.effacerEcran()
        self.parent.menuP.menuPrincipal()
        
    def debuterPartie(self):
        self.effacerEcran()
        self.parent.parent.enJeu()
        
       
    def validerIPort(self):
        adresse = self.ipentry.get()

        temp = adresse.split(':')
        adresse = temp[0]
        port = temp[1]
        port = int(port)

        self.parent.parent.reseau.connecter(adresse, port, self.nom)

        self.debuterPartie()
