# -*- coding: ISO-8859-1 -*-

class Objet():
    def __init__(self, matX, matY, mapX, mapY):
        self.posMatX = matX
        self.posMatY = matY
        self.posMapX = mapX
        self.posMapY = mapY
        self.aTerre = True

class Sac(Objet):
    def __init__(self, matX, matY, mapX, mapY):
        Objet.__init__(self, matX, matY, mapX, mapY)
        self.items = []

    '''
    Va retirer l'item de la liste
    S'il ne se trouve pas dans la liste, rien ne se passe
    Sinon la fonction va l'enlever du coffre
    '''
    def retirerItem(self, item):
        if item in self.items:
            self.items.remove(item)

class Coffre(Objet):
    def __init__(self, matX, matY, mapX, mapY):
        Objet.__init__(self, matX, matY, mapX, mapY)
        self.items = []
        self.ouvert = False

    def ouvrir(self, perso):
        if self.aTerre:
            if not self.ouvert:
                limitePerso = perso.obtenirLimite()
                limiteCoffre = self.obtenirLimite()
                j=0
                while j < 4:
                    if limiteCoffre[j] > limitePerso[0] and limiteCoffre[j] < limitePerso[2]:
                        k=1
                        while k < 4:
                            if limiteCoffre[k] > limitePerso[1] and limiteCoffre[k] < limitePerso[3]:
                                self.ouvert = True
                                return True
                            k+=2
                    j+=2
        
        self.ouvert = False
        return False
    
    '''
    Rajout d'un item au coffre
    '''
    def ajouterItem(self, item):
        self.items.append(item)

    '''
    Va retirer l'item de la liste
    S'il ne se trouve pas dans la liste, rien ne se passe
    Sinon la fonction va l'enlever du coffre
    '''
    def retirerItem(self, item):
        if item in self.items:
            self.items.remove(item)
                 
    def obtenirLimite(self):
        return [self.posMapX, self.posMapY, self.posMapX+60, self.posMapY+60]
       
class Roche(Objet):
    def __init__(self, matX, matY, mapX, mapY, map):
        Objet.__init__(self, matX, matY, mapX, mapY)
        self.depose(map)
        
    def bouge(self, perso):
        self.aTerre = False
        self.posMatX = perso.posMatX
        self.posMatY = perso.posMatY
        self.posMapX = perso.posMapX
        self.posMapY = perso.posMapY
        
    def depose(self, map):
        self.aTerre = True
        if map[self.posMatY][self.posMatX] == 'a':
            #appel la méthode de la switch sens unique
            pass
        elif map[self.posMatY][self.posMatX] == 's':
            #appel la méthode de la switch double sens
            pass
        
    def obtenirLimite(self):
        return [self.posMapX, self.posMapY, self.posMapX+20, self.posMapY+20]