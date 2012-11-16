# -*- coding: ISO-8859-1 -*-
import math

class Balle():
    def __init__(self, perso, finX, finY, force):
        self.posMatX = 0 #sera initialisé au moment de la création dans le controleur.
        self.posMatY = 0 #sera initialisé au moment de la création dans le controleur.
        self.posMapX = perso.posMapX
        self.posMapY = perso.posMapY-30
        self.posEcranX = perso.posEcranX + (self.posMapX - perso.posMapX)
        self.posEcranY = perso.posEcranY + (self.posMapY - perso.posMapY)
        self.force = force
        self.radius = 5
        self.velocite = 10
        self.distanceMax = 300
        self.distanceParcouru = 0
        #calcul la distance entre les deux points. Départ et fin.
        self.entreDeux = math.sqrt(abs((finX-self.posEcranX)**2)+abs((finY-self.posEcranY)**2))
        #calcul la vitesse qu'elle va parcourir en X et Y avec un maximum de self.velocite de vitessse.
        self.veloX = ((self.velocite * (finX - self.posEcranX))/self.entreDeux)
        self.veloY = ((self.velocite * (finY - self.posEcranY))/self.entreDeux)
        
    def bouge(self, perso):
        self.distanceParcouru += math.sqrt(abs((self.veloX)**2)+abs((self.veloY)**2))
        self.posMapX += self.veloX
        self.posMapY += self.veloY
        self.posEcranX = perso.posEcranX + (self.posMapX - perso.posMapX)
        self.posEcranY = perso.posEcranY + (self.posMapY - perso.posMapY)
        
        
    def collision(self, liste, map):
        if self.distanceParcouru < self.distanceMax:
            for i in liste:
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
            try:
                if map[self.posMatX][self.posMatY]=='1':    
                    return True
            except IndexError:
                return True
        else:
            return True
        
        return False
        
    def obtenirLimite(self):
        return [self.posMapX, self.posMapY, self.posMapX+self.radius, self.posMapY+self.radius]
    