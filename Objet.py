# -*- coding: ISO-8859-1 -*-

class Objet():
    def __init__(self, parent, matX, matY, mapX, mapY, largeur, hauteur, nomMap):
        self.parent = parent
        self.nomMap = nomMap
        self.posMatX = matX
        self.posMatY = matY
        self.posMapX = mapX
        self.posMapY = mapY
        self.largeur = largeur
        self.hauteur = hauteur
        self.aTerre = True
        
    def obtenirLimite(self):
        return [self.posMapX, self.posMapY, self.posMapX+self.largeur, self.posMapY+self.hauteur]

class Sac(Objet):
    def __init__(self, parent, matX, matY, mapX, mapY, nomMap):
        Objet.__init__(self, parent, matX, matY, mapX, mapY, 20, 20, nomMap)
        self.items = []

    '''
    Va retirer l'item de la liste
    S'il ne se trouve pas dans la liste, rien ne se passe
    Sinon la fonction va l'enlever du coffre
    '''
    def retirerItem(self, item):
        if item in self.items:
            self.items.remove(item)
        
        if not self.items:
            self.aTerre = False

class Coffre(Objet):
    def __init__(self, parent, matX, matY, mapX, mapY, nomMap):
        Objet.__init__(self, parent, matX, matY, mapX, mapY, 80, 80, nomMap)
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
                        valide = True
                    elif j == 0:
                        if limiteCoffre[j] < limitePerso[0] and limiteCoffre[j+2] > limitePerso[2]:
                            valide = True
                        else:
                            valide = False
                    else:
                        valide = False
                    if valide:
                        k=1
                        while k < 4:
                            if limiteCoffre[k] > limitePerso[1] and limiteCoffre[k] < limitePerso[3]:
                                valide = True
                            elif k == 1:
                                if limiteCoffre[k] < limitePerso[1] and limiteCoffre[k+2] > limitePerso[3]:
                                    valide = True
                                else:
                                    valide = False
                            else:
                                valide = False
                            if valide:
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
       
class Roche(Objet):
    def __init__(self, parent, matX, matY, mapX, mapY, nomMap):
        Objet.__init__(self, parent, matX, matY, mapX, mapY, 20, 20, nomMap)
        self.depose()
        
    def prendre(self, perso):
        if self.aTerre:
            limitePerso = perso.obtenirLimite()
            limiteObjet = self.obtenirLimite()
            j=0
            while j < 4:
                if limiteObjet[j] > limitePerso[0] and limiteObjet[j] < limitePerso[2]:
                    valide = True
                elif j == 0:
                    if limiteObjet[j] > limitePerso[0] and limiteObjet[j+2] < limitePerso[2]:
                        valide = True
                    else:
                        valide = False
                else:
                    valide = False
                if valide:
                    k=1
                    while k < 4:
                        if limiteObjet[k] > limitePerso[1] and limiteObjet[k] < limitePerso[3]:
                            valide = True
                        elif k == 1:
                            if limiteObjet[k] > limitePerso[1] and limiteObjet[k+2] < limitePerso[3]:
                                valide = True
                            else:
                                valide = False
                        else:
                            valide = False
                        if valide:
                            self.aTerre = False
                            return False
                        k+=2
                j+=2
                
        self.aTerre = True
        return True
    
    def bouge(self, perso):
        if not self.aTerre:
            for i in self.parent.listeInterrupteur:
                self.aTerre = True
                if not self.prendre(i):
                    self.aTerre = False
                    i.aTerre = False
                else:
                    self.aTerre = False
        self.posMatX = perso.posMatX
        self.posMatY = perso.posMatY
        self.posMapX = perso.posMapX
        self.posMapY = perso.posMapY-32
        
    def depose(self):
        self.aTerre = True
        for i in self.parent.listeInterrupteur:
            if not self.prendre(i):
                self.aTerre = True
                i.aTerre = True
    
class Interrupteur(Objet):
    def __init__(self, parent, matX, matY, mapX, mapY, unique, nomMap):
        Objet.__init__(self, parent, matX, matY, mapX, mapY, 60, 60, nomMap)
        self.active = False
        self.aTerre = False
        self.usageUnique = unique
        self.out = True
    
    def collision(self, perso):
        if not self.aTerre:
            limitePerso = perso.obtenirLimite()
            limiteObjet = self.obtenirLimite()
            j=0
            while j < 4:
                if limiteObjet[j] > limitePerso[0] and limiteObjet[j] < limitePerso[2]:
                    valide = True
                elif j == 0:
                    if limiteObjet[j] < limitePerso[0] and limiteObjet[j+2] > limitePerso[2]:
                        valide = True
                    else:
                        valide = False
                else:
                    valide = False
                if valide:
                    k=1
                    while k < 4:
                        if limiteObjet[k] > limitePerso[1] and limiteObjet[k] < limitePerso[3]:
                            valide = True
                        elif k == 1:
                            if limiteObjet[k] < limitePerso[1] and limiteObjet[k+2] > limitePerso[3]:
                                valide = True
                            else:
                                valide = False
                        else:
                            valide = False
                        if valide:
                            self.active = True
                            return True
                        k+=2
                j+=2
            
            self.active = False
            return False
    
    def activer(self):
        if self.parent.joueur.nomMap == "F_E1S1":
            #25 par 14-15
            map = self.parent.carte.s.salle
            if self.posMatX == 22 and self.posMatY == 16:
                if self.active:
                    self.ouvrePorte(26, 14, map, "0", False)
                    if self.out:
                        self.out = not self.out
                        self.parent.carte.s.salle = map
                        return True
                else:
                    self.ouvrePorte(26, 14, map, "2", False)
                    if not self.out:
                        self.out = not self.out
                        self.parent.carte.s.salle = map
                        return True
             
            self.parent.carte.s.salle = map
            return False
            
    def ouvrePorte(self, ligne, colonne, map, car, simple):
        temp=[]
        tempLigne = map.pop(ligne)
        i = 0
        while i < colonne:
            temp.append(tempLigne[i])
            i+=1
        
        temp.append(car)
        i+=1
        if not simple:
            temp.append(car)
            i+=1
    
        while i < len(tempLigne):
            temp.append(tempLigne[i])
            i+=1    
        
        map.insert(ligne, temp)
    
