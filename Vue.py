# -*- coding: ISO-8859-1 -*-
import tkinter

class Application(tkinter.Frame):
    def __init__(self, parent):
        self.parent = parent
        
        self.locationJeuX=0
        self.locationJeuY=30
        
        #dimensions de la fenêtre
        self.largeurFrame=1024
        self.hauteurFrame=768
        
        #dimensions du jeu
        self.largeurJeu=1024
        self.hauteurJeu=660
        
        self.largeurTuile=64
        self.hauteurTuile=32 
        
        self.epaisseurContour=20   
        
        self.root=tkinter.Tk()
        self.root.config(width=self.largeurFrame, height=self.hauteurFrame)

        
        self.posEcranX=self.largeurJeu/2
        self.posEcranY=self.hauteurJeu/2
        
        self.mouvement = list() 
        #0-haut,1-droite,2-bas,3-gauche
        for i in range(4):
            self.mouvement.append(False)
            
        self.initMap()
        
    def initMap(self):
        self.posDepartX=self.largeurJeu/2
        self.posDepartY=100
        self.persoAff=True

        self.f2=tkinter.PhotoImage(file="Image/rock1.gif")
        self.f=tkinter.PhotoImage(file="Image/grass.gif")
        self.perso=tkinter.PhotoImage(file="Image/f1.gif")
        
        self.laListe=list()
                
        self.ste=list()
        for q in range(19):
            self.ste.append('1')
        
        self.li=list()   
        self.li.append('1')
        for t in  range(17):
            self.li.append('2')
        self.li.append('1')        
        
        self.laListe.append(self.ste)
        for w in range(17):
            self.laListe.append(self.li)
        self.laListe.append(self.ste)
        
        
        self.testX=self.posDepartX-(len(self.laListe[1])-1)*32
        self.testY=self.posDepartY+(len(self.laListe)-1)*16
        
        self.posX,self.posY=self.coord(self.posEcranX, self.posEcranY)
        
        self.map=tkinter.Canvas(self.root, width=self.largeurJeu, height=self.hauteurJeu, bg="black")
        self.map.place(x=self.locationJeuX, y=self.locationJeuY)
        
        self.barreEtat= tkinter.Canvas(self.root,width=self.largeurJeu,height=self.locationJeuY, bg="red")
        self.barreEtat.place(x=self.locationJeuX, y=0)
        
        self.conversation=tkinter.Canvas(self.root, width=self.largeurJeu, height=self.hauteurFrame-(self.hauteurJeu+self.locationJeuY),bg="blue")
        self.conversation.place(x=self.locationJeuX,y=self.locationJeuY+self.hauteurJeu)
        
        self.inv=tkinter.Canvas(self.root,width=100, height=656,bg="green")
        self.inv.place(x=924,y=self.locationJeuY+2)
                
        self.affichageMap()
        self.ajoutEcouteur()
    
    def affichageMap(self):      
        self.posInitX=self.posDepartX
        self.posInitY=self.posDepartY
                
        for i in range(len(self.laListe)):
            self.posTempX=self.posInitX
            self.posTempY=self.posInitY
            for k in range(len(self.laListe[i])-1,-1,-1):
                
                if self.laListe[i][k]=='1':
                    self.map.create_image(self.posTempX,self.posTempY,image=self.f2,tags="image")
    
                if self.posX<i and self.posY<k and self.persoAff ==True:
                        self.persoAff=False
                        self.map.create_image(self.posEcranX,self.posEcranY-25,image=self.perso,tags="perso")
                
                if self.laListe[i][k]=='2':
                    self.map.create_image(self.posTempX,self.posTempY+16,image=self.f,tags="image")
                
 
                self.posTempX-=(self.largeurTuile/2)
                self.posTempY+=(self.hauteurTuile/2)
            self.posInitX+=(self.largeurTuile/2)
            self.posInitY+=(self.hauteurTuile/2)
        
        self.testX=self.posDepartX-(len(self.laListe[1])-1)*32
        self.testY=self.posDepartY+(len(self.laListe)-1)*16
    
    def ajoutEcouteur(self):        
        #input du clavier        
        self.root.bind("<KeyPress-d>",self.peseDroit)
        self.root.bind("<KeyPress-w>",self.peseHaut)
        self.root.bind("<KeyPress-s>",self.peseBas)
        self.root.bind("<KeyPress-a>",self.peseGauche)
        
        self.root.bind("<KeyRelease-d>",self.relacheDroit)
        self.root.bind("<KeyRelease-w>",self.relacheHaut)
        self.root.bind("<KeyRelease-s>",self.relacheBas)
        self.root.bind("<KeyRelease-a>",self.relacheGauche)
    
    
    def coord(self,x1,y1):
        tempX=self.testX
        tempY=self.testY
            
        if self.testY>y1:
            y=(y1-self.testY)/16
            
            if y<0:
                y*=-1
                    
            y=round(y)
            
            for i in range(y):
                tempX+=32
            
            x=(x1-tempX)/64
            
            x= round(x)
            
            for f in range(x):
                y+=1
        else:
            y=(y1-self.testY)/16
            
            if y<0:
                y*=-1
                    
            y=round(y)
            
            for i in range(y):
                tempX+=32
            
            x=(x1-tempX)/64
            
            x= round(x)
            
            for f in range(x):
                y+=1
            temp=x
            x=y
            y=temp
            
        return x,y
    
    def peseHaut(self,event):
        self.mouvement[0]=True
    def relacheHaut(self,event):
        self.mouvement[0]=False
         
    def peseDroit(self,event):
        self.mouvement[1]=True
    def relacheDroit(self,event):
        self.mouvement[1]=False
    
    def peseBas(self,event):
        self.mouvement[2]=True
    def relacheBas(self,event):
        self.mouvement[2]=False
        
    def peseGauche(self,event):
        self.mouvement[3]=True
    def relacheGauche(self,event):
        self.mouvement[3]=False


