# -*- coding: ISO-8859-1 -*-
import tkinter

class MenuNouvellePartie():
    def __init__(self, parent):
        self.parent = parent
        self.menuSecondaire()

    def raceInfo(self):
        race = self.valRace.get()
        temp= self.parent.parent.raceInfo(race)
        self.parent.menuP.fondEcran.itemconfig(self.textAtt, text='Attribut : ' + temp[0])
        self.parent.menuP.fondEcran.itemconfig(self.textVie, text='Vie : ' + str(temp[1]))
        self.parent.menuP.fondEcran.itemconfig(self.textAtk, text='Attaque : ' + str(temp[2]))
        self.parent.menuP.fondEcran.itemconfig(self.textDef, text='Defense : ' + str(temp[3]))
        self.parent.menuP.fondEcran.itemconfig(self.textPL, text='Poids Limite : ' + str(temp[4]))
         
    def menuSecondaire(self):
        #ajoute les données au list box
        #on efface le menu pour afficher l'autre
        self.variable = tkinter.StringVar(self.parent.root)
        self.variable.set("Veuillez choisir une race...")
        self.nomLabel = tkinter.Label(self.parent.root, text="Nom de Joueur:", width=15)
        self.nomJoueur = tkinter.Entry(self.parent.root,  width="18")
        self.raceLabel = tkinter.Label(self.parent.root, text="Race: ",width=15)
        #afficher les bouton pour les race
        
        self.valRace=tkinter.StringVar()
        self.valRace.set("")

        self.boutonHumain= tkinter.Radiobutton(self.parent.root, text='Humain',variable=self.valRace,value="Humain", command=self.raceInfo)#info humain
        self.boutonRace2= tkinter.Radiobutton(self.parent.root, text='Popamu',variable=self.valRace,value="Popamu", command=self.raceInfo)
        self.boutonRace3= tkinter.Radiobutton(self.parent.root, text='Irki',variable=self.valRace,value="Irki", command=self.raceInfo)
        self.boutonRace4= tkinter.Radiobutton(self.parent.root, text='Atarix',variable=self.valRace,value="Atarix", command=self.raceInfo)
        self.boutonHumain.select()
        #affiche les bouton retour et continuer
        self.boutonContinuer= tkinter.Button(self.parent.root, text='continuer', command=self.validEntre)
        self.boutonRetour= tkinter.Button(self.parent.root, text='retour',command=self.parent.menuP.clear)
        #affiche les images des 4 races
        #self.humainpic = tkinter.PhotoImage(file='th.gif',width=160,height=160)
        #self.fondEcran.create_image(160,250, image= self.humainpic)
        #self.fondEcran.create_image(400,250, image= self.humainpic)
        #self.fondEcran.create_image(160,500, image= self.humainpic)
        #self.fondEcran.create_image(400,500, image= self.humainpic)
        self.textAtt = self.parent.menuP.fondEcran.create_text(700,250,text='Attribut:',fill='white',font=("Arial","30"),tags="attribut")
        self.textVie = self.parent.menuP.fondEcran.create_text(700,300,text='Vie:',fill='white',font=("Arial","20"),tags="attribut")
        self.textAtk = self.parent.menuP.fondEcran.create_text(700,350,text='Attaque:',fill='white',font=("Arial","20"),tags="attribut")
        self.textDef = self.parent.menuP.fondEcran.create_text(700,400,text='Defense',fill='white',font=("Arial","20"),tags="attribut")
        self.textPL = self.parent.menuP.fondEcran.create_text(700,450,text="Poid limite:",fill='white',font=("Arial","20"),tags="attribut")
        
        #place les widget et les bouton
        self.nomLabel.place(x=50, y=50)
        self.nomJoueur.place(x=200, y=50)
        self.raceLabel.place(x=50, y=100)
        self.boutonHumain.place(x=120,y=350)
        self.boutonRace2.place(x=320,y=350)
        self.boutonRace3.place(x=120,y=600)
        self.boutonRace4.place(x=320,y=600)
        #b.place(x=320,y=650)
        self.boutonContinuer.place(x=550,y=650)
        self.boutonRetour.place(x=400,y=650)
        self.nomJoueur.focus_set()
        
    def testRetour(self):  
        self.parent.menuP.fondEcran.delete("nouvelle_partie")
        self.parent.menuP.fondEcran.delete("continuer_partie")
        self.parent.menuP.fondEcran.delete("option")
        self.parent.menuP.fondEcran.delete("quitter")
        self.parent.menuP.fondEcran.delete("screensize")
        self.parent.menuP.fondEcran.delete("save")
        self.parent.menuP.fondEcran.delete("sound")
        self.parent.menuP.fondEcran.delete("backbouton")
        
    def validEntre(self):
        value=self.nomJoueur.get()
        newvalue=self.validate(value)
        if newvalue is None:
            print("nom vide")  
        else:
            self.validRace()
            
    def validRace(self):
        value=self.valRace.get()
        newvalue=self.validate(value)
        if newvalue is None:
            print("race vide")
            
        else:
            self.testRetour()
            self.parent.parent.nouveauJoueur(self.valRace.get(), self.nomJoueur.get())
            self.parent.parent.sauvegardeJoueur()
            self.parent.parent.enJeu(self.parent.parent.jeu.joueur)
            
    def validate(self, newvalue):
        if newvalue:
            return False 