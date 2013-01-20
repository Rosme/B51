import tkinter

class HudHaut():
    def __init__(self,parent,root):
        self.parent=parent
        
        self.frameHudHaut=tkinter.Frame(root)
        self.cHudHaut=tkinter.Canvas(self.frameHudHaut,width=1024,height=80,bg="#000",bd=0,highlightbackground="#000",highlightcolor="#000",highlightthickness=0)
        
        self.affichageImage()
        
        self.cHudHaut.pack()
    
    def hudHaut(self,perso): 
        self.affichageBarre(perso)
        self.frameHudHaut.pack()
    
    def calcul(self,perso):
        self.nbSeringue=0
        self.poidsJoueur=0
        if (perso.race.vie*120)/perso.race.max_vie <0:
            self.grandeurVie = 0
        else:
            self.grandeurVie=(perso.race.vie*120)/perso.race.max_vie
        for i in perso.inventaire.items:
            if i.id==8:
                self.grandeurShield=(i.energie*120)/i.max_energie
            if i.id==7:
                self.grandeurArme=(i.energie*120)/i.max_energie
            if i.id == 3:
                self.nbSeringue+=1
            self.poidsJoueur+=i.poids
        
    def affichageImage(self):
        # la barre pour la vie du joueur. 
        self.cHudHaut.create_image(85 ,40, image = self.parent.getImage("vie"))
        #le shield
        self.cHudHaut.create_image(280,40, image = self.parent.getImage("shield"))
        #le gun power
        self.cHudHaut.create_image(455,40, image = self.parent.getImage("batterie"))
        #le healing
        self.cHudHaut.create_image(610,40, image = self.parent.getImage("seringue"))
        # le poid que le joueur peut avoir
        self.cHudHaut.create_image(785,40, image = self.parent.getImage("sac"))
    
    def affichageBarre(self,perso):
        self.cHudHaut.delete("hudhaut")
        self.calcul(perso)
        self.cHudHaut.create_rectangle(35, 60,self.grandeurVie+35, 75,fill="blue",tag="hudhaut")
        self.cHudHaut.create_rectangle(235, 60, self.grandeurShield+235, 75,fill="blue",tag="hudhaut")
        self.cHudHaut.create_rectangle(410, 60, self.grandeurArme+410, 75,fill="blue",tag="hudhaut")
        self.cHudHaut.create_text(640,40,text=self.nbSeringue,fill='white',font=("Arial","10"),tag="hudhaut")
        self.cHudHaut.create_text(835,40,text=str(self.poidsJoueur)+" /"+str(perso.race.poidsLimite),fill='white',font=("Arial","10"),tag="hudhaut")

    def actualiser(self,perso):
        self.affichageBarre(perso)
   
    def effacer(self):
        self.frameHudHaut.pack_forget()
        
