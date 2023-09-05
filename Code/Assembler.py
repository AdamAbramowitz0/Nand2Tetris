import sys
from SymbolTable import *
from Rparse import *
from CodeMod import *


f = str(sys.argv[1])
y=open(f[:-4]+".hack","w")
x=""
table = SymbolTable()
parse1=Rparse(f)
lineNumber=0
table.addEntry("R0",0)
table.addEntry("R1",1)
table.addEntry("R2",2)
table.addEntry("R3",3)
table.addEntry("R4",4)
table.addEntry("R5",5)
table.addEntry("R6",6)
table.addEntry("R7",7)
table.addEntry("R8",8)
table.addEntry("R9",9)
table.addEntry("R10",10)
table.addEntry("R11",11)
table.addEntry("R12",12)
table.addEntry("R13",13)
table.addEntry("R14",14)
table.addEntry("R15",15)
table.addEntry("SP",0)
table.addEntry("LCL",1)
table.addEntry("ARG",2)
table.addEntry("THIS",3)
table.addEntry("THAT",4)
table.addEntry("SCREEN",16384)
table.addEntry("KBD",24576)
while parse1.hasMoreLines():
 
    
    parse1.advance()
    print(parse1.instructionType())
    if parse1.instructionType()== "L_INSTRUCTION":
        print(parse1.symbol()+"OIHGUHUH")
        table.addEntry(parse1.symbol(),lineNumber)
        print(table.getAddress(parse1.symbol()))
    else:
        lineNumber+=1

parse=Rparse(f)
currentSpot=16
while parse.hasMoreLines():
    
    
    parse.advance()
    if parse.instructionType() == "A_INSTRUCTION":
        if table.contains(parse.symbol()):
            print(parse.symbol())
           
            x += ("0"+table.getAddress(parse.symbol())+"\n")
            
        else:
            if parse.symbol().isdigit():
                x+=("0"+parse.symbol()+"\n")
            else:
                table.addEntry(parse.symbol(),currentSpot)
                currentSpot+=1
                x += ("0"+table.getAddress(parse.symbol())+"\n")
            
    elif parse.instructionType()=="C_INSTRUCTION":
     
        x += "111" + str(CodeMod.Comp(parse.comp()))+str(CodeMod.Dest(parse.dest())) + str(CodeMod.Jump(parse.jump()))+"\n"
        
    else:
       print("")

y.write(x)

