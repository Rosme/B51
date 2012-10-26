import Modele
import Item

class Artisanat():
    def __init__(self, parent):
        self.parent = parent
    
    def fabricationArmure(self):
        self.nbMetal = 0
        self.nbElectro = 0
        for i in self.parent.joueur.inventaire.items:
            if i.id == 0:
                self.nbMetal+=1
            elif i.id == 1:
                self.nbElectro+=1
                
        if self.nbMetal >= 2 and self.nbElectro >= 2:
            #for i in self.parent.joueur.inventaire.items:
                #if i.id == 0:
                    #i.retirerItem
            self.nbMetal-=2
            self.nbElectro-=2
            self.parent.joueur.defense+=1
            print(self.parent.joueur.defense)
    
    def fabricationFusil(self):
        self.nbMetal = 0
        self.nbBatterie = 0
        for i in self.parent.joueur.inventaire.items:
            if i.id == 0:
                self.nbMetal+=1
            elif i.id == 2:
                self.nbBatterie+=1
                
        if self.nbMetal >= 2 and self.nbBatterie >= 2:
            #for i in self.parent.joueur.inventaire.items:
                #if i.id == 0:
                    #i.retirerItem
            self.nbMetal-=2
            self.nbBatterie-=2
            self.parent.joueur.attaque+=1
            print(self.parent.joueur.attaque)
    
    def fabricationDematerialisateur(self):
        self.nbElectro = 0
        self.nbBatterie = 0
        for i in self.parent.joueur.inventaire.items:
            if i.id == 2:
                self.nbBatterie+=1
            elif i.id == 1:
                self.nbElectro+=1
                
        if self.nbBatterie >= 2 and self.nbElectro >= 2:
            #for i in self.parent.joueur.inventaire.items:
                #if i.id == 0:
                    #i.retirerItem
            self.nbBatterie-=2
            self.nbElectro-=2
            self.parent.joueur.inventaire.poidsLimite+=2
            print(self.parent.joueur.inventaire.poidsLimite)