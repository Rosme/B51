# -*- coding: ISO-8859-1 -*-
from Personnage import *
import Race
import Vue
import Item
import Carte
import Artisanat

class Jeu():
    def __init__(self, parent):
        self.parent = parent
        self.listePersonnage = list()
        self.listeBalle = list()
        self.nbId = 0
        self.joueur = ""
        self.carte = Carte.Carte(self)
        self.artisanat = Artisanat.Artisanat(self)
        
    def info(self, race):
        if race == "Humain":
            raceInfo = Race.Humain()
        if race == "Popamu":
            raceInfo = Race.Popamu()
        if race == "Irki":
            raceInfo = Race.Irki()
        if race == "Atarix":
            raceInfo = Race.Atarix()
            
        return raceInfo.info()

    def nouveauLogo(self, posMap):
        pers = Personnage()
        pers.nouveauPersonnage("Logo", Race.Logomate())
        pers.posMapX = posMap[0]
        pers.posMapY = posMap[1]
        self.listeLogomate.append(pers)
        self.nbId+=1
        
    def nouveauJoueur(self, race, nom):
        
        self.joueur = Personnage(self.nbId)
        
        if race == "Humain":
            self.joueur.nouveauPersonnage(nom, Race.Humain())
        
        elif race == "Irki":
            self.joueur.nouveauPersonnage(nom, Race.Irki())
            
        elif race == "Popamu":
            self.joueur.nouveauPersonnage(nom, Race.Popamu())
            
        elif race == "Atarix":
            self.joueur.nouveauPersonnage(nom, Race.Atarix())
            
        self.nbId+=1
        
        pers = Personnage(self.nbId+1)
        pers.nouveauPersonnage("Kevin", Race.Atarix())
        pers.posMapX+=100
        self.listePersonnage.append(pers)
        
        self.nbId+=1

    def chargerJoueur(self, nom):        
        self.joueur = Personnage(self.nbId)
        self.joueur = self.joueur.chargerPersonnage(nom)
            
        self.nbId += 1
        
    def sauvegardeJoueur(self):
        self.joueur.sauvegardePersonnage()
        
    def rajoutMetal(self):
        self.joueur.inventaire.ajouterItem(Item.Upgradable(0, "Metal", "Metal Scrap used to craft Guns and Armors"))
        
    def rajoutElectro(self):
        self.joueur.inventaire.ajouterItem(Item.Upgradable(1, "Electronique", "Electronic parts used to craft Armors and Dematerializator"))
        
    def rajoutBatterie(self):
        self.joueur.inventaire.ajouterItem(Item.Upgradable(2, "Batterie", "Battery used to craft Guns and Dematerializator"))
