# -*- coding: ISO-8859-1 -*-

import Netdata as nd

class Objet():
    def __init__(self, parent, matX, matY, padGauche, padHaut, padDroit, padBas, nomMap):
        self.parent = parent
        self.nomMap = nomMap
        self.posMatX = matX*self.parent.subDivision
        self.posMatY = matY*self.parent.subDivision
        self.padHaut = padHaut*self.parent.subDivision
        self.padBas = padBas*self.parent.subDivision
        self.padGauche = padGauche*self.parent.subDivision
        self.padDroit = padDroit*self.parent.subDivision
        self.aTerre = True
        
    def obtenirLimite(self):
        return [self.posMatX+self.padGauche+self.padHaut, self.posMatY+self.padGauche+self.padHaut, self.posMatX+(self.parent.subDivision-1)+self.padDroit+self.padBas, self.posMatY+(self.parent.subDivision-1)+self.padDroit+self.padBas]

class Sac(Objet):
    def __init__(self, parent, matX, matY, nomMap):
        Objet.__init__(self, parent, matX, matY, -1, -1, 1, 1, nomMap)# -1, -1, -2, -2 (subDivision à 4)
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
    def __init__(self, parent, matX, matY, nomMap):
        Objet.__init__(self, parent, matX, matY, -2, -2, 2, 2, nomMap)
        self.items = []
        self.ouvert = False

    def ouvrir(self, perso):
        if self.aTerre:
            if not self.ouvert:
                limitePerso = perso.obtenirLimite()
                limiteCoffre = self.obtenirLimite()
                j=0
                while j < 4:
                    if limiteCoffre[j] >= limitePerso[0] and limiteCoffre[j] <= limitePerso[2]:
                        valide = True
                    elif j == 0:
                        if limiteCoffre[j] <= limitePerso[0] and limiteCoffre[j+2] >= limitePerso[2]:
                            valide = True
                        else:
                            valide = False
                    else:
                        valide = False
                    if valide:
                        k=1
                        while k < 4:
                            if limiteCoffre[k] >= limitePerso[1] and limiteCoffre[k] <= limitePerso[3]:
                                valide = True
                            elif k == 1:
                                if limiteCoffre[k] <= limitePerso[1] and limiteCoffre[k+2] >= limitePerso[3]:
                                    valide = True
                                else:
                                    valide = False
                            else:
                                valide = False
                            if valide:
                                print("ouvre coffre")
                                self.ouvert = True
                                return True
                            k+=2
                    j+=2
        
        print("ferme coffre")
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
    def __init__(self, parent, matX, matY, nomMap):
        Objet.__init__(self, parent, matX, matY, -1, -1, 2, 2, nomMap)# -1, -1, -2, -2 (subDivision à 4)
        self.depose()
        
    def prendre(self, perso):
        if self.aTerre:
            limitePerso = perso.obtenirLimite()
            limiteObjet = self.obtenirLimite()
            j=0
            while j < 4:
                if limiteObjet[j] >= limitePerso[0] and limiteObjet[j] <= limitePerso[2]:
                    valide = True
                elif j == 0:
                    if limiteObjet[j] >= limitePerso[0] and limiteObjet[j+2] <= limitePerso[2]:
                        valide = True
                    else:
                        valide = False
                else:
                    valide = False
                if valide:
                    k=1
                    while k < 4:
                        if limiteObjet[k] >= limitePerso[1] and limiteObjet[k] <= limitePerso[3]:
                            valide = True
                        elif k == 1:
                            if limiteObjet[k] >= limitePerso[1] and limiteObjet[k+2] <= limitePerso[3]:
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
        
        
    def depose(self):
        self.aTerre = True
        for i in self.parent.listeInterrupteur:
            if not self.prendre(i):
                self.aTerre = True
                i.aTerre = True

