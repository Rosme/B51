# -*- coding: ISO-8859-1 -*-
import tkinter
import math

class FrameJeu():
    def __init__(self,parent):
        self.parent = parent
        
        #dimensions du jeu
        self.largeurJeu=1024
        self.hauteurJeu=700
        
        #dimensions des tuiles affiches
        self.largeurTuile=64
        self.hauteurTuile=32
        
    def initMap(self,perso,laSalle):       
        #position du joueur centre dans l'ecran
        perso.posEcranX=self.largeurJeu/2
        perso.posEcranY=self.hauteurJeu/2
        
        #position des premiers blocs
        self.posDepartX = (((laSalle.nbColonne * self.largeurTuile)/2)+((laSalle.nbLigne * self.largeurTuile)/2))/2 - (perso.posMapX-perso.posEcranX)
        self.posDepartY = -32 - (perso.posMapY-perso.posEcranY)
        
        self.persoAff=True
        #importation des images
        self.roche=tkinter.PhotoImage(file="assets/image/rock1.gif")
        self.gazon=tkinter.PhotoImage(file="assets/image/grass.gif")
        self.pers=tkinter.PhotoImage(file="assets/image/f1.gif")
        
        self.posMilieuDiagoX=(self.posDepartX-(laSalle.nbColonne-1)*32)-32
        self.posMilieuDiagoY=(self.posDepartY+(laSalle.nbLigne-1)*16)

        perso.posMatX,perso.posMatY=self.coord(perso.posEcranX,perso.posEcranY)
        
        #creation du fond noir derriere la map
        self.map=tkinter.Canvas(self.parent.root, width=self.largeurJeu, height=self.hauteurJeu, bg="black")
        self.map.place(x=self.parent.localisationJeuX, y=self.parent.localisationJeuY)
        
        #chat
        self.conversation=tkinter.Canvas(self.parent.root, width=self.largeurJeu, height=self.parent.hauteurFrame-self.hauteurJeu,bg="blue")
        self.conversation.place(x=self.parent.localisationJeuX,y=self.hauteurJeu)
        
        #inventaire
        #self.inv=tkinter.Canvas(self.root,width=300, height=700,bg="green")
        #self.inv.place(x=724,y=0)
                
        self.affichageMap(perso,laSalle.salle)
        
        return perso
        
    def ajoutEcouteuretBoucle(self):
        self.ajoutEcouteur()
        self.parent.parent.miseAJour()
        self.parent.parent.rechargement()
        self.parent.parent.balle()
    
    def affichageMap(self,perso,map):  
        self.vueProximite(perso,len(map[0]),len(map))
        
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
                if k>self.limiteX[0] and k< self.limiteX[1] and i >self.limiteY[0] and i< self.limiteY[1]:
                    if map[i][k]=='1':
                        self.map.create_image(posTempX,posTempY-16,image=self.roche,tags="image")
                        
                    #affichage du personnage
                    if self.persoAff==True:
                        if perso.posMatX<k and perso.posMatY<i:
                            self.map.create_image(perso.posEcranX,perso.posEcranY-32,image=self.pers,tags="perso")
                            self.persoAff=False
                        
                    #affichage du gazon
                    if map[i][k]=='0' or map[i][k]=='v' or map[i][k]=='b' or map[i][k]=='n' or map[i][k]=='m':
                        self.map.create_image(posTempX,posTempY,image=self.gazon,tags="image")
                        self.map.create_text(posTempX,posTempY,text=str(i)+","+str(k),tags="text")
                    
                    if  map[i][k]=='3':
                        self.map.create_text(posTempX, posTempY, text="Coffre", fill='white', tags="image")
                    
                    for p in range(len(self.parent.parent.jeu.carte.listeLogo)):
                        if self.parent.parent.jeu.carte.listeLogo[p][0]==self.parent.parent.jeu.carte.s.nbLigne-(k+1) and self.parent.parent.jeu.carte.listeLogo[p][1]==i:
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
        self.posMilieuDiagoX=(self.posDepartX-(len(map[1])-1)*32)-32
        self.posMilieuDiagoY=(self.posDepartY+(len(map)-1)*16)
        

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
        x=0
        y=0
        mily=self.posMilieuDiagoY-self.posDepartY
        x1-=self.posMilieuDiagoX
        y1-=self.posDepartY

        tempx=math.floor(x1/(self.largeurTuile/2))*self.largeurTuile/2
        tempy=math.floor(y1/(self.hauteurTuile/2))*self.hauteurTuile/2        
        if tempy==mily:
            tempx = math.floor(tempx/self.largeurTuile)
            x=tempx
            y=tempx
        elif tempy<mily:
            while tempy!=mily:
                tempx-=(self.largeurTuile/2)
                tempy+=(self.hauteurTuile/2)
                x+=1
            tempx = math.floor(tempx/self.largeurTuile)
            x+=tempx
            y+=tempx
        elif tempy>mily:
            while tempy!=mily:
                tempx-=(self.largeurTuile/2)
                tempy-=(self.hauteurTuile/2)
                y+=1
            tempx = math.floor(tempx/self.largeurTuile)
            x+=tempx
            y+=tempx
        #print(y,x)
        return x,y
        
    def coordProchaineZone(self,salle,char,perso):
        for i in range(salle.nbLigne):
            for j in range(salle.nbColonne):
                if salle.salle[i][j]==char:
                    try:
                        if salle.salle[i][j+1]==char:
                            try:
                                if salle.salle[i+1][j]=='0':
                                    matx = j
                                    maty = i+1
                                    break
                            except IndexError:
                                if salle.salle[i-1][j]=='0':
                                    matx = j
                                    maty = i-1
                                    break
                    except IndexError:
                        if salle.salle[i][j-1]==char:
                            try:
                                if salle.salle[i][j+1]=='0':
                                    matx = j+1
                                    maty = i
                                    break
                            except IndexError:
                                if salle.salle[i][j-1]=='0':
                                    matx = j-1
                                    maty = i
                                    break
    
        depx=self.largeurJeu/2
        depy=0      
        print(maty,matx)
        matx=salle.nbColonne-matx
        depx+=(((32*maty)-(32*matx))+32)
        depy+=(((16*maty)+(16*matx))-16)
        
        perso.posMapX=depx
        perso.posMapY=depy
       
        self.posDepartX = (((salle.nbColonne * self.largeurTuile)/2)+((salle.nbLigne * self.largeurTuile)/2))/2 - (perso.posMapX-perso.posEcranX)
        self.posDepartY = -32 - (perso.posMapY-perso.posEcranY)
        
        self.posMilieuDiagoX=(self.posDepartX-(salle.nbColonne-1)*32)-32
        self.posMilieuDiagoY=(self.posDepartY+(salle.nbLigne-1)*16)

        print(perso.posMapX,perso.posMapY,self.posDepartX,self.posDepartY,self.posMilieuDiagoX,self.posMilieuDiagoY)
        return perso
        
    
    def vueProximite(self,perso,nbColonne,nbLigne):
        rayon=8
        self.limiteX=list()
        self.limiteY=list()
        
        if perso.posMatX <rayon:
            self.limiteX.append(-1)
            self.limiteX.append((rayon*2)-1)
        elif perso.posMatX> (nbColonne-rayon):
            self.limiteX.append(nbColonne-(rayon*2))
            self.limiteX.append(nbColonne)
        elif perso.posMatX>=rayon and perso.posMatX<= (nbColonne-(rayon)):
            self.limiteX.append(perso.posMatX-rayon)
            self.limiteX.append(perso.posMatX+rayon)
        
        if perso.posMatY <rayon:
            self.limiteY.append(-1)
            self.limiteY.append((rayon*2)-1)
        elif perso.posMatY> (nbLigne-rayon):
            self.limiteY.append(nbLigne-(rayon*2))
            self.limiteY.append(nbLigne)
        elif perso.posMatY>=rayon and perso.posMatY<= (nbLigne-rayon):
            self.limiteY.append(perso.posMatY-rayon)
            self.limiteY.append(perso.posMatY+rayon)
 