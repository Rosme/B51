# -*- coding: ISO-8859-1 -*-
import tkinter
import Personnage
import Item
import Artisanat
class MenuArtisanat():
    def __init__(self, parent):
        self.parent = parent
         
        
        
        
        
        
    def menuArtisanat(self, listeParchemin,itemPerso ):
       
        self.item1=""
        self.item2=""
        self.parch=""
        
        
        
        self.cadreUn=tkinter.Frame(self.parent.parent.root, bg='#152C5F')
        self.cadreUn.grid_rowconfigure(0, weight=0)
        self.cadreUn.grid_columnconfigure(0, weight=0)
        self.lecanevas=tkinter.Canvas(self.cadreUn, width=512, height=500, scrollregion=(0,0,700,1000), bg='#152C5F')
        self.lecanevas.grid(row=0, column=0, sticky='ns')
        
        self.scrollY = tkinter.Scrollbar(self.cadreUn, orient='vertical',command=self.lecanevas.yview)
        self.scrollY.grid(row=0, column=1, sticky='ns')
        
        self.lecanevas.config(yscrollcommand=self.scrollY.set)
        
        self.lecadre=tkinter.Frame(self.lecanevas, bg='#152C5F')
        self.lecanevas.create_window(0, 0, window=self.lecadre, anchor='nw')
               
        self.deuxcanevas=tkinter.Canvas(self.lecadre, bg='#152C5F', width=700, height=500)
        self.deuxcanevas.grid(row=0, column=0)
        
        self.canevabouton=tkinter.Canvas(self.lecadre, bg='#152C5F', width=700, height=500)
        self.canevabouton.grid(row=1, column=0)
        
        self.v = tkinter.IntVar()
        self.p = tkinter.IntVar()
        
        
        self.parcheminEnPoche =listeParchemin
        self.itemEnPoche= itemPerso
        self.validationparchemin =0
     
        self.valitem=tkinter.StringVar()
        self.valitem.set("")
       
        self.cadreUn.place(x=12,y=120)
       
        self.ley=0
        '''self.listeclepossible = list()
        self.listeclepossible.append(22)
        self.listeclepossible.append(23)
        self.listeclepossible.append(24)
        self.listeclepossible.append(25)
        self.listeclepossible.append(26)
        self.listeclepossible.append(27)
        self.listeclepossible.append(28)
        self.listeclepossible.append(29)
        self.listeclepossible.append(30)
        self.premierid=0
        self.deuxiemmeid=0'''
        
        ''' creation de la liste des parchemin que le joueur possede'''
          
        # for pour les parchemin
        self.choixparchemin=""
        self.deuxcanevas.create_text(100,47+80*self.ley,text="Liste de parchemin"  )
        self.ley+=1
        for i in self.parcheminEnPoche:
            if i.possede == True:
                
                print(i.id)
                self.rb= tkinter.Radiobutton(self.deuxcanevas,variable=self.p, value=i.id)
                self.rb.place(x=0,y=29+60*self.ley)
                self.labelItem = self.deuxcanevas.create_text(250,29+60*self.ley,text=i.description,anchor="center",fill='red',font=("Arial","8"))
                #self.labelparchemin= tkinter.Label(self.deuxcanevas,text=i.description)
                #self.labelparchemin.place(x=50,y=29+60*self.ley)
                self.ley+=1 
        
        ''' creation du bouton parchemin et son emplacement et le bouton annuler '''
                
        parchbutton = tkinter.Button(self.deuxcanevas,text="Parchemin Choisi",fg="blue",command= self.validparchemin)     
        parchbutton.place(x=150,y=29+60*self.ley) 
        boutonannule = tkinter.Button(self.deuxcanevas,text="Annuler",fg="blue",command= self.effacemenu)     
        boutonannule.place(x=350,y=40)
        ###########################
        # liste des objets dans l'artisanat que le joueur possede
        ###########################
        
        self.canevabouton.create_text(100,5*self.ley,text="Liste d'objet"  )
        self.ley=1
        
        ''' creation de la liste des items pour mixer dans l'artisanat '''
        for o in self.itemEnPoche:
            if o.id==0 or o.id==1 or o.id==2:
                self.rb= tkinter.Radiobutton(self.canevabouton, variable=self.v, value=o.id)
                self.rb.place(x=0,y=30+40*self.ley)
                self.labelItem = self.canevabouton.create_text(250,45+40*self.ley,text=o.nom+"  "+o.description,anchor="center",fill='red',font=("Arial","8"))       
                self.ley+=1         
          
        ''' creation des boutons pour le mix dans l'artisanats '''  
 
        item1button = tkinter.Button(self.canevabouton, text="Item 1", fg="blue" ,command= self.selection1)   
        item2button = tkinter.Button(self.canevabouton, text="Item 2", fg="blue",command= self.selection2)
        validbutton = tkinter.Button(self.canevabouton, text="Validation",fg="blue",command= self.validation)    
        
        #les placer     
        item1button.place(x=50,y=30+40*self.ley)
        item2button.place(x=150,y=30+40*self.ley)
        validbutton.place(x=250,y=30+40*self.ley)
       
    #####################
    ''' les fonctions'''
    #####################

        
    # selection du premiet item
    def selection1(self):
        self.item1 = self.v.get()
        print(str(self.item1)+" selection1 "+str(self.item2))
        self.valitem.set("")
    #selection du 2e item
    def selection2(self):
        self.item2 = self.v.get()
        print(str(self.item1)+" selection2 " +str(self.item2))
    # fonction pour le choix du parchemin  
    
    def validparchemin(self):
        self.parch=self.p.get()
        if(self.parch):
            print(self.parch)
        else:
            tkinter.messagebox.showinfo("Utilisation De Parchemin", "Erreur parchemin manquant")
    ''' Validation des 2 item selon leur utilisation '''
    
    def validation(self):
        if self.parch== 31: 
            if self.item1 ==0 or  self.item1 ==1:
                print("validation 1") 
                if self.item2 == 0 or self.item2 == 1:
                    print("validation 2")
                    if self.item1 != self.item2 :
                        print("ok")
                        self.parent.parent.parent.jeu.artisanat.fabricationArmure()
                else:
                    self.messageerreur()    
            else:
             self.messageerreur()
            
             
        elif self.parch== 32:
            if self.item1 ==0 or  self.item1 ==2:
                print("validation 1") 
                if self.item2 == 0 or self.item2 == 2:
                    print("validation 2")
                    if self.item1 != self.item2 :
                        print("ok")
                        self.parent.parent.parent.jeu.artisanat.fabricationFusil()
                else:
                    self.messageerreur()    
            else:
             self.messageerreur()            
             
        elif self.parch== 33:
            if self.item1 ==1 or  self.item1 ==2:
                print("validation 1") 
                if self.item2 == 1 or self.item2 == 2:
                    print("validation 2")
                    if self.item1 != self.item2 :
                        print("ok")            
                        self.parent.parent.parent.jeu.artisanat.fabricationDematerialisateur()    
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
                self.parent.parent.parent.jeu.artisanat.mixeCle()    
            else:
             self.messageerreur() 
        else:
         tkinter.messagebox.showinfo("Utilisation D artisanat", "Erreur Objet manquant")
    
    
    ''' faire disparaitre la fenetre en jeu'''
    def effacemenu(self):
        self.cadreUn.destroy()
    def messageerreur(self):
        tkinter.messagebox.showinfo("Utilisation D artisanat", "article invalide")
        
    def cle(self,id):
        self.id =id
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        