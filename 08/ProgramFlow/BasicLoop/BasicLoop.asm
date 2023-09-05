@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 0
@SP
M=M-1
A=M
D=M
@R13
M=D
@LCL
D=M
@0         // initializes sum = 0
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP LCL 0         // initializes sum = 0
(LOOP_START) //LABEL
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
@0	        // sum = sum + counter
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP LCL 0	        // sum = sum + counter
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
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 1
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=M-D
@SP
M=M-1
@SP
M=M-1
A=M
D=M
@R13
M=D
@ARG
D=M
@0      // counter--
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP ARG 0      // counter--
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
@SP
A=M-1
D=M
@SP
M=M-1
@LOOP_START  // If counter != 0, goto LOOP_START
D;JNE
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
