# -*- coding: ISO-8859-1 -*-

#Coucou, ben c'est fais par Gab donc si vous avez de questions venez me voir
#en passant quand le commentaire commence par // sa une notes pour moi pour penser a améliorer certain aspect du code
import math

class IA():
    def __init__(self,parent):
        self.parent = parent
        self.subDivision =self.parent.parent.subDivision
        self.posMatX = self.parent.posMatX
        self.posMatY = self.parent.posMatY
        self.destMatX =5*self.subDivision  ##destination dans la matrice
        self.destMatY = 5*self.subDivision##destination dans la matrice 
        self.listeOuverte =[]  ## liste qui contient tout les noeud qui n'ont pas été analysé 
        self.listeFerme = []   ## liste qui contient tout les noeud qui ont été analysé    
        self.listeMouvement = []  ## liste des nouvement qui'il faut faire pour se rendre a destination
        self.oldDestX =111111       ## notre ancienne destination permet de savoir si la destination a changer 
        self.oldDestY =111111 #/j'ai mis des gros chiffres car j'ai pas trouver de facon de faire si il n'y a rien 
        self.i = 0
        self.first = True
        self.premier= True 
    
    def choisitAction(self):
        pass
        
    def choisitDeplacement(self,map):
        '''
        ###################### À revoir les conditions ne sont pas adapter ######################
        # le logomate choisit la destinationsd
        # le logomate ne se déplace pas horizontalement et verticalement , seulement en diagonale
        #########################################################################################
        '''
        if not self.arriverFin():
            if self.oldDestX != self.destMatX or self.oldDestY != self.destMatY: 
                    ## si la destination n'à pas changer je ne recalcul pas tout comme un tarla 
                self.chercheChemin(map)   
            self.calculDeplacement(self.listeMouvement[-1])
            self.listeMouvement.pop()
        
    def chercheChemin(self,map):
        ## venir voir GAB pour le fonctionnement de la sélection de chemin 
        
        self.h = math.sqrt((self.destMatX-self.posMatX)**2 + (self.destMatY-self.posMatY)**2)
        self.noeudCourant = Noeud(0,self.h,self.posMatX,self.posMatY,10000,10000)
        self.listeFerme.append(self.noeudCourant)
        self.oldDestX = self.destMatX
        self.oldDestY = self.destMatY
        
        while (self.noeudCourant.posX != self.destMatX and self.noeudCourant.posY != self.destMatY):
            i = 1
            while i <10:
                #tempPosX,tempPosY = self.calculDirection(i)
                ##on regarde si ya un mur la ou on va 
                depX,depY = self.deplacementPossible(i,map)
                if depX != 2: 
                    g = self.noeudCourant.g+1
                    h = math.sqrt((self.destMatX-(self.noeudCourant.posX+depX))**2 + (self.destMatY-(self.noeudCourant.posY+depY))**2) 
                     ## //je pourrais p-t créer mon noeud plus tard
                    self.noeudTemp = Noeud(g,h,self.noeudCourant.posX+depX,self.noeudCourant.posY+depY,self.noeudCourant.posX,self.noeudCourant.posY)
                    
                    if not self.dansListeFerme(self.noeudTemp):  ## si le noeud n'a pas déjà été vérifié
                        self.dansListeOuverte(self.noeudTemp)  
                     
                i +=1
            '''
            for i in self.listeOuverte:
                if self.noeudCourant.posX == i.posX and self.noeudCourant.posY == i.posY:
                    print("NOOOOOOO")'''
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
     
    def deplacementPossible(self,direction,map):
        #je vérifie s'il est possible de se déplacer dans cette direction
        #//p-t essayer de rendre sa beau 
        #if map[posX*self.parent.parent.subDivision][posY*self.parent.parent.subDivision] == 1:    
        posX = self.noeudCourant.posX
        posY = self.noeudCourant.posY
        '''
        print("positionREAL",self.posMatX,self.posMatY)
        print("destination",self.destMatX,self.destMatY)
        print("position",posX,posY)
        '''

        #gauche bas 
        if direction == 1:
            if map[posX+1][posY] == 1 and map[posX][posY-1] == 1 or map[posX-1][posY+1] == '1':
                return 2,2
            else:
                return -1, 1
        
        # gauche haut 
        elif direction == 7:
            if map[posX-1][posY-1] == '1':
                if self.premier:
                    self.premier=False
                    print("position",posX,posY)
                return 2,2
            else:
                return -1, -1
                
        # droite haut
        elif direction == 9:
            if map[posX-1][posY] == 1 and map[posX][posY+1] == 1 or map[posX+1][posY-1] == '1':
                return 2,2
            else:
                return 1, -1
                
        #droite bas
        elif direction == 3:
            if map[posX-1][posY] == 1 and map[posX][posY-1] == 1 or map[posX+1][posY+1] == '1':
                return 2,2
            else:
                return 1, 1
            
        else:
            return  2,2
    
        #bas
        if direction ==2:
            if map[posX][posY+1] == '1':
                return 0,1
            
        #droite
        elif direction == 6:
            if map[posX+1][posY] == '1':
                return 1,0
            
        #haut
        elif direction == 8:
            if map[posX][posY-1] == '1':
                return 0,-1
            
        #gauche
        elif direction == 4:
            if map[posX-1][posY] == '1':
                return -1,0
        
        else:
            return  2,2
        
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
                return True
        self.listeOuverte.append(noeud)
        return False
    
    def choisirNoeudCourant(self):        
        ## je me choisi un nouveau noeud courant en prenant celui avec la plus petite distance total (F)
        ##         parmi la liste ouverte( celle qui contient les chemins pas vérifié)
        noeudTemp = None 
        for i in self.listeOuverte:
            if noeudTemp== None:
                noeudTemp=i
            else:
                if noeudTemp.f > i.f:
                    noeudTemp=i
        if self.premier == False:
            for i in self.listeOuverte:
                if i.posX == 224 and i.posY== 224:
                    print("la bonne case",i.f)
        self.listeFerme.append(noeudTemp)
        self.listeOuverte.remove(noeudTemp)
        return noeudTemp
       
    def calculDeplacement(self,destination):
        ## on calcul la direction dans laquelle on doit se déplacer
        #0-haut,1-droite,2-bas,3-gauche
        deplacement = 1
        if destination.posX > self.posMatX:
            self.posMatX +=deplacement
            self.parent.posMatX +=deplacement
            
        elif destination.posX < self.posMatX:
            self.posMatX -=deplacement
            self.parent.posMatX -=deplacement
            
        if destination.posY < self.posMatY:
            self.posMatY -=deplacement
            self.parent.posMatY -=deplacement
            
        elif destination.posY > self.posMatY:
            self.posMatY +=deplacement
            self.parent.posMatY +=deplacement
     
     ### Vérification si le logomate est arrivée a destination       
    def arriverFin(self):
        if self.posMatX == self.destMatX and self.posMatY == self.destMatY:
            return True
        else:
            return False
        
        
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
