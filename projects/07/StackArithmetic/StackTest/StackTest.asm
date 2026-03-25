// push constant 17
// loading constant 17 into D register
@17
D=A
//finished loading constant 17 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 17
// loading constant 17 into D register
@17
D=A
//finished loading constant 17 value into D register
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
@NEG_X_1
D;JLT
@R13
D=M
@FALSE_EQ_1
D;JLT
@R14
D=M
@R13
D=D-M
@TRUE_EQ_1
D;JEQ
@FALSE_EQ_1
0;JMP
(NEG_X_1)
@R13
D=M
@FALSE_EQ_1
D;JGE
@R14
D=M
@R13
D=D-M
@TRUE_EQ_1
D;JEQ
@FALSE_EQ_1
0;JMP
(TRUE_EQ_1)
@SP
A=M-1
M=-1
@END_EQ_1
0;JMP
(FALSE_EQ_1)
@SP
A=M-1
M=0
@END_EQ_1
0;JMP
(END_EQ_1)
// push constant 17
// loading constant 17 into D register
@17
D=A
//finished loading constant 17 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 16
// loading constant 16 into D register
@16
D=A
//finished loading constant 16 value into D register
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
@NEG_X_2
D;JLT
@R13
D=M
@FALSE_EQ_2
D;JLT
@R14
D=M
@R13
D=D-M
@TRUE_EQ_2
D;JEQ
@FALSE_EQ_2
0;JMP
(NEG_X_2)
@R13
D=M
@FALSE_EQ_2
D;JGE
@R14
D=M
@R13
D=D-M
@TRUE_EQ_2
D;JEQ
@FALSE_EQ_2
0;JMP
(TRUE_EQ_2)
@SP
A=M-1
M=-1
@END_EQ_2
0;JMP
(FALSE_EQ_2)
@SP
A=M-1
M=0
@END_EQ_2
0;JMP
(END_EQ_2)
// push constant 16
// loading constant 16 into D register
@16
D=A
//finished loading constant 16 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 17
// loading constant 17 into D register
@17
D=A
//finished loading constant 17 value into D register
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
@FALSE_EQ_3
D;JLT
@R14
D=M
@R13
D=D-M
@TRUE_EQ_3
D;JEQ
@FALSE_EQ_3
0;JMP
(NEG_X_3)
@R13
D=M
@FALSE_EQ_3
D;JGE
@R14
D=M
@R13
D=D-M
@TRUE_EQ_3
D;JEQ
@FALSE_EQ_3
0;JMP
(TRUE_EQ_3)
@SP
A=M-1
M=-1
@END_EQ_3
0;JMP
(FALSE_EQ_3)
@SP
A=M-1
M=0
@END_EQ_3
0;JMP
(END_EQ_3)
// push constant 892
// loading constant 892 into D register
@892
D=A
//finished loading constant 892 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 891
// loading constant 891 into D register
@891
D=A
//finished loading constant 891 value into D register
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
@NEG_X_4
D;JLT
@R13
D=M
@FALSE_LT_4
D;JLT
@R14
D=M
@R13
D=D-M
@TRUE_LT_4
D;JLT
@FALSE_LT_4
0;JMP
(NEG_X_4)
@R13
D=M
@TRUE_LT_4
D;JGE
@R14
D=M
@R13
D=D-M
@TRUE_LT_4
D;JLT
@FALSE_LT_4
0;JMP
(TRUE_LT_4)
@SP
A=M-1
M=-1
@END_LT_4
0;JMP
(FALSE_LT_4)
@SP
A=M-1
M=0
@END_LT_4
0;JMP
(END_LT_4)
// push constant 891
// loading constant 891 into D register
@891
D=A
//finished loading constant 891 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 892
// loading constant 892 into D register
@892
D=A
//finished loading constant 892 value into D register
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
@NEG_X_5
D;JLT
@R13
D=M
@FALSE_LT_5
D;JLT
@R14
D=M
@R13
D=D-M
@TRUE_LT_5
D;JLT
@FALSE_LT_5
0;JMP
(NEG_X_5)
@R13
D=M
@TRUE_LT_5
D;JGE
@R14
D=M
@R13
D=D-M
@TRUE_LT_5
D;JLT
@FALSE_LT_5
0;JMP
(TRUE_LT_5)
@SP
A=M-1
M=-1
@END_LT_5
0;JMP
(FALSE_LT_5)
@SP
A=M-1
M=0
@END_LT_5
0;JMP
(END_LT_5)
// push constant 891
// loading constant 891 into D register
@891
D=A
//finished loading constant 891 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 891
// loading constant 891 into D register
@891
D=A
//finished loading constant 891 value into D register
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
@NEG_X_6
D;JLT
@R13
D=M
@FALSE_LT_6
D;JLT
@R14
D=M
@R13
D=D-M
@TRUE_LT_6
D;JLT
@FALSE_LT_6
0;JMP
(NEG_X_6)
@R13
D=M
@TRUE_LT_6
D;JGE
@R14
D=M
@R13
D=D-M
@TRUE_LT_6
D;JLT
@FALSE_LT_6
0;JMP
(TRUE_LT_6)
@SP
A=M-1
M=-1
@END_LT_6
0;JMP
(FALSE_LT_6)
@SP
A=M-1
M=0
@END_LT_6
0;JMP
(END_LT_6)
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
// push constant 32766
// loading constant 32766 into D register
@32766
D=A
//finished loading constant 32766 value into D register
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
@NEG_X_7
D;JLT
@R13
D=M
@TRUE_GT_7
D;JLT
@R14
D=M
@R13
D=D-M
@TRUE_GT_7
D;JGT
@FALSE_GT_7
0;JMP
(NEG_X_7)
@R13
D=M
@FALSE_GT_7
D;JGE
@R14
D=M
@R13
D=D-M
@TRUE_GT_7
D;JGT
@FALSE_GT_7
0;JMP
(TRUE_GT_7)
@SP
A=M-1
M=-1
@END_GT_7
0;JMP
(FALSE_GT_7)
@SP
A=M-1
M=0
@END_GT_7
0;JMP
(END_GT_7)
// push constant 32766
// loading constant 32766 into D register
@32766
D=A
//finished loading constant 32766 value into D register
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
@NEG_X_8
D;JLT
@R13
D=M
@TRUE_GT_8
D;JLT
@R14
D=M
@R13
D=D-M
@TRUE_GT_8
D;JGT
@FALSE_GT_8
0;JMP
(NEG_X_8)
@R13
D=M
@FALSE_GT_8
D;JGE
@R14
D=M
@R13
D=D-M
@TRUE_GT_8
D;JGT
@FALSE_GT_8
0;JMP
(TRUE_GT_8)
@SP
A=M-1
M=-1
@END_GT_8
0;JMP
(FALSE_GT_8)
@SP
A=M-1
M=0
@END_GT_8
0;JMP
(END_GT_8)
// push constant 32766
// loading constant 32766 into D register
@32766
D=A
//finished loading constant 32766 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 32766
// loading constant 32766 into D register
@32766
D=A
//finished loading constant 32766 value into D register
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
@NEG_X_9
D;JLT
@R13
D=M
@TRUE_GT_9
D;JLT
@R14
D=M
@R13
D=D-M
@TRUE_GT_9
D;JGT
@FALSE_GT_9
0;JMP
(NEG_X_9)
@R13
D=M
@FALSE_GT_9
D;JGE
@R14
D=M
@R13
D=D-M
@TRUE_GT_9
D;JGT
@FALSE_GT_9
0;JMP
(TRUE_GT_9)
@SP
A=M-1
M=-1
@END_GT_9
0;JMP
(FALSE_GT_9)
@SP
A=M-1
M=0
@END_GT_9
0;JMP
(END_GT_9)
// push constant 57
// loading constant 57 into D register
@57
D=A
//finished loading constant 57 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 31
// loading constant 31 into D register
@31
D=A
//finished loading constant 31 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 53
// loading constant 53 into D register
@53
D=A
//finished loading constant 53 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// Add: RAM[SP] = RAM[SP] + RAM[SP-1]
@SP
AM=M-1
D=M
A=A-1
M=D+M
// push constant 112
// loading constant 112 into D register
@112
D=A
//finished loading constant 112 value into D register
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
// Neg: RAM[SP] = -RAM[SP]
@SP
A=M-1
M=-M
// And: RAM[SP] = RAM[SP] & RAM[SP-1]
@SP
AM=M-1
D=M
A=A-1
M=M&D
// push constant 82
// loading constant 82 into D register
@82
D=A
//finished loading constant 82 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// Or: RAM[SP] = RAM[SP] | RAM[SP-1]
@SP
AM=M-1
D=M
A=A-1
M=M|D
// Not: RAM[SP] = ! RAM[SP]
@SP
A=M-1
M=!M
