import tkinter

class MenuInventaire():
    def __init__(self, parent):
        self.parent = parent
        ################ nom,description, qte, poids, image
        self.objetsEnInventaire=[[ 'seringue','soigne 20 de vie',6,6,'assets/image/syringe.gif',''],['nourriture','bonne pour la sante',5,11,'assets/image/nouriture.gif',''],[ 'seringue2','soigne 40 de vie',7,7,'assets/image/syringe.gif','']]
        
        self.cadreUn=tkinter.Frame(self.parent.parent.root)
        self.cadreUn.grid_rowconfigure(0, weight=1)
        self.cadreUn.grid_columnconfigure(0, weight=1)
        self.lecanevas=tkinter.Canvas(self.cadreUn, bg='#FFFFFF', scrollregion=(0,0,400,700))
        self.lecanevas.grid(row=0, column=0, sticky='ns')
        
        self.scrollY = tkinter.Scrollbar(self.cadreUn, orient='vertical',command=self.lecanevas.yview)
        self.scrollY.grid(row=0, column=1, sticky='ns')
        
        self.lecanevas.config(yscrollcommand=self.scrollY.set)
        
        self.lecadre=tkinter.Frame(self.lecanevas)
        self.lecanevas.create_window(0, 0, window=self.lecadre, anchor='nw')
               
        self.deuxcanevas=tkinter.Canvas(self.lecadre, bg='#FFFFFF', width=400, height=700)
        self.deuxcanevas.grid(row=0, column=0)
        
        self.v = tkinter.StringVar()
        self.v.set("L")
        
        self.boutonUtiliser= tkinter.Button(self.deuxcanevas, text='Utiliser',command=self.utiliser)
        self.boutonAbandoner= tkinter.Button(self.deuxcanevas, text='Abandonner',command=self.abandonner)
        
        
    def menuInventaire(self):
        self.cadreUn.place(x=512,y=120)
        self.ley=0
        for o in self.objetsEnInventaire:
            
            o[5]= tkinter.PhotoImage(file=o[4],width=60,height=60)
            self.rb= tkinter.Radiobutton(self.deuxcanevas, variable=self.v, value=o[0], command=self.selectionerObjet)
            self.rb.place(x=5,y=29+60*self.ley)
            la=tkinter.Label(self.deuxcanevas,image=o[5])
            la.place(x=20,y=20+60*self.ley)
            self.deuxcanevas.create_text(140,7,text='description' ,fill='blue',font=("Arial","8"),tags="description")
            self.deuxcanevas.create_text(140,47+60*self.ley,text=o[1] ,fill='blue',font=("Arial","8"),tags="description")
            self.deuxcanevas.create_text(240,7,text='qte' ,fill='blue',font=("Arial","8"),tags="description")
            self.deuxcanevas.create_text(240,47+60*self.ley,text=o[2] ,fill='blue',font=("Arial","8"),tags="qte")
            self.deuxcanevas.create_text(340,7,text='poids' ,fill='blue',font=("Arial","8"),tags="description")
            self.deuxcanevas.create_text(340,47+60*self.ley,text=o[3] ,fill='blue',font=("Arial","8"),tags="poids")
            
            self.ley+=1            
        
        self.boutonUtiliser.place(x=200, y=47+60*self.ley)
        self.boutonAbandoner.place(x=300, y=47+60*self.ley)
       
    def selectionerObjet(self):    
        return str(self.v.get())
        
    def utiliser(self):
        print('utilise '+self.selectionerObjet())    
        
    def abandonner(self):
        print('abandonne '+self.selectionerObjet())    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        