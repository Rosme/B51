# -*- coding: ISO-8859-1 -*-
import tkinter
import pickle

class MenuNouvellePartie():
    def __init__(self, parent):
        self.parent = parent

        self.frameMenuNouvellePartie=tkinter.Frame(self.parent.root)
        self.backgroundImage = tkinter.PhotoImage(file='assets/Image/Prometheus_1.gif',width=1024,height=768)
        self.fondEcran= tkinter.Canvas(self.frameMenuNouvellePartie,width=1024,height=768)
        self.fondEcran.pack()
        self.fondEcran.create_image(512,384, image= self.backgroundImage,tags="fondEcran")
        self.fondEcran.create_text(100,60,text="Nom de Joueur:",fill='white',font=("Arial","15"),tags="nomText")
        self.nomJoueur = tkinter.Entry( self.frameMenuNouvellePartie,  width="18")
        self.fondEcran.create_text(100,100,text="Race :",fill='white',font=("Arial","15"),tags="raceText")
        #afficher les bouton pour les race
        
        self.valRace=tkinter.StringVar()
        self.valRace.set("")

        self.boutonHumain= tkinter.Radiobutton( self.frameMenuNouvellePartie, text='Humain',variable=self.valRace,value="Humain", command=self.raceInfo)#info humain
        self.boutonRace2= tkinter.Radiobutton( self.frameMenuNouvellePartie, text='Popamu',variable=self.valRace,value="Popamu", command=self.raceInfo)
        self.boutonRace3= tkinter.Radiobutton( self.frameMenuNouvellePartie, text='Irki',variable=self.valRace,value="Irki", command=self.raceInfo)
        self.boutonRace4= tkinter.Radiobutton( self.frameMenuNouvellePartie, text='Atarix',variable=self.valRace,value="Atarix", command=self.raceInfo)
        self.boutonHumain.select()
        #affiche les bouton retour et continuer
        self.boutonContinuer= tkinter.Button( self.frameMenuNouvellePartie, text='continuer', command=self.validEntre)
        self.boutonRetour= tkinter.Button(self.frameMenuNouvellePartie, text='retour',command=self.retour)
        
        self.textAtt = self.fondEcran.create_text(700,250,text='Attribut:',fill='white',font=("Arial","30"),tags="attribut")
        self.textVie = self.fondEcran.create_text(700,300,text='Vie:',fill='white',font=("Arial","20"),tags="attribut")
        self.textAtk = self.fondEcran.create_text(700,350,text='Attaque:',fill='white',font=("Arial","20"),tags="attribut")
        self.textDef = self.fondEcran.create_text(700,400,text='Defense',fill='white',font=("Arial","20"),tags="attribut")
        self.textPL = self.fondEcran.create_text(700,450,text="Poid limite:",fill='white',font=("Arial","20"),tags="attribut")
        
        #place les widget et les bouton
        self.nomJoueur.place(x=200, y=50)
        self.boutonHumain.place(x=120,y=350)
        self.boutonRace2.place(x=320,y=350)
        self.boutonRace3.place(x=120,y=600)
        self.boutonRace4.place(x=320,y=600)
        self.boutonContinuer.place(x=550,y=650)
        self.boutonRetour.place(x=400,y=650)
        self.nomJoueur.focus_set()
        self.raceInfo()
   
    def menuNouvellePartie(self):
        self.nomJoueur.delete(0, tkinter.END)
        self.frameMenuNouvellePartie.pack()

    def retour(self):
        self.frameMenuNouvellePartie.pack_forget()
        self.parent.menuPrincipal()
    
    def connexion(self):
        self.frameMenuNouvellePartie.pack_forget()
        self.parent.menuConnexion()
    
    def raceInfo(self):
        race = self.valRace.get()
        temp= self.parent.parent.raceInfo(race)
        self.fondEcran.itemconfig(self.textAtt, text='Attribut : ' + temp[0])
        self.fondEcran.itemconfig(self.textVie, text='Vie : ' + str(temp[1]))
        self.fondEcran.itemconfig(self.textAtk, text='Attaque : ' + str(temp[2]))
        self.fondEcran.itemconfig(self.textDef, text='Defense : ' + str(temp[3]))
        self.fondEcran.itemconfig(self.textPL, text='Poids Limite : ' + str(temp[4]))    
    
    def validEntre(self):
        self.profilename=self.nomJoueur.get()
        newvalue=self.validate(self.profilename)
        if newvalue is None:
            print("nom vide")  
        else:
            self.parent.parent.nouveauJoueur(self.valRace.get(), self.nomJoueur.get())
            self.connexion()

    def validate(self, newvalue):
        if newvalue:
            return False 
    
    def saveChar(self):
        #Pourrait également enregistrer d'autre informations.....(ip client, nombre vie du personnage, position de sauvegarde du personnage
        self.file = open("player.dat", 'a')
        self.file.write("Nom Joueur:")
        self.file.write(self.profilename + " ")
        self.file.write("Race:")
        self.file.write(self.valRace.get())
        self.file.write("\n")
        self.file.close()
        
        

        
