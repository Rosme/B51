# -*- coding: ISO-8859-1 -*-
import tkinter
import MenuPrincipal
import MenuNouvellePartie
import MenuChargerPartie
import MenuConnexion
import MenuLobby
import FrameJeu
import GestionImage

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
        self.root.resizable(0,0)
        self.root.title("AreaB51")
        
        self.gestionnaireImage = GestionImage.GestionImage()
        
        self.initialisationInterfaces()
    
    def initialisationInterfaces(self):
        #création de tous les menus
        self.menuP = MenuPrincipal.MenuPrincipal(self)
        self.menuN = MenuNouvellePartie.MenuNouvellePartie(self)
        #self.menuP = MenuChargerPartie.MenuChargerPartie(self)
        self.menuC = MenuConnexion.MenuConnexion(self)
        self.menuL = MenuLobby.MenuLobby(self)
        #création de l'interface du jeu (seuls certaines variables sont initialisés et les images importés)
        self.frameJeu=FrameJeu.FrameJeu(self)
        
    def menuPrincipal(self):
        self.menuP.menuPrincipal()
        
    def menuNouvellePartie(self,event):
        self.menuP.effaceMenuPrinc()
        self.menuN.menuNouvellePartie()
        
    #def menuChargerPartie(self,event):
        #self.menuP.effaceMenuPrinc()
        #self.menuCP = MenuChargerPartie.MenuChargerPartie(self)
        #self.menuN.menuNouvellePartie()
    
    def menuInventaire(self):
        self.frameJeu.menuI.menuInventaire()
    
    def menuConnexion(self):
        self.menuC.menuConnexion()
        
    def menuLobby(self):
        self.menuL.menuLobby()
        
    def jeu(self,perso,laSalle):
        return self.frameJeu.initMap(perso,laSalle)
    
    def getImage(self,nomImage):
        return self.gestionnaireImage.getImage(nomImage)
        
    def quitter(self):
        #self.parent.reseau.deconnecter()
        self.root.quit()
