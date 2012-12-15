# -*- coding: ISO-8859-1 -*-
import tkinter
import MenuPrincipal
import MenuNouvellePartie
import MenuChargerPartie
import MenuConnexion
import MenuLobby
import HudHaut
import FrameJeu
import GestionImage

class Application():
    def __init__(self, parent):
        self.parent = parent
        
        #dimensions de la fenêtre
        self.largeurFrame=1024
        self.hauteurFrame=700
        
        self.root=tkinter.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.quitter)
        self.root.config(bg="#000")
        self.root.resizable(0,0)
        self.root.title("AreaB51")
        
        self.gestionnaireImage = GestionImage.GestionImage()
        
        self.initialisationInterfaces()
    #############################Initialisation de tous les éléments de base de toutes les interfaces#############################
    def initialisationInterfaces(self):
        #création de tous les menus
        self.menuP = MenuPrincipal.MenuPrincipal(self)
        self.menuN = MenuNouvellePartie.MenuNouvellePartie(self)
        self.menuC = MenuConnexion.MenuConnexion(self)
        self.menuL = MenuLobby.MenuLobby(self)
        #création du hud du haut placé dans frameDuJeu
        self.hudH=HudHaut.HudHaut(self,self.root)
        #création de l'interface du jeu (seuls certaines variables sont initialisés et les images importés)
        self.frameJeu=FrameJeu.FrameJeu(self)
    
    #############################Appel pour afficher les interfaces#############################
    def menuPrincipal(self):
        self.menuP.menuPrincipal()
        
    def menuNouvellePartie(self,event):
        self.menuP.effaceMenuPrinc()
        self.menuN.menuNouvellePartie()
        
    def menuInventaire(self):
        self.frameJeu.menuI.menuInventaire()
    
    def menuConnexion(self):
        self.menuC.menuConnexion()
        
    def menuLobby(self):
        self.menuL.menuLobby()
        
    def jeu(self,perso,laSalle):
        self.hudHaut(perso)
        self.frameJeu.initMap(perso,laSalle)
        
    def hudHaut(self,perso):
        self.hudH.hudHaut(perso)
    
    def effaceTout(self):
        self.hudH.effacer()
        self.frameJeu.effacer()
    
    #############################Retourne l'objet de l'image#############################
    def getImage(self,nomImage):
        return self.gestionnaireImage.getImage(nomImage)    
    
    #############################Appelé à la fermeture du jeu#############################
    def quitter(self):
        self.root.quit()