class Interrupteur(Objet):
    def __init__(self, parent, matX, matY, unique, aTerre, nomMap):
        Objet.__init__(self, parent, matX, matY, -2, -2, 2, 2, nomMap)
        self.active = False
        self.aTerre = aTerre
        self.usageUnique = unique
        self.out = True
    
    def collision(self, perso):
        if not self.aTerre:
            limitePerso = perso.obtenirLimite()
            limiteObjet = self.obtenirLimite()
            j=0
            while j < 4:
                if limiteObjet[j] >= limitePerso[0] and limiteObjet[j] <= limitePerso[2]:
                    valide = True
                elif j == 0:
                    if limiteObjet[j] <= limitePerso[0] and limiteObjet[j+2] >= limitePerso[2]:
                        valide = True
                    else:
                        valide = False
                else:
                    valide = False
                if valide:
                    k=1
                    while k < 4:
                        if limiteObjet[k] >= limitePerso[1] and limiteObjet[k] <= limitePerso[3]:
                            valide = True
                        elif k == 1:
                            if limiteObjet[k] <= limitePerso[1] and limiteObjet[k+2] >= limitePerso[3]:
                                valide = True
                            else:
                                valide = False
                        else:
                            valide = False
                        if valide:
                            if self.usageUnique:
                                self.aTerre = True
                            self.active = True
                            return True
                        k+=2
                j+=2
                
            self.active = False
            return False
    
    def activer(self):
        if self.parent.ownPlayer.nomMap == "F_E1S1":
            map = self.parent.getSalleByName("F_E1S1")
            if self.posMatX == 26*self.parent.subDivision and self.posMatY == 21*self.parent.subDivision:
                if self.active:
                    self.ouvrePorte(26, 14, map, "0", False)
                    if self.out:
                        self.out = not self.out
                        self.parent.carte.s.dictMap["F_E1S1"] = map
                        return True
                else:
                    self.ouvrePorte(26, 14, map, "2", False)
                    if not self.out:
                        self.out = not self.out
                        self.parent.carte.s.dictMap["F_E1S1"] = map
                        return True
             
            self.parent.carte.s.dictMap["F_E1S1"] = map
            return False
        
        if self.parent.ownPlayer.nomMap == "R_E1S1":
            if self.posMatX == 1*self.parent.subDivision and self.posMatY == 9*self.parent.subDivision:
                if self.active:
                    for i in self.parent.listeDeclencheur:
                        if i.nomMap == "R_E1S1":
                            if i.posMatX == 22*self.parent.subDivision and i.posMatY == 10*self.parent.subDivision:
                                i.aTerre = True
                                return False
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
    def __init__(self, parent, matX, matY, nomMap):
        Objet.__init__(self, parent, matX, matY, 0, 0, 0, 4, nomMap)
        self.active = False
        self.aTerre = False
        self.premierDeclenchement = False
        
    def collision(self, perso):
        if not self.aTerre:
            limitePerso = perso.obtenirLimite()
            limiteObjet = self.obtenirLimite()
            j=0
            while j < 4:
                if limiteObjet[j] >= limitePerso[0] and limiteObjet[j] <= limitePerso[2]:
                    valide = True
                elif j == 0:
                    if limiteObjet[j] <= limitePerso[0] and limiteObjet[j+2] >= limitePerso[2]:
                        valide = True
                    else:
                        valide = False
                else:
                    valide = False
                if valide:
                    k=1
                    while k < 4:
                        if limiteObjet[k] >= limitePerso[1] and limiteObjet[k] <= limitePerso[3]:
                            valide = True
                        elif k == 1:
                            if limiteObjet[k] <= limitePerso[1] and limiteObjet[k+2] >= limitePerso[3]:
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
        if self.parent.ownPlayer.nomMap == "R_E1S1":
            if self.posMatX == 22*self.parent.subDivision and self.posMatY == 10*self.parent.subDivision:
                if self.active:
                    #Téléporte le joueur à la case 18
                    self.parent.ownPlayer.posMatX = 18*self.parent.subDivision
                    
                    #Si elle n'a jamais été déclenchée, on fait apparaitre une switch et rafraichie la map
                    if not self.premierDeclenchement:
                        
                        for i in self.parent.listeInterrupteur:
                            
                            if i.nomMap == "R_E1S1":
                                
                                if i.posMatX == 1*self.parent.subDivision and i.posMatY == 9*self.parent.subDivision:
                                    i.aTerre = False
                                    self.placeObjet(10,1,self.parent.carte.s.dictMap["R_E1S1"],'w')
                                    self.premierDeclenchement = True
                                    return True
                            
            return False
        
    def placeObjet(self, ligne, colonne, map, car):
        ligne *=self.parent.subDivision
        colonne *=self.parent.subDivision
        for j in range(self.parent.subDivision):
            temp=[]
            tempLigne = map.pop(ligne+j)
            i = 0
            while i < colonne:
                temp.append(tempLigne[i])
                i+=1
                
            for k in range(self.parent.subDivision):
                temp.append(car)
                i+=1
        
            while i < len(tempLigne):
                temp.append(tempLigne[i])
                i+=1    
            
            map.insert(ligne, temp)
        
