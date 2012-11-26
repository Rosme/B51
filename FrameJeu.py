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
        self.importerImage()
        
        #position des premiers blocs
        self.calculPositionDepart(perso,laSalle)
       
        self.calculPositionMilieu(laSalle)

        perso.posMatX,perso.posMatY=self.coord(perso.posEcranX,perso.posEcranY)
        
        self.dispositionPrincipale()
        
        self.affichageMap(perso,laSalle)
        
        return perso
    def dispositionPrincipale(self):
        #creation du fond noir derriere la map
        self.map=tkinter.Canvas(self.parent.root, width=self.largeurJeu, height=self.hauteurJeu, bg="black")
        self.map.place(x=self.parent.localisationJeuX, y=self.parent.localisationJeuY)
        
        #chat
        self.conversation=tkinter.Canvas(self.parent.root, width=self.largeurJeu, height=self.parent.hauteurFrame-self.hauteurJeu,bg="blue")
        self.conversation.place(x=self.parent.localisationJeuX,y=self.hauteurJeu)
    
    def importerImage(self):
        self.roche=tkinter.PhotoImage(file="assets/image/rock1.gif")
        self.gazon=tkinter.PhotoImage(file="assets/image/grass.gif")
        self.pers=tkinter.PhotoImage(file="assets/image/f1.gif")
    
    def ajoutEcouteuretBoucle(self):
        self.ajoutEcouteur()
        self.parent.parent.miseAJour()
        self.parent.parent.rechargement()
        self.parent.parent.balle()
    
    def calculPositionDepart(self,perso,laSalle):
        self.posDepartX = (((laSalle.nbColonne * self.largeurTuile)/2)+((laSalle.nbLigne * self.largeurTuile)/2))/2 - (perso.posMapX-perso.posEcranX)
        self.posDepartY = -32 - (perso.posMapY-perso.posEcranY)
        
    def calculPositionMilieu(self,laSalle):
        self.posMilieuDiagoX=(self.posDepartX-(laSalle.nbColonne-1)*32)-32
        self.posMilieuDiagoY=(self.posDepartY+(laSalle.nbLigne-1)*16)
    
    def affichageMap(self,perso,laSalle):
        map=laSalle.salle
        limiteX=list()
        limiteY=list()
        limiteX=self.vueProximite(perso.posMatX,len(map[0]))
        limiteY=self.vueProximite(perso.posMatY,len(map))
        #print(perso.posMapX,perso.posMapY,self.posDepartX,self.posDepartY,self.posMilieuDiagoX,self.posMilieuDiagoY)
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
                if k>limiteX[0] and k< limiteX[1] and i >limiteY[0] and i< limiteY[1]:
                    if map[i][k]=='1' or map[i][k] == '2':
                        self.map.create_image(posTempX,posTempY-16,image=self.roche,tags="image")
                        
                    #affichage du personnage
                    if self.persoAff==True:
                        if perso.posMatX<k and perso.posMatY<i:
                            temp = perso.obtenirLimite()
                            self.map.create_rectangle(perso.posEcranX+ temp[0]- perso.posMapX, perso.posEcranY+temp[1]- perso.posMapY, perso.posEcranX+temp[2]- perso.posMapX, perso.posEcranY+temp[3]- perso.posMapY, fill='red', tags="perso")
                            self.map.create_image(perso.posEcranX,perso.posEcranY-32,image=self.pers,tags="perso")
                            self.persoAff=False
                        
                    #affichage du gazon
                    if map[i][k]=='0' or map[i][k]=='v' or map[i][k]=='b' or map[i][k]=='n' or map[i][k]=='m':
                        self.map.create_image(posTempX,posTempY,image=self.gazon,tags="image")
                        #self.map.create_text(posTempX,posTempY,text=str(i)+","+str(k),tags="text")
                    
                    if  map[i][k]=='3':
                        self.map.create_text(posTempX, posTempY, text="Coffre", fill='white', tags="image")
                    
                    for p in self.parent.parent.jeu.listeLogomate:
                        if p.posMatX<k and p.posMatY<i:
                            self.map.create_image(perso.posEcranX+(p.posMapX - perso.posMapX),perso.posEcranY+(p.posMapY - perso.posMapY)-32,image=self.pers,tags="logo")
                     
                   
                #apres chaque affichage, on se dirige dans l'ecran en bas a gauche
                posTempX-=(self.largeurTuile/2)
                posTempY+=(self.hauteurTuile/2)
            #apres chaque ligne, on calcul la position de le premiere tuile de la prochaine ligne a etre affiche
            posInitX+=(self.largeurTuile/2)
            posInitY+=(self.hauteurTuile/2)
        
        #calcul de la position x,y en pixel de la tuile la plus pret de la diagonale dans le tableau
        #si une map est carre, cette valeur represente la position x,y dans l'ecran de la tuile la plus a gauche
        self.calculPositionMilieu(laSalle)
        
        if self.parent.parent.jeu.listePersonnage:
            temp = self.parent.parent.jeu.listePersonnage[0].obtenirLimite()
            self.map.create_image(perso.posEcranX+(self.parent.parent.jeu.listePersonnage[0].posMapX - perso.posMapX),perso.posEcranY+(self.parent.parent.jeu.listePersonnage[0].posMapY- perso.posMapY)-32, image=self.pers, tags="p")
            
        if self.parent.parent.jeu.listeRoche:
            temp = self.parent.parent.jeu.listeRoche[0].obtenirLimite()
            self.map.create_rectangle(perso.posEcranX+ temp[0]- perso.posMapX, perso.posEcranY+temp[1]- perso.posMapY, perso.posEcranX+temp[2]- perso.posMapX, perso.posEcranY+temp[3]- perso.posMapY, fill='blue', tags="p")
    
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
        trouver=False
        depx=self.largeurJeu/2
        depy=0
        
        for i in range(salle.nbLigne):
            for j in range(salle.nbColonne):
                if salle.salle[i][j]==char:
                    try:
                        #si l'autre char à droite
                        if salle.salle[i][j+1]==char:
                            try:
                                if salle.salle[i+1][j]=='0':#porte en bas
                                    matx = j
                                    maty = i+1
                                    trouver=True
                                    matx=salle.nbColonne-matx
                                    depx+=(((32*maty)-(32*matx))+32)+(64*((salle.nbColonne-matx)/2))
                                    depy+=(((16*maty)+(16*matx))-16)-32
                                    break
                            except IndexError:
                                if salle.salle[i-1][j]=='0':#porte en haut
                                    matx = j
                                    maty = i-1
                                    trouver=True
                                    matx=salle.nbColonne-matx
                                    depx+=(((32*maty)-(32*matx))+32)+(64*((salle.nbColonne-matx)/2))+31
                                    depy+=(((16*maty)+(16*matx))-16)-32
                                    break
                        else:
                            raise IndexError
                    except IndexError: 
                        #sil'autre char est en dessous
                        if salle.salle[i+1][j]==char:
                            try:
                                if salle.salle[i][j+1]=='0':#porte à droite
                                    matx = j+1
                                    maty = i
                                    trouver=True
                                    matx=salle.nbColonne-matx
                                    depx+=((32*maty)-(16*matx)-16)+(64*((salle.nbColonne-matx)/2))
                                    depy+=(((16*maty)+(16*matx))-16)-32
                                    break
                            except IndexError:
                                if salle.salle[i][j-1]=='0':#porte à gauche
                                    matx = j-1
                                    maty = i
                                    trouver=True
                                    matx=salle.nbColonne-matx
                                    depx+=(((32*maty)-(32*matx))+32)+(32*((salle.nbColonne-matx)/2))
                                    depy+=(((16*maty)+(16*matx))-16)-32
                                    break
            if trouver:
                break
        
        perso.posMatY=maty
        perso.posMatX=salle.nbColonne-matx
        
        perso.posMapX=depx
        perso.posMapY=depy
        
        self.calculPositionDepart(perso,salle)
        
        self.calculPositionMilieu(salle)

        return perso
        
    
    def vueProximite(self,posMat,nb):
        rayon=8
        limite=list()
        
        if posMat <rayon:
            limite.append(-1)
            limite.append((rayon*2)-1)
        elif posMat> (nb-rayon):
            limite.append(nb-(rayon*2))
            limite.append(nb)
        elif posMat>=rayon and posMat<= (nb-(rayon)):
            limite.append(posMat-rayon)
            limite.append(posMat+rayon)
            
        return limite