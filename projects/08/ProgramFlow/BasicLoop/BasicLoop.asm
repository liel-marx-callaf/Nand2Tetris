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
(BasicLoop$LOOP_START)
// push argument 0
// loading argument 0 into D register
@0
D=A
@ARG
D=D+M
A=D
D=M
//finished loading argument 0 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
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
// Add: RAM[SP] = RAM[SP] + RAM[SP-1]
@SP
AM=M-1
D=M
A=A-1
M=D+M
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
// push argument 0
// loading argument 0 into D register
@0
D=A
@ARG
D=D+M
A=D
D=M
//finished loading argument 0 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push constant 1
// loading constant 1 into D register
@1
D=A
//finished loading constant 1 value into D register
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
// pop argument 0
// loading argument 0 into D register
@0
D=A
@ARG
D=D+M
//finished loading argument 0 address into D register
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
// push argument 0
// loading argument 0 into D register
@0
D=A
@ARG
D=D+M
A=D
D=M
//finished loading argument 0 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
@SP
AM=M-1
D=M
@BasicLoop$LOOP_START
D;JNE
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
