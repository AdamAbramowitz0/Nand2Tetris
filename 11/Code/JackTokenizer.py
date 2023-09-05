class JackTokenizer:
    def __init__(self, f):
        self.spotLine = 0
        self.currentLine  = 0
        self.input = open(f).readlines()
        self.inFunction = False
        self.keywords = ['class','constructor','function','method','field','static'
    ,'var','int','char','boolean','void','true','false','null','this'
    ,'let','do','if','else','while','return']
        self.symbols=['{','}','(',')','[',']','.',',',';','+','-','*','/','&','|','<','>','=',"~"]
        self.final=[]
        self.commentLocation = {}
        self.currentID = ''
        
        self.getRidOfComments()
        print(self.comentLocation)

   


    def MoveChar(self, numberOfSpaces):
        for i in range(0,numberOfSpaces-1):   
            if (self.MoreTokens()==False):
                #Do Nothing
                break
            elif len(self.input[self.currentLine])-1==(self.spotLine):
                self.currentLine+=1
                self.spotLine=0
            else:
                self.spotLine+=1

    def MoreTokens(self):
        if (len(self.input)-1 == self.currentLine) and (len(self.input[self.currentLine])-1 == self.spotLine):
            return False
        else:
            return True

    def getRidOfComments(self):
        inComment = False
        while(self.MoreTokens()):
            if (inComment==False):
                if (self.input[self.currentLine][self.spotLine] == "/") and ((self.input[self.currentLine][self.spotLine]=="/")or (self.input[self.currentLine][self.spotLine]=="*")):
                  inComment==True
                  
                  self.commentLocation[self.currentLine] = [self.spotLine]
                  self.MoveChar(1)
                else:
                    self.MoveChar(1)
            else:
                if (self.input[self.currentLine][self.spotLine]) == "*" and (self.input[self.currentLine][self.spotLine]=="/"):
                    self.commentLocation[self.currentLine] = [self.spotLine]
                    self.MoveChar(1)
                    self.commentLocation[self.currentLine] = [self.spotLine]
                    inComment==False
                
                self.MoveChar(1)