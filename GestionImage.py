import tkinter

class GestionImage():
    def __init__(self):
        self.dictImage=dict()
        #hud
        self.dictImage["vie"]=tkinter.PhotoImage(file="assets/image/vie.gif")
        self.dictImage["sac"]=tkinter.PhotoImage(file='assets/image/backpack.gif')
        #inventaire
        self.dictImage["batterie"] = tkinter.PhotoImage(file='assets/image/energy.gif')
        self.dictImage["shield"] = tkinter.PhotoImage(file='assets/image/bouclier.gif')
        self.dictImage["nouriture"]=tkinter.PhotoImage(file='assets/image/nouriture.gif')
        self.dictImage["gun"] = tkinter.PhotoImage(file='assets/image/gun.gif')
        self.dictImage["seringue"]=tkinter.PhotoImage(file='assets/image/syringe.gif')  
        #map
        self.dictImage["roche"]=tkinter.PhotoImage(file="assets/image/mur_haut_bas2.gif")
        self.dictImage["gazon"]=tkinter.PhotoImage(file="assets/image/plancher_roche1.gif")
        self.dictImage["pers"]=tkinter.PhotoImage(file="assets/image/f1.gif")
        self.dictImage["coffre"]=tkinter.PhotoImage(file="assets/image/vie.gif")
        #self.dictImage["feu"]=tkinter.PhotoImage(file="assets/image/feu.gif")
        
        #menu
        self.dictImage["backgroundImage"] = tkinter.PhotoImage(file='assets/Image/Prometheus_1.gif',width=1024,height=768)
        
    def getImage(self,imageRechercher):
        return self.dictImage[imageRechercher]
        
