# -*- coding: ISO-8859-1 -*-
import tkinter

class Application(tkinter.Frame):
    def __init__(self, parent):
        self.parent = parent
        
        #coordonnées de l'espace de jeu
        self.locationJeuX=0
        self.locationJeuY=0
        
        #dimensions de la fenêtre
        self.largeurFrame=1024
        self.hauteurFrame=768
        
        #dimensions du jeu
        self.largeurJeu=1024
        self.hauteurJeu=700
        
        #dimensions des tuiles affichés
        self.largeurTuile=64
        self.hauteurTuile=32 
        
        self.root=tkinter.Tk()
        self.root.config(width=self.largeurFrame, height=self.hauteurFrame)

        #position du joueur centre dans l'ecran
        self.posEcranX=self.largeurJeu/2
        self.posEcranY=self.hauteurJeu/2
        
        self.mouvement = list() 
        #0-haut,1-droite,2-bas,3-gauche
        for i in range(4):
            self.mouvement.append(False)
            
        self.initMap()
        
    def initMap(self):
        #position des premiers blocs
        self.posDepartX=self.largeurJeu/2
        self.posDepartY=100

        #importation des images
        self.roche=tkinter.PhotoImage(file="Image/rock1.gif")
        self.gazon=tkinter.PhotoImage(file="Image/grass.gif")
        self.perso=tkinter.PhotoImage(file="Image/f1.gif")
        
        #importation de la matrice de la map
        self.laListe=self.parent.jeu.carte.s.salle
        
        self.posMilieuDiagoX=self.posDepartX-(len(self.laListe[1])-1)*32
        self.posMilieuDiagoY=self.posDepartY+(len(self.laListe)-1)*16
        self.posX,self.posY=self.coord(self.posEcranX, self.posEcranY)
        
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
    
    def affichageMap(self):      
        self.posInitX=self.posDepartX
        self.posInitY=self.posDepartY
        
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
                    self.map.create_text(self.posTempX,self.posTempY,text=str(i)+","+str(k),tags="text")
               
                #affichage du personnage
                if self.posX<i and self.posY<k:
                    self.map.create_image(self.posEcranX,self.posEcranY-30,image=self.perso,tags="perso")
                
                #affichage du gazon
                if self.laListe[i][k]=='0' or self.laListe[i][k]=='3':
                    self.map.create_image(self.posTempX,self.posTempY,image=self.gazon,tags="image")
                    self.map.create_text(self.posTempX,self.posTempY,text=str(i)+","+str(k),tags="text")
                
                #apres chaque affichage, on se dirige dans l'ecran en bas à gauche
                self.posTempX-=(self.largeurTuile/2)
                self.posTempY+=(self.hauteurTuile/2)
            #apres chaque ligne, on calcul la position de le premiere tuile de la prochaine ligne a etre affiche
            self.posInitX+=(self.largeurTuile/2)
            self.posInitY+=(self.hauteurTuile/2)
        
        #calcul de la position x,y en pixel de la tuile la plus pret de la diagonale dans le tableau
        #si une map est carre, cette valeur represente la position x,y dans l'ecran de la tuile la plus a gauche
        self.posMilieuDiagoX=self.posDepartX-(len(self.laListe[1])-1)*32
        self.posMilieuDiagoY=self.posDepartY+(len(self.laListe)-1)*16
        
        
    
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
   
    #methode pour le deplacement du pers 
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
    
        
    def actualiser(self):
        tempx=0
        tempy=0
        
        #selon les touche pese on ajoute a une variable temporaire le nombre de pixel egal au deplacemtn sur l'ecran
        if self.mouvement[0]:
            tempy-=4
        if self.mouvement[1]:
            tempx+=4
        if self.mouvement[2]:
            tempy+=4
        if self.mouvement[3]:
            tempx-=4
        
        #calcul de la position apres deplacement 
        tempMatX,tempMatY=self.coord(self.posEcranX+(tempx)*2,self.posEcranY+(tempy)*2)
        
        #si la case ou le joueur se dirige est du gazon il avance
        if self.laListe[tempMatX][tempMatY]=='0':
            self.posX=tempMatX
            self.posY=tempMatY
            self.posDepartX-=tempx
            self.posDepartY-=tempy
              
        #si une touche a ete pese pour le deplacement
        if True in self.mouvement:
            #supprime toutes les images
            self.map.delete("image")
            self.map.delete("perso")
            self.map.delete("text")
            #on reaffiche la map
            self.affichageMap()
        
        
           
        
