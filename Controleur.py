# -*- coding: ISO-8859-1 -*-
import Vue
import Modele

class Controleur():
    def __init__(self):
        self.jeu = Modele.Jeu(self)
        self.app = Vue.Application(self)
        self.miseAJour()
        self.app.root.mainloop()
    
    def chargerJoueur(self):
        self.jeu.chargerJoueur()
        
    def sauvegardeJoueur(self):
        self.jeu.sauvegardeJoueur()
        
    def miseAJour(self):
        self.app.actualiser()
        self.app.map.after(10,self.miseAJour)
        
        
if __name__ == '__main__':
    c = Controleur()