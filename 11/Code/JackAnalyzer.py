import sys,os
from JackTokenizer3 import *
from CompilationEngine import *
f=str(sys.argv[1])
if os.path.isdir(f) == False:

    y=open(f[:-5] + "Final1.txt","w")#for every xml file

    
    compiler = CompilationEngine(f)
    y.write(compiler.compileClass())


    


    #y.write("</tokens>")
else:
    list = os.listdir(f)
    print(list)
    finalList = []
    for i in range (0,len(list)):
        if list[i][-5:] == ".jack":
            finalList.append(f+"/"+list[i])
    print(finalList)
    for i in finalList:
        f=i
        y=open(f[:-5] + "end.txt","w")
        compiler = CompilationEngine(f)
        y.write(compiler.compileClass())
