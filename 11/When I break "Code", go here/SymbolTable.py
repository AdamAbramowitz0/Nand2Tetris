class SymbolTable:
    
    def __init__(self):
        self.names = []
        self.types = []
        self.kinds = []
        self.indexes = []
    
    def reset(self):
        self.names = []
        self.types = []
        self.kinds = []
        self.indexes = []
    
    def define(self, name, type, kind):
        self.names.append(name)
      
        self.types.append(type)
        self.kinds.append(kind)
        index = 0
        for i in range(0,len(self.kinds)):
            if self.kinds[i] == kind:
                index+=1
       
        self.indexes.append(index)
        


    def varCount(self,kind):
        index = 0
        for i in range(0,len(self.kinds)):
            if self.kinds[i] == kind:
                index+=1
        return index


    def kindOf(self,name):
        for i in range(0,len(self.names)):
            if self.names[i] == name:
                return self.kinds[i]

        return "NONE"
    def typeOf(self,name):
        for i in range(0,len(self.names)):
            print("hit")
            if self.names[i] == name:
                return self.types[i]

        return "NONE"

    def indexOf(self,name):
        for i in range(0,len(self.names)):
            if self.names[i] == name:
                
                return str(self.indexes[i])
        return "YO"
            
      
