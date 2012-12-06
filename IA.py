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
        self.destX = None #destination 
        self.destY = 6 #destination 
        self.listeOuverte =[]  ## liste qui contient tout les noeud qui n'ont pas été analysé 
        self.listeFerme = []   ## liste qui contient tout les noeud qui ont été analysé    
        self.listeMouvement = []  ## liste des nouvement qui'il faut faire pour se rendre a destination

    def deplacement(self):
        ## le logomate choisit ce qu'il va faire 
        if self.listeFerme.pop().posX == self.destX & self.listeFerme.pop().posY == self.destY: 
            ## si la destination n'à pas changer je ne recalcul pas tout comme un tarla 
            self.listeMouvement.pop()
            
        if self.listeFerme.pop().posX ==  1:
            pass
		
    def chercheChemin(self,map):
        ## venir voir GAB pour le fonctionnement de la sélection de chemin 
        
        self.h = math.sqrt((self.destX-self.posMatX)**2 + (self.destY-self.posMatY)**2)  
        self.noedCourant = Noeud(0,self.h,self.posMatX,self.posMatY,None,None)
        listeFerme.append(noeudCourant)

        while self.noeudCourant.posX != self.destX & self.noeudCourant.posY != self.destY:         
            i = 1
            while i <10:
                tempPosX,tempsPosY = calculDirection(i)
                
                ##on regarde si ya un mur la ou on va                                                
                if deplacementPossible(tempPosX,tempPosY,i,map): 
                    self.g = noeudCourant.g+1
                    self.h = math.sqrt((self.destX-self.posMatX)**2 + (self.destY-self.posMatY)**2) 
                     ## //je pourrais p-t créer mon noeud plus tard
                    self.noeudTemp = Noeud(self.g,self.h,tempPosX,tempPosY,self.noeudCourant.posX,self.noeudCourant.posY)
                    
                    if not dansListeFerme(self.noeudTemp):  ## si le noeud n'a pas déjà été vérifié
                        if dansListeOuverte(self.noeudTemps):  ## si le noeud est dans la liste ouverte il y a du code 
                            pass
                        else:
                            listeOuverte.append(noeudTemp)
                i +=1
            
            self.noeudCourant = choisirNoeudCourant()
        deplace(noeudCouran)    
 
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
            self.listeMouvement.remove[-1]
    
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
	
class Noeud():
    def __init__(self,g,h,positionX,positionY,parentX,parentY):
        self.g = g   ## distance entre le point de départ et le noeud courrant     
        self.h = h   ## distance entre le noeud courant et l'objectif
        self.f = calculF(self.g,self.h)  ## distance enre le point de départ et l'arriver si on passe par là
        self.posX = positionX
        self.posY = positionY
        self.parentX = parentX
        self.parentY = parentY 
    
    def calculF(self):
        self.f = self.g+self.h