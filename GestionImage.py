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
        '''self.dictImage["pers"]=tkinter.PhotoImage(file="assets/image/f1.gif")'''
        self.dictImage["coffre"]=tkinter.PhotoImage(file="assets/image/vie.gif")
        self.dictImage["simonJaune"]=tkinter.PhotoImage(file="assets/image/Simon/SimonJaune.gif")
        self.dictImage["simonBleu"]=tkinter.PhotoImage(file="assets/image/Simon/SimonBleu.gif")
        self.dictImage["simonVert"]=tkinter.PhotoImage(file="assets/image/Simon/SimonVert.gif")
        self.dictImage["simonRouge"]=tkinter.PhotoImage(file="assets/image/Simon/SimonRouge.gif")
        self.dictImage["feu"]=tkinter.PhotoImage(file="assets/image/feu.gif")
        self.dictImage["eau"]=tkinter.PhotoImage(file="assets/image/eau.gif")
        self.dictImage["zoning"]=tkinter.PhotoImage(file="assets/image/zoning.gif")
        
        #menu
        self.dictImage["backgroundImage"] = tkinter.PhotoImage(file='assets/Image/Prometheus_1.gif',width=1024,height=768)
        
        #personnage
        self.listImagePerso = list()
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/haut1.gif"))#0
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/haut2.gif"))#1
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/haut3.gif"))#2
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/haut4.gif"))#3
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/haut5.gif"))#4
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/haut6.gif"))#5
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/haut7.gif"))#6
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/haut8.gif"))#7
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/haut9.gif"))#8
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/droite1.gif"))#9
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/droite2.gif"))#10
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/droite3.gif"))#11
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/droite4.gif"))#12
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/droite5.gif"))#13
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/droite6.gif"))#14
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/droite7.gif"))#15
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/droite8.gif"))#16
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/droite9.gif"))#17
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/bas1.gif"))#18
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/bas2.gif"))#19
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/bas3.gif"))#20
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/bas4.gif"))#21
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/bas5.gif"))#22
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/bas6.gif"))#23
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/bas7.gif"))#24
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/bas8.gif"))#25
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/bas9.gif"))#26
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/gauche1.gif"))#27
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/gauche2.gif"))#28
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/gauche3.gif"))#29
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/gauche4.gif"))#30
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/gauche5.gif"))#31
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/gauche6.gif"))#32
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/gauche7.gif"))#33
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/gauche8.gif"))#34
        self.listImagePerso.append(tkinter.PhotoImage(file="assets/sprite/gauche9.gif"))#35
        self.dictImage["pers"]=self.listImagePerso
        
    def getImage(self,imageRechercher):
        return self.dictImage[imageRechercher]
