# -*- coding: ISO-8859-1 -*-
import pickle
import Item
        
class Personnage():
    def __init__(self, id):
        '''Caractéristiques uniques'''
        self.id = id
        
    def nouveauPersonnage(self, nom, poidsLimite):
        self.nom = nom
        self.x = 0
        self.y = 0
        self.inventaire = Item.Inventaire(poidsLimite)
        self.inventaire.ajouterItem(Item.Divers(3, 1, "Seringue", "Une seringue qui soigne de 100 de vies", 100))
        self.inventaire.ajouterItem(Item.Divers(3, 1, "Seringue", "Une seringue qui soigne de 100 de vies", 100))
        self.inventaire.ajouterItem(Item.Divers(3, 1, "Seringue", "Une seringue qui soigne de 100 de vies", 100))
    
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
        for i in self.inventaire.items:
            if i.id == 3:
                if self.vie + i.qualite < 350:
                    i.utiliser(self)
                else:
                    self.vie = 350 - i.qualite
                    i.utiliser(self)
                    
                self.inventaire.retirerItem(i)
                break
        
class Humain(Personnage):
    def __init__(self, parent, id):
        Personnage.__init__(self, id)
        
    def nouveauPersonnage(self, nom):
        self.race = "Humain"
        self.vie = 300
        self.attaque = 5
        self.defense = 5
        self.poidsLimite = 20  
        Personnage.nouveauPersonnage(self, nom, self.poidsLimite)
    
class Wohawk(Personnage):
    def __init__(self, parent, id):
        Personnage.__init__(self, id)
        
    def nouveauPersonnage(self, nom):
        self.race = "Wohawk"
        self.vie = 300
        self.attaque = 5
        self.defense = 5
        self.poidsLimite = 20 
        Personnage.nouveauPersonnage(self, nom, self.poidsLimite)     
    
class Zeborf(Personnage):
    def __init__(self, parent, id):
        Personnage.__init__(self, id)
        
    def nouveauPersonnage(self, nom):
        self.race = "Zeborf"
        self.vie = 300
        self.attaque = 5
        self.defense = 5
        self.poidsLimite = 20 
        Personnage.nouveauPersonnage(self, nom, self.poidsLimite)     
    
class Irki(Personnage):
    def __init__(self, parent, id):
        Personnage.__init__(self, id)
        
    def nouveauPersonnage(self, nom):
        self.race = "Irki"
        self.vie = 300
        self.attaque = 5
        self.defense = 5
        self.poidsLimite = 20   
        Personnage.nouveauPersonnage(self, nom, self.poidsLimite)   
    
class Popamu(Personnage):
    def __init__(self, parent, id):
        Personnage.__init__(self, id)
        
    def nouveauPersonnage(self, nom):
        self.race = "Popamu"
        self.vie = 300
        self.attaque = 5
        self.defense = 5 
        self.poidsLimite = 20 
        Personnage.nouveauPersonnage(self, nom, self.poidsLimite)  
        
class Atarix(Personnage):
    def __init__(self, parent, id):
        Personnage.__init__(self, id)
        
    def nouveauPersonnage(self, nom):
        self.race = "Atarix"
        self.vie = 300
        self.attaque = 5
        self.defense = 5
        self.poidsLimite = 20  
        Personnage.nouveauPersonnage(self, nom, self.poidsLimite)     
    
    
    
    