# -*- coding: ISO-8859-1 -*-
import tkinter

class MenuPrincipal():
    def __init__(self, parent):
        self.parent = parent
        self.frameMenuPrincipal=tkinter.Frame(self.parent.root)
        
        self.fondEcran= tkinter.Canvas(self.frameMenuPrincipal,width=1024,height=768)
        self.fondEcran.pack()
        self.fondEcran.create_image(512,384, image= self.parent.getImage("backgroundImage"),tags="fondEcran")
        self.nouvellePartieTexte= self.fondEcran.create_text(512,250,text='Nouvelle partie',fill='white',font=("Arial","30"),tags="nouvelle_partie",activefill='red')
        self.quitterTexte= self.fondEcran.create_text(512,450,text='Quitter',fill='white',font=("Arial","30"),tags="quitter",activefill='red')
        
        self.fondEcran.tag_bind("nouvelle_partie","<Button-1>",self.parent.menuNouvellePartie)
        self.fondEcran.tag_bind("quitter","<Button-1>",self.fermerFenetre)
        
    def menuPrincipal(self):
        self.frameMenuPrincipal.pack()
        
    def effaceMenuPrinc(self):
        #effacer l'ecran principale
        self.frameMenuPrincipal.pack_forget()
        
    def fermerFenetre(self,event):
        self.parent.quitter()