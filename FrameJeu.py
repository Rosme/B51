# -*- coding: ISO-8859-1 -*-
import tkinter
import math
import HudHaut
import MenuInventaire

class FrameJeu():
    def __init__(self,parent):
        self.parent = parent
        
        #dimensions du jeu
        self.largeurJeu=4000
        self.hauteurJeu=4000
        
        #dimensions des tuiles affichées
        self.largeurTuile=40
        self.hauteurTuile=40
        
        #assignation de valeur plus tard pour la position des scrollbars
        self.offX=0
        self.offY=0
    
    def debutDePartie(self,perso,laSalle):
        #appelé a chaque fois que l'on meurt ou que l'on débute une partie
        #variable déterminant si le joueur a déjà été affiché (utilisé dans affichagePerso)
        self.persoAff=True
		
        #position des premiers blocs
        self.calculPositionDepart(laSalle,perso)
    
    def initMap(self,perso,laSalle):
        #appelé une seule fois à la création d'une partie
        self.debutDePartie(perso,laSalle)
        #création du frame principale du jeu
        #contient le haud du haut et l'affichage du jeu
        self.frameDuJeu=tkinter.Frame(self.parent.root)
        
        #création du hud du haut placé dans frameDuJeu
        self.hudHaut=HudHaut.HudHaut(self,perso,self.parent.root)
        
        self.menuI= MenuInventaire.MenuInventaire(self)
        
        #création des canvas pour le jeu, la scrollbar invisible et le futur chat
        self.dispositionPrincipale()
        
        #calcul de la position de la scrollbar pour voir le personnage
        x,y=self.coordMatriceAEcran(perso)
        self.calculOffSet(x,y)
        
        #affichage de la map, des objets et du personnage à l'écran
        self.affichageMap(perso,laSalle)
        
        #ajout des écouteur (souris, clavier)
        self.ajoutEcouteur()
    
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
        self.posDepartX=(self.largeurJeu/2)-(laSalle.dictMap[perso.nomMap + " dimensions"][1]*self.largeurTuile/2)
        #calcul du centre de l'écran sur les y moins le nombre de colonne de la matrice 
        self.posDepartY=(self.hauteurJeu/2)-((laSalle.dictMap[perso.nomMap + " dimensions"][0]*self.hauteurTuile/2))
        
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
            for k in range(len(map[i])):
                #affichage des murs 
                if map[i][k]=='1' or map[i][k] == '2':
                    self.map.create_image(posTempX,posTempY,image=self.parent.getImage("roche"),tags="image")
                
                #affichage du personnage s'il na pas déjà été affiché
                if self.persoAff==True:
                    #affiche un ligne plus loin pour ne pas être imprimé sous le plancher
                    if perso.posMatX<k and perso.posMatY<i: 
                        self.affichagePerso(perso)
                    
                #affichage du plancher
                if map[i][k]=='0' or map[i][k]=='v' or map[i][k]=='b' or map[i][k]=='n' or map[i][k]=='m':
                    self.map.create_image(posTempX,posTempY,image=self.parent.getImage("gazon"),tags="image")
                    #self.map.create_text(posTempX,posTempY,text=str(i)+","+str(k),tags="text")
                
                if map[i][k]=='f':
                     self.map.create_image(posTempX,posTempY,image=self.parent.getImage("feu"),tags="image")
                
                #affichage des coffres
                if  map[i][k]=='3':
                    #self.map.create_text(posTempX, posTempY, text="Coffre", fill='white', tags="image")
                    self.map.create_image(posTempX,posTempY,image=self.parent.getImage("coffre"),tags="coffre")
                
                #affichage des switchs
                if  map[i][k]=='w':
                    self.map.create_text(posTempX, posTempY, text="Switch", fill='white', tags="image")
                        
                        
                #affichage des leviers
                if  map[i][k]=='e':
                    self.map.create_text(posTempX, posTempY, text="Levier", fill='white', tags="image")
                
                #affichage des logomates
                #for p in self.parent.parent.jeu.listeLogomate:
                   # if p.posMatX<k and p.posMatY<i:
                        #x,y=self.coordMatriceAEcran(perso)
                        #self.map.create_image(x,y-16,image=self.parent.getImage("pers"),tags="perso")
                   
                posTempX+=(self.largeurTuile)
            posInitY+=(self.hauteurTuile)
        
    def affichagePerso(self,perso):
        #affichage du personnage
        #on supprime le perso précedement affiché
        self.map.delete("perso")
        x,y=self.coordMatriceAEcran(perso)
        self.map.create_image(x,y-16,image=self.parent.getImage("pers"),tags="perso")
        self.calculOffSet(x,y)
        #puisque le perso a été affiché on ne l'affiche plus
        self.persoAff=False
        
    def tire(self,listeBalle):
        #affichage de toutes les balles existantes s
        for i in listeBalle:
            x,y=self.coordMatriceAEcran(i)   
            self.map.create_oval(x-5, y-5, x+5,y+5, fill='red', tags="balle")
    
    def ajoutEcouteur(self):
        #ecouteur lié au clavier       
        self.parent.root.bind("<KeyPress>",self.parent.parent.peseKeyGestion)
        self.parent.root.bind("<KeyRelease>",self.parent.parent.relacheKeyGestion)
        #ecouteur lié à la souris
        self.parent.root.bind("<Button-1>", self.parent.parent.peseTire)
        self.parent.root.bind("<ButtonRelease-1>", self.parent.parent.relacheTire)
        self.parent.root.bind("<B1-Motion>", self.parent.parent.tireCoord)
    
    def coordEcranAMatrice(self,x,y):
        #permet de trouver à partie des coordonnées d'un personnage dans l'écran sa position sur la matrice
        resteX = math.floor((x-self.posDepartX)/self.largeurTuile)
        resteY = math.floor((y-self.posDepartY)/self.hauteurTuile)
        
        return resteY,resteX
    
    def coordMatriceAEcran(self,divers):
        depx=self.posDepartX
        depy=self.posDepartY
        
        depx+=self.largeurTuile*divers.posMatX
        depy+=self.hauteurTuile*divers.posMatY
        
        return depx,depy
    
    def actualiserAffichage(self,perso,laSalle):
        self.effaceMap()
        
        x,y=self.coordMatriceAEcran(perso)    
        self.calculOffSet(x,y)
            
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
        self.frameDuJeu.pack_forget()
        self.parent.parent.partieCommencer=False
