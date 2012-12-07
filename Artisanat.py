# -*- coding: ISO-8859-1 -*-
import Modele
import Item

class Artisanat():
    def __init__(self, parent):
        self.parent = parent
        self.dictResultatId = dict()
        self.dictResultatId["14"] = ["cleAB", "La clé AB - Utilisable pour l'artisanat"]
        self.dictResultatId["15"] = ["cleCA", "La clé CA - Utilisable pour l'artisanat"]
        self.dictResultatId["16"] = ["cleDAB", "La clé DAB - Utilisable pour l'artisanat"]
        self.dictResultatId["17"] = ["cleBCA", "La clé BCA - Utilisable pour l'artisanat"]
        self.dictResultatId["18"] = ["cleBCAC", "La clé BCAC - Utilisable pour l'artisanat"]
        self.dictResultatId["19"] = ["cleCABCAC", "La clé CABCAC - Utilisable pour l'artisanat"]
        self.dictResultatId["20"] = ["cleCABCACD", "La clé CABCACD - Utilisable pour l'artisanat"]
        self.dictResultatId["21"] = ["cleDABCABCACD", "La clé DABCABCACD - Utilisable pour l'artisanat"]
        self.dictResultatId["6"] = ["cleMaitre", "La clé Maître - Ouvre "]
        
        self.listeParchemin = list()
        #parcheminId, itemId1, itemId2, resultatId, nom, description, inversable, possède
        self.listeParchemin.append(Parchemin(31, 0,1, -1, "P10", "Métal avec Électronique", True, True))
        self.listeParchemin.append(Parchemin(32, 0,2, -1, "P11", "Métal avec Batterie", True, True))
        self.listeParchemin.append(Parchemin(33, 1,2, -1, "P12", "Électronique avec Batterie", True, True))
        self.listeParchemin.append(Parchemin(22, 11,9, 15, "P1", "Clé C avec A"))
        self.listeParchemin.append(Parchemin(23, 9,10, 14, "P2", "Clé A avec B", False, True))
        self.listeParchemin.append(Parchemin(24, 12,14, 16, "P3", "Clé D avec AB"))
        self.listeParchemin.append(Parchemin(25, 16,20, 21, "P4", "Clé DAB avec CABCACD"))
        self.listeParchemin.append(Parchemin(26, 15,18, 19, "P5", "Clé CA avec BCAC"))
        self.listeParchemin.append(Parchemin(27, 10,15, 17, "P6", "Clé B avec CA"))
        self.listeParchemin.append(Parchemin(28, 17,11, 18, "P7", "Clé BCA avec C"))
        self.listeParchemin.append(Parchemin(29, 19,12, 20, "P8", "Clé CABCAC avec D"))
        self.listeParchemin.append(Parchemin(30, 21,6, 6, "P9", "Clé DABCABCACD avec E"))
    
    def mixeCle(self, parcheminId, itemId1, itemId2):
        nbItem1 = 1
        nbItem2 = 1
        tab = []
        for i in self.listeParchemin:
            if i.parcheminId == parcheminId:
                for j in self.parent.joueur.inventaire.items:
                    if j.id == itemId1 and nbItem1 > 0:
                        tab.append(j)
                        nbItem1-=1
                        print("Delete item 1")
                    if j.id == itemId2 and nbItem2 > 0:
                        tab.append(j)
                        nbItem2-=1
                        print("Delete item 2")
                    if nbItem1 == 0 and nbItem2 == 0:
                        temp = self.dictResultatId[str(i.resultatId)]
                        tab.append(Item.Upgradable(i.resultatId, temp[0], temp[1]))
                        print("Ajout item resultat")
                        break
                self.parent.joueur.inventaire.retirerItem(tab[0])
                self.parent.joueur.inventaire.retirerItem(tab[1])
                self.parent.joueur.inventaire.ajouterItem(tab[2])
                break
    
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
    def __init__(self, parcheminId, itemId1, itemId2, resultatId, nom, description, inversable = False, possede = False):
        self.parcheminId = parcheminId
        self.nom = nom
        self.description = description
        self.itemId1 = itemId1
        self.itemId2 = itemId2
        self.resultatId = resultatId
        self.inversable = inversable
        self.possede = possede
        
        
        
        
        