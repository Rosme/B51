import math

class Balle():
    def __init__(self, departX, departY, finX, finY, force):
        self.x = departX
        self.y = departY
        self.force = force
        self.velocite = 5
        self.entreDeux = math.sqrt((finX-departX)^2+(finY-departY)^2)
        self.veloX = (self.velocite * finX - departX)/self.entreDeux
        self.veloY = (self.velocite * finY - departY)/self.entreDeux
        
    def bouge(self):
        self.x += self.veloX
        self.y += self.veloY
        
    def collision(self, listePersonnage):
        for i in listePersonnage:
            rectangle = i.obtenirLimite()
            if self.x > rectangle[0] and self.x < rectangle[2]:
                if self.y > rectangle[1] and self.y < rectangle[3]:
                    i.touche(self.force)
                    return True
                
        return False
        
    def obtenirLimite(self):
        x = self.x+5
        y = self.y+5
        rayon = 5
        return x, y, rayon
    