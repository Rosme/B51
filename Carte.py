# -*- coding: ISO-8859-1 -*-
import os

class Carte():
    def __init__(self):
        self.nomMap = "MainRoom"
        self.s = Salle()
        self.s.chargeCarte(self.nomMap)
        self.chargeObjets()
    	
    def chargeObjets(self):
        try:
            liens = open("assets/liens/liens.txt", 'r')
        except IOError:
            print ("Le fichier liens.txt n'a pas été retrouvé (liens/liens.txt)")
            os._exit(1)
            
        ligne = list()
        ligne = liens.read()

        """Tous les objets possible"""
        self.listeObjet = ["Logomate", "Sac", "Coffre"]

        """Liste des positions de chaque objet """
        self.listeLogo = list()
        self.listeSac = list()
        self.listeCoffre = list()
        
        self.mapValide = False
        self.valideAssign = False
        self.validePlaceFichier = False
        self.posListeObj = 0
        
        for i in ligne.splitlines():
            i.split('\n')
            if(i == self.nomMap):
                print ("Chargement des objets de la map: " + self.nomMap)
                for j in ligne.splitlines():
                    if(j == self.nomMap):
                        self.mapValide = True
                        self.valideEmplacement = True
                    if(j == self.listeObjet[self.posListeObj] and self.mapValide == True):
                        self.valideAssign = True
                        self.mapValide = False
                    elif(self.valideAssign == True and j != "break"):
                        if(self.listeObjet[self.posListeObj] == "Logomate"):
                            self.listeLogo.append(self.convertion(j))
                        elif (self.listeObjet[self.posListeObj] == "Sac"):
                            self.listeSac.append(self.convertion(j))
                        elif(self.listeObjet[self.posListeObj] == "Coffre"):
                            self.listeCoffre.append(self.convertion(j))
                    elif(self.valideAssign == True and j == "break"):
                        self.valideAssign = False
                        self.mapValide = True
                        self.posListeObj += 1
                        
                        if(self.posListeObj >= len(self.listeObjet)):
                            self.posListeObj -= 1
                    if(j == ";" and self.validePlaceFichier == True):
                        break
                break

    def convertion(self, variable): #converti les position (5:5) en liste [(5,5) ...]
        tempo = variable.split(":")
        tempo[0],tempo[1]=int(tempo[0]),int(tempo[1])
        return tempo

class Salle():
    def __init__(self):
        self.salle = list()
    
    def chargeCarte(self, nomMap):
        try:
            f = open("assets/map/" + nomMap + ".mp", 'r')
        except IOError:
            print ("La map " + nomMap + "n'existe pas.")
            os._exit(1)

        """Dimensions de la carte"""    
        self.dimensionCarte = f.readline()
        self.tempo = self.dimensionCarte.split(":")
        self.nbColonne = int(self.tempo[0])
        self.nbLigne = int(self.tempo[1])

        f.readline()
        f.readline()
        self.salle = list()
        ligne = list()
        ligne = f.read()
        
        for i in ligne.splitlines():
            i.split('\n')
            self.salle.append(i)
