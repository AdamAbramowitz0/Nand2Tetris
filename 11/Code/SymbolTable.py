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
    def classname(self):
        return self.names[0]
    def deBug(self):
        return self.names
    def isItAMethod(self):
        if(len(self.names) >= 2):
            if(self.names[1]=="self"):
                return True
            else:
                return False
        else:
            return False
    def define(self, name, type, kind):
        self.names.append(name)
      
        self.types.append(type)
        self.kinds.append(kind)
        index = 0
        for i in range(0,len(self.kinds)):
            if self.kinds[i] == kind and (self.names[i] != name):
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

        return ""
    def typeOf(self,name):
 
        for i in range(1,len(self.names)):
 
            if self.names[i] == name:
                return self.types[i]

        return "NONE"
    def typeOfIncludeClass(self,name):
        for i in range(0,len(self.names)):
 
            if self.names[i] == name:
                return self.types[i]

        return "NONE"
    def indexOf(self,name):
        for i in range(0,len(self.names)):
            if self.names[i] == name:
                
                return str(self.indexes[i])
        return "YO"
    def printNames(self):
        print(self.names)
 
