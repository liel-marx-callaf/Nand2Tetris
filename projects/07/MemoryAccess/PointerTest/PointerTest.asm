// push constant 3030
// loading constant 3030 into D register
@3030
D=A
//finished loading constant 3030 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// pop pointer 0
// loading pointer 0 into D register
@THIS
D=A
//finished loading pointer 0 address into D register
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
// push constant 3040
// loading constant 3040 into D register
@3040
D=A
//finished loading constant 3040 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// pop pointer 1
// loading pointer 1 into D register
@THAT
D=A
//finished loading pointer 1 address into D register
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
// push constant 32
// loading constant 32 into D register
@32
D=A
//finished loading constant 32 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// pop this 2
// loading this 2 into D register
@2
D=A
@THIS
D=D+M
//finished loading this 2 address into D register
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
// push constant 46
// loading constant 46 into D register
@46
D=A
//finished loading constant 46 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// pop that 6
// loading that 6 into D register
@6
D=A
@THAT
D=D+M
//finished loading that 6 address into D register
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
// push pointer 0
// loading pointer 0 into D register
@THIS
D=M
//finished loading pointer 0 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push pointer 1
// loading pointer 1 into D register
@THAT
D=M
//finished loading pointer 1 value into D register
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
// push this 2
// loading this 2 into D register
@2
D=A
@THIS
D=D+M
A=D
D=M
//finished loading this 2 value into D register
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
// push that 6
// loading that 6 into D register
@6
D=A
@THAT
D=D+M
A=D
D=M
//finished loading that 6 value into D register
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
