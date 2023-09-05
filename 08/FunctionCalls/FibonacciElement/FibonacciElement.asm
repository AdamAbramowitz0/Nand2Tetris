@261
D=A
@SP
M=D
@Sys.init
0;JMP
(UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsFibonacciElementSys.Sys.init$ret0)


//instruction:function Sys.init 0

(Sys.init)


//instruction:push constant 4

@4
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 4


//instruction:call Main.fibonacci 1   

@UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsFibonacciElementSys.Main.fibonacci$ret1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M-1
D=D-1
D=D-1
D=D-1
D=D-1
@1   
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsFibonacciElementSys.Main.fibonacci$ret1)


//instruction:label WHILE

(WHILE)//LABEL


//instruction:goto WHILE              

@WHILE
0;JMP


//instruction:function Main.fibonacci 0

(Main.fibonacci)


//instruction:push argument 0

@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH ARG 0


//instruction:push constant 2

@2
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 2


//instruction:lt                     

@SP
A=M-1
D=M
A=A-1
D=M-D
@NO1
D;JLT
@SP
A=M-1
A=A-1
M=0
@SP
M=M-1
@FIN1
0;JMP
(NO1)
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1
(FIN1)


//instruction:if-goto IF_TRUE

@SP
A=M-1
D=M
@SP
M=M-1
@IF_TRUE
D;JNE


//instruction:goto IF_FALSE

@IF_FALSE
0;JMP


//instruction:label IF_TRUE          

(IF_TRUE)//LABEL


//instruction:push argument 0

@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH ARG 0


//instruction:return

@LCL
D=M
@R13
M=D
@R14
M=D
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
D=M
A=D-1
D=M
@THAT
M=D
@R13
D=M
A=D-1
A=A-1
D=M
@THIS
M=D
@R13
D=M
A=D-1
A=A-1
A=A-1
D=M
@ARG
M=D
@R13
D=M
A=D-1
A=A-1
A=A-1
A=A-1
D=M
@LCL
M=D
@R13
D=M
A=D-1
A=A-1
A=A-1
A=A-1
A=A-1
A=M
0;JMP


//instruction:label IF_FALSE         

(IF_FALSE)//LABEL


//instruction:push argument 0

@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH ARG 0


//instruction:push constant 2

@2
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 2


//instruction:sub

@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=M-D
@SP
M=M-1


//instruction:call Main.fibonacci 1  

@UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsFibonacciElementMain.Main.fibonacci$ret2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M-1
D=D-1
D=D-1
D=D-1
D=D-1
@1  
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsFibonacciElementMain.Main.fibonacci$ret2)


//instruction:push argument 0

@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH ARG 0


//instruction:push constant 1

@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 1


//instruction:sub

@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=M-D
@SP
M=M-1


//instruction:call Main.fibonacci 1  

@UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsFibonacciElementMain.Main.fibonacci$ret4
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M-1
D=D-1
D=D-1
D=D-1
D=D-1
@1  
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsFibonacciElementMain.Main.fibonacci$ret4)


//instruction:add                    

@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=D+M
@SP
M=M-1


//instruction:return

@LCL
D=M
@R13
M=D
@R14
M=D
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
D=M
A=D-1
D=M
@THAT
M=D
@R13
D=M
A=D-1
A=A-1
D=M
@THIS
M=D
@R13
D=M
A=D-1
A=A-1
A=A-1
D=M
@ARG
M=D
@R13
D=M
A=D-1
A=A-1
A=A-1
A=A-1
D=M
@LCL
M=D
@R13
D=M
A=D-1
A=A-1
A=A-1
A=A-1
A=A-1
A=M
0;JMP
