exp = ['(', '(', 'y', '+', 'size', ')', '&lt;', '254', ')', '&amp;', '(', '(', 'x', '+', 'size', ')', '&lt;', '510', ')']
exp1 = ['Screen', '.', 'drawRectangle', '(', 'x', ',', '(', 'y', '+', 'size', ')', '-', '1', ',', 'x', '+', 'size', ',', 'y', '+', 'size', ')']


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
self.alg(print(exp[1:counter-1]))
if(len(exp)>counter):
    self.alg(exp[counter:])



