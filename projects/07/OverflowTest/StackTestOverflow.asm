// push constant 0
// loading constant 0 into D register
@0
D=A
//finished loading constant 0 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 32767
// loading constant 32767 into D register
@32767
D=A
//finished loading constant 32767 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// Sub: RAM[SP] = RAM[SP-1] - RAM[SP]
@SP
AM=M-1
D=M
A=A-1
M=M-D
// push constant 2
// loading constant 2 into D register
@2
D=A
//finished loading constant 2 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// Compare LT: RAM[SP] > RAM[SP-1]
@SP
AM=M-1
D=M
@R13
M=D
@SP
A=M-1
D=M
@R14
M=D
@NEG_X_1
D;JLT
@R13
D=M
@FALSE_LT_1
D;JLT
@R14
D=M
@R13
D=D-M
@TRUE_LT_1
D;JLT
@FALSE_LT_1
0;JMP
(NEG_X_1)
@R13
D=M
@TRUE_LT_1
D;JGE
@R14
D=M
@R13
D=D-M
@TRUE_LT_1
D;JLT
@FALSE_LT_1
0;JMP
(TRUE_LT_1)
@SP
A=M-1
M=-1
@END_LT_1
0;JMP
(FALSE_LT_1)
@SP
A=M-1
M=0
@END_LT_1
0;JMP
(END_LT_1)
// push constant 2
// loading constant 2 into D register
@2
D=A
//finished loading constant 2 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 0
// loading constant 0 into D register
@0
D=A
//finished loading constant 0 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 32767
// loading constant 32767 into D register
@32767
D=A
//finished loading constant 32767 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// Sub: RAM[SP] = RAM[SP-1] - RAM[SP]
@SP
AM=M-1
D=M
A=A-1
M=M-D
// Compare LT: RAM[SP] > RAM[SP-1]
@SP
AM=M-1
D=M
@R13
M=D
@SP
A=M-1
D=M
@R14
M=D
@NEG_X_2
D;JLT
@R13
D=M
@FALSE_LT_2
D;JLT
@R14
D=M
@R13
D=D-M
@TRUE_LT_2
D;JLT
@FALSE_LT_2
0;JMP
(NEG_X_2)
@R13
D=M
@TRUE_LT_2
D;JGE
@R14
D=M
@R13
D=D-M
@TRUE_LT_2
D;JLT
@FALSE_LT_2
0;JMP
(TRUE_LT_2)
@SP
A=M-1
M=-1
@END_LT_2
0;JMP
(FALSE_LT_2)
@SP
A=M-1
M=0
@END_LT_2
0;JMP
(END_LT_2)
// push constant 0
// loading constant 0 into D register
@0
D=A
//finished loading constant 0 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 32767
// loading constant 32767 into D register
@32767
D=A
//finished loading constant 32767 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// Sub: RAM[SP] = RAM[SP-1] - RAM[SP]
@SP
AM=M-1
D=M
A=A-1
M=M-D
// push constant 2
// loading constant 2 into D register
@2
D=A
//finished loading constant 2 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// Compare GT: RAM[SP] < RAM[SP-1]
@SP
AM=M-1
D=M
@R13
M=D
@SP
A=M-1
D=M
@R14
M=D
@NEG_X_3
D;JLT
@R13
D=M
@TRUE_GT_3
D;JLT
@R14
D=M
@R13
D=D-M
@TRUE_GT_3
D;JGT
@FALSE_GT_3
0;JMP
(NEG_X_3)
@R13
D=M
@FALSE_GT_3
D;JGE
@R14
D=M
@R13
D=D-M
@TRUE_GT_3
D;JGT
@FALSE_GT_3
0;JMP
(TRUE_GT_3)
@SP
A=M-1
M=-1
@END_GT_3
0;JMP
(FALSE_GT_3)
@SP
A=M-1
M=0
@END_GT_3
0;JMP
(END_GT_3)
// push constant 2
// loading constant 2 into D register
@2
D=A
//finished loading constant 2 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 0
// loading constant 0 into D register
@0
D=A
//finished loading constant 0 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 32767
// loading constant 32767 into D register
@32767
D=A
//finished loading constant 32767 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// Sub: RAM[SP] = RAM[SP-1] - RAM[SP]
@SP
AM=M-1
D=M
A=A-1
M=M-D
// Compare GT: RAM[SP] < RAM[SP-1]
@SP
AM=M-1
D=M
@R13
M=D
@SP
A=M-1
D=M
@R14
M=D
@NEG_X_4
D;JLT
@R13
D=M
@TRUE_GT_4
D;JLT
@R14
D=M
@R13
D=D-M
@TRUE_GT_4
D;JGT
@FALSE_GT_4
0;JMP
(NEG_X_4)
@R13
D=M
@FALSE_GT_4
D;JGE
@R14
D=M
@R13
D=D-M
@TRUE_GT_4
D;JGT
@FALSE_GT_4
0;JMP
(TRUE_GT_4)
@SP
A=M-1
M=-1
@END_GT_4
0;JMP
(FALSE_GT_4)
@SP
A=M-1
M=0
@END_GT_4
0;JMP
(END_GT_4)
