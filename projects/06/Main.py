"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import os
import sys
import typing
from SymbolTable import SymbolTable
from Parser import Parser
from Code import Code


def assemble_file(
        input_file: typing.TextIO, output_file: typing.TextIO) -> None:
    """Assembles a single file.

    Args:
        input_file (typing.TextIO): the file to assemble.
        output_file (typing.TextIO): writes all output to this file.
    """
    # Your code goes here!
    # A good place to start is to initialize a new Parser object:
    # Note that you can write to output_file like so:
    # output_file.write("Hello world! \n")

    parser = Parser(input_file)
    symbol_table = SymbolTable()
    line_index = 0
    while parser.has_more_commands():
        if (parser.command_type() == "A_COMMAND" or parser.command_type() ==
            "C_COMMAND"):
            line_index += 1
        else: #that means that only the L commands are being caught and
            # added first into the symbol table
            symbol_table.add_entry(parser.symbol(), line_index)
        parser.advance()

    available_ram_add = 16
    input_file.seek(0) # "Rewinds" the file before the second pass
    parser = Parser(input_file)

    while parser.has_more_commands():
        write_line = ""
        if parser.command_type() == "L_COMMAND":
            # on the second run, we dont want to write the L commands into
            # the hack file, so we will advance the parser and not write
            # anything to the next line
            parser.advance()
            continue
        elif parser.command_type() == "C_COMMAND":
            dest, comp, jump = parser.dest(), parser.comp(), parser.jump()
            # print("vals:", dest, comp, jump)
            dest = Code.dest(dest)
            comp = Code.comp(comp)
            jump = Code.jump(jump)
            write_line = "1" + comp + dest + jump
        else: # can be either A command or a L command but we dont want to
            # write the L command into the file
            symbol = parser.symbol()
            if symbol_table.contains(symbol):
                address = symbol_table.get_address(symbol) # returns as an int
                address = format(address, '015b')  # turn into binary that
                # is padded with zeros
                write_line = "0" + address
            elif symbol.isdigit():
                address = format(int(symbol), '015b')
                write_line = "0" + address
            else:
                if parser.command_type() == "A_COMMAND":
                    # add symbol for the next RAM address  (assuming that
                    # there is less than 240 variables)
                    address = available_ram_add
                    symbol_table.add_entry(symbol, address)
                    available_ram_add += 1
                    address = format(address, '015b')
                    write_line = "0" + address
        output_file.write(write_line + '\n')
        # line_index += 1
        parser.advance()
    return





if "__main__" == __name__:
    # Parses the input path and calls assemble_file on each input file.
    # This opens both the input and the output files!
    # Both are closed automatically when the code finishes running.
    # If the output file does not exist, it is created automatically in the
    # correct path, using the correct filename.
    if not len(sys.argv) == 2:
        sys.exit("Invalid usage, please use: Assembler <input path>")
    argument_path = os.path.abspath(sys.argv[1])
    if os.path.isdir(argument_path):
        files_to_assemble = [
            os.path.join(argument_path, filename)
            for filename in os.listdir(argument_path)]
    else:
        files_to_assemble = [argument_path]
    for input_path in files_to_assemble:
        filename, extension = os.path.splitext(input_path)
        if extension.lower() != ".asm":
            continue
        output_path = filename + ".hack"
        with open(input_path, 'r') as input_file, \
                open(output_path, 'w') as output_file:
            assemble_file(input_file, output_file)


