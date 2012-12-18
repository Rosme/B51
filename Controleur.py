# -*- coding: ISO-8859-1 -*-
import Vue
import Modele
import os
import ConnecteurReseau as Network

class Controleur():
    ############################# Methode d'initialisation de l'aplication #############################
    def __init__(self):
        self.demarrer()
        self.app.root.mainloop()
    
    def demarrer(self):
        self.network = Network.ConnecteurReseau()
        self.jeu = Modele.Jeu(self)
        self.app = Vue.Application(self)
        self.press = False
        self.contexte="menu"
        self.compteur=0
        self.partieCommencer=False
        self.app.menuPrincipal()
        
    
    ############################# Méthode (boucle) d'actualisation du Jeu #############################
    def miseAJour(self):
        #si la partie est commencé
        if self.partieCommencer:
            #on bouge le personnage
            self.jeu.bougePersonnage()
            #on active les switchs,leviers,etc
            self.jeu.activationObjet()
            #on actualise le hud du haut
            self.app.hudH.actualiser(self.jeu.joueur)
            #on vérifie que le joueur n'est pas mort
            self.jeu.gestionMort()
            
            if self.compteur%20==0:
                #recharge de l'énergie de l'arme
                self.jeu.rechargement()
            if self.compteur%6==0:
                #vérifie les collions du personnage et des balles
                self.jeu.balle() 
            if self.compteur%6==0:
                self.jeu.tire()
                
            self.compteur+=1
            self.app.frameJeu.map.after(50,self.miseAJour)

            self.network.recevoirDonnees()


    
    ############################# Méthode d'initialisation du Jeu et de l'actualisation du Jeu #############################
    def enJeu(self):
        self.contexte="enJeu"
        self.partieCommencer=True
        self.app.frameJeu.debutDePartie(self.jeu.joueur,self.jeu.carte.s)
        self.jeu.carte.chargeObjets()
        self.app.jeu(self.jeu.joueur,self.jeu.carte.s)
        #ajout des écouteur (souris, clavier)
        self.ajoutEcouteur()
        self.miseAJour()
    
    def actualiserAffichageComplet(self,perso,map):
        self.app.frameJeu.actualiserAffichage(perso,map)
        self.app.frameJeu.affichageRoche(perso,self.jeu.listeRoche)
    
    def actusliserPersonnage(self,perso):
        self.app.frameJeu.affichagePerso(perso)
        self.app.frameJeu.affichageRoche(perso,self.jeu.listeRoche)

    def actualisationBalle(self,listeBalle):
        self.app.frameJeu.map.delete("balle")
        self.app.frameJeu.tire(listeBalle)    
    
    #############################Gestion de la mort#############################    
    def joueurMort(self,perso,laSalle):
        self.app.frameJeu.debutDePartie(self.joueur,self.carte.s)
        self.actualiserAffichageComplet(self.joueur,self.carte.s)
    
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
    
    #############################Ajout d'ecouteur#############################
    def ajoutEcouteur(self):
        #ecouteur lié au clavier       
        self.app.root.bind("<KeyPress>",self.peseKeyGestion)
        self.app.root.bind("<KeyRelease>",self.relacheKeyGestion)
        #ecouteur lié à la souris
        self.app.frameJeu.map.bind("<Button-1>", self.peseTire)
        self.app.frameJeu.map.bind("<ButtonRelease-1>", self.relacheTire)
        self.app.frameJeu.map.bind("<B1-Motion>", self.tireCoord)
    
    ############################# Méthodes en lien avec les events de l'utilisateur #############################
    def peseKeyGestion(self, event):
        key = event.char.upper()
        if self.contexte=="enJeu":
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
                    for i in self.jeu.listeRoche:
                        if i.nomMap == self.jeu.joueur.nomMap:
                            if not i.prendre(self.jeu.joueur):
                                i.bouge(self.jeu.joueur)
                            else:
                                i.depose()
                
                if self.jeu.listeLevier and not self.press:
                    for i in self.jeu.listeLevier:
                        if i.nomMap == self.jeu.joueur.nomMap:
                            if i.collision(self.jeu.joueur):
                                if i.tire():
                                    if i.activer():
                                        self.app.frameJeu.actualiserAffichage(self.jeu.joueur,self.jeu.carte.s)
                                    
                if self.jeu.listeCoffre:
                    for i in self.jeu.listeCoffre:
                        if i.nomMap == self.jeu.joueur.nomMap:
                            i.ouvrir(self.jeu.joueur)
                        
                self.press = True
    
    def relacheKeyGestion(self, event):
        key = event.char.upper()
        
        if self.contexte=="enJeu":
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
            
            if event.keysym == 'Escape':
                self.app.effaceTout()
                
                del self.jeu
                self.jeu = Modele.Jeu(self)
                
                self.press = False
                self.contexte="menu"
                self.compteur=0
                self.partieCommencer=False 
                for i in self.jeu.mouvement:
                    i=False
                
                self.app.initialisationInterfaces()
                self.app.menuPrincipal()
            
        
        
        if key=='I':
            if self.contexte == "enJeu":
                self.contexte="inventaire"
                self.app.menuInventaire()
            elif self.contexte == "inventaire":
                #faire disparaitre l'inventaire
                pass
        
        if key == 'Z':
            pass
            
       
        
    def peseTire(self,event):
        if self.contexte == "enJeu":
            self.jeu.mouvement[4] = True
            self.jeu.sourisX = event.x
            self.jeu.sourisY = event.y  
        
    def relacheTire(self,event):
        self.jeu.mouvement[4] = False
    
    #prend a chaque deplacement de souris la nouvelle position en x,y de la souris
    def tireCoord(self,event):
        if self.jeu.mouvement[4]:
            self.jeu.sourisX = event.x
            self.jeu.sourisY = event.y

if __name__ == '__main__':
    c = Controleur()