@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
A=A-1
D=D-MD=-D
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
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
A=A-1
D=D-MD=-D
@NO2
D;JLT
@SP
A=M-1
A=A-1
M=0
@SP
M=M-1
@FIN2
0;JMP
(NO2)
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1
(FIN2)
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
A=A-1
D=D-MD=-D
@NO3
D;JGT
@SP
A=M-1
A=A-1
M=0
@SP
M=M-1
@FIN3
0;JMP
(NO3)
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1
(FIN3)
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
A=A-1
D=D-MD=-D
@NO4
D;JGT
@SP
A=M-1
A=A-1
M=0
@SP
M=M-1
@FIN4
0;JMP
(NO4)
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1
(FIN4)
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
A=A-1
D=D-MD=-D
@NO5
D;JEQ
@SP
A=M-1
A=A-1
M=0
@SP
M=M-1
@FIN5
0;JMP
(NO5)
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1
(FIN5)
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
A=A-1
D=D-MD=-D
@NO6
D;JEQ
@SP
A=M-1
A=A-1
M=0
@SP
M=M-1
@FIN6
0;JMP
(NO6)
@SP
A=M-1
A=A-1
M=-1
@SP
M=M-1
(FIN6)
