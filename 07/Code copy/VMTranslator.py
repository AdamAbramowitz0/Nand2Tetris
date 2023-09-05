import sys
from Parser import *
from CodeWriter import * 

f=str(sys.argv[1])
y=open(f[:-3] + ".asm","w")
parse = Parser(f)
coder=CodeWriter(y)


while(parse.hasMoreLines()):
    parse.advance()
    if parse.commandType() in {"C_PUSH","C_POP"}:
        coder.writePushPop(parse.commandType(),parse.arg1(),parse.arg2(),f[:-3].replace("/",""))
    elif parse.commandType() in {"C_ARITHMETIC"}:
        coder.writeArithmetic(parse.commandType,parse.arg1())
# infinite loop
