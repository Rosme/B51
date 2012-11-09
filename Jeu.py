class FrameJeu():
    def __init__(self,parent):
        self.parent = parent
        
        #dimensions du jeu
        self.largeurJeu=1024
        self.hauteurJeu=700
        
        #dimensions des tuiles affichés
        self.largeurTuile=64
        self.hauteurTuile=32 
        
    def initMap(self):
        self.root.destroy()
        self.root=tkinter.Tk()
        self.root.config(width=self.largeurFrame, height=self.hauteurFrame)
        
        #position du joueur centre dans l'ecran
        self.parent.jeu.joueur.posEcranX=self.largeurJeu/2
        self.parent.jeu.joueur.posEcranY=self.hauteurJeu/2
        
        #position des premiers blocs
        self.parent.jeu.joueur.posDepartX=self.largeurJeu/2
        self.parent.jeu.joueur.posDepartY=100
        
        self.persoAff=True
        #importation des images
        self.roche=tkinter.PhotoImage(file="Image/rock1.gif")
        self.gazon=tkinter.PhotoImage(file="Image/grass.gif")
        self.perso=tkinter.PhotoImage(file="Image/f1.gif")
        
        #importation de la matrice de la map
        self.laListe=self.parent.jeu.carte.s.salle
        
        self.posMilieuDiagoX=self.parent.jeu.joueur.posDepartX-(len(self.laListe[1])-1)*32
        self.posMilieuDiagoY=self.parent.jeu.joueur.posDepartY+(len(self.laListe)-1)*16
        self.parent.jeu.joueur.x,self.parent.jeu.joueur.y=self.coord(self.parent.jeu.joueur.posDepartX,self.parent.jeu.joueur.posDepartY)
        
        #création du fond noir derriere la map
        self.map=tkinter.Canvas(self.root, width=self.largeurJeu, height=self.hauteurJeu, bg="black")
        self.map.place(x=self.locationJeuX, y=self.locationJeuY)
        
        #HUD du joueur
        self.barreEtat= tkinter.Canvas(self.root,width=self.largeurJeu,height=self.locationJeuY)
        self.barreEtat.place(x=self.locationJeuX, y=0)
        
        #chat
        self.conversation=tkinter.Canvas(self.root, width=self.largeurJeu, height=self.hauteurFrame-self.hauteurJeu,bg="blue")
        self.conversation.place(x=self.locationJeuX,y=self.hauteurJeu)
        
        #inventaire
        #self.inv=tkinter.Canvas(self.root,width=300, height=700,bg="green")
        #self.inv.place(x=724,y=0)
                
        self.affichageMap()
        #ajout des ecouteurs pour effectuer des actions en jeu
        self.ajoutEcouteur()
        self.parent.miseAJour()
        self.parent.rechargement()
    
    def affichageMap(self):      
        self.posInitX=self.parent.jeu.joueur.posDepartX
        self.posInitY=self.parent.jeu.joueur.posDepartY
        
        #affichage de toutes les tuiles de la map ainsi que le personnage
        #passe toutes les lignes de la map
        for i in range(len(self.laListe)):
            #retour en haut à droite de l'écran
            self.posTempX=self.posInitX
            self.posTempY=self.posInitY
            #passe toutes les elements de la ligne 1 par 1
            for k in range(len(self.laListe[i])-1,-1,-1):
                                 
                
                #affichage de la roche (mur)
                if self.laListe[i][k]=='1':
                    self.map.create_image(self.posTempX,self.posTempY-16,image=self.roche,tags="image")
                    #self.map.create_text(self.posTempX,self.posTempY,text=str(i)+","+str(k),tags="text")
                
                #affichage du personnage
                if self.persoAff==True:
                    print(self.parent.jeu.joueur.x,i,  self.parent.jeu.joueur.y,k)
                    if self.parent.jeu.joueur.x<i and self.parent.jeu.joueur.y<k:
                        self.map.create_image(self.parent.jeu.joueur.posEcranX,self.parent.jeu.joueur.posEcranY-32,image=self.perso,tags="perso")
                        self.persoAff=False
                    
                #affichage du gazon
                if self.laListe[i][k]=='0' or self.laListe[i][k]=='3':
                    self.map.create_image(self.posTempX,self.posTempY,image=self.gazon,tags="image")
                    #self.map.create_text(self.posTempX,self.posTempY,text=str(i)+","+str(k),tags="text")
                    
                   
                #apres chaque affichage, on se dirige dans l'ecran en bas à gauche
                self.posTempX-=(self.largeurTuile/2)
                self.posTempY+=(self.hauteurTuile/2)
            #apres chaque ligne, on calcul la position de le premiere tuile de la prochaine ligne a etre affiche
            self.posInitX+=(self.largeurTuile/2)
            self.posInitY+=(self.hauteurTuile/2)
        
        #calcul de la position x,y en pixel de la tuile la plus pret de la diagonale dans le tableau
        #si une map est carre, cette valeur represente la position x,y dans l'ecran de la tuile la plus a gauche
        self.posMilieuDiagoX=self.parent.jeu.joueur.posEcranX-(len(self.laListe[1])-1)*32
        self.posMilieuDiagoY=self.parent.jeu.joueur.posEcranY+(len(self.laListe)-1)*16
    
    def ajoutEcouteur(self):
        #input du clavier        
        self.root.bind("<KeyPress-d>",self.parent.peseDroit)
        self.root.bind("<KeyPress-w>",self.parent.peseHaut)
        self.root.bind("<KeyPress-s>",self.parent.peseBas)
        self.root.bind("<KeyPress-a>",self.parent.peseGauche)
        self.root.bind("<KeyPress-D>",self.parent.peseDroit)
        self.root.bind("<KeyPress-W>",self.parent.peseHaut)
        self.root.bind("<KeyPress-S>",self.parent.peseBas)
        self.root.bind("<KeyPress-A>",self.parent.peseGauche)
        
        self.root.bind("<KeyRelease-d>",self.parent.relacheDroit)
        self.root.bind("<KeyRelease-w>",self.parent.relacheHaut)
        self.root.bind("<KeyRelease-s>",self.parent.relacheBas)
        self.root.bind("<KeyRelease-a>",self.parent.relacheGauche)
        self.root.bind("<KeyRelease-D>",self.parent.relacheDroit)
        self.root.bind("<KeyRelease-W>",self.parent.relacheHaut)
        self.root.bind("<KeyRelease-S>",self.parent.relacheBas)
        self.root.bind("<KeyRelease-A>",self.parent.relacheGauche)
        
        self.root.bind("<Button-1>", self.parent.tire)
        #calcul les coordonnees du personnage dans la matrice selon sa position x,y dans l'écran
        #x1 est la position du joueur sur l'axe des X
        #y1 est la position du joueuru sur l'axe des Y
    
    def coord(self,x1,y1):
        #voir le commentaire dans le methode affichageMap() en rapport avec les variables de meme nom
        tempX=self.posMilieuDiagoX
        tempY=self.posMilieuDiagoY
        
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