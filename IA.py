# -*- coding: ISO-8859-1 -*-

#Coucou, ben c'est fais par Gab donc si vous avez de questions venez me voir
#en passant quand le commentaire commence par // sa une notes pour moi pour penser a améliorer certain aspect du code
import math

class IA():
    def __init__(self,parent):
        self.parent = parent
        self.posMatX = 11
        self.posMatY = 11
        self.destMatX = 16 ##destination dans la matrice
        self.destMatY = 16 ##destination dans la matrice 
        self.listeOuverte =[]  ## liste qui contient tout les noeud qui n'ont pas été analysé 
        self.listeFerme = []   ## liste qui contient tout les noeud qui ont été analysé    
        self.listeMouvement = []  ## liste des nouvement qui'il faut faire pour se rendre a destination
        self.oldDestX =111111       ## notre ancienne destination permet de savoir si la destination a changer 
        self.odlDestY =111111 #/j'ai mis des gros chiffres car j'ai pas trouver de facon de faire si il n'y a rien 
    def choisitAction(self):
        pass
        
    def choisitDeplacement(self,map):
        ## le logomate choisit ce qu'il va faire 
        ## // je vais tricher et donner un parent a personnage il ne faut pas faire sa trouve une solution
       # if self.listeFerme :
           # if self.oldDestX == self.destMatX and self.odlDestY == self.destMatY: 
                ## si la destination n'à pas changer je ne recalcul pas tout comme un tarla 
        self.chercheChemin(map)
        #depX  ## le nombre de pixel déplacer en x
        #depY ## le nombre de pixel déplacer en x
        #print(self.destMatX,self.destMatY)
        self.calculDeplacement(self.listeMouvement[-1])

           
        #else:
            ##// tu va avoir un temps de retard si tu fais pas faire le move après mais pour tester sa va
           # self.chercheChemin(map)
		
    def chercheChemin(self,map):
        ## venir voir GAB pour le fonctionnement de la sélection de chemin 
        
        self.h = math.sqrt((self.destMatX-self.posMatX)**2 + (self.destMatY-self.posMatY)**2)
        self.noeudCourant = Noeud(0,self.h,self.posMatX,self.posMatY,10000,10000)
        self.listeFerme.append(self.noeudCourant)
        self.oldDestX = self.destMatX
        self.oldDestY = self.destMatY
        premierefois = True
        while self.noeudCourant.posX != self.destMatX and self.noeudCourant.posY != self.destMatY:         
            i = 1
            while i <10:
                tempPosX,tempPosY = self.calculDirection(i)
                ##on regarde si ya un mur la ou on va                                                
                if self.deplacementPossible(tempPosX,tempPosY,i,map): 
                    self.g = self.noeudCourant.g+1
                    self.h = math.sqrt((self.destMatX-self.posMatX)**2 + (self.destMatY-self.posMatY)**2) 
                     ## //je pourrais p-t créer mon noeud plus tard
                    self.noeudTemp = Noeud(self.g,self.h,tempPosX,tempPosY,self.noeudCourant.posX,self.noeudCourant.posY)
                    
                    if not self.dansListeFerme(self.noeudTemp):  ## si le noeud n'a pas déjà été vérifié
                        if self.dansListeOuverte(self.noeudTemp):  ## si le noeud est dans la liste ouverte il y a du code 
                            pass
                        else:
                            self.listeOuverte.append(self.noeudTemp)
                i +=1
            print("liste")
            for i in self.listeOuverte:
                print(i.posX,i.posY)
            self.noeudCourant = self.choisirNoeudCourant()
        self.listeDeplacement(self.noeudCourant)  
 
    def listeDeplacement(self,noeudCourant): 
    ## on fais une liste de tout les déplacements qu'il faut faire pour se rendre à destination 
        self.listeMouvement.append(noeudCourant)
        while noeudCourant.parentX!= 10000:
            for i in self.listeFerme:
                if noeudCourant.parentX == i.posX and noeudCourant.parentY == i.posY:
                    self.listeMouvement.append(noeudCourant)
                    noeudCourant = i
          
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
            return -1, -1
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
                if map[posX+1][posY] == 1 and map[posX][posY-1] == 1:
                    return False
                else:
                    return True
                    
            elif direction == 7:
                if map[posX+1][posY] == 1 and map[posX][posY+1] == 1:
                    return False
                else:
                    return True
                    
            elif direction == 9:
                if map[posX-1][posY] == 1 and map[posX][posY+1] == 1:
                    return False
                else:
                    return True
                    
            elif direction == 3:
                if map[posX-1][posY] == 1 and map[posX][posY-1] == 1:
                    return False
                else:
                    return True

        else:
            return True
    
    def dansListeFerme(self,noeud):
        ## je regarde si le noeud est dans la liste ferme
        for i in self.listeFerme:
            if noeud.posX == i.posX and noeud.posY == i.posY:
                return True
            return False
            
    def dansListeOuverte(self,noeud):
    ## si le noeud est dans la liste ouverte et que le g est plus petit je change les parent du noeud dans la liste

        for i in self.listeOuverte:
            if i.posX == noeud.posX and i.posY == noeud.posY:
                self.noeudCourant.posX
                if noeud.g < i.g:   ## si la distance du noeud courant entre lui et le début est plus petit que celui du noeud dans la liste
                    i.parentX = noeud.parentX
                    i.parentY = noeud.parentY
                    i.g =noeud.g
                    i.calculF()
    
    def choisirNoeudCourant(self):
        ## je me choisi un nouveau noeud courant en prenant celui avec la plus petite distance total (F)
        ##         parmi la liste ouverte( celle qui contient les chemins pas vérifié)
        noeudTemp = None 
        for i in self.listeOuverte:
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
        #0-haut,1-droite,2-bas,3-gauche

        if destination.posX > self.posMatX:
            self.posMatX +=1
            
        elif destination.posX < self.posMatX:
            self.posMatX -=1
            
        if destination.posY < self.posMatY:
            self.posMatY -=1
            
        elif destination.posY > self.posMatY:
            self.posMatY +=1   
        
        
class Noeud():
    def __init__(self,g,h,positionX,positionY,parentX,parentY):
        self.g = g   ## distance entre le point de départ et le noeud courrant     
        self.h = h   ## distance entre le noeud courant et l'objectif
        self.calculF()  ## distance enre le point de départ et l'arriver si on passe par là
        self.posX = positionX
        self.posY = positionY
        self.parentX = parentX
        self.parentY = parentY 
    
    def calculF(self):
        self.f = self.g+self.h
