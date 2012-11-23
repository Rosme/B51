# -*- coding: ISO-8859-1 -*-
import os

class Carte():
    def __init__(self, parent):
        self.parent = parent
        self.nomMap = "MainRoom"
        self.s = Salle()
        self.s.chargeCarte(self.nomMap)
        #self.s.changementCarte('v') pour tester seulement
        #self.s.sauvegarderMap(self.nomMap, ['yo', 'yo', 'yo']) pour tester seulement
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
        self.listeObjet = ["Logomate", "Sac", "Coffre", "Roche", "Interrupteur", "Declencheur", "Levier"]

        """Liste des positions de chaque objet """
        self.listeLogo = list()
        self.listeSac = list()
        self.listeCoffre = list()
        self.listeRoche = list()
        self.listeInterrupteur = list()
        self.listeDeclencheur = list()
        self.listeLevier = list()
        
        self.mapValide = False
        self.valideAssign = False
        self.posListeObj = 0

        """Processus de lecture des objets (Logomate, Sac, Coffre, Roche...)
            selon la map choisie à partir du fichier lien """
        for i in ligne.splitlines():
            i.split('\n')
            if(i == self.nomMap):
                self.mapValide = True
                self.valideEmplacement = True
            if(i == self.listeObjet[self.posListeObj] and self.mapValide == True):
                self.valideAssign = True
                self.mapValide = False
            elif(self.valideAssign == True and i != "break"):
                if(self.listeObjet[self.posListeObj] == "Logomate"):
                    self.parent.nouveauLogo(self.convertion(i))
                elif (self.listeObjet[self.posListeObj] == "Sac"):
                    self.listeSac.append(self.convertion(i))
                elif(self.listeObjet[self.posListeObj] == "Coffre"):
                    self.listeCoffre.append(self.convertion(i))
                elif(self.listeObjet[self.posListeObj] == "Roche"):
                    self.listeRoche.append(self.convertion(i))
                elif(self.listeObjet[self.posListeObj] == "Interrupteur"):
                    self.listeInterrupteur.append(self.convertion(i))
                elif(self.listeObjet[self.posListeObj] == "Declencheur"):
                    self.listeDeclencheur.append(self.convertion(i))
                elif(self.listeObjet[self.posListeObj] == "Levier"):
                    self.listeLevier.append(self.convertion(i))
            elif(self.valideAssign == True and i == "break"):
                self.valideAssign = False
                self.mapValide = True
                self.posListeObj += 1
                        
                if(self.posListeObj >= len(self.listeObjet)):
                    self.posListeObj -= 1
            if(i == ";" and self.mapValide == True):
                break
        liens.close()

    def convertion(self, variable): #convertit les positions (5:5) en liste [(5,5) ...]
        self.var = variable
        self.tempo = self.var.split(":")
        return self.tempo

class Salle():
    def __init__(self):
        self.salle = list()
        self.dictSauvegarde = dict()
        self.dictionnaireAsso = dict()
    
    def chargeCarte(self, nomMap):
        #On va ignorer le \n qui peut se retrouver dans les noms de map
        self.laMap = nomMap
        self.listeTempo = self.laMap.split('\n')
        self.laMap = self.listeTempo[0]
        
        self.ouvertureMap(self.laMap)

        """Dimensions de la carte"""    
        self.dimensionCarte = self.fichier.readline()
        self.tempo = self.dimensionCarte.split(":")
        self.nbColonne = int(self.tempo[0])
        self.nbLigne = int(self.tempo[1])

        self.fichier.readline()
        self.fichier.readline()
        
        self.salle = list()
        ligne = list()
        ligne = self.fichier.read()
        
        for i in ligne.splitlines():
            i.split('\n')
            self.salle.append(i)

        self.fichier.close()

    def sauvegarderMap(self, nomMap, contenuMap): #Prend le nom de la Map et son contenu modifié
        self.dictSauvegarde[nomMap] = contenuMap

    def ouvertureMap(self, nomMap):
        try:
            self.fichier = open("assets/map/" + nomMap + ".mp", 'r')
            self.nomMap = nomMap
            print(self.nomMap)
        except IOError:
            print ("La map " + nomMap + " n'existe pas.")
            os._exit(1)
    
    def changementCarte(self, charactere):
        #On va ignorer le \n qui peut se retrouver dans les noms de map
        self.listeTempo = self.nomMap.split('\n')
        self.nomMap = self.listeTempo[0]
        
        self.ouvertureMap(self.nomMap)
        self.fichier.readline()
        
        self.assoCarte = self.fichier.readline()
        self.listeAsso = self.assoCarte.split(" ")
        
        i = 0
        while i < len(self.listeAsso):
            self.listeValeur = self.listeAsso[i].split(":")
            self.dictionnaireAsso[self.listeValeur[0]] = self.listeValeur[1]
            i += 1

        self.fichier.close()
        print (self.dictionnaireAsso)
        self.chargeCarte(self.dictionnaireAsso[charactere])
            
#if __name__=="__main__":
    #Carte()
