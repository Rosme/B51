# -*- coding: ISO-8859-1 -*-
import pickle
import Item
from Balle import *
        
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
        self.x = 200
        self.y = 100
        self.posMatX = 11
        self.posMatY = 11
        self.posEcranX = 0
        self.posEcranY = 0
        self.posMapX = 672
        self.posMapY = 336
        self.inventaire = Item.Inventaire(self.poidsLimite)
        self.inventaire.ajouterItem(Item.Arme(7, 5, "Fusil", "Pewpew", 5, 1000000, 2, 0.5))
        self.inventaire.ajouterItem(Item.Armure(8, 10, "Armure", "Q.Q", 5, 20, 1))
        self.inventaire.ajouterItem(Item.Divers(3, 1, "Seringue", "Soigne de 100 de vies", 100))
        self.inventaire.ajouterItem(Item.Divers(4, 1, "Nourriture", "Soigne de 50 de vies", 50))
        self.inventaire.ajouterItem(Item.Divers(5, 1, "Super-Seringue", "Soigne de 200 de vies", 200))
    
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
    
    '''
    La méthode qui descend l'armure selon de les dégâts subits, 
    si l'armure tombe à zéro, le reste va directement sur la vie du joueur    
    '''
    def touche(self, degat):
        for i in self.inventaire.items:
            #Si c'est une armure (ID = 8)
            if i.id == 8:
                #Si l'énergie restante - les dégâts est supérieur ou égale à zéro, descend l'armure. 
                if i.energie - degat >= 0:
                    i.subit(degat)
                    break
                #Sinon, prend le reste et descend la vie.
                else:
                    reste = degat
                    reste -= i.energie
                    degat -= reste
                    i.subit(degat)
                    self.subit(reste)
                    break
    
    def tire(self, listeBalle, x, y):
        for i in self.inventaire.items:
            #ID de l'armure = 7
            if i.id == 7:
                if i.energie - i.cout >= 0:
                    i.utiliser()
                    listeBalle.append(Balle(512, 350, x, y, i.force+self.attaque))
                    break
            
    def recharge(self):
        #Recharge l'arme
        for i in self.inventaire.items:
            if i.id == 7: 
                if i.energie + i.vitesseRecharge < i.max_energie:
                    i.recharge()
                else:
                    i.energie = i.max_energie
                break
        #Recharge l'armure
        for i in self.inventaire.items:
            if i.id == 8:
                if i.energie + i.vitesseRecharge < i.max_energie:
                    i.recharge()
                else:
                    i.energie = i.max_energie
                break
         
    def subit(self, degat):
        self.vie -= degat
                
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
            #ID de la seringue = 3
            if i.id == 3:
                if self.vie + i.qualite < 350:
                    i.utiliser(self)
                else:
                    self.vie = 350 - i.qualite
                    i.utiliser(self)
                    
                self.inventaire.retirerItem(i)
                break
    
    def obtenirLimite(self):
        return [self.posMapX-26, self.posMapY-35, self.posMapX+26, self.posMapY+10]
    