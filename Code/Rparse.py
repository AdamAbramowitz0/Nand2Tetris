class Rparse:
	lineNumber=-1
	x=[]
	def __init__(self,s):
		self.lineNumber=-1
		self.x=open(s).readlines()
		z=0
		for q in self.x:
			
			self.x[z] = self.x[z][0:(len(self.x[z])-1)]
			z+=1
			
	def printer(self):
		print(self.x)

	def hasMoreLines(self):
		if self.lineNumber+1 < len(self.x):
			return True
		else:
			return False
	
	def advance(self):
		while self.hasMoreLines():
			self.lineNumber+=1
			self.x[self.lineNumber]=self.x[self.lineNumber].strip()
			if len(self.x[self.lineNumber])>1:
				if (self.x[self.lineNumber][0] != "/" and self.x[self.lineNumber][1] != "/"):
					

					
					return
			
				

			

	def instructionType(self):
		if len(self.x[self.lineNumber])>1:
			print(self.x[self.lineNumber])
			print(self.x[self.lineNumber][0])
			if self.x[self.lineNumber][0]=="@":
				print("AAAAAAAAAAAA")
				return "A_INSTRUCTION"
			elif self.x[self.lineNumber][0]=="(":
				print("LLLLLLLLLLLLL")
				return "L_INSTRUCTION"
			else:
				print("CCCCCCCCCCCCC")
				return "C_INSTRUCTION"
		else:
			
			return
	
	def symbol(self):
		if (not self.x[self.lineNumber][1:].isdigit()) and self.instructionType()=="L_INSTRUCTION":
			return self.x[self.lineNumber][1:len(self.x[self.lineNumber][1:])]
		elif(not self.x[self.lineNumber][1:].isdigit()):
			return self.x[self.lineNumber][1:]
		q=""
		y = str(bin(int(self.x[self.lineNumber][1:])))[2:]
		z= 15-len(y)
		for z in range(z):
			q+="0"
		q+=y
		return q
	
	def dest(self):
	

		if "=" not in self.x[self.lineNumber]:
			return "null"
		else:
			return self.x[self.lineNumber][0:(self.x[self.lineNumber].index("="))]
	def jump(self):
		
		if ";" not in self.x[self.lineNumber]:
			return "null"
		else:
			if (" ") in self.x[self.lineNumber]:
				z=self.x[self.lineNumber].index(" ")
				return self.x[self.lineNumber][(self.x[self.lineNumber].index(";"))+1:z]
			else:
				return self.x[self.lineNumber][(self.x[self.lineNumber].index(";"))+1:]
	def comp(self):
		
		d="=" in self.x[self.lineNumber]
		j=";" in self.x[self.lineNumber]
		if d and j:
			return self.x[self.lineNumber][(self.x[self.lineNumber].index("="))+1:(self.x[self.lineNumber].index(";"))]
		elif d and not j:
			if (" ") in self.x[self.lineNumber]:
				z=self.x[self.lineNumber].index(" ")
				return self.x[self.lineNumber][(self.x[self.lineNumber].index("="))+1:z]
			else:
				return self.x[self.lineNumber][(self.x[self.lineNumber].index("="))+1:]
		elif j and not d:
			return self.x[self.lineNumber][:(self.x[self.lineNumber].index(";"))]
		else:
			return self.x[self.lineNumber]