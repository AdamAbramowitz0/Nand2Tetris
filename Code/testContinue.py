class JackTokenizer:
    
    def __init__(self, f):
        self.spotLine = 0
        self.currentLine  = 0
        self.input = open(f).readlines()
        self.inFunction = False
        self.keywords = ['class','constructor','function','method','field','static'
    ,'var','int','char','boolean','void','true','false','null','this'
    ,'let','do','if','else','while','return']
        self.symbols=['{','}','(',')','[',']','.',',',';','+','-','*','/','&','|','<','>','=',"~"]
        self.final=[]
       
        currID=""
        zz=True
        
        while(zz):
            print(self.final)
            if (self.currentLine == len(self.input)-1) and (self.spotLine == len(self.input[self.currentLine])-1):
                break
            
            print(str(self.spotLine)+"    "+str(self.currentLine))
        #dealing with comments
    
            if self.inFunction == True:
                if self.input[self.currentLine].startswith("*/",self.spotLine):
                    self.inFunction = False
                if self.spotLine == -1+len(self.input[self.currentLine]):
                    self.spotLine=0
                    self.currentLine+=1
                else:
                    self.spotLine+=1
                    
                continue

            elif self.input[self.currentLine].startswith("/*",self.spotLine) or self.input[self.currentLine].startswith("/**",self.spotLine):
                self.spotLine+=1
                self.inFunction =True
                continue
            
            elif self.input[self.currentLine].startswith("//",self.spotLine):
                self.spotLine = 0
                self.currentLine +=1
                continue
            elif self.input[self.currentLine] == []:
                self.currentLine+=1
                continue
            elif self.input[self.currentLine].startswith(" ",self.spotLine):
                if len(self.input[self.currentLine])==(self.spotLine+1):
                    self.currentLine+=1
                    self.spotLine=0
                else:
                    self.currentLine+=1
                    self.spotLine+=1
                continue

            z=len(self.final)
            for i in self.keywords:
                if self.input[self.currentLine].startswith(i+" ",self.spotLine):
                    self.spotLine=self.spotLine+len(i)+1
                    if len(currID)>0:
                        self.final.append("<IDENTIFIER>"+currID+"</IDENTIFIER>")
                       
                        self.currID=''
                    self.final.append("<keyword>"+i+"</keyword>")
                elif self.input[self.currentLine].startswith(i,self.spotLine) and self.symbols.contains(self.input[self.currentLine][self.spotLine+len(i)]):
                    self.spotLine=self.spotLine+len(i)
                    if len(currID)>0:
                        self.final.append("<IDENTIFIER>"+currID+"</IDENTIFIER>")
                        self.currID=''
                    self.final.append("<keyword>"+i+"</keyword>")
            if z!=len(self.final):
                continue
            z=len(self.final)

            w=0
            for i in self.symbols:   
                
                if self.input[self.currentLine].startswith(i,self.spotLine):
                    w=len(i)

                    
                    if len(currID)>0:
                        self.final.append("<IDENTIFIER>"+currID+"</IDENTIFIER>")
                        self.currID=''
                    self.final.append("<symbol>"+i+"</symbol>")
            self.spotLine=self.spotLine+w
            if z!=len(self.final):
                
                continue
            if self.input[self.currentLine].startswith("0",self.spotLine) or self.input[self.currentLine].startswith("1",self.spotLine) or self.input[self.currentLine].startswith("2",self.spotLine) or self.input[self.currentLine].startswith("3",self.spotLine) or self.input[self.currentLine].startswith("4",self.spotLine) or self.input[self.currentLine].startswith("5",self.spotLine) or self.input[self.currentLine].startswith("6",self.spotLine) or self.input[self.currentLine].startswith("7",self.spotLine) or self.input[self.currentLine].startswith("8",self.spotLine) or self.input[self.currentLine].startswith("9",self.spotLine):
                q=1
                inte=[self.input[self.currentLine][self.spotLine]]
                while(True):
                    if self.input[self.currentLine].startswith("0",self.spotLine+q) or self.input[self.currentLine].startswith("1",self.spotLine+q) or self.input[self.currentLine].startswith("2",self.spotLine+q) or self.input[self.currentLine].startswith("3",self.spotLine+q) or self.input[self.currentLine].startswith("4",self.spotLine+q) or self.input[self.currentLine].startswith("5",self.spotLine+q) or self.input[self.currentLine].startswith("6",self.spotLine+q) or self.input[self.currentLine].startswith("7",self.spotLine+q) or self.input[self.currentLine].startswith("8",self.spotLine+q) or self.input[self.currentLine].startswith("9",self.spotLine+q):
                        q+=1
                        inte.append(self.input[self.currentLine][self.spotLine+q])
                    else:
                        break
                if len(currID)>0:
                    self.final.append("<IDENTIFIER>"+currID+"</IDENTIFIER>")
                    self.currID=''
                self.final.append("<INT_CONST>"+(inte.strip("[")).strip("]").strip("'")+"</INT_CONST>")
                self.spotLine+=q
                continue
            if self.input[self.currentLine].startswith("\"",self.spotLine):
                q=1
                inte=[self.input[self.currentLine][self.spotLine]]
                while(True):
                    if self.input[self.currentLine].startswith("\"",self.spotLine):
                        q+=1
                        inte.append(self.input[self.currentLine][self.spotLine+q])
                    else:
                        break
                if len(currID)>0:
                    self.final.append("<IDENTIFIER>"+currID+"</IDENTIFIER>")
                    self.currID=''
                self.final.append("<STRING_CONST>"+q+"</STRING_CONST>")
                self.spotLine+=q
                continue
            else:
                currID=currID+self.input[self.currentLine][self.spotLine]
                if len(self.input[self.currentLine])==(self.spotLine+1):
                    self.currentLine+=1
                    self.spotLine=0
                else:
                    self.currentLine+=1
                    self.spotLine+=1
                continue
        print(self.final)
        if (len(self.input[self.currentLine]) >= self.currentLine) and (len(self.input[self.currentLine][self.spotLine])>=self.spotLine):
            zz=False              
            




    def getList(self):
        return self.Final                    


    def hasMoreTokens(self):
        if self.currentLine<len(self.input):
            return True
        elif (self.currentLine == len(self.input))&(self.spotLine<len(self.currentLine)):
            return True
        return False


        
            
                    
        