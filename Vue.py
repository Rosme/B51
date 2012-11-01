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
        
        self.root.bind("<KeyPress-q>", self.parent.autoSoin)
            