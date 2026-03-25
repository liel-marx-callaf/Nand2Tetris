// push constant 10
// loading constant 10 into D register
@10
D=A
//finished loading constant 10 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// pop local 0
// loading local 0 into D register
@0
D=A
@LCL
D=D+M
//finished loading local 0 address into D register
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
// push constant 21
// loading constant 21 into D register
@21
D=A
//finished loading constant 21 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 22
// loading constant 22 into D register
@22
D=A
//finished loading constant 22 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// pop argument 2
// loading argument 2 into D register
@2
D=A
@ARG
D=D+M
//finished loading argument 2 address into D register
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
// pop argument 1
// loading argument 1 into D register
@1
D=A
@ARG
D=D+M
//finished loading argument 1 address into D register
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
// push constant 36
// loading constant 36 into D register
@36
D=A
//finished loading constant 36 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// pop this 6
// loading this 6 into D register
@6
D=A
@THIS
D=D+M
//finished loading this 6 address into D register
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
// push constant 42
// loading constant 42 into D register
@42
D=A
//finished loading constant 42 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 45
// loading constant 45 into D register
@45
D=A
//finished loading constant 45 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// pop that 5
// loading that 5 into D register
@5
D=A
@THAT
D=D+M
//finished loading that 5 address into D register
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
// pop that 2
// loading that 2 into D register
@2
D=A
@THAT
D=D+M
//finished loading that 2 address into D register
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
// push constant 510
// loading constant 510 into D register
@510
D=A
//finished loading constant 510 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// pop temp 6
// loading temp 6 into D register
@R11
D=A
//finished loading temp 6 address into D register
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
// push local 0
// loading local 0 into D register
@0
D=A
@LCL
D=D+M
A=D
D=M
//finished loading local 0 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push that 5
// loading that 5 into D register
@5
D=A
@THAT
D=D+M
A=D
D=M
//finished loading that 5 value into D register
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
// push argument 1
// loading argument 1 into D register
@1
D=A
@ARG
D=D+M
A=D
D=M
//finished loading argument 1 value into D register
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
// push this 6
// loading this 6 into D register
@6
D=A
@THIS
D=D+M
A=D
D=M
//finished loading this 6 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push this 6
// loading this 6 into D register
@6
D=A
@THIS
D=D+M
A=D
D=M
//finished loading this 6 value into D register
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
// Sub: RAM[SP] = RAM[SP-1] - RAM[SP]
@SP
AM=M-1
D=M
A=A-1
M=M-D
// push temp 6
// loading temp 6 into D register
@R11
D=M
//finished loading temp 6 value into D register
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