class Levier(Objet):
    def __init__(self, parent, matX, matY, force, energie, contreForce, nomMap):
        Objet.__init__(self, parent, matX, matY, -1, -1, 1, 1, nomMap)
        self.force = force
        self.max_energie = energie
        self.energie = energie
        self.contreForce = contreForce
        self.active = False
        self.player = None
        self.hasBeenActivated = False
        
    def collision(self, perso):
        
        if not self.active:
            limitePerso = perso.obtenirLimite()
            limiteObjet = self.obtenirLimite()
            j=0
            while j < 4:
                if limiteObjet[j] >= limitePerso[0] and limiteObjet[j] <= limitePerso[2]:
                    valide = True
                elif j == 0:
                    if limiteObjet[j] <= limitePerso[0] and limiteObjet[j+2] >= limitePerso[2]:
                        valide = True
                    else:
                        valide = False
                else:
                    valide = False
                if valide:
                    k=1
                    while k < 4:
                        if limiteObjet[k] >= limitePerso[1] and limiteObjet[k] <= limitePerso[3]:
                            valide = True
                        elif k == 1:
                            if limiteObjet[k] <= limitePerso[1] and limiteObjet[k+2] >= limitePerso[3]:
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
        if self.player.nomMap == "F_E1S1":
            map = self.parent.getSalleByName("F_E1S1")
            if self.posMatX == 17*self.parent.subDivision and self.posMatY == 16*self.parent.subDivision:
                if self.active:
                    self.ouvrePorte(16, 14, map, "0", False)
                    self.parent.carte.s.dictMap["F_E1S1"] = map
                    self.hasBeenActivated = True
                    return True
                return False
            
        if self.player.nomMap == "F_E1S3":
            map = self.parent.carte.s.dictMap["F_E1S3"]
            if self.posMatX == 16*self.parent.subDivision and self.posMatY == 2*self.parent.subDivision:
                if self.active:
                    self.ouvrePorte(1, 14, map, "m", False)
                    self.parent.carte.s.dictMap["F_E1S3"] = map
                    self.hasBeenActivated = True
                    return True
                return False
               
            self.parent.carte.s.dictMap["F_E1S3"] = map
        
        if self.player.nomMap == "F_E1S5":
            map = self.parent.getSalleByName("F_E1S5")
            if self.posMatX == 1*self.parent.subDivision and self.posMatY == 24*self.parent.subDivision:
                if self.active:
                    self.ouvrePorte(13, 28, map, "0", False)
                    self.parent.carte.s.dictMap["F_E1S5"]= map
                    self.hasBeenActivated = True
                    return True
                return False
            
        if self.player.nomMap == "F_E2S3":
            map = self.parent.getSalleByName("F_E2S3")
            if self.posMatX == 42*self.parent.subDivision and self.posMatY == 35*self.parent.subDivision:
                if self.active:
                    self.ouvrePorte(17, 21, map, "0", False)
                    self.parent.carte.s.dictMap["F_E2S3"] = map
                    self.hasBeenActivated = True
                    return True
                return False
        
    def ouvrePorte(self, ligne, colonne, map, car, simple):
        ligne *=self.parent.subDivision
        colonne *=self.parent.subDivision
        for j in range(self.parent.subDivision):
            temp=[]
            tempLigne = map.pop(ligne+j)
            i = 0
            while i < colonne:
                temp.append(tempLigne[i])
                i+=1
            for k in range(self.parent.subDivision):
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
            #self.active = True
            return True
        else:
            self.energie-=self.force
            return False
            
    def recharge(self):
        if self.energie + self.contreForce >= self.max_energie:
            self.energie = self.max_energie
        else:
            self.energie+=self.contreForce     
    
    def activatedBy(self, player):
        self.player = player
        self.active = True
        
        
        
        