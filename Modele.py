# -*- coding: ISO-8859-1 -*-
from Personnage import *
import Vue
import Item
import Artisanat

class Jeu():
    def __init__(self, parent):
        self.parent = parent
        self.nbId = 0
        self.joueur = ""
        self.artisanat = Artisanat.Artisanat(self)
        
    def nouveauJoueur(self, race):
        nom = "Marco"
        
        if race == "Humain":
            self.joueur = Humain(self, self.nbId)
            self.joueur.nouveauPersonnage(nom)
            
        elif race == "Wohawk":
            self.joueur = Wohawk(self, self.nbId)
            self.joueur.nouveauPersonnage(nom)
            
        elif race == "Zeborf":
            self.joueur = Zeborf(self, self.nbId)
            self.joueur.nouveauPersonnage(nom)
        
        elif race == "Irki":
            self.joueur = Irki(self, self.nbId)
            self.joueur.nouveauPersonnage(nom)
            
        elif race == "Popamu":
            self.joueur = Popamu(self, self.nbId)
            self.joueur.nouveauPersonnage(nom)
            
        self.nbId+=1
        
        '''Tout ça peut être enlevé plus tard'''
        print("Nom : " + str(self.joueur.nom))
        print("Race : " + str(self.joueur.race))
        print("Vie : " + str(self.joueur.vie))
        print("Attaque : " + str(self.joueur.attaque))
        print("Defense : " + str(self.joueur.defense))
        print("Poids limite : " + str(self.joueur.inventaire.poidsLimite))

    def chargerJoueur(self):
        race = "Zeborf"
        nom = "Marco"
            
        if race == "Humain":
            self.joueur = Humain(self, self.nbId)
            self.joueur = self.joueur.chargerPersonnage(nom)
            
        elif race == "Wohawk":
            self.joueur = Wohawk(self, self.nbId)
            self.joueur = self.joueur.chargerPersonnage(nom)
            
        elif race == "Zeborf":
            self.joueur = Zeborf(self, self.nbId)
            self.joueur = self.joueur.chargerPersonnage(nom)
        
        elif race == "Irki":
            self.joueur = Irki(self, self.nbId)
            self.joueur = self.joueur.chargerPersonnage(nom)
        
        elif race == "Popamu":
            self.joueur = Popamu(self, self.nbId)
            self.joueur = self.joueur.chargerPersonnage(nom)
            
        elif race == "Atarix":
            self.joueur = Atarix(self, self.nbId)
            self.joueur = self.joueur.chargerPersonnage(nom)
            
        self.nbId += 1
        
        '''Tout ça peut être enlevé plus tard'''
        print("Nom : " + str(self.joueur.nom))
        print("Race : " + str(self.joueur.race))
        print("Vie : " + str(self.joueur.vie))
        print("Attaque : " + str(self.joueur.attaque))
        print("Defense : " + str(self.joueur.defense))
        print("Poids limite : " + str(self.joueur.inventaire.poidsLimite))
        self.nbMetal = 0
        self.nbElectro = 0
        self.nbBatterie = 0
        for i in self.joueur.inventaire.items:
            if i.id == 0:
                self.nbMetal+=1
            elif i.id == 1:
                self.nbElectro+=1
            elif i.id == 2:
                self.nbBatterie +=1
        
        print("Nb Metal: " + str(self.nbMetal))
        print("Nb Electro: " + str(self.nbElectro))
        print("Nb Batterie: " + str(self.nbBatterie))
        
        
    def sauvegardeJoueur(self):
        self.joueur.sauvegardePersonnage()
        
    def addMetal(self):
        self.joueur.inventaire.ajouterItem(Item.Upgradable(0, "Metal", "Metal Scrap used to craft Guns and Armors"))
        self.nbMetal+=1
        print("Nb Metal: " + str(self.nbMetal))
        
    def addElectro(self):
        self.joueur.inventaire.ajouterItem(Item.Upgradable(1, "Electronique", "Electronic parts used to craft Armors and Dematerializator"))
        self.nbElectro+=1
        print("Nb Electro: " + str(self.nbElectro))
        
    def addBattery(self):
        self.joueur.inventaire.ajouterItem(Item.Upgradable(2, "Batterie", "Battery used to craft Guns and Dematerializator"))
        self.nbBatterie +=1
        print("Nb Batterie: " + str(self.nbBatterie))