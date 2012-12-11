# -*- coding: ISO-8859-1 -*-
import Vue
import Modele
import os

class Controleur():
    ############################# Methode d'initialisation de l'aplication #############################
    def __init__(self):
        self.demarrer()
        self.app.root.mainloop()
    
    def demarrer(self):
        self.jeu = Modele.Jeu(self)
        self.app = Vue.Application(self)
        self.press = False
        self.compteur=0
        self.partieCommencer=False
        self.app.menuPrincipal()
    
    ############################# Méthode (boucle) d'actualisation du Jeu #############################
    def miseAJour(self):
        if self.partieCommencer:
            self.jeu.bougePersonnage()
            self.jeu.activationObjet()
            self.app.frameJeu.hudHaut.actualiser()
            self.jeu.gestionMort()
            if self.compteur%20==0:
                self.jeu.rechargement()
            if self.compteur%3==0:
                self.jeu.balle() 
            if self.compteur%6==0:
                self.jeu.tire()
                
            self.compteur+=1
            if self.partieCommencer:
                self.app.frameJeu.map.after(10,self.miseAJour)
    
    ############################# Méthode d'initialisation du Jeu et de l'actualisation du Jeu #############################
    def enJeu(self):
        self.partieCommencer=True
        self.app.frameJeu.debutDePartie(self.jeu.joueur,self.jeu.carte.s)
        self.jeu.carte.chargeObjets()
        self.app.jeu(self.jeu.joueur,self.jeu.carte.s)
        self.miseAJour()
            
    ############################# Méthodes en lien avec la création et la suppression d'éléments du modèle #############################
    def raceInfo(self, race):
        return self.jeu.info(race)
        
    def nouveauJoueur(self, race, nom):
        self.jeu.nouveauJoueur(race, nom)
        
    def autoSoin(self):
        self.jeu.joueur.autoSoin()
        
    def rajoutMetal(self):
        self.jeu.rajoutMetal()
        
    def rajoutElectro(self):
        self.jeu.rajoutElectro()
        
    def rajoutBatterie(self):
        self.jeu.rajoutBatterie()
        
    def fabricationArmure(self):
        self.jeu.artisanat.fabricationArmure()
    
    def fabricationFusil(self):
        self.jeu.artisanat.fabricationFusil()
        
    def fabricationDematerialisateur(self):
        self.jeu.artisanat.fabricationDematerialisateur()
    
    ############################# Méthodes en lien avec les events de l'utilisateur #############################
    def peseKeyGestion(self, event):
        key = event.char.upper()
        
        if key == 'W':
            self.jeu.mouvement[0]=True
        if key == 'D':
            self.jeu.mouvement[1]=True
        if key == 'S':
            self.jeu.mouvement[2]=True
        if key == 'A':
            self.jeu.mouvement[3]=True
            
        if key == 'Q':
            self.autoSoin()
            
        if key == 'M':
            self.jeu.joueur.touche(10)
            
        if key == 'E':
            if self.jeu.listeRoche:
                if not self.jeu.listeRoche[0].prendre(self.jeu.joueur):
                    self.jeu.listeRoche[0].bouge(self.jeu.joueur)
                else:
                    self.jeu.listeRoche[0].depose()
            
            if self.jeu.listeLevier and not self.press:
                for i in self.jeu.listeLevier:
                    if i.collision(self.jeu.joueur):
                        if i.tire():
                            if i.activer():
                                self.app.frameJeu.effaceMap()
                                self.app.frameJeu.affichageMap(self.jeu.joueur,self.jeu.carte.s)
                                
            
            self.press = True
    
    def relacheKeyGestion(self, event):
        key = event.char.upper()
        
        if key == 'W':
            self.jeu.mouvement[0]=False
        if key == 'D':
            self.jeu.mouvement[1]=False
        if key == 'S':
            self.jeu.mouvement[2]=False
        if key == 'A':
            self.jeu.mouvement[3]=False
        
        if key == 'E':
            self.press = False
        
        if key=='I':
            self.app.menuInventaire()
        
        if key == 'Z':
            pass
            #print(self.jeu.joueur.posMapX)
            #print(self.jeu.joueur.posMapY)
            
        if event.keysym == 'Escape':
            self.app.frameJeu.effaceTout()
            
            del self.jeu
            self.jeu = Modele.Jeu(self)
            
            self.press = False
            self.compteur=0
            self.partieCommencer=False 
            for i in self.jeu.mouvement:
                i=False
            
            self.app.initialisationInterfaces()
            self.app.menuPrincipal()
        
    def peseTire(self,event):
        self.jeu.mouvement[4] = True
        self.jeu.sourisX = event.x
        self.jeu.sourisY = event.y
        
    def relacheTire(self,event):
        self.jeu.mouvement[4] = False
        
    def tireCoord(self,event):
        if self.jeu.mouvement[4]:
            self.jeu.sourisX = event.x
            self.jeu.sourisY = event.y

if __name__ == '__main__':
    c = Controleur()
