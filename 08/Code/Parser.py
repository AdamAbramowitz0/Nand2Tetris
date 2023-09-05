class Parser:
    lineNumber=0
    def __init__(self,fileName):
       self.lineNumber=-1
       self.x=open(fileName).readlines()

    def hasMoreLines(self):
        if self.lineNumber+1 < len(self.x):
            return True

        else:
            return False
    
    def advance(self):
        while self.hasMoreLines():
            self.lineNumber+=1
            self.x[self.lineNumber]=self.x[self.lineNumber].strip()
            if(len(self.x[self.lineNumber])>1):
                if (self.x[self.lineNumber][0] != "/" and self.x[self.lineNumber][1] != "/"):
                    for i in range(0,len(self.x[self.lineNumber])-2):
                        if self.x[self.lineNumber][i] == "/" and self.x[self.lineNumber][i+1] == "/":
                            self.x[self.lineNumber] = self.x[self.lineNumber][0:i]
                            return
                    return
            
    def instruction(self):
        return self.x[self.lineNumber]
    def arg1(self):
        y=self.x[self.lineNumber].find(" ") 
        y+=1
         #ONLY FOR PUSH POP FUNCTION AND CALL!
        if self.commandType()=="C_ARITHMETIC":
            return self.x[self.lineNumber]
        elif self.commandType() in {"C_PUSH","C_CALL","C_FUNCTION","C_POP"}:
            z=self.x[self.lineNumber].find(" ",y+1)
            
            return self.x[self.lineNumber][y:z]
       
        else:
            return self.x[self.lineNumber][y:]
    def arg2(self):
        y=self.x[self.lineNumber].find(" ")
        z=self.x[self.lineNumber].find(" ",y+1)
        z=z+1
        return self.x[self.lineNumber][z:]
    def commandType(self):
        if((self.x[self.lineNumber][0:2] in {"gt","lt","eq","or"})or(self.x[self.lineNumber][0:3] in {"add","sub","neg","and","not"})):
           
            return "C_ARITHMETIC"
        elif(self.x[self.lineNumber][0:4] == "push"):
            return "C_PUSH"
        elif(self.x[self.lineNumber][0:3] == "pop"):
            return "C_POP"
        elif(self.x[self.lineNumber][0:5] == "label"):
            return "C_LABEL"
        elif(self.x[self.lineNumber][0:4] == "goto"):
            return "C_GOTO"
        elif(self.x[self.lineNumber][0:2] == "if"):
            return "C_IF"
        elif(self.x[self.lineNumber][0:8] == "function"):
            return "C_FUNCTION"
        elif(self.x[self.lineNumber][0:6] == "return"):
            return "C_RETURN"
        elif(self.x[self.lineNumber][0:4] == "call"):
            return "C_CALL"
        else:
            return "COMMANDTYPE ERROR!"
        
