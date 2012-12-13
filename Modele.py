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
        self.mouvement = list() 
        #0-haut,1-droite,2-bas,3-gauche,4-tire
        for i in range(5):
            self.mouvement.append(False)
        self.listeInterrupteur = list()
        self.listeDeclencheur = list()
        self.listePersonnage = list()
        self.listeLogomate = list()
        self.listeCoffre = list()
        self.listeLevier = list()
        self.listeRoche = list()
        self.listeBalle = list()
        self.listeSac = list()
        self.listeMap = ["MainRoom", "F_E1S1", "F_E1S2", "F_E1S3", "F_E1S4", "F_E1S5", "F_E1S6", "F_E2S1", "F_E2S2", "F_E2S3" , "F_E2S4", "I_E1S1", "I_E1S2", "I_E1S3", "I_E1S4", "R_E1S1", "HELL"]
        self.nbObjMap = len(self.listeMap)
        self.joueur = ""
        self.carte = Carte.Carte(self)
        self.artisanat = Artisanat.Artisanat(self)
        self.sourisX = 0
        self.sourisY = 0
        
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
    
    def bougePersonnage(self):
        laMap=self.carte.s.salle
        
        tempMatX, tempMatY = self.joueur.bouge(self.mouvement)
        
        if laMap[tempMatY][tempMatX]== 'm' or laMap[tempMatY][tempMatX] == 'v' or laMap[tempMatY][tempMatX]== 'b' or laMap[tempMatY][tempMatX] == 'n':
            car=laMap[tempMatY][tempMatX]
            self.joueur.nomMap=self.carte.s.changementCarte(car)
            self.coordProchaineZone(car)
            self.parent.actualiserAffichageComplet(self.joueur,self.carte.s)
            
        elif laMap[tempMatY][tempMatX]=='0' or laMap[tempMatY][tempMatX]=='2'  or laMap[tempMatY][tempMatX]=='q' or laMap[tempMatY][tempMatX]=='w':
            self.joueur.posMatX=tempMatX
            self.joueur.posMatY=tempMatY
            self.parent.actusliserPersonnage(self.joueur)
    
    def coordProchaineZone(self,char):
        laMap=self.carte.s.salle
        
        trouver=False
        
        for i in range(len(laMap)):
            for j in range(len(laMap[i])):
                if laMap[i][j]==char:
                    try:
                        #si l'autre char à droite
                        if laMap[i][j+1]==char:
                            try:
                                if laMap[i+1][j]=='0':#porte en haut
                                    matx = j
                                    maty = i+1
                                    trouver=True
                                    break
                            except IndexError:
                                if laMap[i-1][j]=='0':#porte en bas
                                    matx = j
                                    maty = i-1
                                    trouver=True
                                    break
                        else:
                            raise IndexError
                    except IndexError: 
                        #sil'autre char est en dessous
                        if laMap[i+1][j]==char:
                            try:
                                if laMap[i][j+1]=='0':#porte à droite
                                    matx = j+1
                                    maty = i
                                    trouver=True
                                    break
                            except IndexError:
                                if laMap[i][j-1]=='0':#porte à gauche
                                    matx = j-1
                                    maty = i
                                    trouver=True                          
                                    break
            if trouver:
                break

        self.joueur.posMatY=maty
        self.joueur.posMatX=matx        
        
    
    def activationObjet(self):
        if self.listeInterrupteur:
                for i in self.listeInterrupteur:
                    i.collision(self.joueur)
                    if i.activer():
                        self.parent.actualiserAffichageComplet(self.joueur,self.carte.s)
                    
        if self.listeRoche:
            for i in self.listeRoche:
                if not i.aTerre:
                    i.bouge(self.joueur)
    
    def gestionMort(self):
        if self.joueur.race.vie<=0:
            self.joueur.mort()
            self.carte.s.salle=self.carte.s.dictMap[self.joueur.nomMap]
            self.parent.joueurMort(self.joueur,self.carte.s)

    ############################# Méthode en lien avec les balles et le tire du joueur #############################
    def rechargement(self):
        self.joueur.recharge()
        if self.listeLevier:
            for i in self.listeLevier:
                if i.energie != i.max_energie:
                    i.recharge()
                    
    def tire(self):
        if self.mouvement[4]:
            if self.joueur.tire(self.listeBalle, self.sourisX, self.sourisY):
                balle = self.listeBalle[len(self.listeBalle)-1]
            else:
                balle = self.listeBalle[len(self.listeBalle)-1]
                self.listeBalle.remove(balle);

    def balle(self):
        self.collision(self.listePersonnage)
        self.collision(self.listeLogomate)
        
        self.parent.actualisationBalle(self.listeBalle)
   
    def collision(self, liste):  
        temp = self.listeBalle
        
        for i in self.listeBalle:
            i.bouge(self.joueur)
            '''
            if i.veloY<0 and i.veloX<0:
                i.posMatX,i.posMatY=self.parent.app.frameJeu.coordEcranAMatrice(i.posMapX+(i.veloX)*2,(i.posMapY+(i.veloY)*2)+30)
            elif i.veloY>0 and i.veloX>0:
                i.posMatX,i.posMatY=self.parent.app.frameJeu.coordEcranAMatrice((i.posMapX+(i.veloX)*2)+10,(i.posMapY+(i.veloY)*2)+10)
            elif i.veloY<0 and i.veloX>0:
                i.posMatX,i.posMatY=self.parent.app.frameJeu.coordEcranAMatrice((i.posMapX+(i.veloX)*2)+40,(i.posMapY+(i.veloY)*2)+40)                
            else:
                i.posMatX,i.posMatY=self.parent.app.frameJeu.coordEcranAMatrice((i.posMapX+(i.veloX)*2)+25,(i.posMapY+(i.veloY)*2)+25)
            '''
            if i.collision(liste, self.carte.s.salle):
                temp.remove(i)
                
        self.listeBalle = temp
        
    
    def nouveauLogo(self, posMat,nomMap):
        pers = Personnage()
        pers.nouveauPersonnage("Logo", Race.Logomate())
        pers.posMatX = int(posMat[0])
        pers.posMatY = int(posMat[1])
        self.listeLogomate.append(pers)
        
    def nouveauSac(self,posMat, nomMap):
        sac = Objet.Interrupteur(self, int(posMat[0]), int(posMat[1]), nomMap)
        self.listeSac.append(sac)
        
    def nouveauCoffre(self, posMat, nomMap):
        coffre = Objet.Interrupteur(self, int(posMat[0]), int(posMat[1]), nomMap)
        self.listeCoffre.append(coffre)
        
    def nouvelleRoche(self, posMat, nomMap):
        roche = Objet.Roche(self,  int(posMat[0]), int(posMat[1]), nomMap)
        self.listeRoche.append(roche) 
           
    def nouveauInterrupt(self, posMat, nomMap):
        interrupteur = Objet.Interrupteur(self, int(posMat[0]), int(posMat[1]), False, nomMap)
        self.listeInterrupteur.append(interrupteur)
    
    def nouveauDeclencheur(self, posMat, nomMap):
        declencheur = Objet.Interrupteur(self,  int(posMat[0]), int(posMat[1]), nomMap)
        self.listeDeclencheur.append(declencheur)
    
    def nouveauLevier(self, posMat, nomMap):
        levier = Objet.Levier(self, int(posMat[0]), int(posMat[1]), 10, 100, 2, nomMap)
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
        
    def rajoutMetal(self):
        self.joueur.inventaire.ajouterItem(Item.Upgradable(0, "Metal", "Metal Scrap used to craft Guns and Armors"))
        
    def rajoutElectro(self):
        self.joueur.inventaire.ajouterItem(Item.Upgradable(1, "Electronique", "Electronic parts used to craft Armors and Dematerializator"))
        
    def rajoutBatterie(self):
        self.joueur.inventaire.ajouterItem(Item.Upgradable(2, "Batterie", "Battery used to craft Guns and Dematerializator"))
