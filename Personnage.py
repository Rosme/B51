# -*- coding: ISO-8859-1 -*-
import pickle
import Item
        
class Personnage():
    def __init__(self, id):
        '''Caractéristiques uniques'''
        self.id = id
        
    def nouveauPersonnage(self, nom):
        self.nom = nom
        self.x = 0
        self.y = 0
        self.inventaire = Item.Inventaire(50)
        self.inventaire.ajouterItem(Item.Divers(0, 1, "Seringue", "Une seringue qui soigne de 100 de vies", 100))
    
    def chargerPersonnage(self, nom):
        nomFichier = nom + '.plr'
        with open(nomFichier,'rb') as fichier:
            joueur = pickle.Unpickler(fichier)
            self = joueur.load()
        return self
        
    def sauvegardePersonnage(self):
        nomFichier = self.nom + '.plr'
        with open(nomFichier,'wb') as fichier:
            save = pickle.Pickler(fichier)
            save.dump(self)
    
    def autoSoin(self):
        if self.nbSeringue > 0:
            if self.vie + 200 < 500:
                self.vie += 200
            else:
                self.vie = 500
                
    def ouvrirObjet(self):
        if self.nbCle > 0:
            return True
        else:
            return False
        
class Humain(Personnage):
    def __init__(self, parent, id):
        Personnage.__init__(self, id)
        
    def nouveauPersonnage(self, nom):
        Personnage.nouveauPersonnage(self, nom)
        self.race = "Humain"
        self.vie = 275
        self.attaque = 5
        self.defense = 5
    
class Wohawk(Personnage):
    def __init__(self, parent, id):
        Personnage.__init__(self, id)
        
    def nouveauPersonnage(self, nom):
        Personnage.nouveauPersonnage(self, nom)
        self.race = "Wohawk"
        self.vie = 200
        self.attaque = 7
        self.defense = 3    
    
class Zeborf(Personnage):
    def __init__(self, parent, id):
        Personnage.__init__(self, id)
        
    def nouveauPersonnage(self, nom):
        Personnage.nouveauPersonnage(self, nom)
        self.race = "Zeborf"
        self.vie = 370
        self.attaque = 3
        self.defense = 7    
    
    
    
    
    
    
    
    