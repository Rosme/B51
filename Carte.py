class Carte():
    def __init__(self):
        self.nomMap = "Map/MainRoom.mp"
        self.s = Salle()
        self.s.chargeCarte(self.nomMap)
    
class Salle():
    def __init__(self):
        self.salle = list()
    
    def chargeCarte(self, nomMap):
        f = open(str(nomMap), 'r')
        self.salle = list()
        
        f.readline()
        f.readline()
        f.readline()
        ligne = list()
        ligne = f.read()
        
        for i in ligne.splitlines():
            i.split('\n')
            self.salle.append(i)
    