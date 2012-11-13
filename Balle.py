# -*- coding: ISO-8859-1 -*-
import math

class Balle():
    def __init__(self, departX, departY, finX, finY, force):
        #self.posMatX = 11
        #self.posMatY = 11
        self.posEcranX = 0
        self.posEcranY = 0
        self.posMapX = 672
        self.posMapY = 336
        self.x = departX
        self.y = departY
        self.force = force
        self.radius = 5
        self.velocite = 15
        self.entreDeux = math.sqrt(abs((finX-departX)**2)+abs((finY-departY)**2))
        self.veloX = ((self.velocite * (finX - departX))/self.entreDeux)
        self.veloY = ((self.velocite * (finY - departY))/self.entreDeux)
        
    def bouge(self):
        self.x += self.veloX
        self.y += self.veloY
        
    def collision(self, listePersonnage):
        for i in listePersonnage:
            rectPerso = i.obtenirLimite()
            rectBalle = self.obtenirLimite()
            j=0
            while j < 4:
                if rectBalle[j] > rectPerso[0] and rectBalle[j] < rectPerso[2]:
                    k=1
                    while k < 4:
                        if rectBalle[k] > rectPerso[1] and rectBalle[k] < rectPerso[3]:
                            i.touche(self.force)
                            return True
                        k+=2
                j+=2
                
        return False
        
    def obtenirLimite(self):
        return [self.x, self.y, self.x+self.radius, self.y+self.radius]
    