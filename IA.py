# -*- coding: ISO-8859-1 -*-

#Coucou, ben c'est fais par Gab donc si vous avez de questions venez me voir
#en passant quand le commentaire commence par // sa une notes pour moi pour penser a am�liorer certain aspect du code
import math
import random

class IA():
    def __init__(self,parent):
        self.parent = parent
        self.subDivision =self.parent.parent.subDivision
        self.direction = None
        self.posX = self.parent.posMatX
        self.posY = self.parent.posMatY

    def choisitDeplacement(self):
        self.direction = self.calculRandom()
        # ajouter Si y a un player dans son range qu'il d�fend il attaque 
               
          
    
    
    def calculRandom(self):
        return random.randint(0, 7)
        
    def deplacement(self,map):    
        self.mouvement = 4
    
        #gauche Bas
        if self.direction == 5:
            if (map[self.posY-self.subDivision][self.posX] != '0' and map[self.posY][self.posX+self.subDivision] != '0') or map[self.posY-self.subDivision][self.posX+self.subDivision] != '0':
                self.choisitDeplacement()
            else:
                self.posY -= self.mouvement
                self.posX += self.mouvement   
         
        #gauche haut
        elif self.direction == 0:
            if (map[self.posY-self.subDivision][self.posX] != '0' and map[self.posY][self.posX-self.subDivision] != '0') or map[self.posY-self.subDivision][self.posX-self.subDivision] != '0':
                self.choisitDeplacement()
            else:
                self.posY -= self.mouvement
                self.posX -= self.mouvement

        # droite Haut         
        elif self.direction == 2:
            if (map[self.posY+self.subDivision][self.posX] != '0' and map[self.posY][self.posX-self.subDivision] != '0') or map[self.posY+self.subDivision][self.posX-self.subDivision] != '0':
                self.choisitDeplacement()
            else:
                self.posY +=self.mouvement
                self.posX -=self.mouvement
         
        #droite bas
        elif self.direction == 7:
            if (map[self.posY+self.subDivision][self.posX] != '0' and map[self.posY][self.posX+self.subDivision] != '0') or map[self.posY+self.subDivision][self.posX+self.subDivision] != '0':
                self.choisitDeplacement()
            else:
                self.posY +=self.mouvement
                self.posX +=self.mouvement
           
        # droite 
        elif self.direction == 4:
            if map[self.posY+self.subDivision][self.posX]!= '0':
                self.choisitDeplacement()
            else:
                self.posY += self.mouvement
        
        #bas
        elif self.direction == 6:
            if map[self.posY][self.posX+self.subDivision] != '0':
                self.choisitDeplacement()
            else:
                self.posX += self.mouvement
        
        # gauche 
        elif self.direction == 3:
            if map[self.posY-self.subDivision][self.posX] != '0':
                self.choisitDeplacement()
            else:
                self.posY -=self.mouvement
            
        #haut
        elif self.direction == self.subDivision:
            if map[self.posY][self.posX-self.subDivision]!= '0':
                self.choisitDeplacement()
            else:
                self.posX -=self.mouvement
            
        self.parent.posMatX = self.posX
        self.parent.posMatY = self.posY
