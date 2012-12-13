import tkinter

class GestionImage():
    def __init__(self):
        self.dictImage=dict()
        #inventaire
        self.dictImage["baterie"] = tkinter.PhotoImage(file='assets/image/energy.gif',width=35,height=35)
        self.dictImage["metal"] = tkinter.PhotoImage(file='assets/image/bouclier.gif',width=45,height=35)
        self.dictImage["nouriture"]=tkinter.PhotoImage(file='assets/image/nouriture.gif',width=40,height=35)
        self.dictImage["partiElectronique"] = tkinter.PhotoImage(file='assets/image/gun.gif',width=45,height=35)
        self.dictImage["seringue"]=tkinter.PhotoImage(file='assets/image/syringe.gif',width=45,height=35)  
        #map
        self.dictImage["roche"]=tkinter.PhotoImage(file="assets/image/wall.gif")
        self.dictImage["gazon"]=tkinter.PhotoImage(file="assets/image/gazon.gif")
        self.dictImage["pers"]=tkinter.PhotoImage(file="assets/image/f1.gif")
        self.dictImage["coffre"]=tkinter.PhotoImage(file="assets/image/vie.gif")
        #self.dictImage["feu"]=tkinter.PhotoImage(file="assets/image/feu.gif")
        #menu
        self.dictImage["backgroundImage"] = tkinter.PhotoImage(file='assets/Image/Prometheus_1.gif',width=1024,height=768)
        
    def getImage(self,imageRechercher):
        return self.dictImage[imageRechercher]
        
