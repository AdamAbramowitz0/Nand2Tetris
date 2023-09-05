@261
D=A
@SP
M=D
@Sys.init
0;JMP
(UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsStaticsTestSys.Sys.init$ret0)


//instruction:function Sys.init 0

(Sys.init)


//instruction:push constant 6

@6
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 6


//instruction:push constant 8

@8
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 8


//instruction:call Class1.set 2

@UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsStaticsTestSys.Class1.set$ret1
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
@2
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.set
0;JMP
(UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsStaticsTestSys.Class1.set$ret1)


//instruction:pop temp 0 

@SP
M=M-1
A=M
D=M
@R13
M=D
@5
D=A
@0 
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP 5 0 


//instruction:push constant 23

@23
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 23


//instruction:push constant 15

@15
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 15


//instruction:call Class2.set 2

@UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsStaticsTestSys.Class2.set$ret3
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
@2
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.set
0;JMP
(UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsStaticsTestSys.Class2.set$ret3)


//instruction:pop temp 0 

@SP
M=M-1
A=M
D=M
@R13
M=D
@5
D=A
@0 
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP 5 0 


//instruction:call Class1.get 0

@UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsStaticsTestSys.Class1.get$ret5
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
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.get
0;JMP
(UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsStaticsTestSys.Class1.get$ret5)


//instruction:call Class2.get 0

@UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsStaticsTestSys.Class2.get$ret7
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
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.get
0;JMP
(UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsStaticsTestSys.Class2.get$ret7)


//instruction:label WHILE

(WHILE)//LABEL


//instruction:goto WHILE

@WHILE
0;JMP


//instruction:function Class1.set 0

(Class1.set)


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


//instruction:pop static 0

@SP
M=M-1
A=M
D=M
@UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsStaticsTestClass1.0
M=D


//instruction:push argument 1

@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH ARG 1


//instruction:pop static 1

@SP
M=M-1
A=M
D=M
@UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsStaticsTestClass1.1
M=D


//instruction:push constant 0

@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 0


//instruction:return

@LCL
D=M
@R13
M=D
@R14
M=D
@R13
D=M
A=D-1
A=A-1
A=A-1
A=A-1
A=A-1
D=M
@R15
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
@R15
A=M
0;JMP


//instruction:function Class1.get 0

(Class1.get)


//instruction:push static 0

@UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsStaticsTestClass1.0
D=M
@SP
A=M
M=D

@SP
M=M+1


//instruction:push static 1

@UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsStaticsTestClass1.1
D=M
@SP
A=M
M=D

@SP
M=M+1


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


//instruction:return

@LCL
D=M
@R13
M=D
@R14
M=D
@R13
D=M
A=D-1
A=A-1
A=A-1
A=A-1
A=A-1
D=M
@R15
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
@R15
A=M
0;JMP


//instruction:function Class2.set 0

(Class2.set)


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


//instruction:pop static 0

@SP
M=M-1
A=M
D=M
@UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsStaticsTestClass2.0
M=D


//instruction:push argument 1

@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH ARG 1


//instruction:pop static 1

@SP
M=M-1
A=M
D=M
@UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsStaticsTestClass2.1
M=D


//instruction:push constant 0

@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 0


//instruction:return

@LCL
D=M
@R13
M=D
@R14
M=D
@R13
D=M
A=D-1
A=A-1
A=A-1
A=A-1
A=A-1
D=M
@R15
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
@R15
A=M
0;JMP


//instruction:function Class2.get 0

(Class2.get)


//instruction:push static 0

@UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsStaticsTestClass2.0
D=M
@SP
A=M
M=D

@SP
M=M+1


//instruction:push static 1

@UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsStaticsTestClass2.1
D=M
@SP
A=M
M=D

@SP
M=M+1


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


//instruction:return

@LCL
D=M
@R13
M=D
@R14
M=D
@R13
D=M
A=D-1
A=A-1
A=A-1
A=A-1
A=A-1
D=M
@R15
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
@R15
A=M
0;JMP
