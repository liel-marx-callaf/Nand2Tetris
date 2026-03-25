//Bootstrap code
@256
D=A
@SP
M=D
// Call Sys.init
@$ret.1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
($ret.1)
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
// pop that 0
// loading that 0 into D register
@0
D=A
@THAT
D=D+M
//finished loading that 0 address into D register
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
// pop that 1
// loading that 1 into D register
@1
D=A
@THAT
D=D+M
//finished loading that 1 address into D register
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
(FibonacciSeries$MAIN_LOOP_START)
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
@FibonacciSeries$COMPUTE_ELEMENT
D;JNE
@FibonacciSeries$END_PROGRAM
0;JMP
(FibonacciSeries$COMPUTE_ELEMENT)
// push that 0
// loading that 0 into D register
@0
D=A
@THAT
D=D+M
A=D
D=M
//finished loading that 0 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push that 1
// loading that 1 into D register
@1
D=A
@THAT
D=D+M
A=D
D=M
//finished loading that 1 value into D register
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
// Add: RAM[SP] = RAM[SP] + RAM[SP-1]
@SP
AM=M-1
D=M
A=A-1
M=D+M
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
@FibonacciSeries$MAIN_LOOP_START
0;JMP
(FibonacciSeries$END_PROGRAM)
