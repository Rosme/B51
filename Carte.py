# -*- coding: ISO-8859-1 -*-
import os

class Carte():
    def __init__(self, parent):
        self.parent = parent
        self.s = Salle(self)
        self.s.chargeCartes()
        
    def chargeObjets(self):
        try:
            liens = open("assets/liens/liens.txt", 'r')
        except IOError:
            print ("Le fichier liens.txt n'a pas été retrouvé (liens/liens.txt)")
            os._exit(1)
            
        #self.s.salle = self.s.dictMap["MainRoom"]
        ligne = list()
        ligne = liens.read()

        """Tous les objets possible"""
        listeObjet = ["Logomate", "Sac", "Coffre", "Roche", "Interrupteur", "Declencheur", "Levier"]
        
        mapValide = False
        valideAssign = False
        posListeObj = 0
        posListeMap = 0

        """Processus de lecture des objets (Logomate, Sac, Coffre, Roche...)
            à partir du fichier lien """
        for i in ligne.splitlines():
            i.split('\n')
            if(i == self.parent.listeMap[posListeMap]):
                mapValide = True
            if(i == listeObjet[posListeObj] and mapValide == True):
                valideAssign = True
            elif(valideAssign == True and i != "break"):
                if(listeObjet[posListeObj] == "Logomate"):
                    self.parent.nouveauLogo(self.convertion(i), self.parent.listeMap[posListeMap])
                elif (listeObjet[posListeObj] == "Sac"):
                    self.parent.nouveauSac(self.convertion(i), self.parent.listeMap[posListeMap])
                elif(listeObjet[posListeObj] == "Coffre"):
                    self.parent.nouveauCoffre(self.convertion(i), self.parent.listeMap[posListeMap])
                elif(listeObjet[posListeObj] == "Roche"):
                    self.parent.nouvelleRoche(self.convertion(i), self.parent.listeMap[posListeMap])
                elif(listeObjet[posListeObj] == "Interrupteur"):
                    self.parent.nouveauInterrupt(self.convertion(i), self.parent.listeMap[posListeMap])
                elif(listeObjet[posListeObj] == "Declencheur"):
                    self.parent.nouveauDeclencheur(self.convertion(i), self.parent.listeMap[posListeMap])
                elif(listeObjet[posListeObj] == "Levier"):
                    self.parent.nouveauLevier(self.convertion(i), self.parent.listeMap[posListeMap])
            elif(valideAssign == True and i == "break"):
                valideAssign = False
                posListeObj += 1
                        
                if(posListeObj >= len(listeObjet)):
                    posListeObj -= 1
            if(i == ";" and posListeMap == self.parent.nbObjMap-1):
                break
            elif(i == ";" and posListeMap < self.parent.nbObjMap-1):
                mapValide = False
                posListeMap += 1
                posListeObj = 0
        liens.close()

    def convertion(self, variable): #convertir les positions (5:5) en liste [(5,5) ...]
        tempo = variable.split(":")
        return tempo

class Salle():
    def __init__(self, parent):
        self.parent = parent
        #self.salle = list()
        self.dimensionCarte = int()
        self.dictSauvegarde = dict()
        self.dictMap = dict()
        self.nomMap = "MainRoom"

    def chargeCartes(self):
        tempSalle = list()
        for j in self.parent.parent.listeMap:
            self.ouvertureMap(j)
            self.dimensionsMap(j)
            self.liensCarte()
            self.dictMap[j + " liens"] = self.dictionnaireLiens
            ligne = list()
            ligne = self.fichier.read()
            for i in ligne.splitlines():
                i.split('\n')
                tempSalle.append(i)
            tempSalle = self.subdivisionMap(tempSalle)
            self.dictMap[j] = tempSalle
            #print(j)
            #print(self.salle)
            tempSalle = list()
        
        self.fichier.close()
        
    def subdivisionMap(self,tempSalle):
        salleDivise=list()
        tempLigne=list()        
        for i in range(len(tempSalle)):
            for k in range(len(tempSalle[i])):
                for u in range(self.parent.parent.subDivision):
                    tempLigne.append(tempSalle[i][k])
            for r in range(self.parent.parent.subDivision):
                salleDivise.append(tempLigne)
            tempLigne=list()
        tempSalle=salleDivise

        return tempSalle
                    
    def liensCarte(self):
        self.dictionnaireLiens = dict()
        self.assoCarte = self.fichier.readline()
        self.listeAsso = self.assoCarte.split(" ")
        
        i = 0
        while i < len(self.listeAsso):
            self.listeValeur = self.listeAsso[i].split(":")
            self.dictionnaireLiens[self.listeValeur[0]] = self.listeValeur[1]
            i += 1
    
    def changementCarte(self, caractere,nomMap):
        self.liensCarte = self.dictMap[nomMap + " liens"]
        nomMap = self.liensCarte[caractere]
        #On va ignorer le \n qui peut se retrouver dans les noms de map
        self.listeTempo = nomMap.split('\n')
        nomMap = self.listeTempo[0]
        #salle = self.dictMap[nomMap]
        
        return nomMap
        
    def sauvegarderMap(self, nomMap, contenuMap): #Prend le nom de la Map et son contenu modifié
        self.dictSauvegarde[nomMap] = contenuMap

    def ouvertureMap(self, nomMap):
        try:
            self.fichier = open("assets/map/" + nomMap + ".mp", 'r')
        except IOError:
            print ("La map " + nomMap + " n'existe pas.")
            os._exit(1)

    def ignoreSlashN(self, nomMap):
        listeTempo = nomMap.split('\n')
        nomMap = listeTempo[0]
        return nomMap

    def dimensionsMap(self,nomMap):
        self.dimensions = list()
        self.dimensionCarte = self.fichier.readline()
        tempo = self.dimensionCarte.split(":")
        #0-colonne 1-ligne
        self.dimensions.append(int(tempo[0]))
        self.dimensions.append(int(tempo[1]))
        self.dictMap[nomMap + " dimensions"] = self.dimensions