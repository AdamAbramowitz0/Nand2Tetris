import sys, os
from Parser import *
from CodeWriter import * 

f=str(sys.argv[1])
if os.path.isdir(f) == False:
    y=open(f[:-3] + ".asm","w")
    y.write(
        "@261"+"\n"+#set value of stack pointer to 256
        "D=A" + "\n"+
        "@SP"+"\n"+
        "M=D"+"\n"+
        "@LCL"+"\n"+
        "M=D"+"\n"+
        "@256"+"\n"+
        "D=A" + "\n"+
        "@ARG"+"\n"+
        "M=D"+"\n"
            

        )
    parse = Parser(f)
    coder=CodeWriter(y)

    print(f[:-3].replace("/","")) 
    print(f[:-3].replace("/",""))
    while(parse.hasMoreLines()):
        parse.advance()
        if parse.commandType() in {"C_PUSH","C_POP"}:
            coder.writePushPop(parse.commandType(),parse.arg1(),parse.arg2(),f[:-3].replace("/",""))
        elif parse.commandType() in {"C_ARITHMETIC"}:
            coder.writeArithmetic(parse.commandType(),parse.arg1())#Added()
        elif parse.commandType() in {"C_LABEL","C_GOTO","C_IF"}:
            print("HIT!")
            coder.writeBranching(parse.commandType(),parse.arg1())
        elif parse.commandType() in {"C_CALL"}:
            coder.writeCall(parse.commandType(),parse.arg1(),parse.arg2(),f[:-3].replace("/",""))
        elif parse.commandType() in {"C_FUNCTION"}:
            coder.writeFunction(parse.commandType(),parse.arg1(),parse.arg2(),f[:-3].replace("/",""))
        elif parse.commandType() in {"C_RETURN"}:
            coder.writeReturn()
    y.close()
else:

    
    f=str(sys.argv[1])
    list = os.listdir(f)
    finalList = []
    for i in range (0,len(list)):
        if list[i][(len(list[i]))-3:] == ".vm":
            finalList.append(f+"/"+list[i])
    print(finalList)
    z =finalList.index(f+"/Sys.vm")
    print(z)
    finalList.remove(f+"/Sys.vm")
    finalList.insert(0,f+"/Sys.vm")
    
    y =[]
    b=0
    for i in range(0,len(f)-1):
        z=len(f)-i-1
        if f[z]=="/":
            print("hit")
    
            b=i
            break;
    p=f[-b:]
    y=open(f + "/"+p+ ".asm","w")
    for i in range(0, len(finalList)):
        
        print("ROUND + " + str(i))
        
            
        f= finalList[i]
        print("HIHIHIHIHI"+f)
        currFile=f[:-3].replace("/","")
        parse = Parser(f)
        coder=CodeWriter(y) 
        if i == 0:
            y.write(
           
            "@261"+"\n"+#set value of stack pointer to 256
            "D=A" + "\n"+
            "@SP"+"\n"+
            "M=D"+"\n"+
            "@LCL"+"\n"+
            "M=D"+"\n"+
            "@256"+"\n"+
            "D=A" + "\n"+
            "@ARG"+"\n"+
            "M=D"+"\n"+
            
            "@" + "Sys.init" +"\n"+
            
            "0;JMP"+"\n"+

            "("+f[:-3].replace("/","")+"."+ "Sys.init"+"$ret"+str(0)+")"+"\n"

         
            )
        while(parse.hasMoreLines()):
            print("NEW FILE")
            parse.advance()

            y.write("\n"+"\n"+"//instruction:"+parse.instruction()+"\n"+"\n")

            if parse.commandType() in {"C_PUSH","C_POP"}:
                coder.writePushPop(parse.commandType(),parse.arg1(),parse.arg2(),f[:-3].replace("/",""))
            elif parse.commandType() in {"C_ARITHMETIC"}:
                coder.writeArithmetic(parse.commandType(),parse.arg1())#Added()
            elif parse.commandType() in {"C_LABEL","C_GOTO","C_IF"}:
                print("HIT!")
                coder.writeBranching(parse.commandType(),parse.arg1())
            elif parse.commandType() in {"C_CALL"}:
                
                coder.writeCall(parse.commandType(),parse.arg1(),parse.arg2(),f[:-3].replace("/",""))
            elif parse.commandType() in {"C_FUNCTION"}:
                coder.writeFunction(parse.commandType(),parse.arg1(),parse.arg2(),f[:-3].replace("/",""))
            elif parse.commandType() in {"C_RETURN"}:
                coder.writeReturn()
    y.close()