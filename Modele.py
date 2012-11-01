# -*- coding: ISO-8859-1 -*-

class Jeu():
    def __init__(self, parent):
        self.parent = parent
        self.nbId = 0
        self.joueur = ""
        
    def chargerJoueur(self):
        self.joueur = Joueur(self, id = self.nbId, nom = "Marco", nouveau = False)
        self.nbId += 1
        
    def sauvegardeJoueur(self):
        self.joueur.sauvegardeJoueur()
        
class Joueur():
    def __init__(self, parent, id, nom, nouveau = True):
        '''Caractéristiques uniques'''
        self.id = id
        self.nom = nom
        
        if nouveau == True:
            self.nouveauJoueur()
        else:
            self.chargerJoueur() 
        
    def nouveauJoueur(self):
        self.x = 0
        self.y = 0
        '''Attributs'''
        self.niveau = 1
        self.vie = 500
        self.attaque = 5
        self.defense = 0
        '''Items'''
        self.nbCle = 0
        self.nbBandage = 1
        self.grenade = 0
        self.artefact = 0
        self.couteau = True
        self.pistolet = False
        self.mitraillette = False
        self.fusilAPompe = False
    
    def chargerJoueur(self):
        nomFichier = self.nom + '.txt'
        f = open(nomFichier, 'r')
        
        texte = f.read()
        
        for i in texte.splitlines():
            i = i.split('=')
            
            if i[1] == "False":
                i[1] = ""
            
            if i[0] == "x":
                self.x = i[1]
                self.x = int(self.x)
                print(self.x)
            elif i[0] == "y":
                self.y = i[1]
                self.y = int(self.y)
                print(self.y)
            elif i[0] == "niveau":
                self.niveau = i[1]
                self.niveau = int(self.niveau)
                print(self.niveau)
            elif i[0] == "vie":
                self.vie = i[1]
                self.vie = int(self.vie)
                print(self.vie)
            elif i[0] == "attaque":
                self.attaque = i[1]
                self.attaque = int(self.attaque)
                print(self.attaque)
            elif i[0] == "defense":
                self.defense = i[1]
                self.defense = int(self.defense)
                print(self.defense)
            elif i[0] == "nbCle":
                self.nbCle = i[1]
                self.nbCle = int(self.nbCle)
                print(self.nbCle)
            elif i[0] == "nbBandage":
                self.nbBandage = i[1]
                self.nbBandage = int(self.nbBandage)
                print(self.nbBandage)
            elif i[0] == "grenade":
                self.grenade = i[1]
                self.grenade = int(self.grenade)
                print(self.grenade)
            elif i[0] == "artefact":
                self.artefact = i[1]
                self.artefact = int(self.artefact)
                print(self.artefact)
            elif i[0] == "couteau":
                self.couteau = i[1]
                self.couteau = bool(self.couteau)
                print(self.couteau)
            elif i[0] == "pistolet":
                self.pistolet = i[1]
                self.pistolet = bool(self.pistolet)
                print(self.pistolet)
            elif i[0] == "mitraillette":
                self.mitraillette = i[1]
                self.mitraillette = bool(self.mitraillette)
                print(self.mitraillette)
            elif i[0] == "fusilAPompe":
                self.fusilAPompe = i[1]
                self.fusilAPompe = bool(self.fusilAPompe)  
                print(self.fusilAPompe) 
        
        f.close()
        
    def sauvegardeJoueur(self):
        nomFichier = self.nom + '.txt'
        f = open(nomFichier, 'w')
        
        f.write("x=" + str(self.x) + '\n')
        f.write("y=" + str(self.y) + '\n')
        f.write("niveau=" + str(self.niveau) + '\n')
        f.write("vie=" + str(self.vie) + '\n')
        f.write("attaque=" + str(self.attaque) + '\n')
        f.write("defense=" + str(self.defense) + '\n')
        f.write("nbCle=" + str(self.nbCle) + '\n')
        f.write("nbBandage=" + str(self.nbBandage) + '\n')
        f.write("grenade=" + str(self.grenade) + '\n')
        f.write("artefact=" + str(self.artefact) + '\n')
        f.write("couteau=" + str(self.couteau) + '\n')
        f.write("pistolet=" + str(self.pistolet) + '\n')
        f.write("mitraillette=" + str(self.mitraillette) + '\n')
        f.write("fusilAPompe=" + str(self.fusilAPompe))
        
        f.close()
    
    def autoSoin(self):
        if self.nbBandage > 0:
            if self.vie + 200 < 500:
                self.vie += 200
            else:
                self.vie = 500
                
    def ouvrirObjet(self):
        if self.nbCle > 0:
            return True
        else:
            return False
        
        
        
        