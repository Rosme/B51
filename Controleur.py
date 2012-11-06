# -*- coding: ISO-8859-1 -*-
import Vue
import Modele

class Controleur():
    def __init__(self):
        self.jeu = Modele.Jeu(self)
        self.app = Vue.Application(self)
        self.miseAJour()
        self.app.root.mainloop()
    
    def miseAJour(self):
        self.actualiser()
        self.app.map.after(10,self.miseAJour)
    
    def actualiser(self):
        tempx=0
        tempy=0
        
        if self.app.mouvement[0]:
            tempy-=4
        if self.app.mouvement[1]:
            tempx+=4
        if self.app.mouvement[2]:
            tempy+=4
        if self.app.mouvement[3]:
            tempx-=4
        
        
        tempMatX,tempMatY=self.app.coord(self.app.posEcranX+(tempx)*2,self.app.posEcranY+(tempy)*2)
        if self.app.laListe[tempMatX][tempMatY]=='2':
            self.app.posX=tempMatX
            self.app.posY=tempMatY
            self.app.posDepartX-=tempx
            self.app.posDepartY-=tempy
              
        if True in self.app.mouvement:
            self.app.map.delete("image")
            self.app.map.delete("perso")
            self.app.persoAff=True
            self.app.map.delete("text")
            self.app.affichageMap()
    
    def infoHumain(self):
        self.jeu.info("Humain")
        
    def nouveauHumain(self):
        self.jeu.nouveauJoueur("Humain")
    
    def nouveauWohawk(self):
        self.jeu.nouveauJoueur("Wohawk")
    
    def nouveauZeborf(self):
        self.jeu.nouveauJoueur("Zeborf")
    
    def nouveauIrki(self):
        self.jeu.nouveauJoueur("Irki")
    
    def nouveauPopamu(self):
        self.jeu.nouveauJoueur("Popamu")
    
    def nouveauAtarix(self):
        self.jeu.nouveauJoueur("Atarix")
        
    def chargerJoueur(self):
        self.jeu.chargerJoueur()
        
    def sauvegardeJoueur(self):
        self.jeu.sauvegardeJoueur()
        
    def autoSoin(self,Event):
        self.jeu.joueur.autoSoin()
        
    def addMetal(self):
        self.jeu.addMetal()
        
    def addElectro(self):
        self.jeu.addElectro()
        
    def addBattery(self):
        self.jeu.addBattery()
        
    def fabricationArmure(self):
        self.jeu.artisanat.fabricationArmure()
    
    def fabricationFusil(self):
        self.jeu.artisanat.fabricationFusil()
        
    def fabricationDematerialisateur(self):
        self.jeu.artisanat.fabricationDematerialisateur()

if __name__ == '__main__':
    c = Controleur()