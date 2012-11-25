# -*- coding: ISO-8859-1 -*-
from Personnage import *
import Race
import Vue
import Item
import Carte
import Artisanat
import Objet

class Jeu():
    def __init__(self, parent):
        self.parent = parent
        self.listeInterrupteur = list()
        self.listePersonnage = list()
        self.listeLogomate = list()
        self.listeRoche = list()
        self.listeBalle = list()
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
        pers.posMapX = int(posMap[0])
        pers.posMapY = int(posMap[1])
        self.listeLogomate.append(pers)
        
    def nouveauInterrupt(self, posMap):
        posMatX, posMatY = self.parent.app.frameJeu.coord(int(posMap[0]), int(posMap[1]))
        interrupteur = Objet.Interrupteur(self, posMatX, posMatY, int(posMap[0]), int(posMap[1]), False)
        self.listeInterrupteur.append(interrupteur)
        
    def nouvelleRoche(self, posMap):
        posMatX, posMatY = self.parent.app.frameJeu.coord(int(posMap[0]), int(posMap[1]))
        roche = Objet.Roche(self, posMatX, posMatY, int(posMap[0]), int(posMap[1]))
        self.listeRoche.append(roche)
        
    def nouveauJoueur(self, race, nom):
        
        self.joueur = Personnage()
        
        if race == "Humain":
            self.joueur.nouveauPersonnage(nom, Race.Humain())
        
        elif race == "Irki":
            self.joueur.nouveauPersonnage(nom, Race.Irki())
            
        elif race == "Popamu":
            self.joueur.nouveauPersonnage(nom, Race.Popamu())
            
        elif race == "Atarix":
            self.joueur.nouveauPersonnage(nom, Race.Atarix())

    def chargerJoueur(self, nom):        
        self.joueur = Personnage()
        self.joueur = self.joueur.chargerPersonnage(nom)
        
    def sauvegardeJoueur(self):
        self.joueur.sauvegardePersonnage()
        
    def rajoutMetal(self):
        self.joueur.inventaire.ajouterItem(Item.Upgradable(0, "Metal", "Metal Scrap used to craft Guns and Armors"))
        
    def rajoutElectro(self):
        self.joueur.inventaire.ajouterItem(Item.Upgradable(1, "Electronique", "Electronic parts used to craft Armors and Dematerializator"))
        
    def rajoutBatterie(self):
        self.joueur.inventaire.ajouterItem(Item.Upgradable(2, "Batterie", "Battery used to craft Guns and Dematerializator"))
