# -*- coding: ISO-8859-1 -*-
import tkinter
import math

class FrameJeu():
    def __init__(self,parent):
        self.parent = parent
        
        #dimensions du jeu
        self.largeurJeu=4000
        self.hauteurJeu=4000
        
        #dimensions des tuiles affiches
        self.largeurTuile=64
        self.hauteurTuile=32
        
        self.importerImage()
        
        self.frameDuJeu=tkinter.Frame(self.parent.root)
        self.frameHudHaut=tkinter.Frame(self.parent.root)
        
        self.xscrollbar = tkinter.Scrollbar(self.frameDuJeu, orient=tkinter.HORIZONTAL)
        self.yscrollbar = tkinter.Scrollbar(self.frameDuJeu)
        
        self.offX=0.37
        self.offY=0.42
    def initMap(self,perso,laSalle):       
        #position du joueur centre dans l'ecran
        perso.posMapX=self.largeurJeu/2
        perso.posMapY=self.hauteurJeu/2
        
        self.persoAff=True
        
        #position des premiers blocs
        self.calculPositionDepart(laSalle)

        self.calculPositionMilieu(laSalle)

        perso.posMatX,perso.posMatY=self.coord(perso.posMapX,perso.posMapY)
        
        self.dispositionPrincipale()
        
        self.affichageMap(perso,laSalle)
        
        return perso
    def dispositionPrincipale(self):
        #creation du fond noir derriere la map
        self.map=tkinter.Canvas(self.frameDuJeu,width=1024,height=700,  bg="#000")
        self.map.config(scrollregion=(0,0,4000,4000),xscrollcommand=self.xscrollbar.set,yscrollcommand=self.yscrollbar.set)
        self.map.pack()
        self.xscrollbar.config(command=self.map.xview)
        self.yscrollbar.config(command=self.map.yview)
        self.frameDuJeu.pack()
        self.map.xview(tkinter.MOVETO,self.offX)
        self.map.yview(tkinter.MOVETO,self.offY)
		
        #chat
        self.frameHudBas= tkinter.Frame(self.parent.root)
        self.conversation=tkinter.Canvas(self.frameHudBas, width=self.largeurJeu, height=self.parent.hauteurFrame-self.hauteurJeu,bg="blue")
        self.conversation.pack()
    
    def importerImage(self):
        self.roche=tkinter.PhotoImage(file="assets/image/rock1.gif")
        self.gazon=tkinter.PhotoImage(file="assets/image/grass.gif")
        self.pers=tkinter.PhotoImage(file="assets/image/f1.gif")
    
    def ajoutEcouteuretBoucle(self):
        self.ajoutEcouteur()
        self.parent.parent.miseAJour()
        self.parent.parent.rechargement()
        self.parent.parent.balle()
    
    def calculPositionDepart(self,laSalle):
        self.posDepartX=self.largeurJeu/2
        self.posDepartY=(self.hauteurJeu/2)-(laSalle.nbColonne*16)
        
    def calculPositionMilieu(self,laSalle):
        self.posMilieuDiagoX=(self.posDepartX-(laSalle.nbColonne-1)*32)-32
        self.posMilieuDiagoY=(self.posDepartY+(laSalle.nbLigne-1)*16)
    
    def affichageMap(self,perso,laSalle):
        map=laSalle.salle
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
                if map[i][k]=='1' or map[i][k] == '2':
                    self.map.create_image(posTempX,posTempY-16,image=self.roche,tags="image")
                if self.persoAff==True:
                    if perso.posMatX<k and perso.posMatY<i: 
                        self.affichagePerso(perso)
                    
                #affichage du gazon
                if map[i][k]=='0' or map[i][k]=='v' or map[i][k]=='b' or map[i][k]=='n' or map[i][k]=='m':
                    self.map.create_image(posTempX,posTempY,image=self.gazon,tags="image")
                    self.map.create_text(posTempX,posTempY,text=str(i)+","+str(k),tags="text")
                
                if  map[i][k]=='3':
                    self.map.create_text(posTempX, posTempY, text="Coffre", fill='white', tags="image")
                
                if  map[i][k]=='w':
                    self.map.create_text(posTempX, posTempY, text="Switch", fill='white', tags="image")
                        
                if  map[i][k]=='e':
                    self.map.create_text(posTempX, posTempY, text="Levier", fill='white', tags="image")
                    
                #for p in self.parent.parent.jeu.listeLogomate:
                   # if p.posMatX<k and p.posMatY<i:
                        #self.map.create_image(perso.posMapX+(p.posMapX - perso.posMapX),perso.posMapY+(p.posMapY - perso.posMapY)-32,image=self.pers,tags="logo")
                     
                   
                #apres chaque affichage, on se dirige dans l'ecran en bas a gauche
                posTempX-=(self.largeurTuile/2)
                posTempY+=(self.hauteurTuile/2)
            #apres chaque ligne, on calcul la position de le premiere tuile de la prochaine ligne a etre affiche
            posInitX+=(self.largeurTuile/2)
            posInitY+=(self.hauteurTuile/2)
        
        #calcul de la position x,y en pixel de la tuile la plus pret de la diagonale dans le tableau
        #si une map est carre, cette valeur represente la position x,y dans l'ecran de la tuile la plus a gauche
        self.calculPositionMilieu(laSalle)
        
        #if self.parent.parent.jeu.listePersonnage:
            #temp = self.parent.parent.jeu.listePersonnage[0].obtenirLimite()
            #self.map.create_image(perso.posMapX+(self.parent.parent.jeu.listePersonnage[0].posMapX - perso.posMapX),perso.posMapY+(self.parent.parent.jeu.listePersonnage[0].posMapY- perso.posMapY)-32, image=self.pers, tags="p")
            
        #if self.parent.parent.jeu.listeRoche:
            #temp = self.parent.parent.jeu.listeRoche[0].obtenirLimite()
            #self.map.create_rectangle(perso.posMapX+ temp[0]- perso.posMapX, perso.posMapY+temp[1]- perso.posMapY, perso.posMapX+temp[2]- perso.posMapX, perso.posMapY+temp[3]- perso.posMapY, fill='blue', tags="p")
        
        self.map.create_rectangle((self.largeurJeu/2)-2,(self.hauteurJeu/2)-2,(self.largeurJeu/2)+2,(self.hauteurJeu/2)-2,fill='red')

        #self.dessinehud(perso)
    
    
    def affichagePerso(self,perso):
        #affichage du personnage
        self.map.delete("perso")
        temp = perso.obtenirLimite()
        #self.map.create_rectangle(perso.posMapX+ temp[0]- perso.posMapX, perso.posMapY+temp[1]- perso.posMapY, perso.posMapX+temp[2]- perso.posMapX, perso.posMapY+temp[3]- perso.posMapY, fill='red', tags="perso")
        self.map.create_image(perso.posMapX,perso.posMapY-32,image=self.pers,tags="perso")
        self.persoAff=False
        
    def dessinehud(self,perso):
        nbSeringue=0
        poidsJoueur=0
        grandeurVie=(perso.race.vie*120)/perso.race.max_vie
        for i in perso.inventaire.items:
            if i.id==8:
                grandeurShield=(i.energie*120)/i.max_energie
            if i.id==7:
                grandeurArme=(i.energie*120)/i.max_energie
            if i.id == 3:
                nbSeringue+=1
            poidsJoueur+=i.poids
  
         # la barre pour la vie du joueur. 
        self.energy = tkinter.PhotoImage(file='assets/image/energy.gif',width=35,height=35)
        self.map.create_image(85,40, image= self.energy)
        self.map.create_rectangle(35, 60,grandeurVie+35, 75,fill="blue",tag="hudhaut")
        
        #le shield
        self.shield = tkinter.PhotoImage(file='assets/image/bouclier.gif',width=45,height=35)
        self.map.create_image(280,40, image= self.shield)
        self.map.create_rectangle(235, 60, grandeurShield+235, 75,fill="blue",tag="hudhaut")
        
        #le gun power
        self.gunpower = tkinter.PhotoImage(file='assets/image/gun.gif',width=45,height=35)
        self.map.create_image(455,40, image= self.gunpower)
        self.map.create_rectangle(410, 60, grandeurArme+410, 75,fill="blue",tag="hudhaut")
        
        #le healing
        self.healing=tkinter.PhotoImage(file='assets/image/syringe.gif',width=45,height=35)
        self.map.create_image(610,40, image= self.healing)
        self.map.create_text(640,40,text=nbSeringue,fill='white',font=("Arial","10"),tag="hudhaut")
        # le poid que le joueur peut avoir
        self.poids=tkinter.PhotoImage(file='assets/image/backpack.gif',width=40,height=35)
        self.map.create_image(785,40, image= self.poids)
        self.map.create_text(835,40,text=str(poidsJoueur)+" /"+str(personnage.race.poidsLimite),fill='white',font=("Arial","10"),tag="hudhaut")
    def tire(self):  
        for i in self.parent.parent.jeu.listeBalle:
            self.map.create_oval(i.posMapX-5, i.posMapY-5, i.posMapX, i.posMapY, fill='red', tags="balle")
    
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
        print(y,x)
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
        
        self.calculPositionDepart(salle)
        
        self.calculPositionMilieu(salle)

        return perso
        
        
    def depl(self,tempx,tempy):
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
        print(self.offX,self.offY)