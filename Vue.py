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
        
        self.nomJoueur = "Marco"

        self.root=tkinter.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.quitter)
        self.root.config(bg="#000")

        #création de tous les menus
        self.menuP = MenuPrincipal.MenuPrincipal(self)
        self.menuN = MenuNouvellePartie.MenuNouvellePartie(self)
        #self.menuP = MenuChargerPartie.MenuChargerPartie(self)
        self.menuC = MenuConnexion.MenuConnexion(self)
        #création de l'interface du jeu (seuls certaines variables sont initialisés et les images importés)
        self.frameJeu=FrameJeu.FrameJeu(self)
        
    def menuPrincipal(self):
        self.menuP.menuPrincipal()
        
    def menuNouvellePartie(self,event):
        self.menuP.effaceMenuPrinc()
        self.menuN.menuNouvellePartie()
        
    def menuChargerPartie(self,event):
        self.menuP.effaceMenuPrinc()
        #self.menuCP = MenuChargerPartie.MenuChargerPartie(self)
        self.menuN.menuNouvellePartie()
        
    def menuConnexion(self):
        self.menuC.menuConnexion()
    
    def jeu(self,perso,laSalle):
        return self.frameJeu.initMap(perso,laSalle)
        
    def quitter(self):
        self.parent.reseau.deconnecter()
        self.root.quit()
