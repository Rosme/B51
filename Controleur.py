# -*- coding: ISO-8859-1 -*-
import Vue
import Modele

class Controleur():
    def __init__(self):
        self.jeu = Modele.Jeu(self)
        self.app = Vue.Application(self)
        self.app.root.mainloop()
        
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