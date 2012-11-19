import tkinter
import math

class Test():
    def __init__(self):
        self.px=0
        self.py=30
        self.cx=60
        self.cy=10
        self.finx=0
        self.finy=0
        self.largeurT=40
        self.hauteurT=20
        #self.root=tkinter.Tk()
        #self.root.config(width=100, height=20)        
        
        tempx=math.floor(self.cx/(self.largeurT/2))*self.largeurT/2
        tempy=math.floor(self.cy/(self.hauteurT/2))*self.hauteurT/2
        
        if tempy==self.py:
            tempx = math.floor(tempx/self.largeurT)
            self.finx=tempx
            self.finy=tempx
        elif tempy<self.py:
            while tempy!=self.py:
                tempx-=(self.largeurT/2)
                tempy+=(self.hauteurT/2)
                self.finx+=1
            tempx = math.floor(tempx/self.largeurT)
            self.finx+=tempx
            self.finy+=tempx
        elif tempy>self.py:
            while tempy!=self.py:
                tempx-=(self.largeurT/2)
                tempy-=(self.hauteurT/2)
                self.finy+=1
            tempx = math.floor(tempx/self.largeurT)
            self.finx+=tempx
            self.finy+=tempx

        #print(self.finx,self.finy)
        #self.root.mainloop()      

if __name__ == '__main__':
    c = Test()