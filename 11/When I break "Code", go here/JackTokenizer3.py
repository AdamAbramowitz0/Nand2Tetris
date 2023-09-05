import re
class JackTokenizer3:
    def __init__(self,f):
        self.spotLine = 0
        self.currentLine  = 0
        self.input = open(f).readlines()
        self.inFunction = False
        self.keywords = ['class','constructor','function','method','field','static'
    ,'var','int','char','boolean','void','true','false','null','this'
    ,'let','do','if','else','while','return']
        self.symbols=['{','}','(',')','[',']','.',',',';','+','-','*','/','&','|','<','>','=',"~"]
        self.symbols2=['{','}','(',')','[',']','.',',',';','+','-','*','/','&amp;','|','&lt;','&gt;','=',"~"]
        self.currentToken=""
    

        self.final=[]
        self.currentID = ''
        #print(self.input)
        print(self.input)
        try:
            for i in range(0,len(self.input)-1):
            
                c=self.input[i].strip()
                c=re.sub('\n', '', c)
                self.input[i]=c
                if(self.input[i]==''):
                    self.input.pop(i)
                if self.input[i][:-2] =="\n":
                    #print("HVJBJNKVHJBKJLN:LMHJVBKJNK")
                    self.input[i]=self.input[i][:len(self.input[i])-2]
                
        except:
            #print(self.input)
            print(" ")
        #print(self.input)
        
        if self.input[len(self.input)-1] == "\n":
            self.input.pop(len(self.input)-1)
     


    
    def peek(self):#BROKEN
        try:
            if(self.spotLine >= len(self.input[self.currentLine])-1):
                return self.input[self.currentLine+1][0]
            return self.input[self.currentLine][self.spotLine]
        except:
            return "EH"
    


    def advance(self):
        #print(str(self.currentLine) +str(self.input[self.currentLine])+str(len(self.input)))
        if (self.hasMoreTokens()==False):
            #print(self.currentLine)
            return "done"
        
        self.currentToken = ''
        curTok=[]
        if self.input[self.currentLine][self.spotLine]=="\t":
            
            self.MoveChar()
            self.advance()
            #print("HIT")
            return 1

        if self.isComment(self.currentLine,self.spotLine)=="T" or self.input[self.currentLine].startswith(' ',self.spotLine) or (self.input[self.currentLine][self.spotLine])=="\n":
            #print("hit1")
            self.MoveChar()
            self.advance()
            #print("HIT")
            return 1
        
        elif self.isComment(self.currentLine,self.spotLine)=="F" and (self.startswithsymbol() !="none"):
            #print("hit2")
            self.currentToken=self.startswithsymbol()
            self.MoveChar()
            return 1
        
        elif self.isComment(self.currentLine,self.spotLine)=="F" and self.input[self.currentLine].startswith('"',self.spotLine):
            #print("hit3")
            z=True
            curTok.append(self.input[self.currentLine][self.spotLine])
            self.MoveChar()
            while(z):
                if not self.input[self.currentLine].startswith('"',self.spotLine):
                    curTok.append(self.input[self.currentLine][self.spotLine])
                    self.MoveChar()
                else:
                    curTok.append(self.input[self.currentLine][self.spotLine])
                    self.MoveChar()
                    self.currentToken = ''.join(curTok)
                    return 1
        else:
            #print("hit4"+str(self.currentLine) + "  " + str(self.spotLine))
            while (self.isComment(self.currentLine,self.spotLine)=="F" and (not self.input[self.currentLine].startswith(' ',self.spotLine))):
                
                if self.nextstartswithsymbol()=="none" and (not self.input[self.currentLine].startswith(' ',self.spotLine+1)):
                    curTok.append(self.input[self.currentLine][self.spotLine])
                    self.MoveChar()
                else:
                    curTok.append(self.input[self.currentLine][self.spotLine])
                    self.currentToken = ''.join(curTok)
                    self.MoveChar()
                    return 1
                

   

    def startswithsymbol(self):
        x="none"
        for i in self.symbols:
            if (self.input[self.currentLine].startswith(i, self.spotLine)):
                x=i
        return x
    def nextstartswithsymbol(self):
        x="none"
        for i in self.symbols:
            if (self.input[self.currentLine].startswith(i, self.spotLine+1)):
                x=i
        return x

    def MoveBackOne(self):
        if (self.spotLine > 0):
            return self.input[self.currentLine][self.spotLine-1]
        elif(self.currentLine > 1):
            return self.input[self.currentLine-1][len(self.input[self.currentLine-1])-1]
        
    def MoveBackTwo(self):
        try:
            if (self.spotLine > 1):
                return self.input[self.currentLine][self.spotLine-2]
            elif(self.currentLine > 1):
                return self.input[self.currentLine-1][len(self.input[self.currentLine-1])-2]
        except:
            return("NOT")

    def isComment(self,column, row):
        inComment = "F"
        prev1=""
        prev2=""
        if self.hasMoreTokens():
            self.spotLine = 0
            self.currentLine = 0
        while(self.hasMoreTokens()):#//TODO ensure that the lengths etc are correct
            x=False
            try:
                if self.input[self.currentLine].startswith("//",self.spotLine):
                    if (column == self.currentLine) and (row >= self.spotLine):
                        self.spotLine=row
                        self.currentLine=column
                        #print("got here")
                        return "T"
                
                elif self.input[self.currentLine].startswith("/*",self.spotLine):
                    inComment="T"
                
                elif self.MoveBackOne() == "/" and self.MoveBackTwo() =="*":
                     
                    inComment="F"
            except:
                x=True
                #print(self.input[self.currentLine])
                self.MoveChar()
            
            if (column == self.currentLine) and (row == self.spotLine):
                self.spotLine=row
                self.currentLine=column
                return inComment
            if(not x): 
                self.MoveChar()


    def hasMoreTokens(self):
        try:
            if ((len(self.input) <= self.currentLine) and len(self.input[self.currentLine])-1 <= self.spotLine):
            
                return False
            else:
                return True
        except:
            return False

    
    def MoveChar(self):
        if self.hasMoreTokens():
            
            if len(self.input[self.currentLine])-1==(self.spotLine):
                self.currentLine+=1
                self.spotLine=0
            else:
                self.spotLine+=1


    def tokenType(self):
        self.currentToken=self.currentToken.strip()
        #print(str(self.currentLine) +"   "+str(self.spotLine))
        for i in self.symbols:
            if (self.currentToken == i):
                return "symbol"
        for i in self.keywords:
            if (self.currentToken == i):
                return "keyword"
        if self.currentToken.startswith("\""):
            return "stringConstant"
        if self.currentToken[0].isdigit():
            
            return "integerConstant"
        else:
            return "identifier"
        
    def keyWord(self):#STRING
        return self.currentToken

    def symbol(self): #RETURNS A CHAR , eh TODO if in the off chance I get to this.
        #print(self.symbols.index(self.currentToken) +  "index")
        try:
            return self.symbols2[self.symbols.index(self.currentToken)]

        except:
            return"BAD CODING PRACTICE!" + str(self.currentToken)
       
    def identifier(self):#STRING 
        return self.currentToken
    def intVal(self):#INT
        return int(self.currentToken)
    def stringVal(self):#STRING
        return self.currentToken[1:len(self.currentToken)-1]