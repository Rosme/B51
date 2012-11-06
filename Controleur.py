# -*- coding: ISO-8859-1 -*-
import Vue
import Modele

class Controleur():
    def __init__(self):
        self.jeu = Modele.Jeu(self)
        self.app = Vue.Application(self)
        self.mouvement = list() 
        #0-haut,1-droite,2-bas,3-gauche
        for i in range(4):
            self.mouvement.append(False)
            
        self.app.root.mainloop()
    
    def miseAJour(self):
        self.actualiser()
        self.app.map.after(10,self.miseAJour)
    
    def actualiser(self):
        
        self.app.laListe=self.jeu.carte.s.salle
        
        tempx=0
        tempy=0
        
        tempx, tempy = self.jeu.joueur.bouge(self.mouvement)
        
        tempMatX,tempMatY=self.app.coord(self.app.posEcranX+(tempx)*2,self.app.posEcranY+(tempy)*2)
        if self.app.laListe[tempMatX][tempMatY]=='0' and self.app.laListe[tempMatX+1][tempMatY-1]!='1':
            self.app.posX=tempMatX
            self.app.posY=tempMatY
            self.app.posDepartX-=tempx
            self.app.posDepartY-=tempy
              
        if True in self.mouvement:
            self.app.map.delete("image")
            self.app.map.delete("perso")
            self.app.persoAff=True
            self.app.map.delete("text")
            self.app.affichageMap()
    
    def infoHumain(self):
        self.jeu.info("Humain")
        
    def nouveauHumain(self):
        self.jeu.nouveauJoueur("Humain")
        self.app.initMap()
    
    def nouveauWohawk(self):
        self.jeu.nouveauJoueur("Wohawk")
        self.app.initMap()
    
    def nouveauZeborf(self):
        self.jeu.nouveauJoueur("Zeborf")
        self.app.initMap()
    
    def nouveauIrki(self):
        self.jeu.nouveauJoueur("Irki")
        self.app.initMap()
    
    def nouveauPopamu(self):
        self.jeu.nouveauJoueur("Popamu")
        self.app.initMap()
        
    def nouveauAtarix(self):
        self.jeu.nouveauJoueur("Atarix")
        self.app.initMap()
        
    def chargerJoueur(self):
        self.jeu.chargerJoueur()
        
    def sauvegardeJoueur(self):
        self.jeu.sauvegardeJoueur()
        
    def autoSoin(self,Event):
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

    def peseHaut(self,event):
        self.mouvement[0]=True
    def relacheHaut(self,event):
        self.mouvement[0]=False
         
    def peseDroit(self,event):
        self.mouvement[1]=True
    def relacheDroit(self,event):
        self.mouvement[1]=False
    
    def peseBas(self,event):
        self.mouvement[2]=True
    def relacheBas(self,event):
        self.mouvement[2]=False
        
    def peseGauche(self,event):
        self.mouvement[3]=True
    def relacheGauche(self,event):
        self.mouvement[3]=False

if __name__ == '__main__':
    c = Controleur()