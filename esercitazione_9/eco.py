import numpy as np

class hit():
    def __init__(self, mod, sens, time):
        self.mod=mod
        self.sens=sens
        self.time=time

    def __lt__(self, other):
        return self.time < other.time

class event:
     def __init__(self):
         self.num=0
         self.time1=-99
         self.time2=-99
         self.delta=-99
         self.hits=np.empty([])

     def aggiungi(self, hit):
         if self.num==0:
             self.time1=hit.time
         self.time2=hit.time
         self.delta=hit.time-self.time1
         self.hits=np.append(self.hits, hit)
         self.num=np.size(self.hits)
         
    
    
        
