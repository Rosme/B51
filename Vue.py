# -*- coding: ISO-8859-1 -*-
import tkinter
import MenuPrincipal
import MenuNouvellePartie
import MenuChargerPartie
import MenuInventaire
import MenuArtisanat
import MenuConnexion
import MenuLobby
import HudHaut
import FrameJeu
import GestionImage
import GestionSon
import os

class Application():
    def __init__(self, parent,subDivision):
        self.parent = parent
        self.subDivision=subDivision
        
        #dimensions de la fen�tre
        self.largeurFrame=1024
        self.hauteurFrame=700
        
        self.root=tkinter.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.quitter)
        self.root.config(bg="#000")
        self.root.resizable(0,0)
        self.root.title("AreaB51")
        
        self.gestionnaireSon = GestionSon.GestionSon()
        self.gestionnaireImage = GestionImage.GestionImage()
        
        self.initialisationInterfaces()
    #############################Initialisation de tous les �l�ments de base de toutes les interfaces#############################
    def initialisationInterfaces(self):
        #cr�ation de tous les menus
        self.menuP = MenuPrincipal.MenuPrincipal(self)
        self.menuN = MenuNouvellePartie.MenuNouvellePartie(self)
        self.menuC = MenuConnexion.MenuConnexion(self)
        self.menuL = MenuLobby.MenuLobby(self)
        self.menuI = MenuInventaire.MenuInventaire(self)
        self.menuA = MenuArtisanat.MenuArtisanat(self)
        #cr�ation du hud du haut plac� dans frameDuJeu
        self.hudH=HudHaut.HudHaut(self,self.root)
        #cr�ation de l'interface du jeu (seuls certaines variables sont initialis�s et les images import�s)
        self.frameJeu=FrameJeu.FrameJeu(self,self.subDivision)
    
    #############################Appel pour afficher les interfaces#############################
    def menuPrincipal(self):
        self.gestionnaireSon.startTest("hello")
        self.menuP.menuPrincipal()
        
    def menuNouvellePartie(self,event):
        self.menuP.effaceMenuPrinc()
        self.menuN.menuNouvellePartie()
        
    def menuInventaire(self,invperso):
        self.menuI.menuInventaire(invperso)

    def menuArtisanat(self,listeParchemin,itemPerso):
        self.menuA.menuArtisanat(listeParchemin,itemPerso)
    
    def menuConnexion(self):
        self.menuC.menuConnexion()
        
    def menuLobby(self):
        self.menuL.menuLobby()
        
    def jeu(self,perso,listePerso):
        self.hudHaut(perso)
        self.frameJeu.initMap(perso,listePerso)
        
    def hudHaut(self,perso):
        self.hudH.hudHaut(perso)
    
    def effaceTout(self):
        self.hudH.effacer()
        self.frameJeu.effacer()
    
    #############################Retourne l'objet de l'image#############################
    def getImage(self,nomImage):
        return self.gestionnaireImage.getImage(nomImage)    
    
    #############################Appel� � la fermeture du jeu#############################
    def quitter(self):
        self.root.quit()
        os._exit(0)
