# -*- coding: ISO-8859-1 -*-
import tkinter

class FrameJeu():
    def __init__(self,parent,perso,map):
        self.parent = parent
        
        #dimensions du jeu
        self.largeurJeu=1024
        self.hauteurJeu=700
        
        #dimensions des tuiles affiches
        self.largeurTuile=64
        self.hauteurTuile=32
        
    def initMap(self,perso,map):       
        #position du joueur centre dans l'ecran
        perso.posEcranX=self.largeurJeu/2
        perso.posEcranY=self.hauteurJeu/2
        
        #position des premiers blocs
        self.posDepartX=(((self.parent.parent.jeu.carte.s.nbColonne * self.largeurTuile)/2)+((self.parent.parent.jeu.carte.s.nbLigne * self.largeurTuile)/2))/2  - (perso.posMapX-perso.posEcranX)
        self.posDepartY=-32 -(perso.posMapY-perso.posEcranY)
        
        self.persoAff=True
        #importation des images
        self.roche=tkinter.PhotoImage(file="assets/image/rock1.gif")
        self.gazon=tkinter.PhotoImage(file="assets/image/grass.gif")
        self.pers=tkinter.PhotoImage(file="assets/image/f1.gif")
        
        self.posMilieuDiagoX=self.posDepartX-(len(map[1])-1)*32
        self.posMilieuDiagoY=self.posDepartY+(len(map)-1)*16

        perso.posMatX,perso.posMatY=self.coord(perso.posEcranX,perso.posEcranX)
        
        #creation du fond noir derriere la map
        self.map=tkinter.Canvas(self.parent.root, width=self.largeurJeu, height=self.hauteurJeu, bg="black")
        self.map.place(x=self.parent.localisationJeuX, y=self.parent.localisationJeuY)
        
        #chat
        self.conversation=tkinter.Canvas(self.parent.root, width=self.largeurJeu, height=self.parent.hauteurFrame-self.hauteurJeu,bg="blue")
        self.conversation.place(x=self.parent.localisationJeuX,y=self.hauteurJeu)
        
        #inventaire
        #self.inv=tkinter.Canvas(self.root,width=300, height=700,bg="green")
        #self.inv.place(x=724,y=0)
                
        self.affichageMap(perso,map)
        
        return perso
        
    def ajoutEcouteuretBoucle(self):
        self.ajoutEcouteur()
        self.parent.parent.miseAJour()
        self.parent.parent.rechargement()
        self.parent.parent.balle()
        #self.parent.parent.vitesseTire()
    
    def affichageMap(self,perso,map):  
        posInitX=self.posDepartX
        posInitY=self.posDepartY
        
        #affichage de toutes les tuiles de la map ainsi que le personnage
        #passe toutes les lignes de la map
        for i in range(len(map)):
            #retour en haut a droite de l'ecran
            posTempX=posInitX
            posTempY=posInitY
            #passe toutes les elements de la ligne 1 par 1
            for k in range(len(map[i])-1,-1,-1):
                #affichage de la roche (mur)
                if map[i][k]=='1':
                    self.map.create_image(posTempX,posTempY-16,image=self.roche,tags="image")
                    #self.map.create_text(self.posTempX,self.posTempY,text=str(i)+","+str(k),tags="text")
                    
                #affichage du personnage
                if self.persoAff==True:
                    if perso.posMatX<i and perso.posMatY<k:
                        self.map.create_image(perso.posEcranX,perso.posEcranY-32,image=self.pers,tags="perso")
                        self.persoAff=False
                    
                #affichage du gazon
                if map[i][k]=='0' or map[i][k]=='3':
                    self.map.create_image(posTempX,posTempY,image=self.gazon,tags="image")
                    #self.map.create_text(self.posTempX,self.posTempY,text=str(i)+","+str(k),tags="text")
                
                for p in range(len(self.parent.parent.jeu.carte.listeLogo)):
                    if self.parent.parent.jeu.carte.listeLogo[p][0]==i and self.parent.parent.jeu.carte.listeLogo[p][1]==self.parent.parent.jeu.carte.s.nbLigne-(k+1):
                        #print(self.parent.parent.jeu.carte.listeLogo[p])
                        self.map.create_image(posTempX,posTempY-32,image=self.pers,tags="logo")
                     
                   
                #apres chaque affichage, on se dirige dans l'ecran en bas a gauche
                posTempX-=(self.largeurTuile/2)
                posTempY+=(self.hauteurTuile/2)
            #apres chaque ligne, on calcul la position de le premiere tuile de la prochaine ligne a etre affiche
            posInitX+=(self.largeurTuile/2)
            posInitY+=(self.hauteurTuile/2)
        
        #calcul de la position x,y en pixel de la tuile la plus pret de la diagonale dans le tableau
        #si une map est carre, cette valeur represente la position x,y dans l'ecran de la tuile la plus a gauche
        self.posMilieuDiagoX=self.posDepartX-(len(map[1])-1)*32
        self.posMilieuDiagoY=self.posDepartY+(len(map)-1)*16
        
        if self.parent.parent.jeu.listePersonnage:
            temp = self.parent.parent.jeu.listePersonnage[0].obtenirLimite()
            self.map.create_rectangle(perso.posEcranX+ temp[0]- perso.posMapX, perso.posEcranY+temp[1]- perso.posMapY, perso.posEcranX+temp[2]- perso.posMapX, perso.posEcranY+temp[3]- perso.posMapY, fill='blue', tags="p")
            self.map.create_image(perso.posEcranX+(self.parent.parent.jeu.listePersonnage[0].posMapX - perso.posMapX),perso.posEcranY+(self.parent.parent.jeu.listePersonnage[0].posMapY- perso.posMapY)-32, image=self.pers, tags="p")
    
    def tire(self):  
        for i in self.parent.parent.jeu.listeBalle:
            self.map.create_oval(i.posEcranX-5, i.posEcranY-5, i.posEcranX, i.posEcranY, fill='red', tags="balle")
    
    def ajoutEcouteur(self):
        #input du clavier        
        self.parent.root.bind("<KeyPress>",self.parent.parent.peseKeyGestion)
        self.parent.root.bind("<KeyRelease>",self.parent.parent.relacheKeyGestion)
        
        self.parent.root.bind("<Button-1>", self.parent.parent.peseTire)
        self.parent.root.bind("<ButtonRelease-1>", self.parent.parent.relacheTire)
        self.parent.root.bind("<B1-Motion>", self.parent.parent.tireCoord)
    
    def coord(self,x1,y1):
        #voir le commentaire dans le methode affichageMap() en rapport avec les variables de meme nom
        tempX=self.posMilieuDiagoX
        tempY=self.posMilieuDiagoY
        #print("coord",self.posMilieuDiagoY)
        y=(y1-self.posMilieuDiagoY)/16  
        if y<0:
            y*=-1
                    
        y=round(y)
           
        for i in range(y):
            tempX+=32
           
        x=(x1-tempX)/64  
        x= round(x)
        
        for f in range(x):
            y+=1
        
        #si le joueur est au-dessus de la diagonale
        if self.posMilieuDiagoY<y1:
            temp=x
            x=y
            y=temp
        return x,y