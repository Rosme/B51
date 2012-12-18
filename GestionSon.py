import threading , winsound

class GestionSon():
    def __init__(self):
        self.dictSon=dict()
        self.dictSon["hello"]="assets/son/test.wav"
        self.dictSon["inGame"]="assets/son/Epic Escape.wav"        
    
        self.nomSon="hello"
    
    def playTest(self):
        winsound.PlaySound(self.dictSon[self.nomSon],winsound.SND_FILENAME)
    
    def startTest(self,nomSon):
        self.nomSon=nomSon
        self.t=threading.Thread(target=self.playTest)
        self.t.start()
    
    def stopSon(self,nomSon):
         winsound.PlaySound(self.dictSon[nomSon],winsound.SND_PURGE)
        
    def stopAll(self):
        winsound.PlaySound(None, 0)