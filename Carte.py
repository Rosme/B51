class Carte():
    def __init__(self):
        self.nomMap = "Map/map1.mp"
        self.s = Salle()
        self.s.chargeCarte(self.nomMap)

        """Les deux prochaines lignes sont ici pour donner l'exemple seulement"""
        #self.changement(1,2)
        #self.s.chargeCarte(self.nomMap)

    #def changement(self, numEnigme, numSalle):
        #self.nomMap = "assets/map/F_E"+ str(numEnigme) + "S" + str(numSalle) + ".txt"
    
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

        
        
        
    