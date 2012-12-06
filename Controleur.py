# -*- coding: ISO-8859-1 -*-
import Vue
import Modele
import os

class Controleur():
    def __init__(self):
        self.jeu = Modele.Jeu(self)
        self.app = Vue.Application(self)
        self.mouvement = list() 
        #0-haut,1-droite,2-bas,3-gauche,4-tire
        for i in range(5):
            self.mouvement.append(False)
            
        self.demarrer()
        self.app.root.mainloop()
    
    def miseAJour(self):
        self.actualiser()
        self.app.frameJeu.map.after(10,self.miseAJour)
    
    def rechargement(self):
        self.jeu.joueur.recharge()
        self.app.frameJeu.map.after(100,self.rechargement)
    
    def balle(self):
        
        self.collision(self.jeu.listePersonnage)
        self.collision(self.jeu.listeLogomate)
        
        self.app.frameJeu.map.delete("balle")
        self.app.frameJeu.tire()
        self.app.frameJeu.map.after(50, self.balle)

    def collision(self, liste):
        temp = self.jeu.listeBalle
        
        for i in self.jeu.listeBalle:
            i.bouge(self.jeu.joueur)
            if i.veloY<0 and i.veloX<0:
                i.posMatX,i.posMatY=self.app.frameJeu.coord(i.posEcranX+(i.veloX)*2,(i.posEcranY+(i.veloY)*2)+30)
            elif i.veloY>0 and i.veloX>0:
                i.posMatX,i.posMatY=self.app.frameJeu.coord((i.posEcranX+(i.veloX)*2)+10,(i.posEcranY+(i.veloY)*2)+10)
            elif i.veloY<0 and i.veloX>0:
                i.posMatX,i.posMatY=self.app.frameJeu.coord((i.posEcranX+(i.veloX)*2)+40,(i.posEcranY+(i.veloY)*2)+40)                
            else:
                i.posMatX,i.posMatY=self.app.frameJeu.coord((i.posEcranX+(i.veloX)*2)+25,(i.posEcranY+(i.veloY)*2)+25)

            if i.collision(liste, self.jeu.carte.s.salle):
                temp.remove(i)
                
        self.jeu.listeBalle = temp
        
    def demarrer(self):
        self.app.menuPrincipal()
    
    def enJeu(self):
        self.app.jeu()
        self.jeu.joueur=self.app.frameJeu.initMap(self.jeu.joueur,self.jeu.carte.s)
        self.app.frameJeu.ajoutEcouteuretBoucle()
    
    def actualiser(self):
        laMap=self.jeu.carte.s.salle
        
        tempx=0
        tempy=0
        
        tempx, tempy = self.jeu.joueur.bouge(self.mouvement)
        tempMatX,tempMatY=self.app.frameJeu.coord(self.jeu.joueur.posEcranX+(tempx)*2,self.jeu.joueur.posEcranY+(tempy)*2)
        if self.mouvement[4]:
            self.jeu.joueur.tire(self.jeu.listeBalle, self.x, self.y)
            balle = self.jeu.listeBalle[len(self.jeu.listeBalle)-1]
            balle.posMatX,balle.posMatY=self.app.frameJeu.coord(balle.posEcranX+(balle.veloX)*2,balle.posEcranY+(balle.veloY)*2)
        
        if laMap[tempMatY][tempMatX]== 'm' or laMap[tempMatY][tempMatX] == 'v' or laMap[tempMatY][tempMatX]== 'b' or laMap[tempMatY][tempMatX] == 'n':
            car=laMap[tempMatY][tempMatX]
            self.jeu.carte.s.changementCarte(car)
            self.jeu.joueur=self.app.frameJeu.coordProchaineZone(self.jeu.carte.s,car,self.jeu.joueur)
        elif laMap[tempMatY][tempMatX]=='0' or laMap[tempMatY][tempMatX]=='2' or laMap[tempMatY][tempMatX]=='q' or laMap[tempMatY][tempMatX]=='w': #and laMap[tempMatY+1][tempMatX-1]!='1':
            if tempx!=0 or tempy!=0:
                self.jeu.joueur.posMatX=tempMatX
                self.jeu.joueur.posMatY=tempMatY
                self.jeu.joueur.posMapX+=tempx
                self.jeu.joueur.posMapY+=tempy
                self.app.frameJeu.posDepartX = (((self.jeu.carte.s.nbColonne * self.app.frameJeu.largeurTuile)/2)+((self.jeu.carte.s.nbLigne * self.app.frameJeu.largeurTuile)/2))/2 - (self.jeu.joueur.posMapX-self.jeu.joueur.posEcranX)
                self.app.frameJeu.posDepartY = -32 - (self.jeu.joueur.posMapY-self.jeu.joueur.posEcranY)
                
        if self.jeu.listeInterrupteur:
            for i in self.jeu.listeInterrupteur:
                i.collision(self.jeu.joueur)
                i.activer()
                
        if self.jeu.listeRoche:
            for i in self.jeu.listeRoche:
                if not i.aTerre:
                    i.bouge(self.jeu.joueur)
                    
        if self.jeu.listeLogomate:
            for i in self.jeu.listeLogomate:
                i.ia.destXMat, i.ia.destYMat = self.app.frameJeu.coord(i.ia.destXMatEcran,i.ia.destYMatEcran)
                i.ia.choisitDeplacement(self.jeu.carte)
                print(i.ia.posMatX)
                
        
        if True in self.mouvement:
            self.app.frameJeu.map.delete("image")
            self.app.frameJeu.map.delete("perso")
            self.app.frameJeu.map.delete("logo")
            self.app.frameJeu.map.delete("p")
            self.app.frameJeu.map.delete("balle")
            self.app.frameJeu.persoAff=True
            self.app.frameJeu.map.delete("text")
            self.app.frameJeu.affichageMap(self.jeu.joueur,self.jeu.carte.s) 
            self.app.frameJeu.tire()    
    
    
    def raceInfo(self, race):
        return self.jeu.info(race)
        
    def nouveauJoueur(self, race, nom):
        self.jeu.nouveauJoueur(race, nom)
        
    def chargerJoueur(self, nom):
        self.jeu.chargerJoueur(nom)
        
    def sauvegardeJoueur(self):
        self.jeu.sauvegardeJoueur()
        
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
            
        if key == 'E':
            if self.jeu.listeRoche:
                if not self.jeu.listeRoche[0].prendre(self.jeu.joueur):
                    self.jeu.listeRoche[0].bouge(self.jeu.joueur)
                else:
                    self.jeu.listeRoche[0].depose()
                    
            self.jeu.joueur.coffre.ouvrir(self.jeu.joueur)
    
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
            
        if key == 'Z':
            print(self.jeu.joueur.posMapX)
            print(self.jeu.joueur.posMapY)
            
        if event.keysym == 'Escape':
            self.app.root.destroy()
        
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
