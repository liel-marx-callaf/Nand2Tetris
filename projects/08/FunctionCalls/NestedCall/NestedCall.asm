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
(Sys.init)
// push constant 4000
// loading constant 4000 into D register
@4000
D=A
//finished loading constant 4000 value into D register
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
// push constant 5000
// loading constant 5000 into D register
@5000
D=A
//finished loading constant 5000 value into D register
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
@Sys.init$ret.2
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
@Sys.main
0;JMP
(Sys.init$ret.2)
// pop temp 1
// loading temp 1 into D register
@R6
D=A
//finished loading temp 1 address into D register
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
(Sys.init$LOOP)
@Sys.init$LOOP
0;JMP
(Sys.main)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 4001
// loading constant 4001 into D register
@4001
D=A
//finished loading constant 4001 value into D register
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
// push constant 5001
// loading constant 5001 into D register
@5001
D=A
//finished loading constant 5001 value into D register
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
// push constant 200
// loading constant 200 into D register
@200
D=A
//finished loading constant 200 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// pop local 1
// loading local 1 into D register
@1
D=A
@LCL
D=D+M
//finished loading local 1 address into D register
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
// push constant 40
// loading constant 40 into D register
@40
D=A
//finished loading constant 40 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// pop local 2
// loading local 2 into D register
@2
D=A
@LCL
D=D+M
//finished loading local 2 address into D register
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
// push constant 6
// loading constant 6 into D register
@6
D=A
//finished loading constant 6 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// pop local 3
// loading local 3 into D register
@3
D=A
@LCL
D=D+M
//finished loading local 3 address into D register
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
// push constant 123
// loading constant 123 into D register
@123
D=A
//finished loading constant 123 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
@Sys.main$ret.3
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
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.add12
0;JMP
(Sys.main$ret.3)
// pop temp 0
// loading temp 0 into D register
@R5
D=A
//finished loading temp 0 address into D register
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
// push local 1
// loading local 1 into D register
@1
D=A
@LCL
D=D+M
A=D
D=M
//finished loading local 1 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push local 2
// loading local 2 into D register
@2
D=A
@LCL
D=D+M
A=D
D=M
//finished loading local 2 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push local 3
// loading local 3 into D register
@3
D=A
@LCL
D=D+M
A=D
D=M
//finished loading local 3 value into D register
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push local 4
// loading local 4 into D register
@4
D=A
@LCL
D=D+M
A=D
D=M
//finished loading local 4 value into D register
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
// Add: RAM[SP] = RAM[SP] + RAM[SP-1]
@SP
AM=M-1
D=M
A=A-1
M=D+M
// Add: RAM[SP] = RAM[SP] + RAM[SP-1]
@SP
AM=M-1
D=M
A=A-1
M=D+M
// Add: RAM[SP] = RAM[SP] + RAM[SP-1]
@SP
AM=M-1
D=M
A=A-1
M=D+M
@LCL
D=M
@R13
M=D
@5
A=D-A
D=M
@R14
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
AM=M-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@R14
A=M
0;JMP
(Sys.add12)
// push constant 4002
// loading constant 4002 into D register
@4002
D=A
//finished loading constant 4002 value into D register
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
// push constant 5002
// loading constant 5002 into D register
@5002
D=A
//finished loading constant 5002 value into D register
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
// push constant 12
// loading constant 12 into D register
@12
D=A
//finished loading constant 12 value into D register
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
@LCL
D=M
@R13
M=D
@5
A=D-A
D=M
@R14
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
AM=M-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@R14
A=M
0;JMP
