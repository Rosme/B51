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
        self.listeMap = ["MainRoom", "F_S1", "F_E1S1", "F_E1S2", "F_E1S3", "F_E1S4", "F_E1S5", "F_E1S6", "F_E2S1", "F_E2S2", "F_E2S3" , "F_E2S4", "I_S1" ,"I_E1S1", "I_E1S2", "I_E1S3", "I_E1S4" , "R_S1", "R_E1S1", "S_S1" , "HELL"]
        self.nbObjMap = len(self.listeMap)
        self.subDivision = 32
        #self.joueur = ""
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
        
        for joueur in self.listePersonnage:
            tempMatX, tempMatY = joueur.bouge()
            
            if laMap[tempMatY][tempMatX]== 'm' or laMap[tempMatY][tempMatX] == 'v' or laMap[tempMatY][tempMatX]== 'b' or laMap[tempMatY][tempMatX] == 'n' or laMap[tempMatY][tempMatX]== 'M' or laMap[tempMatY][tempMatX] == 'V' or laMap[tempMatY][tempMatX]== 'B' or laMap[tempMatY][tempMatX] == 'N':
                car=laMap[tempMatY][tempMatX]
                joueur.nomMap=self.carte.s.changementCarte(car)
                self.coordProchaineZone(car, joueur)
                self.parent.actualiserAffichageComplet(self.joueur,self.carte.s)
            else:
                try:    
                    if laMap[tempMatY+self.subDivision][tempMatX]!='1':
                        if laMap[tempMatY][tempMatX]=='0' or laMap[tempMatY][tempMatX]=='2'  or laMap[tempMatY][tempMatX]=='q' or laMap[tempMatY][tempMatX]=='w':
                            joueur.posMatX=tempMatX
                            joueur.posMatY=tempMatY
                            self.parent.actusliserPersonnage(joueur)
                except:
                    if laMap[tempMatY][tempMatX]=='0' or laMap[tempMatY][tempMatX]=='2'  or laMap[tempMatY][tempMatX]=='q' or laMap[tempMatY][tempMatX]=='w':
                        joueur.posMatX=tempMatX
                        joueur.posMatY=tempMatY
                        sellf.parent.actusliserPersonnage(joueur)
    
    def coordProchaineZone(self,char, joueur):
        laMap=self.carte.s.salle
        
        trouver=False
        
        for i in range(0,len(laMap),self.subDivision):
            for j in range(0,len(laMap[i]),self.subDivision):
                if laMap[i][j]==char:
                    try:
                        #si l'autre char à droite
                        if laMap[i][j+self.subDivision]==char:
                            try:
                                if laMap[i+self.subDivision][j]=='0':#porte en haut
                                    matx = j
                                    maty = i+self.subDivision
                                    trouver=True
                                    break
                                elif laMap[i+self.subDivision][j] == ' ':
                                    raise IndexError
                            except IndexError:
                                if laMap[i-self.subDivision][j]=='0':#porte en bas
                                    matx = j
                                    maty = i-self.subDivision
                                    trouver=True
                                    break
                        else:
                            raise IndexError
                    except IndexError: 
                        #sil'autre char est en dessous
                        if laMap[i+self.subDivision][j]==char:
                            print("3")
                            try:
                                if laMap[i][j+self.subDivision]=='0':#porte à droite
                                    matx = j+self.subDivision
                                    maty = i
                                    trouver=True
                                    break
                                elif laMap[i+self.subDivision][j] == ' ':
                                    raise IndexError
                            except IndexError:
                                if laMap[i][j-self.subDivision]=='0':#porte à gauche
                                    matx = j-self.subDivision
                                    maty = i
                                    trouver=True                          
                                    break
            if trouver:
                break

        joueur.posMatY=maty
        joueur.posMatX=matx        
        
    
    def activationObjet(self):
        '''
        if self.listeInterrupteur:
            for i in self.listeInterrupteur:
                i.collision(self.joueur)
                if i.activer():
                    self.parent.actualiserAffichageComplet(self.joueur,self.carte.s)
                    break
                    
                    
                    
        if self.listeRoche:
            for i in self.listeRoche:
                if not i.aTerre:
                    i.bouge(self.joueur)
                    
        if self.listeDeclencheur:
            for i in self.listeDeclencheur:
                i.collision(self.joueur)
                i.activer()
                break
        '''
        pass
                
    def gestionMort(self):
        '''
        if self.joueur.race.vie<=0:
            self.joueur.mort()
            self.carte.s.salle=self.carte.s.dictMap[self.joueur.nomMap]
            self.parent.joueurMort(self.joueur,self.carte.s)
        '''
        ownPlayer = self.getPlayerById(self.parent.network.id)
        if ownPlayer.race.vie <= 0:
            ownPlayer.mort()
            self.carte.s.salle = self.carte.s.dictMap[ownPlayer.nomMap]
            self.parent.joueurMort(ownPlayer, self.carte.s)

    ############################# Méthode en lien avec les balles et le tire du joueur #############################
    def rechargement(self):
        '''
        self.joueur.recharge()
        if self.listeLevier:
            for i in self.listeLevier:
                if i.energie != i.max_energie:
                    i.recharge()
        '''
        ownPlayer = self.getPlayerById(self.parent.network.id)
        ownPlayer.recharge()
                    
    def tire(self):
        '''
        if self.mouvement[4]:
            if self.joueur.tire(self.listeBalle, self.sourisX, self.sourisY):
                balle = self.listeBalle[len(self.listeBalle)-1]    
        '''
        pass

    def balle(self):
        self.collision(self.listePersonnage)
        self.collision(self.listeLogomate)
        
        self.parent.actualisationBalle(self.listeBalle)
   
    def collision(self, liste):  
        temp = self.listeBalle
        
        for i in self.listeBalle:
            #i.bouge(self.joueur)
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
        pers = Personnage(self)
        pers.nouveauPersonnage("Logo", Race.Logomate())
        pers.posMatX = int(posMat[0])
        pers.posMatY = int(posMat[1])
        self.listeLogomate.append(pers)
        
    def nouveauSac(self,posMat, nomMap):
        sac = Objet.Sac(self, int(posMat[0]), int(posMat[1]), nomMap)
        self.listeSac.append(sac)
        
    def nouveauCoffre(self, posMat, nomMap):
        coffre = Objet.Coffre(self, int(posMat[0]), int(posMat[1]), nomMap)
        self.listeCoffre.append(coffre)
        
    def nouvelleRoche(self, posMat, nomMap):
        roche = Objet.Roche(self,  int(posMat[0]), int(posMat[1]), nomMap)
        self.listeRoche.append(roche) 
           
    def nouveauInterrupt(self, posMat, nomMap):
        interrupteur = Objet.Interrupteur(self, int(posMat[0]), int(posMat[1]), False, nomMap)
        self.listeInterrupteur.append(interrupteur)
    
    def nouveauDeclencheur(self, posMat, nomMap):
        declencheur = Objet.Declencheur(self,  int(posMat[0]), int(posMat[1]), nomMap)
        self.listeDeclencheur.append(declencheur)
    
    def nouveauLevier(self, posMat, nomMap):
        levier = Objet.Levier(self, int(posMat[0]), int(posMat[1]), 10, 100, 2, nomMap)
        self.listeLevier.append(levier)
    
    def nouveauJoueur(self, id, race, nom):
        joueur = Personnage(self, id)
        if race == "Humain":
            joueur.nouveauPersonnage(nom, Race.Humain())
        elif race == "Irki":
            joueur.nouveauPersonnage(nom, Race.Irki())
        elif race == "Popamu":
            joueur.nouveauPersonnage(nom, Race.Popamu()) 
        elif race == "Atarix":
            joueur.nouveauPersonnage(nom, Race.Atarix())
        self.listePersonnage.append(joueur)
        
    def rajoutMetal(self, id):
        self.getPlayerById(self.parent.network.id).inventaire.ajouterItem(Item.Upgradable(0, "Metal", "Metal Scrap used to craft Guns and Armors"))
        
    def rajoutElectro(self):
        self.getPlayerById(self.parent.network.id).inventaire.ajouterItem(Item.Upgradable(1, "Electronique", "Electronic parts used to craft Armors and Dematerializator"))
        
    def rajoutBatterie(self):
        self.getPlayerById(self.parent.network.id).inventaire.ajouterItem(Item.Upgradable(2, "Batterie", "Battery used to craft Guns and Dematerializator"))

    def getPlayerById(self, id):
        for player in self.listePersonnage:
            if player.id == id:
                return player
        return None

    def treatEventsById(self, tickData):
        player = self.getPlayerById(tickData.id)
        for event in tickData.events:
            if event == "MOVE_UP":
                player.mouvement[0] = True
            if event == "MOVE_RIGHT":
                player.mouvement[1] = True
            if event == "MOVE_DOWN":
                player.mouvement[2] = True
            if event == "MOVE_LEFT":
                player.mouvement[3] = True
            if event == "NO_UP":
                player.mouvement[0] = False
            if event == "NO_RIGHT":
                player.mouvement[1] = False
            if event == "NO_DOWN":
                player.mouvement[2] = False
            if event == "NO_LEFT":
                player.mouvement[3] = False