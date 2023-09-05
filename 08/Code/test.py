import os
list = os.listdir("/Users/adamabramowitz/Desktop/Everything_Coding/nand2tetris/projects/08/FunctionCalls/FibonacciElement")
finalList = []
for i in range (0,len(list)):
    if list[i][(len(list[i]))-3:] == ".vm":
        finalList.append(list[i])

print(finalList)

x="/Users/adamabramowitz/Desktop/Everything_Coding/nand2tetris/projects/08/FunctionCalls/FibonacciElement"
y =[]
b=0
for i in range(0,len(x)-1):
    z=len(x)-i-1
    if x[z]=="/":
        print("hit")
    
        b=i
        break;
p=x[-b:]
print(p)

s="hello"
s=s[:1]+" "+s[2:]
print(s)

hi = "hello"
z=list(hi)
z[3]="p"
hi=''.join(z)
print(hi)
