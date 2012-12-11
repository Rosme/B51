# -*- coding: ISO-8859-1 -*-
import math

class Balle():
    def __init__(self, perso, finX, finY, force):
        self.posMatX = perso.posMatX #sera initialisé au moment de la création dans le controleur.
        self.posMatY = perso.posMatY #sera initialisé au moment de la création dans le controleur.
        #finX += self.posMapX-520
        #finY += self.posMapY-290
        self.force = force
        self.radius = 5
        self.velocite = 10
        self.distanceMax = 10 #300
        self.distanceParcouru = 0
        #calcul la distance entre les deux points. Départ et fin.
        try:
            #self.entreDeux = math.sqrt(abs((finX-self.posMapX)**2)+abs((finY-self.posMapY)**2))
            #calcul la vitesse qu'elle va parcourir en X et Y avec un maximum de self.velocite de vitessse.
            self.veloX = 1#((self.velocite * (finX-self.posMapX))/self.entreDeux)
            self.veloY = 1#((self.velocite * (finY-self.posMapY))/self.entreDeux)
            self.valide = True
        except ZeroDivisionError:
            self.valide = False
        
    def bouge(self, perso):
        self.distanceParcouru += math.sqrt(abs((self.veloX)**2)+abs((self.veloY)**2))
        self.posMatX += self.veloX
        self.posMatY += self.veloY
        
    def collision(self, liste, map):
        pass
        '''
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
                if map[self.posMatY][self.posMatX]=='1':    
                    return True
            except IndexError:
                return True
        else:
            return True
        
        return False
        '''
    def obtenirLimite(self):
        pass
        #return [self.posMapX, self.posMapY, self.posMapX+self.radius, self.posMapY+self.radius]
    