import Personnage

class Race():
    def __init__(self, race, vie, attaque, defense, poidsLimite):
        self.race = race
        self.vie = vie
        self.attaque = attaque
        self.defense = defense
        self.poidsLimite = poidsLimite
        self.description = ""
        
    def info(self):
        return self.race, self.vie, self.attaque, self.defense, self.poidsLimite, self.description
        
class Humain(Race):
    def __init__(self):
        Race.__init__(self, "Humain", 300, 5, 5, 20)
        self.description = "Ceci est un humain"
    
class Wohawk(Race):
    def __init__(self):
        Race.__init__(self, "Wohawk", 300, 5, 5, 20) 
        self.description = "Ceci est un Wohawk"
    
class Zeborf(Race):
    def __init__(self):
        Race.__init__(self, "Zeborf", 300, 5, 5, 20)  
        self.description = "Ceci est un Zeborf"
    
class Irki(Race):
    def __init__(self):
        Race.__init__(self, "Irki", 300, 5, 5, 20)
        self.description = "Ceci est un Irki"
    
class Popamu(Race):
    def __init__(self):
        Race.__init__(self, "Popamu", 300, 5, 5, 20)
        self.description = "Ceci est un Popamu"
        
class Atarix(Race):
    def __init__(self):
        Race.__init__(self, "Atarix", 300, 5, 5, 20) 
        self.description = "Ceci est un Atarix"
    