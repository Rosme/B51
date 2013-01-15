# -*- coding: ISO-8859-1 -*-
import pickle
import Item
import Objet
import random
from Balle import *
        
class Personnage():
    def __init__(self,parent, id):
        self.parent=parent
        self.id = id
        self.mouvement = list() 
        #0-haut,1-droite,2-bas,3-gauche,4-tire
        for i in range(5):
            self.mouvement.append(False)
        self.posTireX = None
        self.posTireY = None
        
    def nouveauPersonnage(self, nom, race):
        #nom du joueur
        self.nom = nom
        
        #numéro de l'animation du personnage
        self.animationId = 19
        self.animationIncrem = 0
        
        #nom de la map dans lqeul il se trouve
        self.nomMap = "MainRoom"
        #objet race contenant toutes les informations spécifiques au races
        self.race = race
        #position dans la matrice  
        self.posAleatoire()
        
        #initialisation des éléments de l'inventaire
        self.inventaire = Item.Inventaire(self.race.poidsLimite)
        self.inventaire.ajouterItem(Item.Arme(7, 2, "Fusil", "Pewpew", 5, 100, 2, 5, 500))
        self.inventaire.ajouterItem(Item.Armure(8, 4, "Armure", "Q.Q", 0.8, 100, 1))
        self.inventaire.ajouterItem(Item.Divers(3, 1, "Seringue", "Soigne de 100 de vies", 100))
        self.inventaire.ajouterItem(Item.Divers(3, 1, "Seringue", "Soigne de 100 de vies", 100))
        self.inventaire.ajouterItem(Item.Divers(3, 1, "Seringue", "Soigne de 100 de vies", 100))
        self.inventaire.ajouterItem(Item.Divers(4, 1, "Nourriture", "Soigne de 50 de vies", 50))
        self.inventaire.ajouterItem(Item.Divers(5, 1, "Super-Seringue", "Soigne de 200 de vies", 200))
    
    def posAleatoire(self):    
        valide=False
        salle = self.parent.getSalleByName(self.nomMap)
        
        while valide==False:
            self.posMatX = (3+(self.id*2))*self.parent.subDivision#random.randrange(0,len(salle),self.parent.subDivision)
            self.posMatY = 11*self.parent.subDivision#random.randrange(0,len(salle),self.parent.subDivision)
            
            try:
                if salle[self.posMatY][self.posMatX] == '0' or laMap[tempMatY][tempMatX-4] == '1':
                    if salle[self.posMatY][self.posMatX+26] != '1':
                        valide=True
            except:
                pass
    
    def mort(self):
        #action engendrées par la mort du joueur
        self.nomMap = "MainRoom"
        self.race.vie=self.race.max_vie/2
        self.posAleatoire()
    
    def bouge(self):
        #si un mouvement a t demandé on calcul le futur position dans la matrice du perso
        tempx = 0
        tempy = 0
        
        if self.mouvement[0]:
            tempy-=16
        if self.mouvement[1]:
            tempx+=16
        if self.mouvement[2]:
            tempy+=16
        if self.mouvement[3]:
            tempx-=16
        
        tempx+=self.posMatX
        tempy+=self.posMatY
        
        #animation
        if self.mouvement[1]:
            if not(self.animationId >= 9 and self.animationId < 17):
                self.animationId = 9
            else:
                self.animationId+=1
            
        elif self.mouvement[3]:
            if not(self.animationId >= 27 and self.animationId < 35):
                self.animationId = 27
            else:
                self.animationId+=1
        
        elif self.mouvement[0]:
            if not(self.animationId >= 0 and self.animationId < 8):
                self.animationId = 0
            else:
                self.animationId+=1
        
        elif self.mouvement[2]:
            if not(self.animationId >= 18 and self.animationId < 26):
                self.animationId = 18
            else:
                self.animationId+=1
        
        else:
            if self.animationId >= 0 and self.animationId <= 8:
                self.animationId = 0
            if self.animationId >= 9 and self.animationId <= 17:
                self.animationId = 9
            if self.animationId >= 18 and self.animationId <= 26:
                self.animationId = 18
            if self.animationId >= 27 and self.animationId <= 35:
                self.animationId = 27
        
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
                #les dégats sont réduits d'un pourcentage égal à la defense de l'armure
                if i.energie - (degat * i.defense) >= 0:
                    degat=degat * i.defense
                    i.subit(degat)
                    break
                else:
                    #on calcul combien d'énergie est nécéssaire pour rendre l'énergie de 
                    #l'armure à 0 en tenant compte de la defense de l'armure
                    reste = i.energie / i.defense
                    #on enleve l'énergie nécéssaire au dégat total
                    reste = degat - reste
                    #on réduit les dégats selon la defense du personnage
                    reste *= self.race.defense
                    
                    i.subit(i.energie)
                    self.subit(reste)
                    break
    
    
    def tire(self, listeBalle, x, y):
        #si on possède un arme l'arme perd de l'énergie et une balle est crée
        for i in self.inventaire.items:
            #ID de l'arme = 7
            if i.id == 7:
                if i.energie - i.cout >= 0:
                    i.utiliser()
                    listeBalle.append(Balle(self.id, self, x, y, i.force+self.race.attaque))
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
        #soustraction des dégats au joueur
        self.race.vie -= degat
    
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
        #limite pour les collisions
        return [self.posMatX-self.parent.subDivision, self.posMatY-self.parent.subDivision,self.posMatX+self.parent.subDivision,self.posMatY+self.parent.subDivision]
    
