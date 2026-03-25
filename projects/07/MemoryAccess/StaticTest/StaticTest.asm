// push constant 111
// loading constant 111 into D register
@111
D=A
//finished loading constant 111 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 333
// loading constant 333 into D register
@333
D=A
//finished loading constant 333 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 888
// loading constant 888 into D register
@888
D=A
//finished loading constant 888 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// pop static 8
// loading static 8 into D register
@StaticTest.8
D=A
//finished loading static 8 address into D register
@address
M=D
// move SP one back
@SP
M=M-1
// save RAM[SP]
A=M
D=M
// RAM[address] = RAM[SP]
@address
A=M
M=D
// pop static 3
// loading static 3 into D register
@StaticTest.3
D=A
//finished loading static 3 address into D register
@address
M=D
// move SP one back
@SP
M=M-1
// save RAM[SP]
A=M
D=M
// RAM[address] = RAM[SP]
@address
A=M
M=D
// pop static 1
// loading static 1 into D register
@StaticTest.1
D=A
//finished loading static 1 address into D register
@address
M=D
// move SP one back
@SP
M=M-1
// save RAM[SP]
A=M
D=M
// RAM[address] = RAM[SP]
@address
A=M
M=D
// push static 3
// loading static 3 into D register
@StaticTest.3
D=M
//finished loading static 3 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push static 1
// loading static 1 into D register
@StaticTest.1
D=M
//finished loading static 1 value into D register
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
// push static 8
// loading static 8 into D register
@StaticTest.8
D=M
//finished loading static 8 value into D register
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
