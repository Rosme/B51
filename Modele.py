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
            
        if race == "Wohawk":
            self.joueur = Wohawk(self, self.nbId)
            self.joueur.nouveauPersonnage(nom)
            
        if race == "Zeborf":
            self.joueur = Zeborf(self, self.nbId)
            self.joueur.nouveauPersonnage(nom)
            
        self.nbId+=1
        
        print("Nom : " + str(self.joueur.nom))
        print("Race : " + str(self.joueur.race))
        print("Vie : " + str(self.joueur.vie))
        print("Attaque : " + str(self.joueur.attaque))
        print("Defense : " + str(self.joueur.defense))

    def chargerJoueur(self):
        race = "Zeborf"
        nom = "Marco"
            
        if race == "Humain":
            self.joueur = Humain(self, self.nbId)
            self.joueur = self.joueur.chargerPersonnage(nom)
            
        if race == "Wohawk":
            self.joueur = Wohawk(self, self.nbId)
            self.joueur = self.joueur.chargerPersonnage(nom)
            
        if race == "Zeborf":
            self.joueur = Zeborf(self, self.nbId)
            self.joueur = self.joueur.chargerPersonnage(nom)
        self.nbId += 1
        
        print("Nom : " + str(self.joueur.nom))
        print("Race : " + str(self.joueur.race))
        print("Vie : " + str(self.joueur.vie))
        print("Attaque : " + str(self.joueur.attaque))
        print("Defense : " + str(self.joueur.defense))
        
    def sauvegardeJoueur(self):
        self.joueur.sauvegardePersonnage()
        
    def addMetal(self):
        self.joueur.inventaire.ajouterItem(Item.Upgradable(0, "Metal", "Metal Scrap used to craft Guns and Armors"))
        
    def addElectro(self):
        self.joueur.inventaire.ajouterItem(Item.Upgradable(1, "Electronique", "Electronic parts used to craft Armors and Dematerializator"))
        
    def addBattery(self):
        self.joueur.inventaire.ajouterItem(Item.Upgradable(2, "Batterie", "Battery used to craft Guns and Dematerializator"))