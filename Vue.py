# -*- coding: ISO-8859-1 -*-
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
        b4 = Button(master, text="Load Player", command=self.parent.chargerJoueur)
        b5 = Button(master, text="Save Player", command=self.parent.sauvegardeJoueur)
        b6 = Button(master, text="Add Metal Scrap", command=self.parent.addMetal)
        b7 = Button(master, text="Add Electronic", command=self.parent.addElectro)
        b8 = Button(master, text="Add Battery", command=self.parent.addBattery)
        b9 = Button(master, text="Craft Armor", command=self.parent.fabricationArmure)
        b10 = Button(master, text="Craft Gun", command=self.parent.fabricationFusil)
        b11 = Button(master, text="Craft Dematerializator", command=self.parent.fabricationDematerialisateur)
        b1.pack()
        b2.pack()
        b3.pack()
        b4.pack()
        b5.pack()
        b6.pack()
        b7.pack()
        b8.pack()
        b9.pack()
        b10.pack()
        b11.pack()
        
        