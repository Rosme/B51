import math

class Balle():
    def __init__(self, departX, departY, finX, finY):
        self.x = departX
        self.y = departY
        self.velocite = 5
        self.entreDeux = math.sqrt((finX-departX)^2+(finY-departY)^2)
        self.veloX = (self.velocite * finX - departX)/self.entreDeux
        self.veloY = (self.velocite * finX - departX)/self.entreDeux
        
    def bouge(self):
        self.x += self.veloX
        self.y += self.veloY
        
    def getBound(self):
        x = self.x+5
        y = self.y+5
        rayon = 5
        return x, y, rayon
    
    