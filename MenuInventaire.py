import tkinter
import Item

class MenuInventaire():
    def __init__(self, parent):
        self.parent = parent
        
        self.interface()
        
    def menuInventaire(self,invperso):
        self.inventaire=invperso
        
        self.cadreUn.pack(side=tkinter.RIGHT)
       
        self.invDict = self.analyserInv(self.inventaire.items)
    
        self.ajoutLigneInventaire()
        
    def ajoutLigneInventaire(self):
        ley=0# variable qui aide placer les items sur le deuxcanvas 
        
        self.deuxcanevas=tkinter.Canvas(self.lecadre, bg='#FFFFFF', width=512, height=800)
        self.deuxcanevas.grid(row=0, column=0)
        
        #boucle pour afficher les items de l'inventaire
        for k,o in self.invDict.items():
            
            self.rb= tkinter.Radiobutton(self.deuxcanevas, variable=self.choisirItemInv, value=k, command=self.selectionerObjet)
            self.rb.place(x=5,y=29+60*ley)
            ''' placer l'image trouve en dictionaire '''

            la=tkinter.Label(self.deuxcanevas,image=self.parent.getImage(o[3]))
            la.place(x=20,y=20+60*ley)
            self.deuxcanevas.create_text(120,7,text='description' ,fill='blue',font=("Arial","8"),tags="inv")
            self.deuxcanevas.create_text(120,47+60*ley,text=o[0] ,fill='blue',font=("Arial","8"),tags="inv")
            self.deuxcanevas.create_text(240,7,text='description' ,fill='blue',font=("Arial","8"),tags="inv")
            self.deuxcanevas.create_text(240,47+60*ley,text=o[1] ,fill='blue',font=("Arial","8"),tags="inv")
            self.deuxcanevas.create_text(320,7,text='qte' ,fill='blue',font=("Arial","8"),tags="inv")
            self.deuxcanevas.create_text(320,47+60*ley,text=o[4] ,fill='blue',font=("Arial","8"),tags="inv")
            self.deuxcanevas.create_text(370,7,text='poids' ,fill='blue',font=("Arial","8"),tags="inv")
            self.deuxcanevas.create_text(370,47+60*ley,text=o[2] ,fill='blue',font=("Arial","8"),tags="inv")
                
            ley+=1            

    def interface(self):
        self.cadreUn=tkinter.Frame(self.parent.root, bg='#FFFFFF')
        self.cadreUn.grid_rowconfigure(0, weight=0)
        self.cadreUn.grid_columnconfigure(0, weight=0)
        #self.cadreUn.place(x=512,y=80)
        self.lecanevas=tkinter.Canvas(self.cadreUn, width=490, height=695, scrollregion=(0,0,512,700),bg='#FFFFFF')
        self.lecanevas.grid(row=0, column=0, sticky='nsew')
        
        self.scrollY = tkinter.Scrollbar(self.cadreUn, orient='vertical',command=self.lecanevas.yview)
        self.scrollY.grid(row=0, column=1, sticky='ns')
        
        self.lecanevas.config(yscrollcommand=self.scrollY.set)
        
        self.lecadre=tkinter.Frame(self.lecanevas, bg='#FFFFFF')
        self.lecanevas.create_window(0, 0, window=self.lecadre, anchor='nw')
        
        self.choisirItemInv = tkinter.StringVar()
        self.choisirItemInv.set("L")
        
        self.boutonUtiliser= tkinter.Button(self.lecanevas, text='Utiliser',command=self.utiliser)
        self.boutonAbandoner= tkinter.Button(self.lecanevas, text='Abandonner',command=self.abandonner)
        
        self.boutonUtiliser.place(x=420, y=10)
        
        self.boutonAbandoner.place(x=420, y=50) 
        
    def analyserInv(self,inv):
        self.objetsEnInventaire={}#3:[0nom, 1desc,2poids,3image',4qte]
        nomImage=''
        for it in inv:
            #print(it.nom, it.description)
            if it.id==3 or it.id==5:
                nomImage='seringue'
            elif it.id==4:
                nomImage='nouriture'
            elif it.id==7:
                nomImage='gun'
            elif it.id==8:
                nomImage='shield'
                
            if it.id in self.objetsEnInventaire:
                self.objetsEnInventaire[it.id][4]+=1
            else:
                self.objetsEnInventaire[it.id]=[it.nom, it.description,it.poids,nomImage,1]
        
        return self.objetsEnInventaire
                        
    def selectionerObjet(self):   
        return str(self.choisirItemInv.get())
        
    def utiliser(self):
        for o in self.inventaire.items:
            if o.id==int(self.selectionerObjet()):
                self.inventaire.retirerItem(o)
                self.effacemenu()
                self.parent.parent.contexte = "enJeu"
                if o.id==3 or o.id==5:#seringue ou super-seringue
                    self.parent.parent.autoSoin()
        
                
    def abandonner(self):
        for o in self.inventaire.items:
            if o.id==int(self.selectionerObjet()):
                self.inventaire.retirerItem(o)
                self.effacemenu()
                self.parent.parent.contexte = "enJeu"    
        
    ''' faire disparaitre la fenetre en jeu'''
    def effacemenu(self):
        self.deuxcanevas.destroy()
        self.cadreUn.pack_forget()
        