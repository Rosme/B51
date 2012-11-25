# -*- coding: ISO-8859-1 -*-
import tkinter

class MenuPrincipal():
    def __init__(self, parent):
        self.parent = parent
        self.menuPrincipal()
        
    def menuPrincipal(self):
        self.backgroundImage = tkinter.PhotoImage(file='assets/Image/Prometheus_1.gif',width=1024,height=768)
        self.fondEcran= tkinter.Canvas(self.parent.root,width=1024,height=768)
        self.fondEcran.place(x=0,y=0)
        self.fondEcran.create_image(512,384, image= self.backgroundImage,tags="fondEcran")
        
        
        self.nouvellePartieTexte= self.fondEcran.create_text(512,250,text='Nouvelle partie',fill='white',font=("Arial","30"),tags="nouvelle_partie",activefill='red')
        self.continuerPartieTexte= self.fondEcran.create_text(512,350,text='Continuer une partie',fill='white',font=("Arial","30"),tags="continuer_partie",activefill='red')
        self.quitterTexte= self.fondEcran.create_text(512,450,text='Quitter',fill='white',font=("Arial","30"),tags="quitter",activefill='red')
        
        
        self.fondEcran.tag_bind("nouvelle_partie","<Button-1>",self.parent.menuNouvellePartie)
        self.fondEcran.tag_bind("continuer_partie","<Button-1>", self.parent.menuChargerPartie)
        self.fondEcran.tag_bind("quitter","<Button-1>",self.fermerFenetre)
        
    def effaceMenuPrinc(self):
        #effacer l'ecran principale
        self.fondEcran.tag_unbind("nouvelle_partie","<Button-1>")
        self.fondEcran.tag_unbind("continuer_partie","<Button-1>")
        self.fondEcran.tag_unbind("quitter","<Button-1>")
        self.fondEcran.destroy()
        
    def fermerFenetre(self,event):
        self.parent.quitter()