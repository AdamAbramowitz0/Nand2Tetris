class CodeWriter:
    stack=[]
    counter = 0
    fileName=""
    def __init__(self,f):
        self.counter=0
        self.stack=[]
        self.fileName=f
    

    def writeArithmetic(self,commandType,arg1):
        
        print(len(self.stack))
        top = int(self.stack[len(self.stack)-1])
        second = int(self.stack[len(self.stack)-2])
        if arg1 == "add":
            self.fileName.write("@SP" +"\n" +"A=M-1" + "\n"+"D=M"+"\n"+"@SP"+"\n"+"A=M-1"+"\n"+"A=A-1"+"\n"+"M=D+M"+"\n"+"@SP"+"\n"+"M=M-1"+"\n")
            second=top+second
            self.stack.remove(top)
        elif arg1 == "sub":
            self.fileName.write("@SP" +"\n" +"A=M-1" + "\n"+"D=M"+"\n"+"@SP"+"\n"+"A=M-1"+"\n"+"A=A-1"+"\n"+"M=M-D"+"\n"+"@SP"+"\n"+"M=M-1"+"\n")
            second=int(top)-int(second)
            self.stack.remove(top)
        elif arg1=="neg":
            top=-top
            self.fileName.write("@SP" +"\n"+ "A=M-1" +"\n"+ "M=-M"+"\n")
        elif arg1=="not":
            top=65535-top#NOT SURE IF WORKS
            self.fileName.write("@SP" +"\n"+ "A=M-1" +"\n"+ "M=!M"+"\n")
        elif arg1=="and":
            if top==second:
                self.stack.remove(top)
                self.stack.remove(second)
                self.stack.append(-1)
                self.fileName.write("@SP" +"\n" +"A=M-1" + "\n"+"D=M"+"\n"+"@SP"+"\n"+"A=M-1"+"\n"+"A=A-1"+"\n"+"M=D&M"+"\n"+"@SP"+"\n"+"M=M-1"+"\n")
            else:
                self.stack.remove(top)
                self.stack.remove(second)
                self.stack.append(0)
                self.fileName.write("@SP" +"\n" +"A=M-1" + "\n"+"D=M"+"\n"+"@SP"+"\n"+"A=M-1"+"\n"+"A=A-1"+"\n"+"M=D&M"+"\n"+"@SP"+"\n"+"M=M-1"+"\n")

        elif arg1 == "or":
            if top|second:
                self.stack.remove(top)
                self.stack.remove(second)
                self.stack.append(-1)
                self.fileName.write("@SP" +"\n" +"A=M-1" + "\n"+"D=M"+"\n"+"@SP"+"\n"+"A=M-1"+"\n"+"A=A-1"+"\n"+"M=D|M"+"\n"+"@SP"+"\n"+"M=M-1"+"\n")
            else:
                self.stack.remove(top)
                self.stack.remove(second)
                self.stack.append(0)
                self.fileName.write("@SP" +"\n" +"A=M-1" + "\n"+"D=M"+"\n"+"@SP"+"\n"+"A=M-1"+"\n"+"A=A-1"+"\n"+"M=D|M"+"\n"+"@SP"+"\n"+"M=M-1"+"\n")
        elif arg1=="gt":
           
            self.fileName.write(self.jumps("JGT"))#JUMP CODE IS OPPOSITE TO OPERATION
            if int(top)>int(second):
                self.stack.remove(top)
                self.stack.remove(second)
                self.stack.append(0)

            else:
                self.stack.remove(top)
                self.stack.remove(second)
                self.stack.append(-1)
        elif arg1=="lt":
            self.fileName.write(self.jumps("JLT"))
            if top<second:
                self.stack.remove(top)
                self.stack.remove(second)
                self.stack.append(0)

            else:
                self.stack.remove(top)
                self.stack.remove(second)
                self.stack.append(-1)
        elif arg1=="eq":

            self.fileName.write(self.jumps("JEQ"))
            if  top==second:
                self.stack.remove(top)
                self.stack.remove(second)
                self.stack.append(0)

            else:
                self.stack.remove(top)
                self.stack.remove(second)
                self.stack.append(-1)
                
    def jumps(self, jumpCode):
        self.counter+=1
        return "@SP"+"\n"+"A=M-1" +"\n"+"D=M"+"\n"+"A=A-1"+"\n"+"D=M-D"+"\n"+"@NO" + str(self.counter) +"\n"+ "D;" + str(jumpCode)+"\n"+"@SP"+"\n"+"A=M-1" +"\n"+"A=A-1"+"\n"+"M=0"+"\n"+"@SP"+"\n"+"M=M-1"+"\n"+"@FIN"+str(self.counter)+"\n"+"0;JMP"+"\n"+"(NO"+str(self.counter)+")"+"\n"+"@SP"+"\n"+"A=M-1"+"\n"+"A=A-1"+"\n"+"M=-1"+"\n"+"@SP"+"\n"+"M=M-1"+"\n"+"(FIN"+str(self.counter)+")"+"\n"
    
    def writePushPop(self, commandType, arg1, arg2,nameOfFile):
        if arg1 == "argument":
            arg1 = "ARG"
        if arg1 == "temp":
            arg1 = "5"
        if arg1 == "local":
            arg1 = "LCL" 
        if arg1 == "this":
            arg1="THIS"
        if arg1 == "that":
            arg1="THAT"
      

        if arg1=="constant":
            
            if commandType == "C_PUSH":
                
                
                self.fileName.write("@" +arg2+ "\n"+
"D=A"+ "\n"+
"@SP"+ "\n"+
"A=M"+ "\n"+
"M=D"+ "\n"+
"@SP"+ "\n"+
"M=M+1"+"\n"+ "//PUSH " + arg1 + " " + arg2+"\n")
                self.stack.append(int(arg2))
                
            elif commandType=="C_POP":
                print("Never")
                top = self.stack[len(self.stack)-1]

                self.fileName.write("@SP"+"\n"+"M=M-1"+"\n"+ "//POP " + arg1 + " " + arg2+"\n")
                self.stack.remove(top)
        else:
           
            if commandType=="C_PUSH":
                if arg1=="pointer":
                    if arg2=="0":
                        arg1="THIS"
                    else:
                        arg1="THAT"
                    self.fileName.write("@"+arg1+"\n"+"D=M"+"\n"+"@SP"+"\n"+"A=M"+"\n"+"M=D"+"\n"+"\n" + "@SP"+"\n"+"M=M+1"+"\n")
                    return
                if arg1=="static":
                    self.fileName.write("@"+nameOfFile+"."+arg2+"\n"+"D=M"+"\n"+"@SP""\n"+"A=M"+"\n"+"M=D"+"\n"+"\n"+"@SP"+"\n"+"M=M+1"+"\n")
                    return
                print(arg1+" push " + arg2)
                c=""
                if arg1=="5":
                    c="A"
                else:
                    c="M"
                
                self.fileName.write("@"+arg1+"\n"+
                "D="+c+"\n"+
                "@"+arg2+"\n"+
                "A=D+A"+"\n"+
                "D=M"+"\n"+
                "@SP"+"\n"
                "A=M"+"\n"
                "M=D"+"\n"
                "@SP"+"\n"
                "M=M+1"+"\n"+ "//PUSH " + arg1 + " " + arg2+"\n")
                self.stack.append(int(arg2))
            else:
                if arg1=="pointer":
                    if arg2=="0":
                        arg1="THIS"
                    else:
                        arg1="THAT"
                    self.fileName.write("@SP"+"\n"+"A=M-1"+"\n" +"D=M"+"\n"+"@"+arg1+"\n"+"M=D"+"\n"+"//comment"+"\n" + "@SP"+"\n"+"M=M-1"+"\n")
                    return

                if arg1=="static":
                    self.fileName.write("@SP"+"\n"+"M=M-1"+"\n"+"A=M"+"\n"+"D=M"+"\n"+"@"+nameOfFile+"."+arg2+"\n"+"M=D"+"\n")
                    return
                print(arg1+" pop " + arg2)
                c=""
                if arg1=="5":
                    c="A"
                else:
                    c="M"
                self.fileName.write(
                "@SP"+"\n"+
                "M=M-1"+"\n"+
                "A=M"+"\n"+
                "D=M"+"\n"+
                "@R13"+"\n"+
                "M=D"+"\n"
                "@"+arg1+"\n"
                "D="+c+"\n"
                "@"+arg2+"\n"
                +"D=D+A"+"\n"+"@R14"+"\n"+"M=D"+"\n"+"@R13"+"\n"+"D=M"+"\n" + "@R14"+"\n" + "A=M"+"\n" +"M=D"+ "\n" + "//POP " + arg1 + " " + arg2 +"\n") 
                top = int(self.stack[len(self.stack)-1])
                self.stack.remove(top)
                
#CAN I JUST REPRESENT THE STACK AS AN INTEGER

