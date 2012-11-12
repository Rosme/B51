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
            a=self.nbMetal
            b=self.nbElectro
            itemASupprimer = list()
            
            for i in self.parent.joueur.inventaire.items:
                if i.id == 0 and self.nbMetal+2 != a:
                    itemASupprimer.append(i)
                    self.nbMetal-=1
                elif i.id == 1 and self.nbElectro+2 != b:
                    itemASupprimer.append(i)
                    self.nbElectro-=1
                
                if self.nbMetal+2 == a and self.nbElectro+2 == b:
                    break
                
            for i in itemASupprimer:
                self.parent.joueur.inventaire.retirerItem(i)
                
            del itemASupprimer
            self.parent.joueur.defense+=1
            self.parent.nbMetal-=2
            self.parent.nbElectro-=2
            print("Defense : " + str(self.parent.joueur.defense))
    
    def fabricationFusil(self):
        self.nbMetal = 0
        self.nbBatterie = 0
        for i in self.parent.joueur.inventaire.items:
            if i.id == 0:
                self.nbMetal+=1
            elif i.id == 2:
                self.nbBatterie+=1
                
        if self.nbMetal >= 2 and self.nbBatterie >= 2:
            a=self.nbMetal
            b=self.nbBatterie
            itemASupprimer = list()
            
            for i in self.parent.joueur.inventaire.items:
                if i.id == 0 and self.nbMetal+2 != a:
                    itemASupprimer.append(i)
                    self.nbMetal-=1
                elif i.id == 2 and self.nbBatterie+2 != b:
                    itemASupprimer.append(i)
                    self.nbBatterie-=1
                
                if self.nbMetal+2 == a and self.nbBatterie+2 == b:
                    break
                
            for i in itemASupprimer:
                self.parent.joueur.inventaire.retirerItem(i)
                
            del itemASupprimer
            self.parent.joueur.attaque+=1
            self.parent.nbMetal-=2
            self.parent.nbBatterie-=2
            print("Attaque : " + str(self.parent.joueur.attaque))
    
    def fabricationDematerialisateur(self):
        self.nbElectro = 0
        self.nbBatterie = 0
        for i in self.parent.joueur.inventaire.items:
            if i.id == 2:
                self.nbBatterie+=1
            elif i.id == 1:
                self.nbElectro+=1
                
        if self.nbBatterie >= 2 and self.nbElectro >= 2:
            a=self.nbBatterie
            b=self.nbElectro
            itemASupprimer = list()
            
            for i in self.parent.joueur.inventaire.items:
                if i.id == 2 and self.nbBatterie+2 != a:
                    itemASupprimer.append(i)
                    self.nbBatterie-=1
                elif i.id == 1 and self.nbElectro+2 != b:
                    itemASupprimer.append(i)
                    self.nbElectro-=1
                
                if self.nbBatterie+2 == a and self.nbElectro+2 == b:
                    break
                
            for i in itemASupprimer:
                self.parent.joueur.inventaire.retirerItem(i)
                
            del itemASupprimer
            self.parent.joueur.inventaire.poidsLimite+=2
            self.parent.nbBatterie-=2
            self.parent.nbElectro-=2
            print("Poids limite : " + str(self.parent.joueur.inventaire.poidsLimite))