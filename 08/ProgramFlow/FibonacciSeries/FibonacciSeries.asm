@256
D=A
@SP
M=D
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
@THAT
M=D
//comment
@SP
M=M-1
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
@THAT
D=M
@0              // first element in the series = 0
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP THAT 0              // first element in the series = 0
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 1
@SP
M=M-1
A=M
D=M
@R13
M=D
@THAT
D=M
@1              // second element in the series = 1
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP THAT 1              // second element in the series = 1
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
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH constant 2
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
@0          // num_of_elements -= 2 (first 2 elements are set)
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP ARG 0          // num_of_elements -= 2 (first 2 elements are set)
(MAIN_LOOP_START) //LABEL
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
@COMPUTE_ELEMENT // if num_of_elements > 0, goto COMPUTE_ELEMENT
D;JNE
@END_PROGRAM        // otherwise, goto END_PROGRAM
0;JMP
(COMPUTE_ELEMENT) //LABEL
@THAT
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH THAT 0
@THAT
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH THAT 1
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
@THAT
D=M
@2              // that[2] = that[0] + that[1]
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP THAT 2              // that[2] = that[0] + that[1]
@THAT
D=M
@SP
A=M
M=D

@SP
M=M+1
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
M=D+M
@SP
M=M-1
@SP
A=M-1
D=M
@THAT
M=D
//comment
@SP
M=M-1
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
@0          // num_of_elements--
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
//POP ARG 0          // num_of_elements--
@MAIN_LOOP_START
0;JMP
(END_PROGRAM) //LABEL
