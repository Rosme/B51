import tkinter

class HudHaut():
    def __init__(self,parent,perso):
        self.parent=parent
        self.perso=perso
        self.nbSeringue=0
        self.poidsJoueur=0
        
        self.grandeurVie=(self.perso.race.vie*120)/self.perso.race.max_vie
        for i in self.perso.inventaire.items:
            if i.id==8:
                self.grandeurShield=(i.energie*120)/i.max_energie
            if i.id==7:
                self.grandeurArme=(i.energie*120)/i.max_energie
            if i.id == 3:
                self.nbSeringue+=i.qte
            self.poidsJoueur+=(i.poids*i.qte)
        
        self.importerImage()
        
        self.frameHudHaut=tkinter.Frame(self.parent.parent.root)
        
        self.affichageImageEtBarre()
        
        self.frameHudHaut.pack()
        
    def affichageImageEtBarre(self):
        self.cHudHaut=tkinter.Canvas(self.frameHudHaut,width=1024,height=80,bg="#000",bd=0,highlightbackground="#000",highlightcolor="#000",highlightthickness=0)
    
        # la barre pour la vie du joueur. 
        self.cHudHaut.create_image(85,40, image= self.energy)
        self.cHudHaut.create_rectangle(35, 60,self.grandeurVie+35, 75,fill="blue",tag="hudhaut")
        
        #le shield
        self.cHudHaut.create_image(280,40, image= self.shield)
        self.cHudHaut.create_rectangle(235, 60, self.grandeurShield+235, 75,fill="blue",tag="hudhaut")
        
        #le gun power
        self.cHudHaut.create_image(455,40, image= self.gunpower)
        self.cHudHaut.create_rectangle(410, 60, self.grandeurArme+410, 75,fill="blue",tag="hudhaut")
        
        #le healing
        self.cHudHaut.create_image(610,40, image= self.healing)
        self.cHudHaut.create_text(640,40,text=self.nbSeringue,fill='white',font=("Arial","10"),tag="hudhaut")
        
        # le poid que le joueur peut avoir
        self.cHudHaut.create_image(785,40, image= self.poids)
        self.cHudHaut.create_text(835,40,text=str(self.poidsJoueur)+" /"+str(self.perso.race.poidsLimite),fill='white',font=("Arial","10"),tag="hudhaut")
        
        self.cHudHaut.pack()
        
    def importerImage(self):
        self.energy = tkinter.PhotoImage(file='assets/image/energy.gif',width=35,height=35)
        self.shield = tkinter.PhotoImage(file='assets/image/bouclier.gif',width=45,height=35)
        self.gunpower = tkinter.PhotoImage(file='assets/image/gun.gif',width=45,height=35)
        self.healing=tkinter.PhotoImage(file='assets/image/syringe.gif',width=45,height=35)
        self.poids=tkinter.PhotoImage(file='assets/image/backpack.gif',width=40,height=35)