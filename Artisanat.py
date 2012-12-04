# -*- coding: ISO-8859-1 -*-
import Modele
import Item

class Artisanat():
    def __init__(self, parent):
        self.parent = parent
        self.listeParchemin = list()
        self.listeParchemin.append(Parchemin(0,1,"Métal avec Électronique", True, True))
        self.listeParchemin.append(Parchemin(0,2,"Métal avec Batterie", True, True))
        self.listeParchemin.append(Parchemin(1,2,"Électronique avec Batterie", True, True))
        self.listeParchemin.append(Parchemin(11,12,"A avec B"))
    
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
            itemASupprimer = self.parent.joueur.inventaire.items
            
            for i in self.parent.joueur.inventaire.items:
                if i.id == 0 and self.nbMetal+2 != a:
                    itemASupprimer.retirerItem(i)
                    self.nbMetal-=1
                elif i.id == 1 and self.nbElectro+2 != b:
                    itemASupprimer.retirerItem(i)
                    self.nbElectro-=1
                
                if self.nbMetal+2 == a and self.nbElectro+2 == b:
                    break
                
            self.parent.joueur.inventaire.items = itemASupprimer
            self.parent.joueur.defense+=1
    
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
            itemASupprimer = self.parent.joueur.inventaire.items
            
            for i in self.parent.joueur.inventaire.items:
                if i.id == 0 and self.nbMetal+2 != a:
                    itemASupprimer.retirerItem(i)
                    self.nbMetal-=1
                elif i.id == 2 and self.nbBatterie+2 != b:
                    itemASupprimer.retirerItem(i)
                    self.nbBatterie-=1
                
                if self.nbMetal+2 == a and self.nbBatterie+2 == b:
                    break
                
            self.parent.joueur.inventaire.items = itemASupprimer
            self.parent.joueur.attaque+=1
    
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
            itemASupprimer = self.parent.joueur.inventaire.items
            
            for i in self.parent.joueur.inventaire.items:
                if i.id == 2 and self.nbBatterie+2 != a:
                    itemASupprimer.retirerItem(i)
                    self.nbBatterie-=1
                elif i.id == 1 and self.nbElectro+2 != b:
                    itemASupprimer.retirerItem(i)
                    self.nbElectro-=1
                
                if self.nbBatterie+2 == a and self.nbElectro+2 == b:
                    break
                
            self.parent.joueur.inventaire.items = itemASupprimer
            self.parent.joueur.inventaire.poidsLimite+=2

class Parchemin():
    def __init__(self, itemId1, itemId2, nom, inversable = False, possede = False):
        self.nom = nom
        self.itemId1 = itemId1
        self.itemId2 = itemId2
        self.inversable = inversable
        self.possede = possede
        
        
        
        
        