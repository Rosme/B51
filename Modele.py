# -*- coding: ISO-8859-1 -*-
from Personnage import *
import Race
import Vue
import Item
import Artisanat

class Jeu():
    def __init__(self, parent):
        self.parent = parent
        self.nbId = 0
        self.joueur = ""
        self.artisanat = Artisanat.Artisanat(self)
        
    def info(self, race):
        if race == "Humain":
            raceInfo = Race.Humain()
        
        racename, vie, attaque, defense, poidsLimite, description = raceInfo.info()
            
        print("Race : " + str(racename))
        print("Vie : " + str(vie))
        print("Attaque : " + str(attaque))
        print("Defense : " + str(defense))
        print("Poids limite : " + str(poidsLimite))
        print("Description : " + description)
        
    def nouveauJoueur(self, race):
        nom = "Marco"
        
        self.joueur = Personnage(self.nbId)
        
        if race == "Humain":
            self.joueur.nouveauPersonnage(nom, Race.Humain())
            
        elif race == "Wohawk":
            self.joueur.nouveauPersonnage(nom, Race.Wohawk())
            
        elif race == "Zeborf":
            self.joueur.nouveauPersonnage(nom, Race.Zeborf())
        
        elif race == "Irki":
            self.joueur.nouveauPersonnage(nom, Race.Irki())
            
        elif race == "Popamu":
            self.joueur.nouveauPersonnage(nom, Race.Popamu())
            
        elif race == "Atarix":
            self.joueur.nouveauPersonnage(nom, Race.Atarix())
            
        self.nbId+=1
        
        '''Tout ça peut être enlevé plus tard'''
        print("Nom : " + str(self.joueur.nom))
        print("Race : " + str(self.joueur.race))
        print("Vie : " + str(self.joueur.vie))
        print("Attaque : " + str(self.joueur.attaque))
        print("Defense : " + str(self.joueur.defense))
        print("Poids limite : " + str(self.joueur.inventaire.poidsLimite))
        print("Description : " + self.joueur.description)

    def chargerJoueur(self):
        nom = "Marco"
        
        self.joueur = Personnage(self.nbId)
        self.joueur = self.joueur.chargerPersonnage(nom)
            
        self.nbId += 1
        
        '''Tout ça peut être enlevé plus tard'''
        print("Nom : " + str(self.joueur.nom))
        print("Race : " + str(self.joueur.race))
        print("Vie : " + str(self.joueur.vie))
        print("Attaque : " + str(self.joueur.attaque))
        print("Defense : " + str(self.joueur.defense))
        print("Poids limite : " + str(self.joueur.inventaire.poidsLimite))
        print("Description : " + self.joueur.description)
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