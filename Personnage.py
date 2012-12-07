# -*- coding: ISO-8859-1 -*-
import pickle
import Item
import Objet
from Balle import *
        
class Personnage():
    def __init__(self):
        pass
        
    def nouveauPersonnage(self, nom, race):
        self.nom = nom
        self.nomMap = "MainRoom"
        self.race = race
        self.posMatX = 0
        self.posMatY = 0
        self.posMapX = 0
        self.posMapY = 0
        self.inventaire = Item.Inventaire(self.race.poidsLimite)
        self.inventaire.ajouterItem(Item.Arme(7, 2, "Fusil", "Pewpew", 5, 100, 2, 5, 500))
        self.inventaire.ajouterItem(Item.Armure(8, 4, "Armure", "Q.Q", 0.8, 100, 1))
        self.inventaire.ajouterItem(Item.Divers(3, 1, "Seringue", "Soigne de 100 de vies", 100))
        self.inventaire.ajouterItem(Item.Divers(3, 1, "Seringue", "Soigne de 100 de vies", 100))
        self.inventaire.ajouterItem(Item.Divers(3, 1, "Seringue", "Soigne de 100 de vies", 100))
        self.inventaire.ajouterItem(Item.Divers(4, 1, "Nourriture", "Soigne de 50 de vies", 50))
        self.inventaire.ajouterItem(Item.Divers(5, 1, "Super-Seringue", "Soigne de 200 de vies", 200))
    
    def mort(self):
        self.nomMap = "MainRoom"
        self.race.vie=self.race.max_vie/2
        for p in self.inventaire:
            if p.id==8:
                pass
    
    def bouge(self,mouvement):
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
                if i.energie - (degat * i.defense) >= 0:
                    degat=degat * i.defense
                    i.subit(degat)
                    break
                #Sinon, prend le reste et descend la vie.
                else:                
                    reste = degat * i.defense 
                    reste -= i.energie                    
                    degat -= reste
                    reste
                    i.subit(degat)
                    self.subit(reste)
                    break
					
    def calculDegat(self,item,degat):
        item.defense*self.race.defense*degat
        
    
    def tire(self, listeBalle, x, y):
        for i in self.inventaire.items:
            #ID de l'arme = 7
            if i.id == 7:
                if i.energie - i.cout >= 0:
                    i.utiliser()
                    listeBalle.append(Balle(self, x, y, i.force+self.race.attaque))
                    if listeBalle[len(listeBalle)-1].valide:
                        return True
                    else:
                        return False
            
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
        self.race.vie -= degat
                
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
                if self.race.vie + i.qualite < self.race.max_vie:
                    i.utiliser(self)
                else:
                    self.race.vie = self.race.max_vie - i.qualite
                    i.utiliser(self)
                    
                self.inventaire.retirerItem(i)
                break
    
    def obtenirLimite(self):
        return [self.posMapX-26, self.posMapY-35, self.posMapX+26, self.posMapY+10]
    
