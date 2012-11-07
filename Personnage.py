# -*- coding: ISO-8859-1 -*-
import pickle
import Item
        
class Personnage():
    def __init__(self, id):
        '''Caractéristiques uniques'''
        self.id = id
        
    def nouveauPersonnage(self, nom, race):
        self.nom = nom
        self.race = race.race
        self.vie = race.vie
        self.attaque = race.attaque
        self.defense = race.defense
        self.poidsLimite = race.poidsLimite
        self.description = race.description
        self.x = 0
        self.y = 0
        self.inventaire = Item.Inventaire(self.poidsLimite)
        self.inventaire.ajouterItem(Item.Divers(3, 1, "Seringue", "Une seringue qui soigne de 100 de vies", 100))
        self.inventaire.ajouterItem(Item.Divers(3, 1, "Seringue", "Une seringue qui soigne de 100 de vies", 100))
        self.inventaire.ajouterItem(Item.Divers(3, 1, "Seringue", "Une seringue qui soigne de 100 de vies", 100))
        self.inventaire.ajouterItem(Item.Arme(7, 5, "Fusil", "Pewpew", 5, 1000, 75, 2))
    
    def bouge(self, mouvement):
        tempx = 0
        tempy = 0
        
        if mouvement[0]:
            tempy-=4
        if mouvement[1]:
            tempx+=4
        if mouvement[2]:
            tempy+=4
        if mouvement[3]:
            tempx-=4
            
        return tempx, tempy
    
    def tire(self):
        for i in self.inventaire.items:
            if i.id == 7:
                if i.energie > 0:
                    i.use()
                    print(i.energie)
                    break
            
    def recharge(self):
        for i in self.inventaire.items:
            if i.id == 7: 
                if i.energie + i.vitesseRecharge < 1000:
                    i.recharge()
                    print(i.energie)
                else:
                    i.energie = 1000
                break
                
    def chargerPersonnage(self, nom):
        nomFichier = nom + '.plr'
        with open(nomFichier,'rb') as fichier:
            joueur = pickle.Unpickler(fichier)
            self = joueur.load()
        return self
        
    def sauvegardePersonnage(self):
        nomFichier = self.nom + '.plr'
        with open(nomFichier,'wb') as fichier:
            save = pickle.Pickler(fichier)
            save.dump(self)
    
    def autoSoin(self):
        for i in self.inventaire.items:
            if i.id == 3:
                if self.vie + i.qualite < 350:
                    i.utiliser(self)
                else:
                    self.vie = 350 - i.qualite
                    i.utiliser(self)
                    
                self.inventaire.retirerItem(i)
                break
    
    def getBound(self):
        return [0,0], [10,0], [10,10], [0,10]