class Declencheur(Objet):
    def __init__(self, parent, matX, matY, mapX, mapY, nomMap):
        Objet.__init__(self, parent, matX, matY, mapX, mapY, 20, 20, nomMap)
        self.active = False
        
    def collision(self, perso):
        if not self.aTerre:
            limitePerso = perso.obtenirLimite()
            limiteObjet = self.obtenirLimite()
            j=0
            while j < 4:
                if limiteObjet[j] > limitePerso[0] and limiteObjet[j] < limitePerso[2]:
                    valide = True
                elif j == 0:
                    if limiteObjet[j] < limitePerso[0] and limiteObjet[j+2] > limitePerso[2]:
                        valide = True
                    else:
                        valide = False
                else:
                    valide = False
                if valide:
                    k=1
                    while k < 4:
                        if limiteObjet[k] > limitePerso[1] and limiteObjet[k] < limitePerso[3]:
                            valide = True
                        elif k == 1:
                            if limiteObjet[k] < limitePerso[1] and limiteObjet[k+2] > limitePerso[3]:
                                valide = True
                            else:
                                valide = False
                        else:
                            valide = False
                        if valide:
                            self.active = True
                            return True
                        k+=2
                j+=2
                
            self.active = False
            return False
        
    def active(self, nomMap):
        if nomMap == "F_E1S1":
            pass
        
class Levier(Objet):
    def __init__(self, parent, matX, matY, mapX, mapY, force, energie, contreForce, nomMap):
        Objet.__init__(self, parent, matX, matY, mapX, mapY, 80,60, nomMap)
        self.force = force
        self.max_energie = energie
        self.energie = energie
        self.contreForce = contreForce
        self.active = False
        
    def collision(self, perso):
        if not self.active:
            limitePerso = perso.obtenirLimite()
            limiteObjet = self.obtenirLimite()
            j=0
            while j < 4:
                if limiteObjet[j] > limitePerso[0] and limiteObjet[j] < limitePerso[2]:
                    valide = True
                elif j == 0:
                    if limiteObjet[j] < limitePerso[0] and limiteObjet[j+2] > limitePerso[2]:
                        valide = True
                    else:
                        valide = False
                else:
                    valide = False
                if valide:
                    k=1
                    while k < 4:
                        if limiteObjet[k] > limitePerso[1] and limiteObjet[k] < limitePerso[3]:
                            valide = True
                        elif k == 1:
                            if limiteObjet[k] < limitePerso[1] and limiteObjet[k+2] > limitePerso[3]:
                                valide = True
                            else:
                                valide = False
                        else:
                            valide = False
                        if valide:
                            return True
                        k+=2
                j+=2
                
            return False
    
    def activer(self):
        if self.parent.carte.nomMap == "F_E1S1":
            #25 par 14-15
            map = self.parent.carte.s.salle
            if self.posMatX == 12 and self.posMatY == 19:
                if self.active:
                    self.ouvrePorte(15, 14, map, "0", False)
                else:
                    self.ouvrePorte(15, 14, map, "2", False)
                
            self.parent.carte.s.salle = map
            
    def ouvrePorte(self, ligne, colonne, map, car, simple):
        temp=[]
        tempLigne = map.pop(ligne)
        i = 0
        while i < colonne:
            temp.append(tempLigne[i])
            i+=1
        
        temp.append(car)
        i+=1
        if not simple:
            temp.append(car)
            i+=1
    
        while i < len(tempLigne):
            temp.append(tempLigne[i])
            i+=1    
        
        map.insert(ligne, temp)
    
    def tire(self):
        if self.energie - self.force <= 0:
            self.energie=0
            self.active = True
            print("La porte est ouverte")
            return True
        else:
            self.energie-=self.force
            return False
            
    def recharge(self):
        if self.energie + self.contreForce >= self.max_energie:
            self.energie = self.max_energie
        else:
            self.energie+=self.contreForce
        
        
class Portail(Objet):
    def __init__(self, parent, matX, matY, mapX, mapY):
        Objet.__init__(self, parent, matX, matY, mapX, mapY, 60, 60)       
        
        
        
        
        