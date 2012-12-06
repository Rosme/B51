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
        self.listeDeclencheur = list()
        self.listePersonnage = list()
        self.listeLogomate = list()
        self.listeCoffre = list()
        self.listeLevier = list()
        self.listeRoche = list()
        self.listeBalle = list()
        self.listeSac = list()
        self.listeMap = ["MainRoom", "F_E1S1", "F_E1S2", "F_E1S3", "F_E1S4", "F_E1S5", "F_E1S6"]
        self.nbObjMap = len(self.listeMap)
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

    def nouveauLogo(self, posMap, nomMap):
        pers = Personnage()
        pers.nouveauPersonnage("Logo", Race.Logomate())
        pers.posMapX = int(posMap[0])
        pers.posMapY = int(posMap[1])
        self.listeLogomate.append(pers)
        
    def nouveauSac(self, posMap, nomMap):
        posMatX, posMatY = self.parent.app.frameJeu.coord(self.joueur.posEcranX+ int(posMap[0])- self.joueur.posMapX, self.joueur.posEcranY+ int(posMap[1])- self.joueur.posMapY)
        sac = Objet.Interrupteur(self, posMatX, posMatY, int(posMap[0]), int(posMap[1]), nomMap)
        self.listeSac.append(sac)
        
    def nouveauCoffre(self, posMap, nomMap):
        posMatX, posMatY = self.parent.app.frameJeu.coord(self.joueur.posEcranX+ int(posMap[0])- self.joueur.posMapX, self.joueur.posEcranY+ int(posMap[1])- self.joueur.posMapY)
        coffre = Objet.Interrupteur(self, posMatX, posMatY, int(posMap[0]), int(posMap[1]), nomMap)
        self.listeCoffre.append(coffre)
        
    def nouvelleRoche(self, posMap, nomMap):
        posMatX, posMatY = self.parent.app.frameJeu.coord(self.joueur.posEcranX+ int(posMap[0])- self.joueur.posMapX, self.joueur.posEcranY+ int(posMap[1])- self.joueur.posMapY)
        roche = Objet.Roche(self, posMatX, posMatY, int(posMap[0]), int(posMap[1]), nomMap)
        self.listeRoche.append(roche) 
           
    def nouveauInterrupt(self, posMap, nomMap):
        posMatX, posMatY = self.parent.app.frameJeu.coord(self.joueur.posEcranX+ int(posMap[0])- self.joueur.posMapX, self.joueur.posEcranY+ int(posMap[1])- self.joueur.posMapY)
        interrupteur = Objet.Interrupteur(self, posMatX, posMatY, int(posMap[0]), int(posMap[1]), False, nomMap)
        self.listeInterrupteur.append(interrupteur)
    
    def nouveauDeclencheur(self, posMap, nomMap):
        posMatX, posMatY = self.parent.app.frameJeu.coord(self.joueur.posEcranX+ int(posMap[0])- self.joueur.posMapX, self.joueur.posEcranY+ int(posMap[1])- self.joueur.posMapY)
        declencheur = Objet.Interrupteur(self, posMatX, posMatY, int(posMap[0]), int(posMap[1]), nomMap)
        self.listeDeclencheur.append(declencheur)
    
    def nouveauLevier(self, posMap, nomMap):
        posMatX, posMatY = self.parent.app.frameJeu.coord(self.joueur.posEcranX+ int(posMap[0])- self.joueur.posMapX, self.joueur.posEcranY+ int(posMap[1])- self.joueur.posMapY)
        levier = Objet.Levier(self, posMatX, posMatY, int(posMap[0]), int(posMap[1]), 10, 100, 2, nomMap)
        self.listeLevier.append(levier)
        
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
