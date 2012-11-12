import tkinter

class MenuNouvellePartie():
    def __init__(self, parent):
        self.parent = parent

    def menuNouvellePartie(self,event):
        #ajoute les donnees au list box
        #on efface le menu pour afficher l'autre
        self.variable = tkinter.StringVar(self.root)
        self.variable.set("Veuillez choisir une race...") 
        self.effaceMenuPrinc()
        self.nomLabel = tkinter.Label(self.root, text="Nom de Joueur:", width=15)
        self.nomJoueur = tkinter.Entry(self.root,  width="18")
        self.raceLabel = tkinter.Label(self.root, text="Race: ",width=15)
        #afficher les bouton pour les race
        #self.valRace=tkinter.StringVar()
        #self.valRace.set(""),var=self.valRace
        self.boutonHumain= tkinter.Radiobutton(self.root, text='Humain',value="Humain",command=self.attribuhumain)#info humain
        self.boutonRace2= tkinter.Radiobutton(self.root, text='Popamu',value="Popamu" )
        self.boutonRace3= tkinter.Radiobutton(self.root, text='Irki',value="Irki" )
        self.boutonRace4= tkinter.Radiobutton(self.root, text='Atarix',value="Atarix" )
        #affiche les bouton retour et continuer
        self.boutonContinuer= tkinter.Button(self.root, text='continuer', command=self.validEntre)
        self.boutonRetour= tkinter.Button(self.root, text='retour',command=self.clear)
        #affiche les images des 4 races
        self.humainpic = tkinter.PhotoImage(file='th.gif',width=160,height=160)
        self.fondEcran.create_image(160,250, image= self.humainpic)
        self.fondEcran.create_image(400,250, image= self.humainpic)
        self.fondEcran.create_image(160,500, image= self.humainpic)
        self.fondEcran.create_image(400,500, image= self.humainpic)
        self.attribue = self.fondEcran.create_text(700,250,text='Attribut:',fill='white',font=("Arial","30"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,300,text='force',fill='white',font=("Arial","20"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,350,text='poid',fill='white',font=("Arial","20"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,400,text='intelligence',fill='white',font=("Arial","20"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,450,text='blabla',fill='white',font=("Arial","20"),tags="attribut")
  
        #place les widget et les bouton
        self.nomLabel.place(x=50, y=50)
        self.nomJoueur.place(x=200, y=50)
        self.raceLabel.place(x=50, y=100)
        self.boutonHumain.place(x=120,y=350)
        self.boutonRace2.place(x=320,y=350)
        self.boutonRace3.place(x=120,y=600)
        self.boutonRace4.place(x=320,y=600)
        self.boutonContinuer.place(x=550,y=650)
        self.boutonRetour.place(x=400,y=650)
        
    def validEntre(self):
        value=self.nomJoueur.get()
        newvalue=self.validate(value)
        if newvalue is None:
            print("nom vide")  
        else:
            self.validRace()
    def validRace(self):
        value=self.race.get()
        newvalue=self.validate(value)
        if newvalue is None:
            print("race vide")
            
        else:
            self.testRetour()
    def validate(self, newvalue):
        if newvalue:
            return False     
    
    def attribuhumain(self):
        self.race="Humain"