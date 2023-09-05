class VMWriter:
    
    def __init__(self, file):
        self.y = open(file[:-5] + ".vm","w")
        self.final = ''
        self.field="field" #uncertain
        self.sub="neg"
    def setSub(self,insert):
        self.sub = "sub"
    def writePush(self, segment, index):
        if(segment == "field"):
            segment = "this"
        if(segment == "var"):
            segment = "local"
        if((segment == "constant") and (index == "-1")):
            index = 1
            self.final+=("push " + segment + " " + str(index) + "\n")
            self.final+=("neg"+"\n")        
        else:
            if(isinstance(index,str)):
                if(index[0]=="-"):
                    self.final+=("push " + segment + " " + str(index[1:]) + "\n")
                 
                    self.final+=("neg"+"\n")   
                else:
                    self.final+=("push " + segment + " " + str(index) + "\n")
            elif(index <0):
                self.final+=("push " + segment + " " + str(index-1) + "\n")
                self.final+=("neg"+"\n")  
            else: 
                self.final+=("push " + segment + " " + str(index) + "\n")
       
        

    def writePop(self, segment, index):
        if(segment == "field"):
            segment = "this"
        if(segment == "var"):
            segment = "local"
        self.final+=("pop " + segment + " " + index + "\n")

    def writeArithmetic(self, command):
      #,"&amp;","&lt;","&gt;"
        if command == "*":
            command= "call Math.multiply 2"
        elif command == "/":
            command= "call Math.divide 2"
        elif command == "+":
            command= "add"
        elif command == "-":
            command= self.sub
        elif command == "=":
            command= "eq"
        elif command in [">","&gt;"]:
            command=  "gt"
        elif command in ["<","&lt;"]:
            command=  "lt"
        elif command in ["&","&amp;"]:
            command= "and"
        elif command == "|":
            command=  "or"
        elif command == "~":
            command=  "not"
        elif command == "neg":
            print("HIT")
            print(self.sub)
            command = self.sub

       
      

        
        self.final+=(command + "\n")
        self.sub="neg"
    def writeLabel(self,label):
        self.final+=("label " + label + "\n")
    def writeGoto(self, label):
        self.final+=("goto " + label + "\n")
    def writeIf(self,label): #IF GOTO
        self.final+=("if-goto " + label + "\n")
    def writeCall(self, name, nArgs):
        
        self.final+=("call " + name + " " + str(nArgs) + "\n")
    def writeFunction(self, name, nVars):
    
        self.final+=("function " + name + " " + str(nVars) + "\n")
    def writeReturn(self):
        self.final+=("return" + "\n")
    #def close() not necessary
    def dump(self):
        self.y.write(self.final)


    def changeToMethod(self,strin):
        self.field = strin
  
        
#if while let do return