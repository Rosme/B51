# -*- coding: ISO-8859-1 -*-

#Coucou, ben c'est fais par Gab donc si vous avez de questions venez me voir
#en passant quand le commentaire commence par // sa une notes pour moi pour penser a améliorer certain aspect du code
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
        # ajouter Si y a un player dans son range qu'il défend il attaque 
               
          
    
    
    def calculRandom(self):
        return random.randint(0, 7)
        
    def deplacement(self,map):
    #    0self.subDivision2
    #    3#4
    #    567
    
        self.mouvement = 4
    
        #gauche Bas
        if self.direction == 5:
            if (map[self.posX-self.subDivision][self.posY] == '1' and map[self.posX][self.posY+self.subDivision] == '1') or map[self.posX-self.subDivision][self.posY+self.subDivision] == '1':
                self.choisitDeplacement()
            else:
                self.posX -= self.mouvement
                self.posY += self.mouvement   
         
        #gauche haut
        elif self.direction == 0:
            if (map[self.posX-self.subDivision][self.posY] == '1' and map[self.posX][self.posY-self.subDivision] == '1') or map[self.posX-self.subDivision][self.posY-self.subDivision] == '1':
                self.choisitDeplacement()
            else:
                self.posX -= self.mouvement
                self.posY -= self.mouvement

        # droite Haut         
        elif self.direction == 2:
            if (map[self.posX+self.subDivision][self.posY] == '1' and map[self.posX][self.posY-self.subDivision] == '1') or map[self.posX+self.subDivision][self.posY-self.subDivision] == '1':
                self.choisitDeplacement()
            else:
                self.posX +=self.mouvement
                self.posY -=self.mouvement
         
        #droite bas
        elif self.direction == 7:
            if (map[self.posX+self.subDivision][self.posY] == '1' and map[self.posX][self.posY+self.subDivision] == '1') or map[self.posX+self.subDivision][self.posY+self.subDivision] == '1':
                self.choisitDeplacement()
            else:
                self.posX +=self.mouvement
                self.posY +=self.mouvement
           
        # droite 
        elif self.direction == 4:
            if map[self.posX+self.subDivision][self.posY]=='1':
                self.choisitDeplacement()
            else:
                self.posX += self.mouvement
        
        #bas
        elif self.direction == 6:
            if map[self.posX][self.posY+self.subDivision] == '1':
                self.choisitDeplacement()
            else:
                self.posY += self.mouvement
        
        # gauche 
        elif self.direction == 3:
            if map[self.posX-self.subDivision][self.posY] == '1':
                self.choisitDeplacement()
            else:
                self.posX -=self.mouvement
            
        #haut
        elif self.direction == self.subDivision:
            if map[self.posX][self.posY-self.subDivision]== '1':
                self.choisitDeplacement()
            else:
                self.posY -=self.mouvement
            
        self.parent.posMatX = self.posX
        self.parent.posMatY = self.posY
        
   