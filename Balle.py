# -*- coding: ISO-8859-1 -*-
import math

class Balle():
    def __init__(self, perso, finX, finY, force):
        #self.posMatX = 11
        #self.posMatY = 11
        self.posMapX = perso.posMapX
        self.posMapY = perso.posMapY-30
        self.posEcranX = perso.posEcranX + (self.posMapX - perso.posMapX)
        self.posEcranY = perso.posEcranY + (self.posMapY - perso.posMapY)
        self.force = force
        self.radius = 5
        self.velocite = 15
        self.entreDeux = math.sqrt(abs((finX-self.posEcranX)**2)+abs((finY-self.posEcranY)**2))
        self.veloX = ((self.velocite * (finX - self.posEcranX))/self.entreDeux)
        self.veloY = ((self.velocite * (finY - self.posEcranY))/self.entreDeux)
        
    def bouge(self, perso):
        self.posMapX += self.veloX
        self.posMapY += self.veloY
        self.posEcranX = perso.posEcranX + (self.posMapX - perso.posMapX)
        self.posEcranY = perso.posEcranY + (self.posMapY - perso.posMapY)
        
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
        return [self.posMapX, self.posMapY, self.posMapX+self.radius, self.posMapY+self.radius]
    