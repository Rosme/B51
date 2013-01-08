# -*- coding: ISO-8859-1 -*-
import Vue
import Modele
import os
import ConnecteurReseau as Network
import Netdata as nd

class Controleur():
    ############################# Methode d'initialisation de l'aplication #############################
    def __init__(self):
        self.demarrer()
        self.app.root.mainloop()
    
    def demarrer(self):
        self.network = Network.ConnecteurReseau(self)
        self.jeu = Modele.Jeu(self)
        self.app = Vue.Application(self, self.jeu.subDivision)
        self.press = False
        self.contexte="menu"
        self.compteur=0
        self.partieCommencer=False
        self.app.menuPrincipal()

        self.ownEventQueue = []
        self.totalEventQueue = []
        
    
    ############################# Méthode (boucle) d'actualisation du Jeu #############################
    def miseAJour(self):
        #si la partie est commencé
        if self.partieCommencer:
            #on bouge le personnage
            self.jeu.bougePersonnage()
            #on active les switchs,leviers,etc
            self.jeu.activationObjet()
            #on actualise le hud du haut
            self.app.hudH.actualiser(self.jeu.getPlayerById(self.network.id))
            #on vérifie que le joueur n'est pas mort
            self.jeu.gestionMort()
            
            if self.compteur%20==0:
                #recharge de l'énergie de l'arme
                self.jeu.rechargement()
            if self.compteur%1==0:
                #vérifie les collions du personnage et des balles
                self.jeu.balle() 
            if self.compteur%1==0:
                self.jeu.tire()

            self.network.sendData(nd.ClientTickInfo(self.network.id, self.compteur, self.ownEventQueue))

            self.network.recevoirDonnees()

            for listEvents in self.totalEventQueue:
                if self.compteur in listEvents: #Si on est dans le frame avec des events
                    listEventData = listEvents[self.compteur] #List des evenements pour le frame
                    for tickData in listEventData: #Liste des events par id au frame
                        self.jeu.treatEventsById(tickData)
                    listEvents.pop(self.compteur, None) #On enleve le frame de la liste
            self.ownEventQueue = []
            
            self.compteur+=1
            
            self.app.frameJeu.map.after(25,self.miseAJour)


    def mettreAJourAutreClient(self, id, events):
        pass

    ############################# Méthode d'initialisation du Jeu et de l'actualisation du Jeu #############################
    def enJeu(self):
        self.contexte="enJeu"
        self.partieCommencer=True
        
        self.jeu.carte.chargeObjets()
        self.app.jeu(self.jeu.getPlayerById(self.network.id),self.jeu.listePersonnage)
        #ajout des écouteur (souris, clavier)
        self.ajoutEcouteur()
        self.miseAJour()
    
    def actualiserAffichageComplet(self,perso,listePerso):
        self.app.frameJeu.actualiserAffichage(perso,listePerso)
        #self.app.frameJeu.affichageRoche(perso,self.jeu.listeRoche)
    
    def actusliserPersonnage(self):
        self.app.frameJeu.effaceLesPersos()
        for joueur in self.jeu.listePersonnage:
            self.app.frameJeu.affichagePerso(joueur)
        #self.app.frameJeu.affichageRoche(perso,self.jeu.listeRoche)

    def actualisationBalle(self,listeBalle):
        self.app.frameJeu.map.delete("balle")
        self.app.frameJeu.tire(listeBalle)    
    
    #############################Gestion de la mort#############################    
    def joueurMort(self,perso,laSalle):
        self.app.frameJeu.debutDePartie(perso,lasalle)
        self.actualiserAffichageComplet(perso,lasalle)
    
    ############################# Méthodes en lien avec la création et la suppression d'éléments du modèle #############################
    def raceInfo(self, race):
        return self.jeu.info(race)
        
    def nouveauJoueur(self, id, race, nom):
        self.jeu.nouveauJoueur(id, race, nom)
        
    def autoSoin(self):
        self.jeu.joueur.autoSoin()
        
    def rajoutMetal(self):
        self.jeu.rajoutMetal()
        
    def rajoutElectro(self):
        self.jeu.rajoutElectro()
        
    def rajoutBatterie(self):
        self.jeu.rajoutBatterie()
        
    def fabricationArmure(self):
        self.jeu.artisanat.fabricationArmure()
    
    def fabricationFusil(self):
        self.jeu.artisanat.fabricationFusil()
        
    def fabricationDematerialisateur(self):
        self.jeu.artisanat.fabricationDematerialisateur()
    
    #############################Ajout d'ecouteur#############################
    def ajoutEcouteur(self):
        #ecouteur lié au clavier       
        self.app.root.bind("<KeyPress>",self.peseKeyGestion)
        self.app.root.bind("<KeyRelease>",self.relacheKeyGestion)
        #ecouteur lié à la souris
        self.app.frameJeu.map.bind("<Button-1>", self.peseTire)
        self.app.frameJeu.map.bind("<ButtonRelease-1>", self.relacheTire)
        self.app.frameJeu.map.bind("<B1-Motion>", self.tireCoord)
    
    ############################# Méthodes en lien avec les events de l'utilisateur #############################
    def peseKeyGestion(self, event):
        key = event.char.upper()
        if self.contexte=="enJeu":
            if key == 'W':
                self.ownEventQueue.append("MOVE_UP")
            if key == 'D':
                self.ownEventQueue.append("MOVE_RIGHT")
            if key == 'S':
                self.ownEventQueue.append("MOVE_DOWN")
            if key == 'A':
                self.ownEventQueue.append("MOVE_LEFT")
                
            if key == 'Q':
                self.autoSoin()
                
            if key == 'M':
                self.jeu.joueur.touche(10)
            
            if key == 'E':
                if self.jeu.listeRoche:
                    for i in self.jeu.listeRoche:
                        if i.nomMap == self.jeu.joueur.nomMap:
                            if not i.prendre(self.jeu.joueur):
                                i.bouge(self.jeu.joueur)
                            else:
                                i.depose()
                
                if self.jeu.listeLevier and not self.press:
                    for i in self.jeu.listeLevier:
                        if i.nomMap == self.jeu.joueur.nomMap:
                            if i.collision(self.jeu.joueur):
                                if i.tire():
                                    if i.activer():
                                        self.app.frameJeu.actualiserAffichage(self.jeu.joueur,self.jeu.carte.s)
                                    
                if self.jeu.listeCoffre:
                    for i in self.jeu.listeCoffre:
                        if i.nomMap == self.jeu.joueur.nomMap:
                            i.ouvrir(self.jeu.joueur)
                        
                self.press = True
    
    def relacheKeyGestion(self, event):
        key = event.char.upper()
        
        if self.contexte=="enJeu":
            if key == 'W':
                self.ownEventQueue.append("NO_UP")
            if key == 'D':
                self.ownEventQueue.append("NO_RIGHT")
            if key == 'S':
                self.ownEventQueue.append("NO_DOWN")
            if key == 'A':
                self.ownEventQueue.append("NO_LEFT")
            if key == 'E':
                self.press = False
            
            if event.keysym == 'Escape':
                self.app.effaceTout()
                
                del self.jeu
                self.jeu = Modele.Jeu(self)
                
                self.press = False
                self.contexte="menu"
                self.compteur=0
                self.partieCommencer=False
                self.jeu.listePersonnage = list()


                self.app.initialisationInterfaces()
                self.app.menuPrincipal()
                if self.network.socket != None:
                    self.network.disconnect()
            
        
        
        if key=='I':
            if self.contexte == "enJeu":
                self.contexte="inventaire"
                self.app.menuInventaire()
            elif self.contexte == "inventaire":
                #faire disparaitre l'inventaire
                pass
        
        if key == 'Z':
            pass
            
       
        
    def peseTire(self,event):
        pass
        '''
        if self.contexte == "enJeu":
            self.jeu.mouvement[4] = True
            self.jeu.sourisX = event.x
            self.jeu.sourisY = event.y  
        '''
        
    def relacheTire(self,event):
        pass
        #self.jeu.mouvement[4] = False
    
    #prend a chaque deplacement de souris la nouvelle position en x,y de la souris
    def tireCoord(self,event):
        pass
        '''
        if self.jeu.mouvement[4]:
            x,y = self.app.frameJeu.coordMatriceAEcran(self.jeu.joueur)
            x-=self.app.largeurFrame/2
            y-=self.app.hauteurFrame/2
            self.jeu.sourisY, self.jeu.sourisX = self.app.frameJeu.coordEcranAMatrice(event.x+x,event.y+y)
        '''

    def getMap(self):
        return self.jeu.getCurrentSalle()
        
    def getMapByName(self,name):
        return self.jeu.getSalleByName(name)
    
    def getIdPlayer(self):
        return self.jeu.getPlayerById(self.network.id).id

if __name__ == '__main__':
    c = Controleur()