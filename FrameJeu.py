# -*- coding: ISO-8859-1 -*-
import tkinter
import math
import HudHaut

class FrameJeu():
    def __init__(self,parent):
        self.parent = parent
        
        #dimensions du jeu
        self.largeurJeu=4000
        self.hauteurJeu=4000
        
        #dimensions des tuiles affichées
        self.largeurTuile=64
        self.hauteurTuile=32
        
        #assignation de valeur plus tard pour la position des scrollbars
        self.offX=0
        self.offY=0
        
        #importation des images
        self.importerImage()
        
    def importerImage(self):
        self.roche=tkinter.PhotoImage(file="assets/image/rock1.gif")
        self.gazon=tkinter.PhotoImage(file="assets/image/grass.gif")
        self.pers=tkinter.PhotoImage(file="assets/image/f1.gif")
        self.coffre=tkinter.PhotoImage(file="assets/image/coffre.gif")
        
    def posInitPerso(self):
        #position du joueur centrer dans l'ecran et dans le canvas
        return self.largeurJeu/2,self.hauteurJeu/2
    
    def debutDePartie(self,perso,laSalle):
        #appelé a chaque fois que l'on meurt ou que l'on débute une partie
        #position du personnage dans la mainRoom
        perso.posMapX,perso.posMapY=self.posInitPerso()
        
        #variable déterminant si le joueur a déjà été affiché (utilisé dans affichagePerso)
        self.persoAff=True
		
        #position des premiers blocs
        self.calculPositionDepart(laSalle,perso)
        
        #calcul du point le plus à gauche de la map
        self.calculPositionMilieu(laSalle,perso)
        
        #calcul de la position du personnage dans la matrice par rapport a sa position relative au canvas
        perso.posMatX,perso.posMatY=self.coordEcranAMatrice(perso.posMapX,perso.posMapY)
        
        return perso
    
    def initMap(self,perso,laSalle):
        #appelé une seule fois à la création d'une partie
        #création du frame principale du jeu
        #contient le haud du haut et l'affichage du jeu
        self.frameDuJeu=tkinter.Frame(self.parent.root)
        
        
         
        #initialisation relatif à la map et au personnage
        perso=self.debutDePartie(perso,laSalle)
        
        #création du hud du haut placé dans frameDuJeu
        self.hudHaut=HudHaut.HudHaut(self,perso,self.frameDuJeu)
            
        #création des canvas pour le jeu, la scrollbar invisible et le futur chat
        self.dispositionPrincipale()
        
        #calcul de la position de la scrollbar pour voir le personnage
        self.calculOffSet(perso.posMapX,perso.posMapY)
        
        #affichage de la map, des objets et du personnage à l'écran
        self.affichageMap(perso,laSalle)
        
        #ajout des écouteur (souris, clavier)
        self.ajoutEcouteur()
		
        return perso
    
    def dispositionPrincipale(self):
        #appelé une seule fois lors d'une nouvelle partie
        #création des scrollbars en x et y
        self.xscrollbar = tkinter.Scrollbar(self.frameDuJeu, orient=tkinter.HORIZONTAL)
        self.yscrollbar = tkinter.Scrollbar(self.frameDuJeu)

        #creation du canvas contenant la map, perso...
        self.map=tkinter.Canvas(self.frameDuJeu,width=1024,height=700,  bg="#000",highlightbackground="#000",highlightcolor="#000",highlightthickness=0)
        self.map.config(scrollregion=(0,0,self.largeurJeu,self.hauteurJeu),xscrollcommand=self.xscrollbar.set,yscrollcommand=self.yscrollbar.set)
        self.map.pack()
        self.frameDuJeu.pack()
        
        #configuration des scrollbars
        self.xscrollbar.config(command=self.map.xview)
        self.yscrollbar.config(command=self.map.yview)
        self.map.xview(tkinter.MOVETO,self.offX)
        self.map.yview(tkinter.MOVETO,self.offY)
		
        '''#chat
        self.frameHudBas= tkinter.Frame(self.parent.root)
        self.conversation=tkinter.Canvas(self.frameHudBas, width=self.largeurJeu, height=self.parent.hauteurFrame-self.hauteurJeu,bg="blue")
        self.conversation.pack()'''
    
    def calculPositionDepart(self,laSalle,perso):
        #calcul la position de la première tuile a être affiché de la map
        #calcul du centre de l'écran sur les X
        self.posDepartX=(self.largeurJeu/2)
        #calcul du centre de l'écran sur les y moins le nombre de colonne de la matrice 
        self.posDepartY=(self.hauteurJeu/2)-((laSalle.dictMap[perso.nomMap + " dimensions"][0]*16))+32
        
    def calculPositionMilieu(self,laSalle,perso):
        #calcul les coordonnées du point dans le canvas le plus à gauche ou à la position (0,0) de la matrice
        self.posMilieuDiagoX=(self.posDepartX-(laSalle.dictMap[perso.nomMap + " dimensions"][0]-1)*32)-32
        self.posMilieuDiagoY=(self.posDepartY+(laSalle.dictMap[perso.nomMap + " dimensions"][1]-1)*16)
    
    def calculOffSet(self,x,y):
        #calcul du pourcentage sur les 2 axe de la position du personnage
        self.offX=(x/self.largeurJeu)
        self.offY=(y/self.hauteurJeu)
        #ajustement de la position de la scrollbar
        self.ajustOffSet()
    
    def ajustOffSet(self):
        #ajustement de la position de la scrollbar
        self.offX-=0.13
        self.offY-=0.08
        #fix un problème de clignement lors des premiers mouvement en x,y du joueur
        self.deplScrollBar(-4,-4)
        self.deplScrollBar(4,4)
        
    def affichageMap(self,perso,laSalle):
        map=laSalle.salle
        
        #variable déterminant si le joueur a déjà été affiché (utilisé dans affichagePerso)
        self.persoAff=True
        
        #print(perso.posMapX,perso.posMapY,self.posDepartX,self.posDepartY,self.posMilieuDiagoX,self.posMilieuDiagoY)
        #position de la tuile la plus haute affiché dans l'écran
        posInitX=self.posDepartX
        posInitY=self.posDepartY
        
        #affichage de toutes les tuiles de la map ainsi que le personnage et les objets
        #passe toutes les lignes de la map
        for i in range(len(map)):
            #retour en haut a droite de l'ecran
            posTempX=posInitX
            posTempY=posInitY
            #passe toutes les elements de la ligne 1 par 1
            for k in range(len(map[i])-1,-1,-1):
                #affichage des murs 
                if map[i][k]=='1' or map[i][k] == '2':
                    self.map.create_image(posTempX,posTempY-16,image=self.roche,tags="image")
                
                #affichage du personnage s'il na pas déjà été affiché
                if self.persoAff==True:
                    #affiche un ligne plus loin pour ne pas être imprimé sous le plancher
                    if perso.posMatX<k and perso.posMatY<i: 
                        self.affichagePerso(perso)
                    
                #affichage du plancher
                if map[i][k]=='0' or map[i][k]=='v' or map[i][k]=='b' or map[i][k]=='n' or map[i][k]=='m':
                    self.map.create_image(posTempX,posTempY,image=self.gazon,tags="image")
                    #self.map.create_text(posTempX,posTempY,text=str(i)+","+str(k),tags="text")
                
                #affichage des coffres
                if  map[i][k]=='3':
                    #self.map.create_text(posTempX, posTempY, text="Coffre", fill='white', tags="image")
                    self.map.create_image(posTempX,posTempY-17,image=self.coffre,tags="coffre")
                
                #affichage des switchs
                if  map[i][k]=='w':
                    self.map.create_text(posTempX, posTempY, text="Switch", fill='white', tags="image")
                        
                        
                #affichage des leviers
                if  map[i][k]=='e':
                    self.map.create_text(posTempX, posTempY, text="Levier", fill='white', tags="image")
                
                #affichage des logomates
                for p in self.parent.parent.jeu.listeLogomate:
                    if p.posMatX<k and p.posMatY<i:
                        self.map.create_image(perso.posMapX+(p.posMapX - perso.posMapX),perso.posMapY+(p.posMapY - perso.posMapY)-32,image=self.pers,tags="logo")
                                           
                #apres chaque affichage, on se se déplace d'une tuile en bas a gauche
                posTempX-=(self.largeurTuile/2)
                posTempY+=(self.hauteurTuile/2)
            #apres chaque ligne, on calcul la position de le premiere tuile de la prochaine ligne a etre affiche situé en haut à droite
            posInitX+=(self.largeurTuile/2)
            posInitY+=(self.hauteurTuile/2)
        
        
        #affichage des logomates 2... mauvaise place a vérifier
        if self.parent.parent.jeu.listePersonnage:
            temp = self.parent.parent.jeu.listePersonnage[0].obtenirLimite()
            self.map.create_image(perso.posMapX+(self.parent.parent.jeu.listePersonnage[0].posMapX - perso.posMapX),perso.posMapY+(self.parent.parent.jeu.listePersonnage[0].posMapY- perso.posMapY)-32, image=self.pers, tags="p")
        
        #affichage des roches... mauvaise place a vérifier
        #if self.parent.parent.jeu.listeRoche:
            #temp = self.parent.parent.jeu.listeRoche[0].obtenirLimite()
            #self.map.create_rectangle(perso.posMapX+ temp[0]- perso.posMapX, perso.posMapY+temp[1]- perso.posMapY, perso.posMapX+temp[2]- perso.posMapX, perso.posMapY+temp[3]- perso.posMapY, fill='blue', tags="p")
            
		
    def affichagePerso(self,perso):
        #affichage du personnage
        #on supprime le perso précedement affiché
        self.map.delete("perso")
        #temp = perso.obtenirLimite()
        #self.map.create_rectangle(perso.posMapX+ temp[0]- perso.posMapX, perso.posMapY+temp[1]- perso.posMapY, perso.posMapX+temp[2]- perso.posMapX, perso.posMapY+temp[3]- perso.posMapY, fill='red', tags="perso")
        self.map.create_image(perso.posMapX,perso.posMapY-32,image=self.pers,tags="perso")
        #puisque le perso a été affiché on ne l'affiche plus
        self.persoAff=False
        
    def tire(self):
        #affichage de toutes les balles existantes s
        for i in self.parent.parent.jeu.listeBalle:
            self.map.create_oval(i.posMapX-5, i.posMapY-5, i.posMapX, i.posMapY, fill='red', tags="balle")
    
    def ajoutEcouteur(self):
        #ecouteur lié au clavier       
        self.parent.root.bind("<KeyPress>",self.parent.parent.peseKeyGestion)
        self.parent.root.bind("<KeyRelease>",self.parent.parent.relacheKeyGestion)
        #ecouteur lié à la souris
        self.parent.root.bind("<Button-1>", self.parent.parent.peseTire)
        self.parent.root.bind("<ButtonRelease-1>", self.parent.parent.relacheTire)
        self.parent.root.bind("<B1-Motion>", self.parent.parent.tireCoord)
    
    def coordEcranAMatrice(self,x1,y1):
        #permet de trouver à partie des coordonnées d'un personnage dans l'écran sa position sur la matrice
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
        return x,y
        
    def coordProchaineZone(self,salle,char,perso):
        #permet le changement de zone
        tempX=0
        tempY=0
        trouver=False
        
        self.calculPositionDepart(salle,perso)
        self.calculPositionMilieu(salle,perso)
        
        for i in range(len(salle.salle)):
            for j in range(len(salle.salle[i])):
                if salle.salle[i][j]==char:
                    try:
                        #si l'autre char à droite
                        if salle.salle[i][j+1]==char:
                            try:
                                if salle.salle[i+1][j]=='0':#porte en haut
                                    matx = j
                                    maty = i+1
                                    trouver=True
                                    break
                            except IndexError:
                                if salle.salle[i-1][j]=='0':#porte en bas
                                    matx = j
                                    maty = i-1
                                    trouver=True
                                    tempX+=32
                                    tempY-=16
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
                                    break
                            except IndexError:
                                if salle.salle[i][j-1]=='0':#porte à gauche
                                    matx = j-1
                                    maty = i
                                    trouver=True                          
                                    break
            if trouver:
                break
        
        tempMatX=salle.dictMap[perso.nomMap + " dimensions"][0]-matx
        
        perso.posMatY=maty
        perso.posMatX=matx
        
        perso.posMapX,perso.posMapY=self.coordMatriceAEcran(tempMatX,maty)
        perso.posMapX+=tempX
        perso.posMapY+=tempY
        
        self.changementDeMap(salle,perso)
        
        return perso
    
    def coordMatriceAEcran(self,x,y):
        depx=self.posDepartX
        depy=self.posDepartY
        depx+=(32*y)-(32*x)+32
        depy+=(16*y)+(16*x)-16
        
        return depx,depy
    
    def changementDeMap(self,laSalle,perso):
        self.effaceMap()
            
        self.calculOffSet(perso.posMapX,perso.posMapY)
            
        self.affichageMap(perso,laSalle)
    
    def deplScrollBar(self,tempx,tempy):
        incr=0.001

        if tempx>0:
            if self.offX+incr<=1.000:
                self.offX+=incr
                self.map.xview(tkinter.MOVETO,self.offX)
        elif tempx<0:
            if self.offX-incr>=0.000:
                self.offX-=incr
                self.map.xview(tkinter.MOVETO,self.offX)

        if tempy>0:
            if self.offY<=1.000:
                self.offY+=incr
                self.map.yview(tkinter.MOVETO,self.offY)
        elif tempy<0:
            if self.offY-incr>=0.000:
                self.offY-=incr
                self.map.yview(tkinter.MOVETO,self.offY)  
        if tempy==0 and tempx==0: 
            self.map.yview(tkinter.MOVETO,self.offX)
            self.map.xview(tkinter.MOVETO,self.offY)
        
    def effaceMap(self):
         self.map.delete(tkinter.ALL)
    
    def effaceTout(self):
        self.frameDuJeu.destroy()
        self.parent.parent.partieCommencer=False
