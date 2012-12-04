# -*- coding: ISO-8859-1 -*-
import tkinter
import MenuPrincipal
import MenuNouvellePartie
import MenuChargerPartie
import MenuConnexion
import FrameJeu

class Application():
    def __init__(self, parent):
        self.parent = parent
        
        #dimensions de la fenêtre
        self.largeurFrame=1024
        self.hauteurFrame=700
        
        self.root=tkinter.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.quitter)
        
    def menuPrincipal(self):
        self.menuP=MenuPrincipal.MenuPrincipal(self)
        
    def menuNouvellePartie(self,event):
        self.menuP.effaceMenuPrinc()
        self.menuN=MenuNouvellePartie.MenuNouvellePartie(self)
        
    def menuChargerPartie(self,event):
        self.menuP.effaceMenuPrinc()
        #self.menuCP = MenuChargerPartie.MenuChargerPartie(self)
        self.menuNouvellePartie("allo")
        
    def menuConnexion(self):
        self.menuC=MenuConnexion.MenuConnexion(self)
    
    def jeu(self):
        self.frameJeu=FrameJeu.FrameJeu(self)
        
    def quitter(self):
        self.root.quit()