# -*- coding: ISO-8859-1 -*-
import Vue
import Modele
import os

class Controleur():
    ############################# Methode d'initialisation de l'aplication #############################
    def __init__(self):
        self.jeu = Modele.Jeu(self)
        self.app = Vue.Application(self)
        self.press = False
        self.compteur=0
        self.partieCommencer=False
        self.mouvement = list() 
        #0-haut,1-droite,2-bas,3-gauche,4-tire
        for i in range(5):
            self.mouvement.append(False)
            
        self.demarrer()
        self.app.root.mainloop()
    
    def demarrer(self):
        self.app.menuPrincipal()
    
    ############################# Méthode (boucle) d'actualisation du Jeu #############################
    def miseAJour(self):
        self.actualiser()
        if self.compteur%20==0:
            self.rechargement()
        if self.compteur%3==0:
            self.balle() 
        if self.compteur%6==0:
            self.pewpew()
            
        self.compteur+=1
        if self.partieCommencer==True:
            self.app.frameJeu.map.after(10,self.miseAJour)
            
    ############################# Méthode en lien avec les balles et le tire du joueur #############################
    def rechargement(self):
        self.jeu.joueur.recharge()
        if self.jeu.listeLevier:
            for i in self.jeu.listeLevier:
                if i.energie != i.max_energie:
                    i.recharge()
    
    def pewpew(self):
        if self.mouvement[4]:
            if self.jeu.joueur.tire(self.jeu.listeBalle, self.x, self.y):
                balle = self.jeu.listeBalle[len(self.jeu.listeBalle)-1]
                balle.posMatX,balle.posMatY=self.app.frameJeu.coordEcranAMatrice(balle.posMapX+(balle.veloX)*2,balle.posMapY+(balle.veloY)*2)
            else:
                balle = self.jeu.listeBalle[len(self.jeu.listeBalle)-1]
                self.jeu.listeBalle.remove(balle);
    
    def balle(self):
        self.collision(self.jeu.listePersonnage)
        self.collision(self.jeu.listeLogomate)
        
        self.app.frameJeu.map.delete("balle")
        self.app.frameJeu.tire()
   
    def collision(self, liste):
        temp = self.jeu.listeBalle
        
        for i in self.jeu.listeBalle:
            i.bouge(self.jeu.joueur)
            if i.veloY<0 and i.veloX<0:
                i.posMatX,i.posMatY=self.app.frameJeu.coordEcranAMatrice(i.posMapX+(i.veloX)*2,(i.posMapY+(i.veloY)*2)+30)
            elif i.veloY>0 and i.veloX>0:
                i.posMatX,i.posMatY=self.app.frameJeu.coordEcranAMatrice((i.posMapX+(i.veloX)*2)+10,(i.posMapY+(i.veloY)*2)+10)
            elif i.veloY<0 and i.veloX>0:
                i.posMatX,i.posMatY=self.app.frameJeu.coordEcranAMatrice((i.posMapX+(i.veloX)*2)+40,(i.posMapY+(i.veloY)*2)+40)                
            else:
                i.posMatX,i.posMatY=self.app.frameJeu.coordEcranAMatrice((i.posMapX+(i.veloX)*2)+25,(i.posMapY+(i.veloY)*2)+25)

            if i.collision(liste, self.jeu.carte.s.salle):
                temp.remove(i)
                
        self.jeu.listeBalle = temp
    
    ############################# Méthode d'initialisation du Jeu et de l'actualisation du Jeu #############################
    def enJeu(self):
        self.partieCommencer=True
        self.jeu.carte.chargeObjets()
        self.jeu.joueur=self.app.jeu(self.jeu.joueur,self.jeu.carte.s)
        self.miseAJour()
        
    def actualiser(self):
        laMap=self.jeu.carte.s.salle
        
        tempx, tempy = self.jeu.joueur.bouge(self.mouvement)
        
        tempMatX,tempMatY=self.app.frameJeu.coordEcranAMatrice(self.jeu.joueur.posMapX+tempx,self.jeu.joueur.posMapY+tempy)
        if laMap[tempMatY][tempMatX]== 'm' or laMap[tempMatY][tempMatX] == 'v' or laMap[tempMatY][tempMatX]== 'b' or laMap[tempMatY][tempMatX] == 'n':
            car=laMap[tempMatY][tempMatX]
            self.jeu.joueur.nomMap=self.jeu.carte.s.changementCarte(car)
            self.jeu.joueur=self.app.frameJeu.coordProchaineZone(self.jeu.carte.s,car,self.jeu.joueur)
            
        elif laMap[tempMatY][tempMatX]=='0' or laMap[tempMatY][tempMatX]=='2'  or laMap[tempMatY][tempMatX]=='q' or laMap[tempMatY][tempMatX]=='w':
            if laMap[tempMatY+1][tempMatX-1]!='1':
                if tempx!=0 or tempy!=0:
                    self.jeu.joueur.posMatX=tempMatX
                    self.jeu.joueur.posMatY=tempMatY
                    self.jeu.joueur.posMapX+=tempx
                    self.jeu.joueur.posMapY+=tempy
                    self.app.frameJeu.deplScrollBar(tempx,tempy)
                    self.app.frameJeu.affichagePerso(self.jeu.joueur)
        
        if self.jeu.listeInterrupteur:
            for i in self.jeu.listeInterrupteur:
                i.collision(self.jeu.joueur)
                i.activer()
                
        if self.jeu.listeRoche:
            for i in self.jeu.listeRoche:
                if not i.aTerre:
                    i.bouge(self.jeu.joueur)  
            
        self.app.frameJeu.hudHaut.actualiser() 
        
        if self.jeu.joueur.race.vie==0:
            #self.jeu.joueur.posMapX,self.jeu.joueur.posMapY=self.app.frameJeu.posInitPerso()
            self.jeu.joueur.mort()
            self.jeu.carte.s.salle=self.jeu.carte.s.dictMap[self.jeu.joueur.nomMap]
            
            self.jeu.joueur=self.app.frameJeu.debutDePartie(self.jeu.joueur,self.jeu.carte.s)
            self.app.frameJeu.changementDeMap(self.jeu.carte.s,self.jeu.joueur)
           
            
    ############################# Méthodes en lien avec la création et la suppression d'éléments du modèle #############################
    def raceInfo(self, race):
        return self.jeu.info(race)
        
    def nouveauJoueur(self, race, nom):
        self.jeu.nouveauJoueur(race, nom)
        
        
    def chargerJoueur(self, nom):
        pass
        #self.jeu.chargerJoueur(nom)
        
    def sauvegardeJoueur(self):
        pass
        #self.jeu.sauvegardeJoueur()
        
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
            self.mouvement[0]=True
        if key == 'D':
            self.mouvement[1]=True
        if key == 'S':
            self.mouvement[2]=True
        if key == 'A':
            self.mouvement[3]=True
            
        if key == 'Q':
            self.autoSoin()
            
        if key == 'M':
            self.jeu.joueur.race.vie-=10
            
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
                            i.activer()
            
            self.press = True
    
    def relacheKeyGestion(self, event):
        key = event.char.upper()
        
        if key == 'W':
            self.mouvement[0]=False
        if key == 'D':
            self.mouvement[1]=False
        if key == 'S':
            self.mouvement[2]=False
        if key == 'A':
            self.mouvement[3]=False
        
        if key == 'E':
            self.press = False
        
        if key == 'Z':
            print(self.x)
            print(self.y)
            
        if event.keysym == 'Escape':
            self.app.frameJeu.effaceTout()
            self.partieCommencer=False
            self.app.menuPrincipal()
        
    def peseTire(self,event):
        self.mouvement[4] = True
        self.x = event.x
        self.y = event.y
        
    def relacheTire(self,event):
        self.mouvement[4] = False
        
    def tireCoord(self,event):
        if self.mouvement[4]:
            self.x = event.x
            self.y = event.y

if __name__ == '__main__':
    c = Controleur()
