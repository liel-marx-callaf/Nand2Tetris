// push constant 7
// loading constant 7 into D register
@7
D=A
//finished loading constant 7 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 8
// loading constant 8 into D register
@8
D=A
//finished loading constant 8 value into D register
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
