# -*- coding: ISO-8859-1 -*-
import tkinter
import math
import MenuInventaire

class FrameJeu():
    #############################Initialisation de variables#############################
    def __init__(self,parent,subDivision):
        self.parent = parent
        self.subDivision=subDivision
        
        #dimensions du jeu
        self.largeurJeu=4000
        self.hauteurJeu=4000
        
        #dimensions des tuiles affichées
        self.largeurTuile=32
        self.hauteurTuile=32
        
        #assignation de valeur plus tard pour la position des scrollbars
        self.offX=0
        self.offY=0
    
    def debutDePartie(self,perso,laSalle):		
        #position des premiers blocs
        self.calculPositionDepart(laSalle,perso)
    
    def initMap(self,perso,listePerso):
        laSalle = self.parent.parent.getMap()
        
        #appelé une seule fois à la création d'une partie
        self.debutDePartie(perso,laSalle)
        
        #création du frame principale du jeu
        #contient le haud du haut et l'affichage du jeu
        self.frameDuJeu=tkinter.Frame(self.parent.root)
        
        self.menuI= MenuInventaire.MenuInventaire(self)
        
        #création des canvas pour le jeu, la scrollbar invisible et le futur chat
        self.dispositionPrincipale()
        
        #affichage de la map, des objets et du personnage à l'écran
        self.affichageMap(perso,listePerso)
    
    def dispositionPrincipale(self):
        #appelé une seule fois lors d'une nouvelle partie
        #création des scrollbars en x et y
        self.xscrollbar = tkinter.Scrollbar(self.frameDuJeu, orient=tkinter.HORIZONTAL)
        self.yscrollbar = tkinter.Scrollbar(self.frameDuJeu)

        #creation du canvas contenant la map, perso...
        self.map=tkinter.Canvas(self.frameDuJeu,width=self.parent.largeurFrame,height=self.parent.hauteurFrame,  bg="#000",highlightbackground="#000",highlightcolor="#000",highlightthickness=0)
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
        
    #############################Affichage à l'écran#############################
    def affichageMap(self,perso,listePerso): 
        map = self.parent.parent.getMapByName(perso.nomMap)
        
        x,y=self.coordMatriceAEcran(perso) 
        self.calculOffSet(x,y)
        self.effaceLesPersos()
        
        #position de la tuile la plus haute affiché dans l'écran
        posInitX=self.posDepartX
        posInitY=self.posDepartY
        
        #affichage de toutes les tuiles de la map ainsi que le personnage et les objets
        #passe toutes les lignes de la map
        for i in range(0,len(map),self.subDivision):
            posTempX=posInitX
            posTempY=posInitY
            for k in range(0,len(map[i]),self.subDivision):
                self.affichageImage(map[i][k],posTempX,posTempY)
                
                for pers in listePerso:
                    if pers.nomMap == perso.nomMap:
                        #affiche un ligne plus loin pour ne pas être imprimé sous le plancher
                        if pers.posMatX==k and pers.posMatY==i:
                            self.affichagePerso(pers)
                '''
                #affichage des logomates
                for p in self.parent.parent.jeu.listeLogomate:
                    if p.posMatX<k and p.posMatY<i:
                        x,y=self.coordMatriceAEcran(perso)
                        self.map.create_image(x,y-16,image=self.parent.getImage("pers"),tags="perso")
                '''   
                posTempX+=(self.largeurTuile)
            posInitY+=(self.hauteurTuile)
        
    def affichageImage(self,car,posX,posY):
        nomImage=None
        tag="image"
        texte=None
        
        if car=='v' or car=='b' or car=='n' or car=='m' or car=='B' or car=='V' or car=='N' or car=='M':
            nomImage="zoning"
        elif car=='0':
            nomImage="gazon"
        elif car=='1' or car=='2':
            nomImage="roche"
            posY-=14
            '''elif car=='3':
            tag="coffre"
            nomImage=d"coffre"'''
        elif car=='e':
            texte="Levier"
        elif car=='w':
            texte="Switch"
        elif car=='f':
            nomImage="feu"
        elif car=="u":
            nomImage="simonBleu"
        elif car=="i":
            nomImage="simonJaune"
        elif car=="o":
            nomImage="simonRouge"
        elif car=="p":
            nomImage="simonVert"
        elif car=="y":
            nomImage="eau"
        
        
        if nomImage:
            self.map.create_image(posX,posY,image=self.parent.getImage(nomImage),tags=tag)
        if texte:
            self.map.create_text(posX, posY, text=texte, fill='white', tags=tag)
    
    def affichagePerso(self,perso):
        #affichage du personnage
        x,y=self.coordMatriceAEcran(perso)
        
        if perso.id == self.parent.parent.getIdUsagerLocal():
            self.calculOffSet(x,y)
        
        self.map.create_text(x, y-67, text=perso.nom, fill='white', tags="perso")
        self.map.create_image(x,y-28,image=self.parent.getImage("pers")[perso.animationId],tags="perso")

    
    def affichageRoche(self,perso,listeRoche):
        for i in listeRoche:
            if i.nomMap == perso.nomMap:
                tempPosX, tempPosY = self.coordMatriceAEcran(i)
                self.map.create_rectangle(tempPosX, tempPosY, tempPosX+31, tempPosY+31, fill='blue', tags="perso")
                
        
    def tire(self,listeBalle):
        #affichage de toutes les balles existantes 
        for i in listeBalle:
            if self.parent.parent.getPlayerById(i.ownerId).nomMap == self.parent.parent.getPlayerLocal().nomMap:
                x,y=self.coordMatriceAEcran(i)   
                self.map.create_oval(x, y, x+5,y+5, fill='red', tags="balle")

    def actualiserAffichage(self,perso,listePerso):
        self.map.delete(tkinter.ALL)
        self.affichageMap(perso,listePerso)
    
    #############################Calcul de postion#############################
    def calculPositionDepart(self,laSalle,perso):
        #calcul la position de la première tuile a être affiché de la map
        #calcul du centre de l'écran sur les X
        self.posDepartX=(self.largeurJeu/2)-(laSalle.dictMap[perso.nomMap + " dimensions"][1]*self.largeurTuile/2)
        #calcul du centre de l'écran sur les y moins le nombre de colonne de la matrice 
        self.posDepartY=(self.hauteurJeu/2)-((laSalle.dictMap[perso.nomMap + " dimensions"][0]*self.hauteurTuile/2))
        
    def coordEcranAMatrice(self,x,y):
        #permet de trouver à partie des coordonnées d'un personnage dans l'écran sa position sur la matrice
        resteX = math.floor((x-self.posDepartX)/(self.largeurTuile/self.subDivision))
        resteY = math.floor((y-self.posDepartY)/(self.hauteurTuile/self.subDivision))
        
        return int(resteY),int(resteX)
    
    def coordMatriceAEcran(self,divers):
        depx=self.posDepartX+(divers.posMatX/(self.hauteurTuile/self.subDivision))
        depy=self.posDepartY+(divers.posMatY/(self.largeurTuile/self.subDivision))
        
        return int(depx),int(depy)
    
    #############################Modification des scrollbars#############################
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
    
    #############################Supression de masse#############################    
    def effacer(self):
        self.frameDuJeu.pack_forget()
        self.parent.parent.partieCommencer=False
    def effaceLesPersos(self):
        #on supprime le perso précedement affiché
        self.map.delete("perso")
