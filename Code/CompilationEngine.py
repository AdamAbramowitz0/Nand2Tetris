from JackTokenizer3 import *
class CompilationEngine:
    def __init__(self,file):
        self.currentToken=''
        self.tokens = JackTokenizer3(file)
    def compileClass(self): # class classname { classVarDec* subroutineDec* }
        list=''
        self.tokens.advance()#for class
        
        list += ("<class> \n")
        list+= "<keyword> class </keyword> \n"

        self.tokens.advance()
        list+=( "<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+"> \n")
    
        self.tokens.advance()
        list+=( "<"+self.tokens.tokenType()+">"+self.tokens.keyWord()+"</"+self.tokens.tokenType()+"> \n")
        self.tokens.advance()
        while self.tokens.keyWord() in ["static","field"]:

           

            list+=(self.compileClassVarDec()+"\n")
            self.tokens.advance()
        
        while(self.tokens.keyWord() in ["function","constructor","method"]):
            list+=self.compileSubroutine()+"\n"
            #self.tokens.advance()
        #self.tokens.advance()
        list+=("<symbol>}</symbol> \n")
        list+="</class> \n"
       
        return list

    def compileClassVarDec(self):#static or field  type  varname(, varName)
        list = ''

        list+=("<classVarDec> \n" + "<"+self.tokens.tokenType()+">"+self.tokens.keyWord()+"</"+self.tokens.tokenType()+">\n")#static or field
        self.tokens.advance()
        if self.tokens.tokenType == "keyword":
            list+=("<"+self.tokens.tokenType()+">"+self.tokens.keyWord()+"</"+self.tokens.tokenType()+">\n")#type
        else:
            list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")
       
        self.tokens.advance()
        list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")
        self.tokens.advance()
        while(self.tokens.symbol() != ";"):
            if self.tokens.tokenType() == "identifier":
                list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")
            else:
                list+=("<"+self.tokens.tokenType()+">"+self.tokens.symbol()+"</"+self.tokens.tokenType()+">\n")

            self.tokens.advance()
             
        list+=("<"+self.tokens.tokenType()+">"+self.tokens.symbol()+"</"+self.tokens.tokenType()+">\n")
       
        list+=("</classVarDec>")

    
        while(self.tokens.keyWord == "field" or self.tokens.keyWord == "static"):
            list+=("<classVarDec> \n" + "<"+self.tokens.tokenType()+">"+self.tokens.keyWord()+"</"+self.tokens.tokenType()+">\n")#static or field
            self.tokens.advance()
            if self.tokens.tokenType == "keyword":
                list+=("<"+self.tokens.tokenType()+">"+self.tokens.keyWord()+"</"+self.tokens.tokenType()+">\n")#type
            else:
                list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")
            self.tokens.advance()
            list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")#varname

            self.tokens.advance()
            list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")
            self.tokens.advance()
            while(self.tokens.symbol() != ";"):#future error
                list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")
                self.tokens.advance()
            list+=("<"+self.tokens.tokenType()+">"+self.tokens.symbol()+"</"+self.tokens.tokenType()+">\n")
            self.tokens.advance()
            
            list+=("</classVarDec>")
    
        return list
        
            
    def compileSubroutine(self):
      
        list = ''
        list+=("<subroutineDec> \n" + "<"+self.tokens.tokenType()+">"+self.tokens.keyWord()+"</"+self.tokens.tokenType()+">\n")#const func method
        self.tokens.advance()
        if self.tokens.tokenType == "keyword":
            list+=("<"+self.tokens.tokenType()+">"+self.tokens.keyWord()+"</"+self.tokens.tokenType()+">\n")#type
        else:
            list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")
        self.tokens.advance()
        list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")#subname
       
        self.tokens.advance()
        list+=("<"+self.tokens.tokenType()+">"+self.tokens.symbol()+"</"+self.tokens.tokenType()+">\n")#(

        self.tokens.advance()
        list+=(self.compileParameterList())

     
        list+=("<"+self.tokens.tokenType()+">"+self.tokens.symbol()+"</"+self.tokens.tokenType()+">\n")#)

        self.tokens.advance()
        list+=(self.compileSubroutineBody())
        list+="</subroutineDec>"
        #self.advance

        return list

    def compileParameterList(self): #Can be nothing. type varName (, type VarName)*
        list = ''
  
       
        list+=("<parameterList> \n")

        while(self.tokens.symbol() != ")"):#future error
            if self.tokens.tokenType() == "keyword":
                list+=("<"+self.tokens.tokenType()+">"+self.tokens.keyWord()+"</"+self.tokens.tokenType()+">\n")#type
            elif self.tokens.tokenType()=="symbol":
                list+=("<"+self.tokens.tokenType()+">"+self.tokens.symbol()+"</"+self.tokens.tokenType()+">\n")
            else:
                list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")
            self.tokens.advance()

        list+=("</parameterList>\n")

        return list
  
    
    
    
    def compileSubroutineBody(self):

        list = ''

        list+="<subroutineBody> \n" + "<symbol> { </symbol> \n"
        self.tokens.advance()
        while self.tokens.keyWord() == "var":
            list += self.compileVarDec()
            self.tokens.advance()
        
        while(self.tokens.keyWord() in ["do","while","if","let","return"]):
            list+=self.compileStatements()
    
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n" 
        self.tokens.advance()
        list+="</subroutineBody> \n"

        return list




    def compileVarDec(self):
        list = ''
       
        list+="<varDec> \n"+"<keyword>"+self.tokens.keyWord()+"</keyword> \n"

        self.tokens.advance()
        if self.tokens.tokenType() == "keyword":
            list+="<keyword>"+self.tokens.keyWord()+"</keyword> \n"
        else:
            list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
        self.tokens.advance()
        list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
        self.tokens.advance()
        while(self.tokens.symbol() != ";"):
            #self.tokens.tokenType())
            if self.tokens.tokenType() == "symbol":
                list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
            else:
                list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
            self.tokens.advance()
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"+"</varDec> \n"
      
        return list

    def compileStatements(self):
        #"the error is here")
        #print(self.tokens.keyWord())
        list = ''
        list+="<statements>\n"
        while(self.tokens.keyWord() in ["let","if","while","do","return"]):
            if(self.tokens.keyWord() =="let"):
                list+= self.compileLet()
                self.tokens.advance()
            elif(self.tokens.keyWord() =="if"):
                list+= self.compileIf()
            elif(self.tokens.keyWord() =="while"):
                list+= self.compileWhile()
                self.tokens.advance()
            elif(self.tokens.keyWord() =="do"):
                list+= self.compileDo()
                self.tokens.advance()
            elif(self.tokens.keyWord() =="return"):
                list+= self.compileReturn()
                self.tokens.advance()
            
        list+="</statements>\n"
        
        return list
    

    def compileLet(self): 
        list = ''
        list+="<letStatement> \n <keyword>"+self.tokens.keyWord()+"</keyword> \n"
        self.tokens.advance()
        list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
        self.tokens.advance()
        if self.tokens.symbol() == "[":
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
            self.tokens.advance()
            list+=self.compileExpression()
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
            self.tokens.advance()
            
        list+="<symbol>"+self.tokens.symbol()+"</symbol>\n"
        self.tokens.advance()
        x=self.compileExpression()
        
        list+=x
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n </letStatement> \n"
       

        return list



    def compileIf(self):
        list = ''
        list+="<ifStatement> \n <keyword>"+self.tokens.keyWord()+"</keyword> \n"

        self.tokens.advance()
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
    
        self.tokens.advance()
        list+=self.compileExpression() #expression

        
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"

        self.tokens.advance()
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
        self.tokens.advance()
        if (self.tokens.keyWord() in ["let","if","while","do","return"]):
            list+=self.compileStatements()
        else:
            list+="<statements> \n </statements> \n"
            

        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
        self.tokens.advance()
        if self.tokens.keyWord() == "else":
            list+="<keyword>"+self.tokens.keyWord()+"</keyword> \n"

            self.tokens.advance()
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"

            self.tokens.advance()
            if (self.tokens.keyWord() in ["let","if","while","do","return"]):
                list+=self.compileStatements()
            else:
                list+="<statements> \n </statements> \n"
            
                
           

            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n "
            self.tokens.advance()
        list+="</ifStatement> \n"

        return list


    def compileWhile(self):
        list = ''
        list+="<whileStatement> \n <keyword>"+self.tokens.keyWord()+"</keyword> \n"

        self.tokens.advance()
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
    
        self.tokens.advance()
        list+=self.compileExpression() #expression

        
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"

        self.tokens.advance()
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"

        self.tokens.advance()
        while(self.tokens.keyWord() in ["do","while","if","let","return"]):
            
            list+=self.compileStatements()
            
            
        
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n </whileStatement>\n"
        
        return list

    def compileDo(self):
        list = ''
        list+="<doStatement> \n <keyword>"+self.tokens.keyWord()+"</keyword> \n"

        self.tokens.advance()
        list+="<identifier>"+self.tokens.keyWord()+"</identifier> \n"
        self.tokens.advance()
        if self.tokens.symbol() == "(":
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
            self.tokens.advance()
            list+=self.compileExpressionList()
            self.tokens.advance()

            list+="<symbol>"+")"+"</symbol>"+" \n"
            
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n</doStatement> \n"
            return list
        else:
           
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
            self.tokens.advance()
            list+="<identifier>"+self.tokens.keyWord()+"</identifier> \n"
            self.tokens.advance()
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
            self.tokens.advance()
            print("HERE")
            list+=self.compileExpressionList()
            print("HERE")
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
            self.tokens.advance()
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n </doStatement> \n"
            
            return list

    
    
    
    
    def compileReturn(self):
        list = ''
        list+="<returnStatement> \n <keyword>"+self.tokens.keyWord()+"</keyword> \n"
        self.tokens.advance()
        
        if self.tokens.symbol() != ";":
            
            list+=self.compileExpression() #expression
            
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n </returnStatement> \n"
   
        return list



    
    def compileExpression(self):
        list = ''
        list+="<expression> \n" +self.compileTerm()
        #self.tokens.advance()
        print(self.tokens.symbol())
        while self.tokens.symbol() in ["+","-","/","*","|","<",">","=","&lt;","&gt;","&quot;","&amp;"]:
            print(self.tokens.symbol())
            
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
            self.tokens.advance()
            list+=self.compileTerm()
            #self.tokens.advance()
        list+="</expression> \n"
        
        return list

    def compileTerm(self):
        list = ''
        list+="<term> \n"
     
        if(self.tokens.tokenType() == "integerConstant"):
            list+= "<integerConstant>"+str(self.tokens.intVal())+ "</integerConstant> \n"
            self.tokens.advance()
        elif(self.tokens.tokenType() == "stringConstant"):
            list+= "<stringConstant>"+self.tokens.stringVal()+ "</stringConstant> \n"
            self.tokens.advance()
        elif(self.tokens.keyWord() in ["true","false","null","this"]):
            list+= "<keyword>"+self.tokens.keyWord()+ "</keyword> \n"
            self.tokens.advance()
        elif(self.tokens.symbol() in ["-","~"]):
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
            self.tokens.advance()
            list+=self.compileTerm()
            #self.tokens.advance()
        elif(self.tokens.symbol() == "("):
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
            self.tokens.advance()
            list+=self.compileExpression()
            
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
            self.tokens.advance()

        else:
            
            if self.tokens.peek() == "[":
                list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
                self.tokens.advance()
                list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
                self.tokens.advance()
                list+=self.compileExpression()
        
                list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
                self.tokens.advance()

            elif self.tokens.peek() in ["(","."]:
         
                if self.tokens.peek() =="(":
                    list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
                    self.tokens.advance()
                    list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
                    self.tokens.advance()
                    list+=self.compileExpression()
                    
                    list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
                    self.tokens.advance()
                else:
                    list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
                    self.tokens.advance()
                    list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
                    self.tokens.advance()
                    list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
                    self.tokens.advance()
                    list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
                    self.tokens.advance()
                    list+=self.compileExpressionList()
                    
                    
                    list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
                    self.tokens.advance()
            elif self.tokens.peek() != "EH":
                
                list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
                self.tokens.advance()
        list+="</term>\n"
        
        return list

    def compileExpressionList(self):
        list = ''
        list+="<expressionList> \n"
        print(self.tokens.input[self.tokens.currentLine])
        
        while(self.tokens.symbol() != ")" and self.tokens.symbol() != ";"):
        
            list+=self.compileExpression()
            

            if self.tokens.symbol() == ",":
                list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
                self.tokens.advance()
                
                
        
        list+="</expressionList> \n"
        return list

