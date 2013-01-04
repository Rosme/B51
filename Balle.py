# -*- coding: ISO-8859-1 -*-
import math

class Balle():
    def __init__(self, perso, finX, finY, force):
        self.posMatX = perso.posMatX #sera initialisé au moment de la création dans le controleur.
        self.posMatY = perso.posMatY #sera initialisé au moment de la création dans le controleur.
        self.force = force
        self.radius = 1
        self.velocite = 10
        self.distanceMax = 300
        self.distanceParcouru = 0
        #calcul la distance entre les deux points. Départ et fin.
        try:
            self.entreDeux = math.sqrt(abs((finX-self.posMatX)**2)+abs((finY-self.posMatY)**2))
            #calcul la vitesse qu'elle va parcourir en X et Y avec un maximum de self.velocite de vitessse.
            self.veloX = ((self.velocite * (finX-self.posMatX))/self.entreDeux)
            self.veloY = ((self.velocite * (finY-self.posMatY))/self.entreDeux)

            if self.veloX <= 0.49 and self.veloX >= 0:
                self.veloX = 0
            elif self.veloX > 0.49 and self.veloX <= 1:
                self.veloX = 1
            elif self.veloX >= -1 and self.veloX < -0.49:
                self.veloX = -1
            elif self.veloX >= -0.49 and self.veloX <= 0:
                self.veloX = 0
            
            if self.veloY <= 0.49 and self.veloY >= 0: #Entre 0 et 0.49
                self.veloY = 0
            elif self.veloY > 0.49 and self.veloY <= 1: #Entre 0.5 et 1
                self.veloY = 1
            elif self.veloY >= -1 and self.veloY < -0.49: #Entre -1 et -0.5
                self.veloY = -1
            elif self.veloY >= -0.49 and self.veloY <= 0: #Entre -0.49 et 0
                self.veloY = 0
                
            self.valide = True
        except ZeroDivisionError:
            self.valide = False
        
    def bouge(self, perso):
        self.distanceParcouru +=1 #math.sqrt(abs((self.veloX)**2)+abs((self.veloY)**2))
        self.posMatX += int(self.veloX)
        self.posMatY += int(self.veloY)
        
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
                if map[self.posMatY][self.posMatX]=='1':    
                    return True
            except IndexError:
                return True
        else:
            return True
        
        return False
        
    def obtenirLimite(self):
        return [self.posMatX-self.radius, self.posMatY-self.radius, self.posMatX+self.radius, self.posMatY+self.radius]
    