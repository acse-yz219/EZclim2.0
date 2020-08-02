"""
Created by Adanna Akwataghibe (Github: AdannaAkwats)
"""
import time
import sys
class ProgressBar:

    def __init__(self, n_iter, total_width, description="Desc"):
        self.n_iter         = n_iter
        self.total_width    = total_width
        self.width          = int(self.total_width/self.n_iter)
        self.iter           = 0
        self.description    = description + ': '
        self.start          = time.clock()
        self.percent        = 0 
        self.initialize()
    def initialize(self):
        self.start = time.clock()
        sys.stdout.write(self.description+"  "+'%.2f%%' % (self.percent)+"   "+'|'*(self.iter*self.width) + ' '*((self.n_iter-self.iter)*self.width)+ "|"+"   "+"ETA: ")
        sys.stdout.flush()

    def update(self, q=1):
        self.iter +=1
        self.percent = self.iter/self.n_iter*100
        current = time.clock()
        sys.stdout.write("\r"+self.description+"  "+ '%.2f%%' % (self.percent )+"  "+"|"*(self.iter*self.width) + " "*((self.n_iter-self.iter)*self.width)+ "|"+"   "+"ETA: "+ str( current - self.start))
        sys.stdout.flush()

    def finish(self):
        current = time.clock()
        sys.stdout.write("\r"+">> Total Time: "+ str(current - self.start) )
        sys.stdout.flush()