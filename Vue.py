# -*- coding: ISO-8859-1 -*-
import tkinter
import MenuPrincipal
import MenuNouvellePartie
import FrameJeu

class Application():
    def __init__(self, parent):
        self.parent = parent
        
        #coordonn�es de l'espace de jeu
        self.localisationJeuX=0
        self.localisationJeuY=0
        
        #dimensions de la fen�tre
        self.largeurFrame=1024
        self.hauteurFrame=768
        
        self.root=tkinter.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.config(width=self.largeurFrame, height=self.hauteurFrame)
        
    def menuPrincipal(self):
        self.menuP=MenuPrincipal.MenuPrincipal(self)
        
    def menuNouvellePartie(self):
        self.menuN=MenuNouvellePartie.MenuNouvellePartie(self)
    
    def jeu(self,perso,map):
        self.frameJeu=FrameJeu.FrameJeu(self,perso,map)
        
    def exit(self):
        print("c la fin!!!")
        self.root.destroy()