class CodeMod:
    @staticmethod
    def Dest(input):
        if input == "null":
            return   ("000")
        elif input == "M":
            return   ("001")
        elif input == "D":
            return   ("010")
        elif input == "MD":
            return   ("011")
        elif input == "A":
            return   ("100")
        elif input == "AM":
            return   ("101")
        elif input == "AD":
            return   ("110")
        elif input == "ADM":
            return   ("111")
        else:
            print("INPUT")
            print(input)
            return "ERROR!!!" + input
            
    @staticmethod
    def Comp(input):
        
        if input == "0":
            return   ("0101010")
        elif input == "1":
            return   ("0111111") 
        elif input == "-1":
            return   ("0111010")
        elif input == "D":
            return   ("0001100")
        elif input == "A":
            return   ("0110000")
        elif input == "M":
            return   ("1110000")
        elif input == "!D":
            return   ("0001101")
        elif input == "!A":
            return   ("0110001")
        elif input == "!M":
            return   ("1110001")
        elif input == "-D":
            return   ("0001111")
        elif input == "-A":
            return   ("0110011")
        elif input == "-M":
            return   ("1110011")
        elif input == "D+1":
            return   ("0011111")
        elif input == "A+1":
            return   ("0110111")
        elif input == "M+1":
            return   ("1110111")
        elif input == "D-1":
            return   ("0001110")
        elif input == "A-1":
            return   ("0110010")
        elif input == "M-1":
            return   ("1110010")
        elif input == "D+A":
            return   ("0000010")
        elif input == "D+M":
            return   ("1000010")
        elif input == "D-A":
            return   ("0010011")
        elif input == "D-M":
            return   ("1010011")
        elif input == "A-D":
            return   ("0000111")
        elif input == "M-D":
            return   ("1000111")
        elif input == "D&A":
            return   ("0000000")
        elif input == "D|A":
            return   ("0010101")
        elif input == "D&M":
            return   ("1000000")
        elif input == "D|M":
            return   ("1010101")
        else:
            print("INPUT")
            print(input)
            return "ERROR!!" + input
    @staticmethod    
    def Jump(input):
        if input == "null":
            return  ("000")
        elif input == "JGT":
            return   ("001")
        elif input == "JEQ":
            return   ("010")
        elif input == "JGE":
            return   ("011")
        elif input == "JLT":
            return   ("100")
        elif input == "JNE":
            return   ("101")
        elif input == "JLE":
            return   ("110")
        elif input == "JMP":
            return   ("111")
        else:
            return "ERROR!" + input