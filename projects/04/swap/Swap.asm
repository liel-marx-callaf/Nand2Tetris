// This file is part of nand2tetris, as taught in The Hebrew University, and
// was written by Aviv Yaish. It is an extension to the specifications given
// [here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
// as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
// Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).

// The program should swap between the max. and min. elements of an array.
// Assumptions:
// - The array's start address is stored in R14, and R15 contains its length
// - Each array value x is between -16384 < x < 16384
// - The address in R14 is at least >= 2048
// - R14 + R15 <= 16383
//
// Requirements:
// - Changing R14, R15 is not allowed.

// Put your code here.
(INIT)
	@R15
	D=M
	@i
	M=D
	// set min value
	@R14
	D=M
	@minAdd
	M=D
	A=D
	D=M
	@minVal
	M=D
	
	// set max value
	@R14
	D=M
	@maxAdd
	M=D
	A=D
	D=M
	@maxVal
	M=D
	
(LOOP)	
	// check if finished loop when i<0
	@i
	D=M
	@SWAPVAL
	D;JLT
	// get to the i element in the array
	@i
	M=M-1
	D=M
	@R14
	A=D+M	
	D=M
	//save the value in the i position in the array
	@cur
	M=D
	//start testing
	@MAX
	0;JMP

	
(MAX)
	@cur
	D=M
	@maxVal
	D=D-M
	@SETMAX
	D;JGT
	@MIN
	0;JMP

(SETMAX)
	@cur
	D=M
	@maxVal
	M=D
	// go back to the i elements address
	@i
	D=M
	@R14
	A=D+M	
	D=A
	@maxAdd
	M=D
	@MIN
	0;JMP

(MIN)
	@cur
	D=M
	@minVal
	D=D-M
	@SETMIN
	D;JLT
	@LOOP
	0;JMP

(SETMIN)
	@cur
	D=M
	@minVal
	M=D
	// go back to the i elements address
	@i
	D=M
	@R14
	A=D+M	
	D=A
	@minAdd
	M=D
	@LOOP
	0;JMP
	
(SWAPVAL)
	@maxVal
	D=M
	@minAdd
	A=M
	M=D
	@minVal
	D=M
	@maxAdd
	A=M
	M=D
	@END
	0;JMP
(END)
	@END
	0;JMP