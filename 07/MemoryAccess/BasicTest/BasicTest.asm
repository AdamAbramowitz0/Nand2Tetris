@10
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 10
@SP
M=M-1
A=M
D=M
@R13
M=D
@LCL
D=M
@0
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP LCL 0
@21
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 21
@22
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 22
@SP
M=M-1
A=M
D=M
@R13
M=D
@ARG
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
//POP ARG 2
@SP
M=M-1
A=M
D=M
@R13
M=D
@ARG
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
//POP ARG 1
@36
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 36
@SP
M=M-1
A=M
D=M
@R13
M=D
@THIS
D=M
@6
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP THIS 6
@42
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 42
@45
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 45
@SP
M=M-1
A=M
D=M
@R13
M=D
@THAT
D=M
@5
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP THAT 5
@SP
M=M-1
A=M
D=M
@R13
M=D
@THAT
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
//POP THAT 2
@510
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 510
@SP
M=M-1
A=M
D=M
@R13
M=D
@5
D=A
@6
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP 5 6
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
@THAT
D=M
@5
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH THAT 5
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=D+M
@SP
M=M-1
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
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=M-D
@SP
M=M-1
@THIS
D=M
@6
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH THIS 6
@THIS
D=M
@6
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH THIS 6
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=D+M
@SP
M=M-1
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=M-D
@SP
M=M-1
@5
D=A
@6
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH 5 6
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=D+M
@SP
M=M-1
