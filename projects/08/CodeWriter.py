"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing


class CodeWriter:
    """Translates VM commands into Hack assembly code."""
    D_TRANS = {"argument": "ARG",
               "local": "LCL",
               "static": "{filename}_{index}",
               "constant": "",
               "this": "THIS",
               "that": "THAT",
               "pointer": "",
               "temp": ""}
    BUILT_IN_TRANS = {
        "argument": "ARG",
        "local": "LCL",
        "this": "THIS",
        "that": "THAT"
    }
    POINTER = ["THIS", "THAT"]

    def __init__(self, output_stream: typing.TextIO) -> None:
        """Initializes the CodeWriter.

        Args:
            output_stream (typing.TextIO): output stream.
        """
        # Your code goes here!
        # Note that you can write to output_stream like so:
        # output_stream.write("Hello world! \n")
        self.file = output_stream
        self.filename = None  # used for creating unique static label names
        self.function_name = ""
        self.label_counter = 1  # used for creating unique eq/lt/gt label names

    def set_file_name(self, filename: str) -> None:
        """Informs the code writer that the translation of a new VM file is 
        started.

        Args:
            filename (str): The name of the VM file.
        """
        # Your code goes here!
        # This function is useful when translating code that handles the
        # static segment. For example, in order to prevent collisions between two
        # .vm files which push/pop to the static segment, one can use the current
        # file's name in the assembly variable's name and thus differentiate between
        # static variables belonging to different files.
        # To avoid problems with Linux/Windows/MacOS differences with regards
        # to filenames and paths, you are advised to parse the filename in
        # the function "translate_file" in Main.py using python's os library,
        # For example, using code similar to:
        # input_filename, input_extension = os.path.splitext(os.path.basename(input_file.name))
        self.filename = filename
        # print(filename)
        self.function_name = ""  # reset the function name between files

    def write_arithmetic(self, command: str) -> None:
        """Writes assembly code that is the translation of the given 
        arithmetic command. For the commands eq, lt, gt, you should correctly
        compare between all numbers our computer supports, and we define the
        value "true" to be -1, and "false" to be 0.

        Args:
            command (str): an arithmetic command.
        """
        # Your code goes here!
        if command == "add":
            lines = self._add()
        elif command == "sub":
            lines = self._sub()
        elif command == "neg":
            lines = self._neg()
        elif command == "and":
            lines = self._and()
        elif command == "or":
            lines = self._or()
        elif command == "not":
            lines = self._not()
        elif command == "eq":
            lines = self._eq()
        elif command == "gt":
            lines = self._gt()
        elif command == "lt":
            lines = self._lt()
        elif command == "shiftleft":
            lines = self._shiftleft()
        elif command == "shiftright":
            lines = self._shiftright()
        else:
            lines = "arithmetic command not recognized.\n"
        self.file.write(lines)

    # <editor-fold desc="Arithmetic Helper Methods">

    def _add(self):
        new_command = ("// Add: RAM[SP] = RAM[SP] + RAM[SP-1]\n"
                       "@SP\n"
                       "AM=M-1\n"
                       "D=M\n"
                       "A=A-1\n"
                       "M=D+M\n")
        return new_command

    def _sub(self):
        new_command = ("// Sub: RAM[SP] = RAM[SP-1] - RAM[SP]\n"
                       "@SP\n"
                       "AM=M-1\n"
                       "D=M\n"
                       "A=A-1\n"
                       "M=M-D\n")
        return new_command

    def _neg(self):
        new_command = ("// Neg: RAM[SP] = -RAM[SP]\n"
                       "@SP\n"
                       "A=M-1\n"
                       "M=-M\n")
        return new_command

    def _and(self):
        new_command = ("// And: RAM[SP] = RAM[SP] & RAM[SP-1]\n"
                       "@SP\n"
                       "AM=M-1\n"
                       "D=M\n"
                       "A=A-1\n"
                       "M=M&D\n")
        return new_command

    def _or(self):
        new_command = ("// Or: RAM[SP] = RAM[SP] | RAM[SP-1]\n"
                       "@SP\n"
                       "AM=M-1\n"
                       "D=M\n"
                       "A=A-1\n"
                       "M=M|D\n")
        return new_command

    def _not(self) -> str:
        new_command = ("// Not: RAM[SP] = ! RAM[SP]\n"
                       "@SP\n"
                       "A=M-1\n"
                       "M=!M\n")
        return new_command

    def _eq(self):
        true_label = f"TRUE_EQ_{self.label_counter}"
        false_label = f"FALSE_EQ_{self.label_counter}"
        end_label = f"END_EQ_{self.label_counter}"

        new_command = (f"// Compare GT: RAM[SP] < RAM[SP-1]\n"
                       # SP--, R13 = RAM[SP] = y
                       "@SP\n"
                       "AM=M-1\n"
                       "D=M\n"
                       "@R13\n"
                       "M=D\n"
                       # R14 = RAM[SP-1] = x
                       "@SP\n"
                       "A=M-1\n"
                       "D=M\n"
                       "@R14\n"
                       "M=D\n"

                       # Jump to case x < 0
                       f"@NEG_X_{self.label_counter}\n"
                       "D;JLT\n"

                       # Case x >= 0
                       # In case x >= 0 & y < 0, then x > y (False)
                       "@R13\n"
                       "D=M\n"
                       f"@{false_label}\n"
                       "D;JLT\n"
                       # In case x >= 0 & y >=0, do subtraction
                       "@R14\n"
                       "D=M\n"
                       "@R13\n"
                       "D=D-M\n"
                       # if (x - y = 0) then jump to True label
                       f"@{true_label}\n"
                       "D;JEQ\n"
                       # else jump to False label
                       f"@{false_label}\n"
                       "0;JMP\n"

                       # Case x < 0
                       # In case x < 0 & y >= 0, then x < y (False)
                       f"(NEG_X_{self.label_counter})\n"
                       "@R13\n"
                       "D=M\n"
                       f"@{false_label}\n"
                       "D;JGE\n"
                       # In case x < 0 & y < 0, do subtraction
                       "@R14\n"
                       "D=M\n"
                       "@R13\n"
                       "D=D-M\n"
                       # if (x - y = 0) then jump to True label
                       f"@{true_label}\n"
                       "D;JEQ\n"
                       # else jump to False label
                       f"@{false_label}\n"
                       "0;JMP\n"

                       # True label
                       f"({true_label})\n"
                       "@SP\n"
                       "A=M-1\n"
                       "M=-1\n"
                       f"@{end_label}\n"
                       "0;JMP\n"

                       # False label
                       f"({false_label})\n"
                       "@SP\n"
                       "A=M-1\n"
                       "M=0\n"
                       f"@{end_label}\n"
                       "0;JMP\n"

                       f"({end_label})\n")
        self.label_counter += 1
        return new_command
        # return self._compare("eq")

    def _gt(self):
        true_label = f"TRUE_GT_{self.label_counter}"
        false_label = f"FALSE_GT_{self.label_counter}"
        end_label = f"END_GT_{self.label_counter}"

        new_command = (f"// Compare GT: RAM[SP] < RAM[SP-1]\n"
                       # SP--, R13 = RAM[SP] = y
                       "@SP\n"
                       "AM=M-1\n"
                       "D=M\n"
                       "@R13\n"
                       "M=D\n"
                       # R14 = RAM[SP-1] = x
                       "@SP\n"
                       "A=M-1\n"
                       "D=M\n"
                       "@R14\n"
                       "M=D\n"

                       # Jump to case x < 0
                       f"@NEG_X_{self.label_counter}\n"
                       "D;JLT\n"

                       # Case x >= 0
                       # In case x >= 0 & y < 0, then x > y (True)
                       "@R13\n"
                       "D=M\n"
                       f"@{true_label}\n"
                       "D;JLT\n"
                       # In case x >= 0 & y >=0, do subtraction
                       "@R14\n"
                       "D=M\n"
                       "@R13\n"
                       "D=D-M\n"
                       # if (x - y > 0) then jump to True label
                       f"@{true_label}\n"
                       "D;JGT\n"
                       # else jump to False label
                       f"@{false_label}\n"
                       "0;JMP\n"

                       # Case x < 0
                       # In case x < 0 & y >= 0, then x < y (False)
                       f"(NEG_X_{self.label_counter})\n"
                       "@R13\n"
                       "D=M\n"
                       f"@{false_label}\n"
                       "D;JGE\n"
                       # In case x < 0 & y < 0, do subtraction
                       "@R14\n"
                       "D=M\n"
                       "@R13\n"
                       "D=D-M\n"
                       # if (x - y > 0) then jump to True label
                       f"@{true_label}\n"
                       "D;JGT\n"
                       # else jump to False label
                       f"@{false_label}\n"
                       "0;JMP\n"

                       # True label
                       f"({true_label})\n"
                       "@SP\n"
                       "A=M-1\n"
                       "M=-1\n"
                       f"@{end_label}\n"
                       "0;JMP\n"

                       # False label
                       f"({false_label})\n"
                       "@SP\n"
                       "A=M-1\n"
                       "M=0\n"
                       f"@{end_label}\n"
                       "0;JMP\n"

                       f"({end_label})\n")
        self.label_counter += 1
        return new_command
        # return self._compare("gt")

    def _lt(self):
        true_label = f"TRUE_LT_{self.label_counter}"
        false_label = f"FALSE_LT_{self.label_counter}"
        end_label = f"END_LT_{self.label_counter}"

        new_command = (f"// Compare LT: RAM[SP] > RAM[SP-1]\n"
                       # SP--, R13 = RAM[SP] = y
                       "@SP\n"
                       "AM=M-1\n"
                       "D=M\n"
                       "@R13\n"
                       "M=D\n"
                       # R14 = RAM[SP-1] = x
                       "@SP\n"
                       "A=M-1\n"
                       "D=M\n"
                       "@R14\n"
                       "M=D\n"

                       # Jump to case x < 0
                       f"@NEG_X_{self.label_counter}\n"
                       "D;JLT\n"

                       # Case x >= 0
                       # In case x >= 0 & y < 0, then x > y (False)
                       "@R13\n"
                       "D=M\n"
                       f"@{false_label}\n"
                       "D;JLT\n"
                       # In case x >= 0 & y >=0, do subtraction
                       "@R14\n"
                       "D=M\n"
                       "@R13\n"
                       "D=D-M\n"
                       # if (x - y < 0) then jump to True label
                       f"@{true_label}\n"
                       "D;JLT\n"
                       # else jump to False label
                       f"@{false_label}\n"
                       "0;JMP\n"

                       # Case x < 0
                       # In case x < 0 & y >= 0, then x < y (True)
                       f"(NEG_X_{self.label_counter})\n"
                       "@R13\n"
                       "D=M\n"
                       f"@{true_label}\n"
                       "D;JGE\n"
                       # In case x < 0 & y < 0, do subtraction
                       "@R14\n"
                       "D=M\n"
                       "@R13\n"
                       "D=D-M\n"
                       # if (x - y < 0) then jump to True label
                       f"@{true_label}\n"
                       "D;JLT\n"
                       # else jump to False label
                       f"@{false_label}\n"
                       "0;JMP\n"

                       # True label
                       f"({true_label})\n"
                       "@SP\n"
                       "A=M-1\n"
                       "M=-1\n"
                       f"@{end_label}\n"
                       "0;JMP\n"

                       # False label
                       f"({false_label})\n"
                       "@SP\n"
                       "A=M-1\n"
                       "M=0\n"
                       f"@{end_label}\n"
                       "0;JMP\n"

                       f"({end_label})\n")
        self.label_counter += 1
        return new_command
        # return self._compare("lt")

    def _shiftleft(self):
        new_command = ("// Shiftleft: RAM[SP] = RAM[SP]<<\n"
                       "@SP\n"
                       "A=M-1\n"
                       "M=M<<\n")
        return new_command

    def _shiftright(self):
        new_command = ("// Shiftright: RAM[SP] = RAM[SP]>>\n"
                       "@SP\n"
                       "A=M-1\n"
                       "M=M>>\n")
        return new_command

    # </editor-fold>

    # <editor-fold desc="Push Pop Functions">

    def write_push_pop(self, command: str, segment: str, index: int) -> None:
        """Writes assembly code that is the translation of the given 
        command, where command is either C_PUSH or C_POP.

        Args:
            command (str): "C_PUSH" or "C_POP".
            segment (str): the memory segment to operate on."
            index (int): the index in the memory segment.
        """
        # Your code goes here!
        # Note: each reference to "static i" appearing in the file Xxx.vm should
        # be translated to the assembly symbol "Xxx.i". In the subsequent
        # assembly process, the Hack assembler will allocate these symbolic
        # variables to the RAM, starting at address 16.
        if command == "C_PUSH":
            lines = self._push(segment=segment, index=index)
        else:
            lines = self._pop(segment=segment, index=index)
        self.file.write(lines)

    def _push(self, segment: str, index: int) -> str:
        command = f"// push {segment} {index}\n"
        command += self._load_seg_index_into_d_reg(segment=segment,
                                                   index=index, for_push=True)
        command += ("// RAM[SP] = D\n"
                    "@SP\n"
                    "A=M\n"
                    "M=D\n"
                    "// SP++\n"
                    "@SP\n"
                    "M=M+1\n")
        return command

    def _pop(self, segment: str, index: int) -> str:
        new_command = f"// pop {segment} {index}\n"
        new_command += self._load_seg_index_into_d_reg(segment=segment,
                                                       index=index, for_push=False)
        new_command += ("@address\n"
                        "M=D\n"
                        "// move SP one back\n"
                        "@SP\n"
                        "M=M-1\n"
                        "// save RAM[SP]\n"
                        "A=M\n"
                        "D=M\n"
                        "// RAM[address] = RAM[SP]\n"
                        "@address\n"
                        "A=M\n"
                        "M=D\n")
        return new_command

    def _load_seg_index_into_d_reg(self, segment: str, index: int, for_push: bool = True) -> str:
        """
        Build Hack assembly that loads the value/address of `segment[index]`
        into the D register and return the generated assembly string.

        Args:
            segment (str): VM memory segment name (e.g. "local", "argument",
                "temp", "pointer", "static", "constant").
            index (int): Index within the segment.

        Returns:
            str: Assembly code that, when executed, leaves the requested value
            or address in the D register.

        Notes:
            - Built-in segments (`local`, `argument`, `this`, `that`) are handled
              by computing base+index.
            - `temp` maps to R5..R12 (index + 5).
            - `static` uses `self.filename` to form a symbol `filename.index`.
            - `pointer` maps index 0->THIS and 1->THAT; callers should ensure
              0 <= index < len(self.POINTER) to avoid out-of-range access.
        """
        # Begin assembly for loading the requested segment/index into D.
        start_command = f"// loading {segment} {index} into D register\n"
        if segment in self.BUILT_IN_TRANS:
            segment_id = self.BUILT_IN_TRANS[segment]
            start_command += (f"@{index}\n"
                              "D=A\n"
                              f"@{segment_id}\n"
                              "D=D+M\n")

            # if we are pushing, we want to load the value into the D
            # register and not the address
            if for_push:
                start_command += ("A=D\n"
                                  "D=M\n")
        elif segment == "temp":
            start_command += (f"@R{index + 5}\n"
                              f"D={'M' if for_push else 'A'}\n")

        elif segment == "static":
            start_command += (f"@{self.filename}.{index}\n"
                              f"D={'M' if for_push else 'A'}\n")

        elif segment == "pointer":
            if not (0 <= index < len(self.POINTER)):  # just a check to make
                # sure that the pointer is 0 or 1
                raise IndexError(f"pointer index out of range: {index}")
            start_command += (f"@{self.POINTER[index]}\n"
                              f"D={'M' if for_push else 'A'}\n")

        else:  # only const left
            start_command += (f"@{index}\n"
                              "D=A\n")
        start_command += (f"//finished loading {segment} {index} "
                          f"{'value' if for_push else 'address'} "
                          f"into D register\n")
        return start_command

    # </editor-fold>

    def write_label(self, label: str) -> None:
        """Writes assembly code that affects the label command. 
        Let "Xxx.foo" be a function within the file Xxx.vm. The handling of
        each "label bar" command within "Xxx.foo" generates and injects the symbol
        "Xxx.foo$bar" into the assembly code stream.
        When translating "goto bar" and "if-goto bar" commands within "foo",
        the label "Xxx.foo$bar" must be used instead of "bar".

        Args:
            label (str): the label to write.
        """
        # This is irrelevant for project 7,
        # you will implement this in project 8!
        full_label = self._get_full_label(label)
        # print(full_label)
        new_command = f"({full_label})\n"
        self.file.write(new_command)

    def _get_full_label(self, label: str) -> str:
        """helper function to get full label from label
        if the scope is in a function then it will return Xxx.foo$bar
        if the scope is in the file level then it will return Xxx$bar"""
        if self.function_name != "":
            full_label = f"{self.function_name}${label}"
        else:
            full_label = f"{self.filename}${label}"
        # print(full_label)
        return full_label

    def write_goto(self, label: str) -> None:
        """Writes assembly code that affects the goto command.

        Args:
            label (str): the label to go to.
        """
        # This is irrelevant for project 7,
        # you will implement this in project 8!
        full_label = self._get_full_label(label)
        new_command = (f"@{full_label}\n"
                       f"0;JMP\n")
        self.file.write(new_command)

    def write_if(self, label: str) -> None:
        """Writes assembly code that affects the if-goto command. 

        Args:
            label (str): the label to go to.
        """
        # This is irrelevant for project 7,
        # you will implement this in project 8!
        # remember that true = -1 and false = 0
        full_label = self._get_full_label(label)
        new_command = (f"@SP\n"
                       f"AM=M-1\n"  # we remove  and go to the last place in the stack 
                       f"D=M\n"
                       f"@{full_label}\n"
                       # if D == -1 that means that the value is true and we should jump
                       f"D;JNE\n")
        self.file.write(new_command)

    def write_function(self, function_name: str, n_vars: int) -> None:
        """Writes assembly code that affects the function command. 
        The handling of each "function Xxx.foo" command within the file Xxx.vm
        generates and injects a symbol "Xxx.foo" into the assembly code stream,
        that labels the entry-point to the function's code.
        In the subsequent assembly process, the assembler translates this 
        symbol into the physical address where the function code starts.

        Args:
            function_name (str): the name of the function.
            n_vars (int): the number of local variables of the function.
        """
        # This is irrelevant for project 7,
        # you will implement this in project 8!
        # The pseudo-code of "function function_name n_vars" is:
        # (function_name)       // injects a function entry label into the code
        # repeat n_vars times:  // n_vars = number of local variables
        #   push constant 0     // initializes the local variables to 0

        self.function_name = function_name  # needed for labels, dont remove.

        # injects a function entry label into the code
        self.file.write(f"({function_name})\n")

        # initializes n_vars of local variables to 0
        var = []
        for i in range(n_vars):
            var.append(
                # holds 0
                "@0\n"
                "D=A\n"
                # add to stack
                "@SP\n"
                "A=M\n"
                "M=D\n"
                # SP++
                "@SP\n"
                "M=M+1\n"
            )
        self.file.write("".join(var))

    def _call_push(self, arg: str) -> str:
        return (
            f"@{arg}\n"
            "D=M\n"
            "@SP\n"
            "A=M\n"
            "M=D\n"
            "@SP\n"
            "M=M+1\n"
        )

    def write_call(self, function_name: str, n_args: int) -> None:
        """Writes assembly code that affects the call command. 
        Let "Xxx.foo" be a function within the file Xxx.vm.
        The handling of each "call" command within Xxx.foo's code generates and
        injects a symbol "Xxx.foo$ret.i" into the assembly code stream, where
        "i" is a running integer (one such symbol is generated for each "call"
        command within "Xxx.foo").
        This symbol is used to mark the return address within the caller's 
        code. In the subsequent assembly process, the assembler translates this
        symbol into the physical memory address of the command immediately
        following the "call" command.

        Args:
            function_name (str): the name of the function to call.
            n_args (int): the number of arguments of the function.
        """
        # This is irrelevant for project 7,
        # you will implement this in project 8!
        # The pseudo-code of "call function_name n_args" is:
        # push return_address   // generates a label and pushes it to the stack
        # push LCL              // saves LCL of the caller
        # push ARG              // saves ARG of the caller
        # push THIS             // saves THIS of the caller
        # push THAT             // saves THAT of the caller
        # ARG = SP-5-n_args     // repositions ARG
        # LCL = SP              // repositions LCL
        # goto function_name    // transfers control to the callee
        # (return_address)      // injects the return address label into the code

        # generates a label and pushes it to the stack
        return_label = f"{self.function_name}$ret.{self.label_counter}"
        self.label_counter += 1

        cmd = []

        # generates a label and pushes it to the stack: push return-address
        cmd.append(
            f"@{return_label}\n"
            "D=A\n"
            "@SP\n"
            "A=M\n"
            "M=D\n"
            "@SP\n"
            "M=M+1\n"
        )

        # save current state of caller
        cmd.append(self._call_push("LCL"))
        cmd.append(self._call_push("ARG"))
        cmd.append(self._call_push("THIS"))
        cmd.append(self._call_push("THAT"))

        # repositions ARG: ARG = SP - 5 - n_args
        cmd.append(
            "@SP\n"
            "D=M\n"
            "@5\n"
            "D=D-A\n"
            f"@{n_args}\n"
            "D=D-A\n"
            "@ARG\n"
            "M=D\n"
        )

        # repositions LCL: LCL = SP
        cmd.append(
            "@SP\n"
            "D=M\n"
            "@LCL\n"
            "M=D\n"
        )

        # transfers control to the callee: goto function_name
        cmd.append(
            f"@{function_name}\n"
            "0;JMP\n"
        )

        # injects the return address label into the code: (return_address)
        cmd.append(f"({return_label})\n")

        self.file.write("".join(cmd))

        pass

    def _return_restore(self, segment: str) -> str:
        return (
            "@R13\n"
            "AM=M-1\n"
            "D=M\n"
            f"@{segment}\n"
            "M=D\n"
        )

    def write_return(self) -> None:
        """Writes assembly code that affects the return command."""
        # This is irrelevant for project 7,
        # you will implement this in project 8!
        # The pseudo-code of "return" is:
        # frame = LCL                   // frame is a temporary variable
        # return_address = *(frame-5)   // puts the return address in a temp var
        # *ARG = pop()                  // repositions the return value for the caller
        # SP = ARG + 1                  // repositions SP for the caller
        # THAT = *(frame-1)             // restores THAT for the caller
        # THIS = *(frame-2)             // restores THIS for the caller
        # ARG = *(frame-3)              // restores ARG for the caller
        # LCL = *(frame-4)              // restores LCL for the caller
        # goto return_address           // go to the return address

        cmd = []

        # copy LCL to a temporary variable R13
        cmd.append(
            "@LCL\n"
            "D=M\n"  # address of caller local stack 
            "@R13\n"
            "M=D\n"
        )

        # copy return address to a temporary variable R14
        cmd.append(
            "@5\n"
            "A=D-A\n"  # address of caller local stack - 5 = address of return address
            "D=M\n"  # value of return address
            "@R14\n"
            "M=D\n"
        )

        # repositions the return value for the caller: *ARG = pop()
        cmd.append(
            "@SP\n"
            "AM=M-1\n"
            "D=M\n"  # the return value
            "@ARG\n"
            "A=M\n"
            "M=D\n"
        )

        # repositions SP for the caller: SP = ARG + 1
        cmd.append(
            "@ARG\n"
            "D=M+1\n"
            "@SP\n"
            "M=D\n"
        )

        # restore frame of the caller: SEGMENT = *(frame-i)
        cmd.append(self._return_restore("THAT"))
        cmd.append(self._return_restore("THIS"))
        cmd.append(self._return_restore("ARG"))
        cmd.append(self._return_restore("LCL"))

        # goto return_address
        cmd.append(
            "@R14\n"
            "A=M\n"
            "0;JMP\n"
        )

        self.file.write("".join(cmd))

    def write_init(self) -> None:
        """Writes assembly code that effects the VM initialization (bootstrap code).
        This code should be placed at the beginning of the output file.
        """
        # Your code goes here!
        init_code = ("//Bootstrap code\n"
                     "@256\n"
                     "D=A\n"
                     "@SP\n"
                     "M=D\n"
                     "// Call Sys.init\n")
        self.file.write(init_code)
        self.write_call("Sys.init", 0)