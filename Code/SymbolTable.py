class SymbolTable:
    di={}
    def __init__(self):
        self.di={}

    def getAddress(self,sym):
        print(sym)
        q=""
     
        y=str(bin(int(self.di[sym])))[2:]
        print(self.di[sym])
        z=15-len(str(y))
        for i in range(z):
            q+="0"
        q+=y
        return q
    def addEntry(self,sym,adr):
        self.di[sym]=adr
    def contains(self,sym):
        
        if sym in self.di:
            return True
        else:
            return False
        #return self.di.has_key(sym)
    def printer(self):
        return self.di

