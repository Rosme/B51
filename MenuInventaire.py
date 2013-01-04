import tkinter
import Item

class MenuInventaire():
    def __init__(self, parent):
        self.parent = parent
        '''
        self.importerImage()
        
        self.cadreUn=tkinter.Toplevel()
        self.cadreUn.grid_rowconfigure(0, weight=1)
        self.cadreUn.grid_columnconfigure(0, weight=1)
        
        self.lecanevas=tkinter.Canvas(self.cadreUn, bg='#FFFFFF', scrollregion=(0,0,512,700))
        self.lecanevas.grid(row=0, column=0, sticky='ns')
        
        self.scrollY = tkinter.Scrollbar(self.cadreUn, orient='vertical',command=self.lecanevas.yview)
        self.scrollY.grid(row=0, column=1, sticky='ns')
        
        self.lecanevas.config(yscrollcommand=self.scrollY.set)
        
        self.lecadre=tkinter.Frame(self.lecanevas)
        self.lecanevas.create_window(0, 0, window=self.lecadre, anchor='nw')
        
               
        self.deuxcanevas=tkinter.Canvas(self.lecadre, bg='#FFFFFF', width=512, height=700)
        self.deuxcanevas.grid(row=3, column=0)
        self.ley=0# variable qui aide placer les items sur le deuxcanvas 
        
        self.choisirItemInv = tkinter.StringVar()
        self.choisirItemInv.set("L")
        
        self.boutonUtiliser= tkinter.Button(self.lecanevas, text='Utiliser',command=self.utiliser)
        self.boutonAbandoner= tkinter.Button(self.lecanevas, text='Abandonner',command=self.abandonner)
        '''
        
        
    def menuInventaire(self,invperso):
        pass
        '''
        self.cadreUn.place(x=512,y=120)
        self.ley=0
        for o in self.inventaire.items:
            if o.id==7 or o.id==8:
                pass
            else:
                self.imgeLoad=tkinter.PhotoImage()
                self.rb= tkinter.Radiobutton(self.deuxcanevas, variable=self.choisirItemInv, value=o.id, command=self.selectionerObjet)
                self.rb.place(x=5,y=29+60*self.ley)
                
                if o.id==3:
                    self.imgeLoad=self.seringue
                if o.id==4:
                    self.imgeLoad=self.nouriture
                if o.id==5:
                    self.imgeLoad=self.seringue
                la=tkinter.Label(self.deuxcanevas,image=self.imgeLoad)
                la.place(x=20,y=20+60*self.ley)
                
                self.deuxcanevas.create_text(140,7,text='description' ,fill='blue',font=("Arial","8"),tags="description")
                self.deuxcanevas.create_text(140,47+60*self.ley,text=o.description ,fill='blue',font=("Arial","8"),tags="description")
    #            self.deuxcanevas.create_text(240,7,text='qte' ,fill='blue',font=("Arial","8"),tags="description")
    #            self.deuxcanevas.create_text(240,47+60*self.ley,text=o[2] ,fill='blue',font=("Arial","8"),tags="qte")
                self.deuxcanevas.create_text(340,7,text='poids' ,fill='blue',font=("Arial","8"),tags="description")
                self.deuxcanevas.create_text(340,47+60*self.ley,text=o.poids ,fill='blue',font=("Arial","8"),tags="poids")
                
                self.ley+=1                     
        
        self.boutonUtiliser.place(x=200, y=47+60*self.ley)
        self.boutonAbandoner.place(x=300, y=47+60*self.ley)
        '''
    def selectionerObjet(self):    
         return str(self.choisirItemInv.get())
        
    def utiliser(self):
        print('utilise '+self.selectionerObjet())    
        
    def abandonner(self):
        print('abandonne '+self.selectionerObjet())    
        
        
    def importerImage(self):
        self.baterie = tkinter.PhotoImage(file='assets/image/energy.gif',width=35,height=35)
        self.metal = tkinter.PhotoImage(file='assets/image/bouclier.gif',width=45,height=35)
        self.nouriture=tkinter.PhotoImage(file='assets/image/nouriture.gif',width=40,height=35)
        self.partiElectronique = tkinter.PhotoImage(file='assets/image/gun.gif',width=45,height=35)
        self.seringue=tkinter.PhotoImage(file='assets/image/syringe.gif',width=45,height=35)        
        
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        