# -*- coding: ISO-8859-1 -*-
import tkinter
import Personnage
import Item
import Artisanat
class MenuArtisanat():
    def __init__(self, parent):
        self.parent = parent

        self.interface()

        self.v = tkinter.IntVar()
        self.p = tkinter.IntVar()
     
        self.valitem=tkinter.StringVar()
        self.valitem.set("")
         
    def menuArtisanat(self, listeParchemin,itemPerso ):
       
        self.item1=""
        self.item2=""
        self.parch=""

        self.parcheminEnPoche =listeParchemin
        self.itemEnPoche= itemPerso
       
        self.ajoutSectionParchemin()
        self.ajoutSectionItemArtisanat()

        self.cadreUn.pack(side=tkinter.LEFT)
    
    def ajoutSectionItemArtisanat(self):
        ###########################
        # liste des objets dans l'artisanat que le joueur possede
        ###########################
        self.canevabouton=tkinter.Canvas(self.lecadre, bg='#FFFFFF', width=500, height=500)
        self.canevabouton.pack()
        
        self.canevabouton.create_text(100,15,text="Liste d'objet" ,font=("Arial","20"))
        ley=1
        
        ''' creation de la liste des items pour mixer dans l'artisanat '''
        for o in self.itemEnPoche:
            if o.id==0 or o.id==1 or o.id==2:
                self.rb= tkinter.Radiobutton(self.canevabouton, variable=self.v, value=o.id)
                self.rb.place(x=0,y=30+40*ley)
                self.labelItem = self.canevabouton.create_text(250,45+40*ley,text=o.nom+"  "+o.description,anchor="center",fill='blue',font=("Arial","8"))       
                ley+=1         
          
        ''' creation des boutons pour le mix dans l'artisanats '''  
 
        item1button = tkinter.Button(self.canevabouton, text="Item 1", fg="blue" ,command= self.selection1)   
        item2button = tkinter.Button(self.canevabouton, text="Item 2", fg="blue",command= self.selection2)
        validbutton = tkinter.Button(self.canevabouton, text="Validation",fg="blue",command= self.validation)    
        
        #les placer     
        item1button.place(x=50,y=30+40*ley)
        item2button.place(x=150,y=30+40*ley)
        validbutton.place(x=250,y=30+40*ley)


    def ajoutSectionParchemin(self):
        self.deuxcanevas=tkinter.Canvas(self.lecadre, bg='#FFFFFF', width=500, height=500)
        self.deuxcanevas.pack()

        ley=0        
        ''' creation de la liste des parchemin que le joueur possede'''
          
        # for pour les parchemin
        self.deuxcanevas.create_text(100,47+80*ley,text="Liste de parchemins",font=("Arial","15"))
        ley+=1
        for i in self.parcheminEnPoche:
            if i.possede == True:
                
                self.rb= tkinter.Radiobutton(self.deuxcanevas,variable=self.p, value=i.parcheminId)
                self.rb.place(x=0,y=29+60*ley)
                self.labelItem = self.deuxcanevas.create_text(250,29+60*ley,text=i.description,anchor="center",fill='blue',font=("Arial","8"))
                ley+=1 
        
        ''' creation du bouton parchemin et son emplacement et le bouton annuler '''
                
        parchbutton = tkinter.Button(self.deuxcanevas,text="Parchemin Choisi",fg="blue",command= self.validparchemin)     
        parchbutton.place(x=150,y=29+60*ley) 
        boutonannule = tkinter.Button(self.deuxcanevas,text="Annuler",fg="blue",command= self.effacemenu)     
        boutonannule.place(x=350,y=40)

    def interface(self):
        self.cadreUn=tkinter.Frame(self.parent.root, bg='#FFFFFF')
        self.cadreUn.grid_rowconfigure(0, weight=0)
        self.cadreUn.grid_columnconfigure(0, weight=0)
        self.lecanevas=tkinter.Canvas(self.cadreUn, width=490, height=695, scrollregion=(0,0,700,1000), bg='#FFFFFF')
        self.lecanevas.grid(row=0, column=0, sticky='ns')
        
        self.scrollY = tkinter.Scrollbar(self.cadreUn, orient='vertical',command=self.lecanevas.yview)
        self.scrollY.grid(row=0, column=1, sticky='ns')
        
        self.lecanevas.config(yscrollcommand=self.scrollY.set)
        
        self.lecadre=tkinter.Frame(self.lecanevas, bg='#000000')
        self.lecanevas.create_window(0, 0, window=self.lecadre, anchor='nw')
        
    # selection du premiet item
    def selection1(self):
        self.item1 = self.v.get()

        self.valitem.set("")
    #selection du 2e item
    def selection2(self):
        self.item2 = self.v.get()

    # fonction pour le choix du parchemin  
    
    def validparchemin(self):
        self.parch=self.p.get()
        if(self.parch):
            pass
        else:
            tkinter.messagebox.showinfo("Utilisation De Parchemin", "Erreur parchemin manquant")
    ''' Validation des 2 item selon leur utilisation '''
    
    def validation(self):
        if self.parch== 31: 
            if self.item1 ==0 or  self.item1 ==1:
                if self.item2 == 0 or self.item2 == 1:
                    if self.item1 != self.item2 :
                        self.parent.parent.fabricationArmure()
                else:
                    self.messageerreur()    
            else:
             self.messageerreur()
            
             
        elif self.parch== 32:
            if self.item1 ==0 or  self.item1 ==2:
                if self.item2 == 0 or self.item2 == 2:
                    if self.item1 != self.item2 :
                        self.parent.parent.fabricationFusil()
                else:
                    self.messageerreur()    
            else:
             self.messageerreur()            
             
        elif self.parch== 33:
            if self.item1 ==1 or  self.item1 ==2:
                if self.item2 == 1 or self.item2 == 2:
                    if self.item1 != self.item2 :           
                        self.parent.parent.fabricationDematerialisateur()    
                else:
                    self.messageerreur()    
            else:
             self.messageerreur()            
             
            
        elif self.parch >=22 or self.parch <=30:
            for i in range(22,30):
               if self.item1 ==i:
                    self.premierid== self.item1
               if self.item2 == i:
                  self.deuxiemmeid== self.item2
            if self.premierid != self.deuxiemmeid:                
                self.parent.parent.mixeCle()    
            else:
             self.messageerreur() 
        else:
         tkinter.messagebox.showinfo("Utilisation D artisanat", "Erreur Objet manquant")
    
    ''' faire disparaitre la fenetre en jeu'''
    def effacemenu(self):
        #self.cadreUn.destroy()
        self.deuxcanevas.destroy()
        self.canevabouton.destroy()
        self.cadreUn.pack_forget()
        
    def messageerreur(self):
        tkinter.messagebox.showinfo("Utilisation D artisanat", "article invalide")

        