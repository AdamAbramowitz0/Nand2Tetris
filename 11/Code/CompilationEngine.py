from JackTokenizer3 import *
from SymbolTable import *
from VMWriter import *
class CompilationEngine:
    def __init__(self,file):
        self.currentToken=''
      
        self.tokens = JackTokenizer3(file)
        self.classLevelTable = SymbolTable()
        self.routineLevelTable = SymbolTable()
        self.writer = VMWriter(file)
        self.queue = []
        self.counter = 0
    def compileClass(self): # class classname { classVarDec* subroutineDec* }
        list=''
        list2 = ''
        self.tokens.advance()#for class
        
        list += ("<class> \n")
        list+= "<keyword> class </keyword> \n"

        self.tokens.advance()
        self.classLevelTable.define(self.tokens.identifier(),"class","NA0")
        list+=( "<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+"> \n")
        list+=("<Eleven>"+ " Name: " + self.tokens.identifier() + " Catagory: " 
               + "class"+ " Index: " + str(self.classLevelTable.indexOf(self.tokens.identifier())) + " Usage: " + "Declared " +"</Eleven> \n")
        self.tokens.advance()
        list+=( "<"+self.tokens.tokenType()+">"+self.tokens.keyWord()+"</"+self.tokens.tokenType()+"> \n")
        self.tokens.advance()
        while self.tokens.keyWord() in ["static","field"]:

           
            
            list+=(self.compileClassVarDec()+"\n")
            self.tokens.advance()
        
        while(self.tokens.keyWord() in ["function","constructor","method"]):#TODO: Important blocsk here
            if(self.tokens.keyWord() in ["method"]):
                list+=self.compileSubroutine("method")+"\n"
            elif(self.tokens.keyWord() in ["constructor"]):
                list+=self.compileSubroutine("constructor")+"\n"
            else:
                list+=self.compileSubroutine("function")+"\n"


            #self.tokens.advance()
        #self.tokens.advance()
        list+=("<symbol>}</symbol> \n")
        list+="</class> \n"
        self.writer.dump()
        return list

    def compileClassVarDec(self):#static or field  type  varname(, varName)
        list = ''

        name = "" #Example, John
        type = "" #Example int, class name
        kind = "" # static/field/arg/var

        list+=("<classVarDec> \n" + "<"+self.tokens.tokenType()+">"+self.tokens.keyWord()+"</"+self.tokens.tokenType()+">\n")#static or field
        
        kind = self.tokens.keyWord()

        self.tokens.advance()
        if self.tokens.tokenType == "keyword": #NOTE THAT THIS CODE IS NEVER RUN. ABSOLUTELY HORRIBLE!
            list+=("<"+self.tokens.tokenType()+">"+self.tokens.keyWord()+"</"+self.tokens.tokenType()+">\n")#type
        
        else:                                       #Technically a keyword
            list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")
        type= self.tokens.identifier()
        self.tokens.advance()
        list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")
        name = self.tokens.identifier()
        self.tokens.advance()
        self.classLevelTable.define(name,type,kind)
        
        list+=("<Eleven>"+ " Name: " + name + " Catagory: " 
               + self.classLevelTable.kindOf(name)+ " Index: " + self.classLevelTable.indexOf(name) + 
               " Usage: " + "Declared " +"</Eleven> \n")
        
        while(self.tokens.symbol() != ";"):
            if self.tokens.tokenType() == "identifier":
                list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")
                name=self.tokens.identifier()
                self.classLevelTable.define(name,type,kind)
                list+=("<Eleven>"+ " Name: " + name + " Catagory: " 
               + self.classLevelTable.kindOf(name)+ " Index: " + self.classLevelTable.indexOf(name) + 
               " Usage: " + "Declared " +"</Eleven> \n")
            else:
                list+=("<"+self.tokens.tokenType()+">"+self.tokens.symbol()+"</"+self.tokens.tokenType()+">\n")

            self.tokens.advance()
             
        list+=("<"+self.tokens.tokenType()+">"+self.tokens.symbol()+"</"+self.tokens.tokenType()+">\n")
       
        list+=("</classVarDec>")

    
        while(self.tokens.keyWord == "field" or self.tokens.keyWord == "static"):
            list+=("<classVarDec> \n" + "<"+self.tokens.tokenType()+">"+self.tokens.keyWord()+"</"+self.tokens.tokenType()+">\n")#static or field
            self.tokens.advance()
            kind = self.tokens.keyWord()
            if self.tokens.tokenType == "keyword":
                list+=("<"+self.tokens.tokenType()+">"+self.tokens.keyWord()+"</"+self.tokens.tokenType()+">\n")#type
            else:
                list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")
            type = self.tokens.identifier()

            self.tokens.advance()
            list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")#varname
            name = self.tokens.identifier()
            self.classLevelTable.define(name,type,kind)
            list+=("<Eleven>"+ " Name: " + name + " Catagory: " 
               + self.classLevelTable.kindOf(name)+ " Index: " + self.classLevelTable.indexOf(name) + 
               " Usage: " + "Declared " +"</Eleven> \n")
            self.tokens.advance()
            list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")# I think unnecessary but double jeapordy
            self.tokens.advance()
            while(self.tokens.symbol() != ";"):#future error

                list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")
                if(self.tokens.tokenType() != "symbol"):
                    name = self.tokens.identifier()
                    self.classLevelTable.define(name,type,kind)
                    list+=("<Eleven>"+ " Name: " + name + " Catagory: " 
               + self.classLevelTable.kindOf(name)+ " Index: " + self.classLevelTable.indexOf(name) + 
               " Usage: " + "Declared " +"</Eleven> \n")
                self.tokens.advance()
            list+=("<"+self.tokens.tokenType()+">"+self.tokens.symbol()+"</"+self.tokens.tokenType()+">\n")
            self.tokens.advance()
            
            list+=("</classVarDec>")
    
        return list
        
            
    def compileSubroutine(self, spec):
        
        self.routineLevelTable.reset()
        #if(isMethod==True):
            
            #self.routineLevelTable.define("this",self.classLevelTable.classname(),"argument")TODO
            #list+=("<Eleven>"+ " Name: " + self.classLevelTable.classname() + " Catagory: " TODO
            # TODO  + self.classLevelTable.kindOf(self.classLevelTable.classname())+ " Index: " + self.classLevelTable.indexOf(self.classLevelTable.classname()) + 
            #   " Usage: " + "Declared " +"</Eleven> \n")TODO
        #name = "" #Example, John
        #type = "" #Example int, class name
        #kind = "" # static/field/arg/var
        #list+=("<Eleven>"+ " Name: " + name + " Catagory: " 
               #+ self.classLevelTable.kindOf(name)+ " Index: " + self.classLevelTable.indexOf(name) + 
               #" Usage: " + "Declared " +"</Eleven> \n")
        list = ''
        list+=("<subroutineDec> \n" + "<"+self.tokens.tokenType()+">"+self.tokens.keyWord()+"</"+self.tokens.tokenType()+">\n")#const func method
        
        self.tokens.advance()
        if self.tokens.tokenType == "keyword":
            list+=("<"+self.tokens.tokenType()+">"+self.tokens.keyWord()+"</"+self.tokens.tokenType()+">\n")#type
        else:
            list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")
            self.routineLevelTable.define(self.tokens.identifier(),"subroutine","NA1")
            list+=("<Eleven>"+ " Name: " + self.tokens.identifier() + " Catagory: " 
               + self.routineLevelTable.kindOf(self.tokens.identifier())+ " Index: " + self.routineLevelTable.indexOf(self.tokens.identifier()) + 
               " Usage: " + "Declared " +"</Eleven> \n")
        self.tokens.advance()
        name = self.tokens.identifier()
        list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")#subname
        self.classLevelTable.define(self.tokens.identifier(),"NA2","NA3")
        list+=("<Eleven>"+ " Name: " + self.tokens.identifier() + " Catagory: " 
               + self.routineLevelTable.kindOf(self.tokens.identifier())+ " Index: " + self.routineLevelTable.indexOf(self.tokens.identifier()) + 
               " Usage: " + "Declared " +"</Eleven> \n")
        self.tokens.advance()
        list+=("<"+self.tokens.tokenType()+">"+self.tokens.symbol()+"</"+self.tokens.tokenType()+">\n")#(

        self.tokens.advance()
        if(spec =="method"):
            self.routineLevelTable.define("this","argument","argument") #TODO!
        list+=(self.compileParameterList())

     
        list+=("<"+self.tokens.tokenType()+">"+self.tokens.symbol()+"</"+self.tokens.tokenType()+">\n")#)

        self.tokens.advance()
       

        list+=(self.compileSubroutineBody(name,spec))
        list+="</subroutineDec>"
        #self.advance
        
        return list

    def compileParameterList(self): #Can be nothing. type varName (, type VarName)*
        list = ''
        #name = "" #Example, John
        #type = "" #Example int, class name
        #kind = "" # static/field/arg/var
        #self.routineLevelTable.define(self.tokens.identifier(),"subroutine","NA")
        #list+=("<Eleven>"+ " Name: " + name + " Catagory: " 
               #+ self.classLevelTable.kindOf(name)+ " Index: " + self.classLevelTable.indexOf(name) + 
               #" Usage: " + "Declared " +"</Eleven> \n")

       
        list+=("<parameterList> \n")

        

        while(self.tokens.symbol() != ")"):#future error TODO if it is method something different
            type=''
            kind = "argument"
            if self.tokens.tokenType() == "keyword":
                list+=("<"+self.tokens.tokenType()+">"+self.tokens.keyWord()+"</"+self.tokens.tokenType()+">\n")#type
                type = self.tokens.keyWord()
            elif self.tokens.tokenType()=="symbol":
                list+=("<"+self.tokens.tokenType()+">"+self.tokens.symbol()+"</"+self.tokens.tokenType()+">\n")
            
            else:
                
                if(self.tokens.peek() in [",",")"]):
                    
                    list+=("<"+self.tokens.tokenType()+">"+self.tokens.identifier()+"</"+self.tokens.tokenType()+">\n")
                    self.routineLevelTable.define(self.tokens.identifier(),type,kind)
                    list+=("<Eleven>"+ " Name: " + self.tokens.identifier() + " Catagory: " 
                + self.routineLevelTable.kindOf(self.tokens.identifier())+ " Index: " + self.routineLevelTable.indexOf(self.tokens.identifier()) + 
                " Usage: " + "Declared " +"</Eleven> \n")
                
                else:
                    type = self.tokens.identifier()
            self.tokens.advance()
                
        list+=("</parameterList>\n")

        return list
  
    
    
    
    def compileSubroutineBody(self,name, spec):
        
        list = ''

        list+="<subroutineBody> \n" + "<symbol> { </symbol> \n"
        self.tokens.advance()
        
        while self.tokens.keyWord() == "var":
            list += self.compileVarDec()
            self.tokens.advance()
        self.writer.writeFunction(self.classLevelTable.classname()+"."+name,self.routineLevelTable.varCount("var"))#className is returning the subname in this case

        if(spec == "method"): #TODO TODO THIS IS WRONG
            self.writer.writePush("argument","0")
            self.writer.writePop("pointer","0")
            self.writer.changeToMethod("this")
        elif(spec == "constructor"):
            self.writer.writePush("constant",self.classLevelTable.varCount("field"))
            self.writer.writeCall("Memory.alloc", "1")
            self.writer.writePop("pointer", "0")
        #if(spec =="constructor"):

           # while(self.tokens.keyWord() in ["do","while","if","let"]):
                #list+=self.compileStatements()
       # else:
      
        if(spec!= "constructor"):
            while(self.tokens.keyWord() in ["do","while","if","let","return"]):
                list+=self.compileStatements(spec)
        else:
            while(self.tokens.keyWord() in ["do","while","if","let"]):
                list+=self.compileStatements(spec)
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n" 
        self.tokens.advance()
        list+="</subroutineBody> \n"
        if(spec == "constructor"):
            #self.writer.writePush("pointer",0)
            self.writer.writeReturn()
        self.writer.changeToMethod("this")


        self.queue.clear()
        return list




    def compileVarDec(self):
        name = "" #Example, John
        type = "" #Example int, class name
        kind = "" # static/field/arg/var
        #self.routineLevelTable.define(self.tokens.identifier(),"subroutine","NA")
        #list+=("<Eleven>"+ " Name: " + name + " Catagory: " 
               #+ self.classLevelTable.kindOf(name)+ " Index: " + self.classLevelTable.indexOf(name) + 
               #" Usage: " + "Declared " +"</Eleven> \n")
        list = ''
       
        list+="<varDec> \n"+"<keyword>"+self.tokens.keyWord()+"</keyword> \n"
        kind = self.tokens.keyWord()
        self.tokens.advance()
        if self.tokens.tokenType() == "keyword":
            list+="<keyword>"+self.tokens.keyWord()+"</keyword> \n"
            type = self.tokens.identifier()
        else:
            list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
            type = self.tokens.identifier()
        self.tokens.advance()
        list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
        name = self.tokens.identifier()
        self.routineLevelTable.define(name,type,kind)
        list+=("<Eleven>"+ " Name: " + name + " Catagory: " 
                + self.routineLevelTable.kindOf(name)+ " Index: " + self.routineLevelTable.indexOf(name) + 
                " Usage: " + "Declared " +"</Eleven> \n")
        self.tokens.advance()
        while(self.tokens.symbol() != ";"):
            #self.tokens.tokenType())
            if self.tokens.tokenType() == "symbol":
                list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
            else:
                list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
                
                self.routineLevelTable.define(self.tokens.identifier(),type,kind)
                name = self.tokens.identifier()
                list+=("<Eleven>"+ " Name: " + name + " Catagory: " 
                + self.routineLevelTable.kindOf(name)+ " Index: " + self.routineLevelTable.indexOf(name) + 
                " Usage: " + "Declared " +"</Eleven> \n")
            self.tokens.advance()
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"+"</varDec> \n"
      
        return list

    def compileStatements(self,spec):
        #"the error is here")
        #print(self.tokens.keyWord())

        #name = "" #Example, John
        #type = "" #Example int, class name
        #kind = "" # static/field/arg/var
        #self.routineLevelTable.define(self.tokens.identifier(),"subroutine","NA")
        #list+=("<Eleven>"+ " Name: " + name + " Catagory: " 
               #+ self.classLevelTable.kindOf(name)+ " Index: " + self.classLevelTable.indexOf(name) + 
               #" Usage: " + "Declared " +"</Eleven> \n")
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
                list+= self.compileReturn(spec)
                self.tokens.advance()
            
        list+="</statements>\n"
        
        return list
    

    



    def compileIf(self):
        z=self.counter
        self.counter+=2
        list = ''
        list+="<ifStatement> \n <keyword>"+self.tokens.keyWord()+"</keyword> \n"

        self.tokens.advance()
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
    
        self.tokens.advance()
        list+=self.compileExpression() #expression

        self.writeCode()
        self.queue.clear()
        self.writer.writeArithmetic("~")
        self.writer.writeIf(self.classLevelTable.classname() + str(z)) #l1
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"

        self.tokens.advance()
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
        self.tokens.advance()
        if (self.tokens.keyWord() in ["let","if","while","do","return"]):
            list+=self.compileStatements("none")
        else:
            list+="<statements> \n </statements> \n"
        self.writer.writeGoto(self.classLevelTable.classname() + str(z+1))

        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
        self.tokens.advance()
        self.writer.writeLabel(self.classLevelTable.classname() + str(z))
        if self.tokens.keyWord() == "else":
            list+="<keyword>"+self.tokens.keyWord()+"</keyword> \n"

            self.tokens.advance()
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"

            self.tokens.advance()
            if (self.tokens.keyWord() in ["let","if","while","do","return"]):
                list+=self.compileStatements("none")
            else:
                list+="<statements> \n </statements> \n"
            
                
           

            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n "
            self.tokens.advance()
        self.writer.writeLabel(self.classLevelTable.classname() + str(z+1))

        list+="</ifStatement> \n"

        return list


    def compileWhile(self):
        z=self.counter
        self.counter+=2
        list = ''
        list+="<whileStatement> \n <keyword>"+self.tokens.keyWord()+"</keyword> \n"

        self.tokens.advance()
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
    
        self.tokens.advance()
        list+=self.compileExpression() #expression
        self.writer.writeLabel(self.classLevelTable.classname() + str(z))
        self.counter+=1
        self.writeCode()
        self.queue.clear()
        self.writer.writeArithmetic("~")
        self.writer.writeIf(self.classLevelTable.classname() + str(z+1))

        
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"

        self.tokens.advance()
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"

        self.tokens.advance()
        while(self.tokens.keyWord() in ["do","while","if","let","return"]):
            
            list+=self.compileStatements("none")
            
        self.writer.writeGoto(self.classLevelTable.classname() + str(z))
        self.writer.writeLabel(self.classLevelTable.classname() + str(z+1))
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n </whileStatement>\n"
        
        return list

    def compileDo(self): #subName(exp list), classname/varname.subName(explist)
        # expression statement and then pop temp 0
        #name = "" #Example, John
        #type = "" #Example int, class name
        #kind = "" # static/field/arg/var
        #self.routineLevelTable.define(self.tokens.identifier(),"subroutine","NA")
        #list+=("<Eleven>"+ " Name: " + name + " Catagory: " 
               #+ self.classLevelTable.kindOf(name)+ " Index: " + self.classLevelTable.indexOf(name) + 
               #" Usage: " + "Declared " +"</Eleven> \n") 
       
        list = ''
        list+="<doStatement> \n <keyword>"+self.tokens.keyWord()+"</keyword> \n"
        name2=''
        functions = self.tokens.numCombfPar() +1
        
        
        self.tokens.advance()
        x=self.compileExpression()
  

        self.writeCode()
        self.queue.clear()
            #self.writer.writeCall(name+"."+name2, str(functions))
        self.writer.writePop("temp", str(0))
        return list
    
    
    
    
    
    def compileReturn(self,spec):
        list = ''
        list+="<returnStatement> \n <keyword>"+self.tokens.keyWord()+"</keyword> \n"
        self.tokens.advance()
        
        if self.tokens.symbol() != ";":
            
            list+=self.compileExpression() #expression
            if(spec != "constructor"):
                self.writeCode()
                self.queue.clear()
        else:
            
            self.writer.writePush("constant",0)
        list+="<symbol>"+self.tokens.symbol()+"</symbol> \n </returnStatement> \n"
 
            
        if(spec != "constructor"):
            self.writer.writeReturn()
        else:
            self.writer.writePush("pointer",0)
        return list


    

    def compileLet(self):
        #name = "" #Example, John
        #type = "" #Example int, class name
        #kind = "" # static/field/arg/var
        #self.routineLevelTable.define(self.tokens.identifier(),"subroutine","NA")
        #list+=("<Eleven>"+ " Name: " + name + " Catagory: " 
               #+ self.classLevelTable.kindOf(name)+ " Index: " + self.classLevelTable.indexOf(name) + 
               #" Usage: " + "Declared " +"</Eleven> \n") 
        list = ''
        list+="<letStatement> \n <keyword>"+self.tokens.keyWord()+"</keyword> \n"
        self.tokens.advance()
        name = self.tokens.identifier()
        
        list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
        list+=("<Eleven>"+ " Name: " + self.tokens.identifier() + " Catagory: " 
               + self.routineLevelTable.kindOf(name)+ " Index: " + self.routineLevelTable.indexOf(self.tokens.identifier()) + 
               " Usage: " + "declared " + "TYPE AGH:"+self.routineLevelTable.typeOf(name) + "</Eleven> \n") 
        self.tokens.advance()
        z=[]
        if self.tokens.symbol() == "[":
            z=["YOYOYO",name]
            while(self.tokens.identifier() != "="):
                z.append(self.tokens.identifier())
                self.tokens.advance()
            self.queue = z
            self.writeCode()
            
    
            self.queue.clear()
            self.tokens.advance()
            
            self.compileExpression()
            
            self.writeCode()
            self.writer.writePop("temp","0")
            self.writer.writePop("pointer","1")
            self.writer.writePush("temp","0")
            self.writer.writePop("that","0")#Wrong

        #else
        # 
        else:    
            list+="<symbol>"+self.tokens.symbol()+"</symbol>\n"
            self.tokens.advance()

            x=self.compileExpression()
            
            
            self.writeCode()

            

      

            if(self.routineLevelTable.typeOf(name) !="NONE"):
                
                self.writer.writePop(self.routineLevelTable.kindOf(name),self.routineLevelTable.indexOf(name))
            else:
                self.writer.writePop(self.classLevelTable.kindOf(name),self.classLevelTable.indexOf(name))

        self.queue.clear()

        #list+=x
    
        #list+="<symbol>"+self.tokens.symbol()+"</symbol> \n </letStatement> \n"

        return list
    
    def compileExpression(self):
        
        list = ''
        list+="<expression> \n" +self.compileTerm()
        
        #self.tokens.advance()
        while self.tokens.symbol() in ["+","-","/","*","|","<",">","=","&lt;","&gt;","&quot;","&amp;"]:
            
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
            self.queue.append(self.tokens.symbol())
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
            self.queue.append(str(self.tokens.intVal()))
            self.tokens.advance()
        elif(self.tokens.tokenType() == "stringConstant"):
            list+= "<stringConstant>"+self.tokens.stringVal()+ "</stringConstant> \n"
            self.queue.append(self.tokens.stringVal())
            self.tokens.advance()
        elif(self.tokens.keyWord() in ["true","false","null","this"]):
            list+= "<keyword>"+self.tokens.keyWord()+ "</keyword> \n"
            if(self.tokens.keyWord() == "true"):
                self.queue.append("-1")
            elif(self.tokens.keyWord() in ["false","null"]):
                self.queue.append("0")
            else:
                self.queue.append(self.tokens.keyWord())

            self.tokens.advance()
        elif(self.tokens.symbol() in ["-","~"]):
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
            self.queue.append(self.tokens.symbol())
            self.tokens.advance()
            list+=self.compileTerm()
            #self.tokens.advance()
        elif(self.tokens.symbol() == "("):
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
            self.queue.append(self.tokens.symbol())
            self.tokens.advance()
            list+=self.compileExpression()
            
            
            list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
            self.queue.append(self.tokens.symbol())
            self.tokens.advance()

        else:
            
            if self.tokens.peek() == "[":
                list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
                self.queue.append(self.tokens.identifier())
                list+=("<Eleven>"+ " Name: " + self.tokens.identifier() + " Catagory: " 
               + self.routineLevelTable.kindOf(self.tokens.identifier())+ " Index: " + self.routineLevelTable.indexOf(self.tokens.identifier()) + 
               " Usage: " + "used " +"</Eleven> \n") 
                self.tokens.advance()
                list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
                self.queue.append(self.tokens.symbol())
                self.tokens.advance()
                list+=self.compileExpression()
        
                list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
                self.queue.append(self.tokens.symbol())
                self.tokens.advance()

            elif self.tokens.peek() in ["(","."]:
                
                if self.tokens.peek() =="(":
                    list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
                    self.queue.append(self.tokens.identifier())
                    list+=("<Eleven>"+ " Name: " + self.tokens.identifier() + " Catagory: " 
               + self.classLevelTable.kindOf(self.tokens.identifier())+ " Index: " + 
               self.classLevelTable.indexOf(self.tokens.identifier()) + 
               " Usage: " + "used " +"</Eleven> \n") 
                    self.tokens.advance()
                    list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
                    self.queue.append(self.tokens.symbol())
                    self.tokens.advance()
                    #while(self.tokens.identifier() !=")"):
                        #self.queue.append(self.tokens.identifier)
                        #self.tokens.advance()
                    list+=self.compileExpressionList()
                    #if(self.tokens.identifier() !=")"): #TODO SHOULD I USE EXPLIST
                        #list+=self.compileExpression()
                    
                    list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
                   
                    self.queue.append(self.tokens.symbol())

                    self.tokens.advance()
                else:
                    list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
                    self.queue.append(self.tokens.identifier())

                    list+=("<Eleven>"+ " Name: " + self.tokens.identifier() + " Catagory: " 
               + self.classLevelTable.kindOf(self.tokens.identifier())+ " Index: " + self.classLevelTable.indexOf(self.tokens.identifier()) + 
               " Usage: " + "used " +"</Eleven> \n") 
                    self.tokens.advance()
                    list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
                    self.queue.append(self.tokens.symbol())

                    self.tokens.advance()
                    list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
                    self.queue.append(self.tokens.identifier())

                    self.tokens.advance()
                    list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
                    self.queue.append(self.tokens.symbol())
                    self.tokens.advance()
                    list+=self.compileExpressionList()
                    
                    
                    list+="<symbol>"+self.tokens.symbol()+"</symbol> \n"
                    self.queue.append(self.tokens.symbol())
                    self.tokens.advance()
        
            elif self.tokens.peek() != "EH":
                list+=("<Eleven>"+ " Name: " + self.tokens.identifier() + " Catagory: " 
               + self.routineLevelTable.kindOf(self.tokens.identifier())+ " Index: " + self.routineLevelTable.indexOf(self.tokens.identifier()) + 
               " Usage: " + "used " +"</Eleven> \n") 
                list+="<identifier>"+self.tokens.identifier()+"</identifier> \n"
                self.queue.append(self.tokens.identifier())
                self.tokens.advance()
        list+="</term>\n"
        
        return list
    def writeCode(self):
        self.alg(self.queue)
      
    def alg(self, exp):#['1', '+', '(', '2', '*', '3', ')']
#or isinstance(exp,str)
        if(isinstance(exp,str)):
      
            if(exp in ["*","/","+","-","=",">","<","&","|","&amp;","&lt;","&gt;"]):
               
                self.writer.writeArithmetic(exp)
            elif(not(exp.isdigit() or exp[0]=="-")):
                
                if(exp == "this"):
                    self.writer.writePush("pointer","0")#TODO uncertain
                elif(exp == "true"):
                    self.writer.writePush("constant", "-1")
                elif(exp == "false"):
                    self.writer.writePush("constant", "0")
                else:
                    
               
                    if(self.routineLevelTable.typeOf(exp)!="NONE"):
                        self.writer.writePush(self.routineLevelTable.kindOf(exp), self.routineLevelTable.indexOf(exp))
                    else:
                        self.writer.writePush(self.classLevelTable.kindOf(exp), self.classLevelTable.indexOf(exp))
            
            else:
                self.writer.writePush("constant",exp)
        elif(len(exp)==1): 
           
            if(exp[0] in ["*","/","+","-","=",">","<","&","|","&amp;","&lt;","&gt;"]):
        
                self.writer.writeArithmetic(exp[0])
            #print(isinstance(exp,str))
            elif(exp[0][0]=="\""):
                length=0
                i=1
                while(exp[0][i]!="\""):
                    length+=1
                    i+=1
                i=1
                self.writer.writePush("constant",length)
                self.writer.writeCall("String.new",1)
                while(exp[0][i]!="\""):
                        self.writer.writePush("constant",ord(exp[0][i]))#character code
                        self.writer.writeCall("String.appendChar",2)
                        i+=1
                if(len(exp)>length+2):
                    self.alg(exp[length+2:])
            elif(not (exp[0].isdigit() or exp[0][0]=="-")): 
                
                if(exp[0] == "this"):
                    self.writer.writePush("pointer",0)#TODO uncertain

                elif(exp[0] == "true"):
                    self.writer.writePush("constant", "-1")
                elif(exp[0] == "false"):
                    self.writer.writePush("constant", "0")
                else:
                    
                    
                    if((self.routineLevelTable.typeOf(exp[0])!="NONE")):
                     
                        self.writer.writePush(self.routineLevelTable.kindOf(exp[0]), self.routineLevelTable.indexOf(exp[0]))
                    else:
                        self.writer.writePush(self.classLevelTable.kindOf(exp[0]), self.classLevelTable.indexOf(exp[0]))
            
            else: 
                self.writer.writePush("constant",exp[0])
        elif(exp[0]=="YOYOYO"):
            exp=exp[1:]
            if((self.routineLevelTable.typeOf(exp[0])!="NONE")):
                self.writer.writePush(self.routineLevelTable.kindOf(exp[0]), self.routineLevelTable.indexOf(exp[0]))
            else:
                self.writer.writePush(self.classLevelTable.kindOf(exp[0]), self.classLevelTable.indexOf(exp[0]))

            if(len(exp)>3):
        
                self.alg(exp[2:-1])
                self.writer.writeArithmetic("+")
                #TEST

        elif(exp[1] =="["):
            if((self.routineLevelTable.typeOf(exp[0])!="NONE")):
                self.writer.writePush(self.routineLevelTable.kindOf(exp[0]), self.routineLevelTable.indexOf(exp[0]))
            else:
                self.writer.writePush(self.classLevelTable.kindOf(exp[0]), self.classLevelTable.indexOf(exp[0]))
        

            x=True
            i = 2
            nPar=0
            while(x):
                if(exp[i]=="]" and nPar == 0):
                    x=False
                elif(exp[i]=="["):
                     i+=1
                     nPar+=1
                elif(exp[i]=="]" and nPar != 0):
                    nPar = nPar-1
                    i+=1
                else:
                    i+=1    
            if(i!=2):
                self.alg(exp[2:i])
                self.writer.writeArithmetic("+")
            self.writer.writePop("pointer","1")
            self.writer.writePush("that",0)
            if(len(exp)>i+1):
                self.alg(exp[i+1:])
            

            
        elif(exp[0]=="("):
            counter = 0
            nPar = 0
            x=True
            while(x):
                if(exp[counter] == "("):
                    nPar+=1
                elif(exp[counter]==")" and nPar >1):
                    nPar -= 1
                elif(exp[counter]==")" and nPar ==1):
                    x=False
                counter +=1
            self.alg(exp[1:counter-1])
       
            if(len(exp)>counter):
                self.writer.setSub("sub")
                self.alg(exp[counter:])
        #elif(exp[1]=="." and exp[2] == "new"):

        
        
       
        #,"&amp;","&lt;","&gt;"
        elif(exp[1] in ["*","/","+","-","=",">","<","&","|","&amp;","&lt;","&gt;"]):
            a=exp[0]
            b=exp[2]
            c= exp[2:]
          
            d=exp[1]
          
            self.alg(a)
        
            if(len(exp) == 3):
               self.alg(b) 
            else:
                self.alg(c) #['2', '*', '3']
            self.writer.setSub("sub")
            self.writer.writeArithmetic(d)
        elif(exp[0] in ["*","/","+","-","=",">","<","&","|","~","&amp;","&lt;","&gt;"]):
            #might need to have one more of these for other unary op.
            if(isinstance(exp,str)):
                if(exp[0] == "-"):
                    self.writer.writePush("constant",exp[1:])

            elif(exp[0] == "-" and exp[1].isdigit()):
                if(exp[0] == "-"):
                    self.writer.writePush("constant",exp[1])
                    self.writer.writeArithmetic("neg")
                    if(len(exp)>2):
                        self.alg(exp[2:])
            
            else:
                b=exp[0]
                
                self.alg(exp[1:])
            
                self.writer.writeArithmetic(b)
            
        elif(exp[1]in[".","("]):#routine (COULD CAUSE ISSUES) ie (.5)*10 is not a routine IDEALLY THIS DOES NOT EXIST AT ALL
            x=0
            n=0

            self.classLevelTable.printNames()
            if(exp[1] == "."):
                n=4
                title = exp[0]+exp[1]+exp[2]
               
         
                if(self.routineLevelTable.typeOf(exp[0])!="NONE" and exp[1] == "."): #METHOD
                    
                    x=1
                    title = self.routineLevelTable.typeOf(exp[0])+exp[1]+exp[2]
                    self.writer.writePush(self.routineLevelTable.kindOf(exp[0]), self.routineLevelTable.indexOf(exp[0]))
                elif(self.classLevelTable.typeOf(exp[0])!="NONE" and exp[1] == "."): #METHOD
                    x=1
                   
                    title = self.classLevelTable.typeOf(exp[0])+exp[1]+exp[2]
                    self.classLevelTable.kindOf(exp[0])
                    self.writer.writePush(self.classLevelTable.kindOf(exp[0]), self.classLevelTable.indexOf(exp[0]))
                n =4
            elif(exp[1] == "("):
                x=1
                title = str(self.classLevelTable.classname())+"."+exp[0]
                self.writer.writePush("pointer",0)
                n=2
            z=[]
            nArgs=0
            nPar = 0
            p=True
      
            nArgs = 0
            while(p==True):
                if(exp[n] == ")" and nPar == 0):
                  
             

                    if(len(z) >0):
                        self.alg(z)
                        nArgs+=1
                    z=[]
                    p=False
                elif(exp[n] == ")" and nPar != 0):
                    nPar-=1
                    z.append(exp[n])
                elif(exp[n] =="("):
                    nPar+=1
                    z.append(exp[n])
                elif(exp[n] == ","):
                    nArgs+=1

                    self.alg(z)

             
                    z=[]
                else:
                    z.append(exp[n])
                n+=1
            self.writer.writeCall(title, nArgs+x)
     
            if(len(exp)> n+1):
               
                self.alg(exp[n+1:])
            


    def compileExpressionList(self):
     
        list = ''
        list+="<expressionList> \n"
        nPar = 0
        while(True):
            if(self.tokens.identifier() == ")" and nPar == 0):
                list+="</expressionList> \n"
             
                return list
            elif(self.tokens.identifier() == ")" and nPar != 0):
                nPar = nPar-1
            elif(self.tokens.identifier() =="("):
                nPar+=1
            self.queue.append(self.tokens.identifier())
            self.tokens.advance()
        
            
        
 

