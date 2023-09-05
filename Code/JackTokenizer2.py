class JackTokenizer2:
    def __init__(self, f):
        self.spotLine = 0
        self.currentLine  = 0
        self.input = open(f).readlines()
        self.inFunction = False
        self.keywords = ['class','constructor','function','method','field','static'
    ,'var','int','char','boolean','void','true','false','null','this'
    ,'let','do','if','else','while','return']
        self.symbols=['{','}','(',')','[',']','.',',',';','+','-','*','/','&','|','<','>','=',"~"]
        self.symbols2=['{','}','(',')','[',']','.',',',';','+','-','*','/','&amp','|','&lt','&gt','=',"~"]

        self.final=[]
        self.currentID = ''

        ##while there are more characters, and if the current spot is not a character 
        ##THEN get the current token and its type then add it to an array in teh form
        ##[<type>token</type>]
        
        try:
            for i in range(0,len(self.input)):
            
                c=self.input[i].strip()
                c=c.rstrip("\\n")
                self.input[i]=c
                if(self.input[i]==''):
                    self.input.pop(i)
        except:
            #print(self.input)
            print(" ")


        

       
        






    def MoreTokens(self):
        if (len(self.input)-1 == self.currentLine) and (len(self.input[self.currentLine])-1 == self.spotLine):
            return False
        else:
            return True

    def isComment(self,column, row):
        inComment = "F"
        prev1=""
        prev2=""
        self.spotLine = 0
        self.currentLine = 0
        while(self.MoreTokens()):#//TODO ensure that the lengths etc are correct
            try:
                if self.input[self.currentLine].startswith("//",self.spotLine):
                    if (column == self.currentLine) and (row >= self.spotLine):
                        self.spotLine=row
                        self.currentLine=column
                        return "T"
                
                elif self.input[self.currentLine].startswith("/*",self.spotLine):
                    inComment="T"
                
                elif self.input[self.currentLine].startswith("*/",self.spotLine-2):
                    
                    inComment="F"
            except:
                print(self.input[self.currentLine])
            
            if (column == self.currentLine) and (row == self.spotLine):
                self.spotLine=row
                self.currentLine=column
                return inComment
            self.MoveChar(1)


    def GetXML(self):
        self.currentLine=0
        self.spotLine=0
        while(self.MoreTokens()):
            print(str(self.currentLine)+"  "+str(self.spotLine))
            print(self.final)
            if self.input[self.currentLine]=='':
                print("HERE")
                self.currentLine = self.currentLine+1
                continue
            if (self.isComment(self.currentLine,self.spotLine)=="F"):
                print(str(self.currentLine) + "--" + str(self.spotLine))
                print(self.final)
                print(self.isComment(self.currentLine,self.spotLine))
                for i in self.keywords:
                    if (self.input[self.currentLine].startswith(i, self.spotLine)):
                        self.final.append("<keyword>"+i+"</keyword>")
                        self.MoveChar(len(i))
                        continue
                for i in self.symbols:
                    if (self.input[self.currentLine].startswith(i, self.spotLine)):
                        if len(self.currentID) > 0:
                            self.final.append("<identifier>"+self.currentID+"</identifier>")
                            self.currentID=''
                        self.final.append("<symbol>"+self.symbols2[self.symbols.index(i)]+"</symbol>")
                        self.MoveChar(len(i))
                        continue
                
                if self.input[self.currentLine].startswith(" ", self.spotLine):
                    if len(self.currentID)>0:
                            self.final.append("<identifier>"+self.currentID+"</identifier>")
                            self.currentID=''
                    self.MoveChar(1)
                    continue
               
                    
                
                elif self.input[self.currentLine].startswith("\"", self.spotLine):
                    x=True
                    strng=[]
                    while(x==True):
                        self.MoveChar(1)
                        
                        if self.input[self.currentLine].startswith("\"", self.spotLine):
                            x=False
                            self.MoveChar(1)
                        else:
                            strng.append(self.input[self.currentLine][self.spotLine])
                            
                    self.final.append("<string_const>"+''.join(strng)+"</string_const>")
                    continue
                elif self.input[self.currentLine].startswith("0",self.spotLine) or self.input[self.currentLine].startswith("1",self.spotLine) or self.input[self.currentLine].startswith("2",self.spotLine) or self.input[self.currentLine].startswith("3",self.spotLine) or self.input[self.currentLine].startswith("4",self.spotLine) or self.input[self.currentLine].startswith("5",self.spotLine) or self.input[self.currentLine].startswith("6",self.spotLine) or self.input[self.currentLine].startswith("7",self.spotLine) or self.input[self.currentLine].startswith("8",self.spotLine) or self.input[self.currentLine].startswith("9",self.spotLine):
                    x=True
                    strng=[]
                    while(x==True):#TODO TODO COMMENT CHECKING!
                        self.MoveChar(1)
                        
                        if not (self.input[self.currentLine].startswith("0",self.spotLine) or self.input[self.currentLine].startswith("1",self.spotLine) or self.input[self.currentLine].startswith("2",self.spotLine) or self.input[self.currentLine].startswith("3",self.spotLine) or self.input[self.currentLine].startswith("4",self.spotLine) or self.input[self.currentLine].startswith("5",self.spotLine) or self.input[self.currentLine].startswith("6",self.spotLine) or self.input[self.currentLine].startswith("7",self.spotLine) or self.input[self.currentLine].startswith("8",self.spotLine) or self.input[self.currentLine].startswith("9",self.spotLine)):
                            x=False
                        else:
                            strng.append(self.input[self.currentLine][self.spotLine])
                    self.final.append("<int_const>"+''.join(strng)+"</int_const>")
                    continue
                else:
                    if((self.input[self.currentLine][self.spotLine] != " ") and (self.input[self.currentLine][-1:] != "\n") ):
                        
                        x=self.currentID + self.input[self.currentLine][self.spotLine]
                        self.currentID = x
                    self.MoveChar(1)
                    continue
               
            else:
                self.MoveChar(1)

   

                        






                    
            




         