'''# -*- coding: ISO-8859-1 -*-
from tkinter import *

class Application():
    def __init__(self, parent, master=None):
        self.parent = parent
        self.root=Tk()
        self.root.config(width=800, height=600)
        self.root.title("Area B51")
        
        b1 = Button(master, text="New Humain", command=self.parent.nouveauHumain)
        b2 = Button(master, text="New Wohawk", command=self.parent.nouveauWohawk)
        b3 = Button(master, text="New Zeborf", command=self.parent.nouveauZeborf)
        b4 = Button(master, text="New Irki", command=self.parent.nouveauIrki)
        b5 = Button(master, text="New Popamu", command=self.parent.nouveauPopamu)
        b6 = Button(master, text="New Atarix", command=self.parent.nouveauAtarix)
        b7 = Button(master, text="Load Player", command=self.parent.chargerJoueur)
        b8 = Button(master, text="Save Player", command=self.parent.sauvegardeJoueur)
        b9 = Button(master, text="Add Metal Scrap", command=self.parent.addMetal)
        b10 = Button(master, text="Add Electronic", command=self.parent.addElectro)
        b11 = Button(master, text="Add Battery", command=self.parent.addBattery)
        b12= Button(master, text="Craft Armor", command=self.parent.fabricationArmure)
        b13 = Button(master, text="Craft Gun", command=self.parent.fabricationFusil)
        b14 = Button(master, text="Craft Dematerializator", command=self.parent.fabricationDematerialisateur)
        b15 = Button(master, text="get Humain info", command=self.parent.infoHumain)
        b1.grid(column=0, row=0)
        b2.grid(column=1, row=0)
        b3.grid(column=2, row=0)
        b4.grid(column=0, row=1)
        b5.grid(column=1, row=1)
        b6.grid(column=2, row=1)
        b7.grid(column=0, row=2)
        b8.grid(column=1, row=2)
        b9.grid(column=0, row=3)
        b10.grid(column=1, row=3)
        b11.grid(column=2, row=3)
        b12.grid(column=0, row=4)
        b13.grid(column=1, row=4)
        b14.grid(column=2, row=4)
        b15.grid(column=0, row=5)
        
        self.root.bind("<KeyPress-q>", self.parent.autoSoin)
            '''