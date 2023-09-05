import os
f= "/Users/adamabramowitz/Desktop/Everything_Coding/nand2tetris/projects/10/ExpressionLessSquare"
list = os.listdir(f)
print(list)
finalList = []
for i in range (0,len(list)-1):
    if list[i][(len(list[i]))-5:] == ".jack":
        finalList.append(f+"/"+list[i])
print(finalList)
for i in finalList:
    f=i
    y=open(f[:-5] + "final.xml","w")
    compiler = CompilationEngine(f)
    y.write(compiler.compileClass())


# python3 /Users/adamabramowitz/Desktop/Everything_Coding/nand2tetris/projects/10/Code/JackAnalyzer.py /Users/adamabramowitz/Desktop/Everything_Coding/nand2tetris/projects/10/Square
# sh /Users/adamabramowitz/Desktop/Everything_Coding/nand2tetris/tools/TextComparer.sh /Users/adamabramowitz/Desktop/Everything_Coding/nand2tetris/projects/10/ExpressionLessSquare/Main.xml /Users/adamabramowitz/Desktop/Everything_Coding/nand2tetris/projects/10/ExpressionLessSquare/Mainend.xml
# sh /Users/adamabramowitz/Desktop/Everything_Coding/nand2tetris/tools/TextComparer.sh /Users/adamabramowitz/Desktop/Everything_Coding/nand2tetris/projects/10/ExpressionLessSquare/Square.xml /Users/adamabramowitz/Desktop/Everything_Coding/nand2tetris/projects/10/ExpressionLessSquare/Squareend.xml
# sh /Users/adamabramowitz/Desktop/Everything_Coding/nand2tetris/tools/TextComparer.sh /Users/adamabramowitz/Desktop/Everything_Coding/nand2tetris/projects/10/ExpressionLessSquare/SquareGame.xml /Users/adamabramowitz/Desktop/Everything_Coding/nand2tetris/projects/10/ExpressionLessSquare/SquareGameend.xml






