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
        self.jeu.nouveauJoueur("Humain")
        self.app.root.mainloop()
    
    def miseAJour(self):
        self.actualiser()
        self.app.frameJeu.map.after(10,self.miseAJour)
    
    def rechargement(self):
        self.jeu.joueur.recharge()
        self.app.frameJeu.map.after(100,self.rechargement)
    
    def enJeu(self,perso):
        self.app.jeu(perso,self.jeu.carte.s.salle)
        self.jeu.joueur=self.app.frameJeu.initMap(self.jeu.joueur,self.jeu.carte.s.salle)
        self.app.frameJeu.ajoutEcouteuretBoucle()
    
    def actualiser(self):
        self.map=self.jeu.carte.s.salle
        
        tempx=0
        tempy=0
        
        tempx, tempy = self.jeu.joueur.bouge(self.mouvement)
        tempMatX,tempMatY=self.app.frameJeu.coord(self.jeu.joueur.posEcranX+(tempx)*2,self.jeu.joueur.posEcranY+(tempy)*2)
        if self.map[tempMatX][tempMatY]=='0' and self.map[tempMatX+1][tempMatY-1]!='1':
            self.jeu.joueur.x=tempMatX
            self.jeu.joueur.y=tempMatY
            self.jeu.joueur.posDepartX-=tempx
            self.jeu.joueur.posDepartY-=tempy
        print("actu",self.jeu.joueur.posEcranX,self.jeu.joueur.posEcranY)      
        if True in self.mouvement:
            self.app.frameJeu.map.delete("image")
            self.app.frameJeu.map.delete("perso")
            self.app.frameJeu.persoAff=True
            self.app.frameJeu.map.delete("text")
            self.app.frameJeu.affichageMap(self.jeu.joueur,self.map)
            
    
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
        
    def tire(self,event):
        self.jeu.joueur.tire()
        

if __name__ == '__main__':
    c = Controleur()