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
        self.perso=perso        
        #position du joueur centre dans l'ecran
        self.perso.posEcranX=self.largeurJeu/2
        self.perso.posEcranY=self.hauteurJeu/2
        
        #position des premiers blocs
        self.posDepartX=((21 * self.largeurTuile)/2) - (self.perso.posMapX-self.perso.posEcranX)
        self.posDepartY=-32 -(self.perso.posMapY-self.perso.posEcranY)
        
        self.persoAff=True
        #importation des images
        self.roche=tkinter.PhotoImage(file="Image/rock1.gif")
        self.gazon=tkinter.PhotoImage(file="Image/grass.gif")
        self.pers=tkinter.PhotoImage(file="Image/f1.gif")
        
        self.posMilieuDiagoX=self.posDepartX-(len(map[1])-1)*32
        self.posMilieuDiagoY=self.posDepartY+(len(map)-1)*16

        self.perso.posMatX,self.perso.posMatY=self.coord(self.perso.posEcranX,self.perso.posEcranX)
        
        #creation du fond noir derriere la map
        self.map=tkinter.Canvas(self.parent.root, width=self.largeurJeu, height=self.hauteurJeu, bg="black")
        self.map.place(x=self.parent.localisationJeuX, y=self.parent.localisationJeuY)
        
        #HUD du joueur
        self.barreEtat= tkinter.Canvas(self.parent.root,width=self.largeurJeu,height=self.parent.localisationJeuY)
        self.barreEtat.place(x=self.parent.localisationJeuX, y=0)
        
        #chat
        self.conversation=tkinter.Canvas(self.parent.root, width=self.largeurJeu, height=self.parent.hauteurFrame-self.hauteurJeu,bg="blue")
        self.conversation.place(x=self.parent.localisationJeuX,y=self.hauteurJeu)
        
        #inventaire
        #self.inv=tkinter.Canvas(self.root,width=300, height=700,bg="green")
        #self.inv.place(x=724,y=0)
                
        self.affichageMap(self.perso,map)
        #print(self.perso.posEcranX,self.perso.posEcranY,self.perso.x,self.perso.y)
        #ajout des ecouteurs pour effectuer des actions en jeu
        
        return self.perso
        
    def ajoutEcouteuretBoucle(self):
        self.ajoutEcouteur()
        self.parent.parent.miseAJour()
        self.parent.parent.rechargement()
        self.parent.parent.balle()
    
    def affichageMap(self,perso,map):
        self.perso=perso  
        self.posInitX=self.posDepartX
        self.posInitY=self.posDepartY
        
        #affichage de toutes les tuiles de la map ainsi que le personnage
        #passe toutes les lignes de la map
        for i in range(len(map)):
            #retour en haut a droite de l'ecran
            self.posTempX=self.posInitX
            self.posTempY=self.posInitY
            #passe toutes les elements de la ligne 1 par 1
            for k in range(len(map[i])-1,-1,-1):
                #affichage de la roche (mur)
                if map[i][k]=='1':
                    self.map.create_image(self.posTempX,self.posTempY-16,image=self.roche,tags="image")
                    #self.map.create_text(self.posTempX,self.posTempY,text=str(i)+","+str(k),tags="text")
                
                #affichage du personnage
                if self.persoAff==True:
                    if self.perso.posMatX<i and self.perso.posMatY<k:
                        self.map.create_image(self.perso.posEcranX,self.perso.posEcranY-32,image=self.pers,tags="perso")
                        self.persoAff=False
                    
                #affichage du gazon
                if map[i][k]=='0' or map[i][k]=='3':
                    self.map.create_image(self.posTempX,self.posTempY,image=self.gazon,tags="image")
                    #self.map.create_text(self.posTempX,self.posTempY,text=str(i)+","+str(k),tags="text")
                    
                   
                #apres chaque affichage, on se dirige dans l'ecran en bas a gauche
                self.posTempX-=(self.largeurTuile/2)
                self.posTempY+=(self.hauteurTuile/2)
            #apres chaque ligne, on calcul la position de le premiere tuile de la prochaine ligne a etre affiche
            self.posInitX+=(self.largeurTuile/2)
            self.posInitY+=(self.hauteurTuile/2)
        
        #calcul de la position x,y en pixel de la tuile la plus pret de la diagonale dans le tableau
        #si une map est carre, cette valeur represente la position x,y dans l'ecran de la tuile la plus a gauche
        self.posMilieuDiagoX=self.posDepartX-(len(map[1])-1)*32
        self.posMilieuDiagoY=self.posDepartY+(len(map)-1)*16
        
        if self.parent.parent.jeu.listePersonnage:
            temp = self.parent.parent.jeu.listePersonnage[0].obtenirLimite()
            #self.map.create_rectangle(self.parent.jeu.listePersonnage[0].x, self.parent.jeu.listePersonnage[0].y, self.parent.jeu.listePersonnage[0].x+100, self.parent.jeu.listePersonnage[0].y+100, fill='blue')
            self.map.create_rectangle(self.perso.posEcranX+ temp[0]- self.perso.posMapX, self.perso.posEcranY+temp[1]- self.perso.posMapY, self.perso.posEcranX+temp[2]- self.perso.posMapX, self.perso.posEcranY+temp[3]- self.perso.posMapY, fill='blue', tags="p")
            self.map.create_image(self.perso.posEcranX+(self.parent.parent.jeu.listePersonnage[0].posMapX - self.perso.posMapX),self.perso.posEcranY+(self.parent.parent.jeu.listePersonnage[0].posMapY- self.perso.posMapY)-32, image=self.pers, tags="p")
    
    def ajoutEcouteur(self):
        #input du clavier        
        self.parent.root.bind("<KeyPress-d>",self.parent.parent.peseDroit)
        self.parent.root.bind("<KeyPress-w>",self.parent.parent.peseHaut)
        self.parent.root.bind("<KeyPress-s>",self.parent.parent.peseBas)
        self.parent.root.bind("<KeyPress-a>",self.parent.parent.peseGauche)
        self.parent.root.bind("<KeyPress-D>",self.parent.parent.peseDroit)
        self.parent.root.bind("<KeyPress-W>",self.parent.parent.peseHaut)
        self.parent.root.bind("<KeyPress-S>",self.parent.parent.peseBas)
        self.parent.root.bind("<KeyPress-A>",self.parent.parent.peseGauche)
        
        self.parent.root.bind("<KeyRelease-d>",self.parent.parent.relacheDroit)
        self.parent.root.bind("<KeyRelease-w>",self.parent.parent.relacheHaut)
        self.parent.root.bind("<KeyRelease-s>",self.parent.parent.relacheBas)
        self.parent.root.bind("<KeyRelease-a>",self.parent.parent.relacheGauche)
        self.parent.root.bind("<KeyRelease-D>",self.parent.parent.relacheDroit)
        self.parent.root.bind("<KeyRelease-W>",self.parent.parent.relacheHaut)
        self.parent.root.bind("<KeyRelease-S>",self.parent.parent.relacheBas)
        self.parent.root.bind("<KeyRelease-A>",self.parent.parent.relacheGauche)
        
        self.parent.root.bind("<KeyPress-q>",self.parent.parent.autoSoin)
        self.parent.root.bind("<KeyPress-Q>",self.parent.parent.autoSoin)
        
        self.parent.root.bind("<Button-1>", self.parent.parent.tire)
        #calcul les coordonnees du personnage dans la matrice selon sa position x,y dans l'ecran
        #x1 est la position du joueur sur l'axe des X
        #y1 est la position du joueuru sur l'axe des Y
    
    def tire(self):  
        for i in self.parent.parent.jeu.listeBalle:
            self.map.create_oval(i.posEcranX-5, i.posEcranY-5, i.posEcranX, i.posEcranY, fill='red', tags="balle")
    
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