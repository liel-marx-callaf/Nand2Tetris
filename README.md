# Nand2Tetris

A full-stack implementation of the **Nand to Tetris** journey: building a complete 16-bit computer platform from first principles, starting with elementary logic gates and ending with a working high-level language, compiler, and operating system.

This repository contains my public portfolio version of the project, organized across the 12 course projects and focused on the implementation layers of the Hack platform.

## Academic Context

This project was completed as part of the **Nand2Tetris / Elements of Computing Systems** track at **The Hebrew University of Jerusalem**.

This public repository includes my implementation work and documentation only.

## Credit and Attribution

This work is based on the materials and architecture of **Nand2Tetris**, created by **Noam Nisan** and **Shimon Schocken**, authors of *The Elements of Computing Systems*.

Several source files in this repository preserve the original course attribution headers. Those headers are intentionally kept intact.

Where applicable, this repository also preserves attribution references included in the original course framework and Hebrew University course materials.

## High-Level Overview

The project follows the complete abstraction ladder of a modern computer system:

- **Hardware layer** — elementary gates, combinational chips, sequential memory elements, ALU, CPU, and computer architecture
- **Machine language layer** — Hack assembly programs and binary execution model
- **Systems software layer** — assembler, VM translator, compiler, and runtime services
- **High-level programming layer** — application development in **Jack**, a Java-like teaching language

The result is a full educational computer stack in which each layer is implemented on top of the one built before it.

## Technical Stack

- **HDL** for hardware design and chip implementation
- **Hack Assembly** for low-level programming on the Hack computer
- **Virtual Machine (VM) layer** for stack-based intermediate code
- **Jack** for high-level application and OS development
- **Python** for toolchain components such as the assembler, VM translator, and compiler stages in this implementation

## Repository Structure

```text
projects/
├── 01/  Elementary logic gates
├── 02/  Arithmetic and combinational chips
├── 03/  Sequential logic and memory
├── 04/  Machine language programming
├── 05/  Computer architecture
├── 06/  Assembler
├── 07/  VM translator: stack arithmetic and memory access
├── 08/  VM translator: program flow and function calls
├── 09/  Jack application
├── 10/  Syntax analysis
├── 11/  Compiler code generation
└── 12/  Operating system
```

## Project Breakdown

### Project 01 - Elementary Logic Gates
Implemented the basic building blocks of the Hack hardware platform using HDL, including primitive combinational chips such as multiplexers, demultiplexers, and multi-bit logic gates. This project establishes the gate-level foundation used throughout the rest of the stack.

### Project 02 - Arithmetic Logic Components
Built arithmetic and bitwise chips such as adders, incrementers, and the **ALU**, combining lower-level gates into reusable computational units. This project defines the core arithmetic behavior that later powers the CPU.

### Project 03 - Sequential Logic and Memory
Implemented clocked hardware components including bit registers, multi-bit registers, RAM units, and the program counter. The challenge here was moving from pure combinational logic to stateful sequential systems.

### Project 04 - Machine Language Programming
Wrote low-level programs directly in **Hack assembly**, working close to the hardware execution model. This project focuses on control flow, memory access, and problem solving without the abstraction of a high-level language.

### Project 05 - Computer Architecture
Integrated the previously built components into a complete **Hack computer**, including CPU, instruction memory, data memory, and overall execution flow. This project is the architectural milestone where individual chips become a functioning machine.

### Project 06 - Assembler
Developed an assembler that translates Hack assembly programs into binary machine code. The implementation handles parsing, symbol resolution, and instruction encoding, bridging human-readable assembly and executable hardware instructions.

### Project 07 - VM Translator I
Implemented the first stage of the **VM translator**, converting stack arithmetic and memory access commands into Hack assembly. This project introduces the intermediate abstraction layer that decouples high-level language compilation from the target hardware.

### Project 08 - VM Translator II
Extended the VM translator to support branching, function calls, returns, and multi-file program translation. The main challenge was preserving correct call-frame behavior and execution flow across nested routines.

### Project 09 - Jack Application
Built an application in **Jack** to exercise the software stack from the high-level language downward. This stage demonstrates how user programs interact with the VM, compiler, and operating system layers built in the later projects.

### Project 10 - Syntax Analysis
Implemented the front end of the Jack compiler, including tokenization and parsing into the language grammar. This project focuses on turning raw source code into a structured syntactic representation.

### Project 11 - Compiler Code Generation
Extended the compiler to emit VM code from parsed Jack programs. The implementation covers symbol management, expression compilation, control structures, subroutine handling, and object-oriented language constructs.

### Project 12 - Operating System
Implemented core components of the **Jack OS**, including standard library functionality such as memory handling, screen output, math support, strings, arrays, and keyboard interaction. This completes the software platform needed to run nontrivial high-level applications on the Hack computer.

## What This Repository Demonstrates

- End-to-end understanding of computer systems across multiple abstraction layers
- Digital logic design using HDL
- Low-level programming and instruction set reasoning
- Language tooling: parsing, translation, and code generation
- Systems thinking across hardware, runtime, compiler, and application boundaries

## Notes

- This repository is presented as a **public portfolio version** of the project.
- Course-distributed tools, local IDE metadata, caches, and nonessential archive files were intentionally excluded from the public version.
- Original attribution headers inside source files were preserved where provided by the course materials.

## License / Usage

This repository is intended for educational and portfolio purposes. Please respect the original Nand2Tetris authorship, course materials, and any attribution preserved in the source headers.
