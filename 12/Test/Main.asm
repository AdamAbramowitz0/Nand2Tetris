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
(Main.main)
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
@10110
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 10110
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
@10010
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 10010
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
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 0
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
