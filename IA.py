# -*- coding: ISO-8859-1 -*-

#Coucou, ben c'est fais par Gab donc si vous avez de questions venez me voir
#en passant quand le commentaire commence par // sa une notes pour moi pour penser a améliorer certain aspect du code
import math

class IA():
    def __init__(self,parent):
        self.parent = parent
        self.posMatX = self.parent.posMatX
        self.posMatY = self.parent.posMatY
        self.posMapX = self.parent.posMapX
        self.posMapY = self.parent.posMapY
        self.destXMatEcran = 50 #destination en pixel 
        self.destYMatEcran = 50 #destination en pixel
        self.destXMat = 0 ##destination dans la matrice
        self.destYMat = 0 ##destination dans la matrice 
        self.listeOuverte =[]  ## liste qui contient tout les noeud qui n'ont pas été analysé 
        self.listeFerme = []   ## liste qui contient tout les noeud qui ont été analysé    
        self.listeMouvement = []  ## liste des nouvement qui'il faut faire pour se rendre a destination

    def choisitAction(self):
        pass
        
    def choisitDeplacement(self,map):
        ## le logomate choisit ce qu'il va faire 
        ## // je vais tricher et donner un parent a personnage il ne faut pas faire sa trouve une solution
        if self.listeFerme :
            noeudTemp = self.listeFerme.pop()
            if noeudTemp.posX == self.destXMat & noeudTemp.posY == self.destYMat: 
                ## si la destination n'à pas changer je ne recalcul pas tout comme un tarla 
                depX  ## le nombre de pixel déplacer en x
                depY ## le nombre de pixel déplacer en x
                
                depX, depY = calculDeplacement(self.listeMouvement.pop())
                self.deplacement(depX,depY)
            
        else:
            ##// tu va avoir un temps de retard si tu fais pas faire le move après mais pour tester sa va
            self.chercheChemin(map)
		
    def chercheChemin(self,map):
        ## venir voir GAB pour le fonctionnement de la sélection de chemin 
        
        self.h = math.sqrt((self.destXMat-self.posMatX)**2 + (self.destYMat-self.posMatY)**2)  
        self.noeudCourant = Noeud(0,self.h,self.posMatX,self.posMatY,None,None)
        self.listeFerme.append(self.noeudCourant)

        while self.noeudCourant.posX != self.destXMat & self.noeudCourant.posY != self.destYMat:         
            i = 1
            while i <10:
                tempPosX,tempsPosY = calculDirection(i)
                
                ##on regarde si ya un mur la ou on va                                                
                if deplacementPossible(tempPosX,tempPosY,i,map): 
                    self.g = noeudCourant.g+1
                    self.h = math.sqrt((self.destXMat-self.posMatX)**2 + (self.destYMat-self.posMatY)**2) 
                     ## //je pourrais p-t créer mon noeud plus tard
                    self.noeudTemp = Noeud(self.g,self.h,tempPosX,tempPosY,self.noeudCourant.posX,self.noeudCourant.posY)
                    
                    if not dansListeFerme(self.noeudTemp):  ## si le noeud n'a pas déjà été vérifié
                        if dansListeOuverte(self.noeudTemps):  ## si le noeud est dans la liste ouverte il y a du code 
                            pass
                        else:
                            listeOuverte.append(noeudTemp)
                i +=1
            
            self.noeudCourant = choisirNoeudCourant()
        self.listeDeplacement(self.noeudCourant)    
 
    def listeDeplacement(self,noeudCourant): 
    ## on fais une liste de tout les déplacements qu'il faut faire pour se rendre à destination 
        self.listeMouvement.append(noeudCourant)
        while noeudCourant.parentX!= None:
            for i in self.listeFerme:
                if noeudCourant.parenX == i.parentX & noeudCourant.parentY == i.parentY:
                    noeudCourant = i
                    self.listeMouvement.append(noeudCourant)
                    
        if self.listeMouvement[-1] != None:   # si on est pas au point de départ on move
            ## FAIT LE DÉPLACEMENT
            self.listeMouvement.pop()
    
    def calculDirection(self,direction):
        ## je renvoi la position des cases alentours du noeud courant pour pouvoir les analysé
        ## La direction est basé sur le numpad 
        if direction==1:
            return self.noeudCourant.posX-1,self.noeudCourant.posY+1
        elif direction == 2:
            return self.noeudCourant.posX,self.noeudCourant.posY+1
        elif direction == 3:
            return self.noeudCourant.posX+1,self.noeudCourant.posY+1
        elif direction == 4:
            return self.noeudCourant.posX-1,self.noeudCourant.posY
        elif direction == 5:
            pass
        elif direction == 6:
            return self.noeudCourant.posX+1,self.noeudCourant.posY
        elif direction == 7:
            return self.noeudCourant.posX-1, self.noeudCourant.posY-1
        elif direction == 8:
            return self.noeudCourant.posX, self.noeudCourant.posY-1
        elif direction == 9:
            return self.noeudCourant.posX+1, self.noeudCourant.posY-1
    
    def deplacementPossible(self,posX,posY,direction,map):
        #je vérifie s'il est possible de se déplacer dans cette direction
        #//p-t essayer de rendre sa beau 
		
        if map[posX][posY] == 1:
            return False
            
        elif direction%2 ==1:
            if direction == 1:
                if map[posX+1][posY] == 1 & map[posX][posY-1] == 1:
                    return False
                else:
                    return True
                    
            elif direction == 7:
                if map[posX+1][posY] == 1 & map[posX][posY+1] == 1:
                    return False
                else:
                    return True
                    
            elif direction == 9:
                if map[posX-1][posY] == 1 & map[posX][posY+1] == 1:
                    return False
                else:
                    return True
                    
            elif direction == 3:
                if map[posX-1][posY] == 1 & map[posX][posY-1] == 1:
                    return False
                else:
                    return True

        else:
            return True
    
    def dansListeFerme(self,noeud):
        ## je regarde si le noeud est dans la liste ferme
        for i in self.listeFerme:
            if noeud.posX == i.posX & noeud.posY == i.posY:
                return True
            return False
            
    def dansListeOuverte(self,noeud):
    ## si le noeud est dans la liste ouverte et que le g est plus petit je change les parent du noeud dans la liste
        for i in listeOuverte:
            if i.posX == noeud.posX & i.posY == noeud.posY:
                if noeud.g < i.g:   ## si la distance du noeud courant entre lui et le début est plus petit que celui du noeud dans la liste
                    i.parentX = noeud.parentX
                    i.parentY = noeud.parentY
                    i.g =noeud.g
                    i.calulF()
    
    def choisirNoeudCourant(self):
        ## je me choisi un nouveau noeud courant en prenant celui avec la plus petite distance total (F)
        ##         parmi la liste ouverte( celle qui contient les chemins pas vérifié)
        noeudTemp = None 
        
        for i in listeOuverte:
            if noeudTemp== None:
                noeudTemp=i
            else:
                if noeudTemp.f < i.f:
                    noeudTemp=i
                    
        self.listeFerme.append(noeudTemp)
        self.listeOuverte.remove(noeudTemp)
        return noeudTemp
	        
    def calculDeplacement(self,destination):
        ## on calcul la direction dans laquelle on doit se déplacer
        mouvement = list() 
        #0-haut,1-droite,2-bas,3-gauche
        for i in range(4):
            self.mouvement.append(False)
            
        if destination.posX > self.posMatX:
            mouvement[1]= True
            
        if destination.posX < self.posMatX:
            mouvement[3]= True
            
        if destination.posY < self.posMatY:
            mouvement[0]= True
            
        if destination.posY > self.posMatY:
            mouvement[2]= True
            
        return self.parent.bouge(mouvement)
    
    def deplacement (self, depX,depY):
        ## on déplace le logomate
        self.posMapX += depX
        self.posMapY += depY
        
        self.posMatX, self.posMatY = coord(self,posMapX,posMapY)
        
class Noeud():
    def __init__(self,g,h,positionX,positionY,parentX,parentY):
        self.g = g   ## distance entre le point de départ et le noeud courrant     
        self.h = h   ## distance entre le noeud courant et l'objectif
        self.f = self.calculF()  ## distance enre le point de départ et l'arriver si on passe par là
        self.posX = positionX
        self.posY = positionY
        self.parentX = parentX
        self.parentY = parentY 
    
    def calculF(self):
        self.f = self.g+self.h