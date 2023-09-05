@261
D=A
@SP
M=D
@LCL
M=D
@256
D=A
@ARG
M=D
@Sys.init
0;JMP
(UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsNestedCallSys.Sys.init$ret0)


//instruction:function Sys.init 0

(Sys.init)


//instruction:push constant 4000	

@4000	
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 4000	


//instruction:pop pointer 0

@SP
A=M-1
D=M
@THIS
M=D
//comment
@SP
M=M-1


//instruction:push constant 5000

@5000
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 5000


//instruction:pop pointer 1

@SP
A=M-1
D=M
@THAT
M=D
//comment
@SP
M=M-1


//instruction:call Sys.main 0

@UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsNestedCallSys.Sys.main$ret1
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
@Sys.main
0;JMP
(UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsNestedCallSys.Sys.main$ret1)


//instruction:pop temp 1

@SP
M=M-1
A=M
D=M
@R13
M=D
@5
D=A
@1
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP 5 1


//instruction:label LOOP

(LOOP)//LABEL


//instruction:goto LOOP

@LOOP
0;JMP


//instruction:function Sys.main 5

(Sys.main)
@SP

A=M
M=0
@SP
M=M+1
@SP

A=M
M=0
@SP
M=M+1
@SP

A=M
M=0
@SP
M=M+1
@SP

A=M
M=0
@SP
M=M+1
@SP

A=M
M=0
@SP
M=M+1


//instruction:push constant 4001

@4001
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 4001


//instruction:pop pointer 0

@SP
A=M-1
D=M
@THIS
M=D
//comment
@SP
M=M-1


//instruction:push constant 5001

@5001
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 5001


//instruction:pop pointer 1

@SP
A=M-1
D=M
@THAT
M=D
//comment
@SP
M=M-1


//instruction:push constant 200

@200
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 200


//instruction:pop local 1

@SP
M=M-1
A=M
D=M
@R13
M=D
@LCL
D=M
@1
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP LCL 1


//instruction:push constant 40

@40
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 40


//instruction:pop local 2

@SP
M=M-1
A=M
D=M
@R13
M=D
@LCL
D=M
@2
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP LCL 2


//instruction:push constant 6

@6
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 6


//instruction:pop local 3

@SP
M=M-1
A=M
D=M
@R13
M=D
@LCL
D=M
@3
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP LCL 3


//instruction:push constant 123

@123
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 123


//instruction:call Sys.add12 1

@UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsNestedCallSys.Sys.add12$ret3
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
@Sys.add12
0;JMP
(UsersadamabramowitzDesktopEverything_Codingnand2tetrisprojects08FunctionCallsNestedCallSys.Sys.add12$ret3)


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


//instruction:push local 0

@LCL
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH LCL 0


//instruction:push local 1

@LCL
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH LCL 1


//instruction:push local 2

@LCL
D=M
@2
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH LCL 2


//instruction:push local 3

@LCL
D=M
@3
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH LCL 3


//instruction:push local 4

@LCL
D=M
@4
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH LCL 4


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


//instruction:function Sys.add12 0

(Sys.add12)


//instruction:push constant 4002

@4002
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 4002


//instruction:pop pointer 0

@SP
A=M-1
D=M
@THIS
M=D
//comment
@SP
M=M-1


//instruction:push constant 5002

@5002
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 5002


//instruction:pop pointer 1

@SP
A=M-1
D=M
@THAT
M=D
//comment
@SP
M=M-1


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


//instruction:push constant 12

@12
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 12


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
