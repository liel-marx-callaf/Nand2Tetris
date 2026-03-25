"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import re
import typing


class Parser:
    """Encapsulates access to the input code. Reads an assembly program
    by reading each command line-by-line, parses the current command,
    and provides convenient access to the commands components (fields
    and symbols). In addition, removes all white space and comments.
    """

    A_COMM_PATTERN = re.compile(r"""
        ^@
        (\d+ | [A-Za-z_\.\$:][A-Za-z0-9_\.\$:]*)   # Group 1: number or symbol
        $
    """, re.VERBOSE)

    C_COMM_PATTERN = re.compile(r"""
        (?:([AMD]{1,3})=)?                         # Group 1: dest (optional)
        ([^;]+)                                    # Group 2: comp (mandatory)
        (?:;([A-Z]{3}))?                           # Group 3: jump (optional)
    """, re.VERBOSE)

    L_COMM_PATTERN = re.compile(r"""
        ^\(
        ([A-Za-z_\.\$:][A-Za-z0-9_\.\$:]*)         # Group 1: label symbol
        \)$
    """, re.VERBOSE)

    def __init__(self, input_file: typing.TextIO) -> None:
        """Opens the input file and gets ready to parse it.

        Args:
            input_file (typing.TextIO): input file.
        """
        # Your code goes here!
        # A good place to start is to read all the lines of the input:
        self.last = True
        self.lines = input_file.read().splitlines()[::-1]  # in reverse order
        self.lines = [re.sub(r"\s+|//.*", "", l)
                      for l in self.lines]  # remove comments
        self.lines = [l for l in self.lines if l]  # remove empty lines
        self.current_line = self.lines.pop()

    def has_more_commands(self) -> bool:
        """Are there more commands in the input?

        Returns:
            bool: True if there are more commands, False otherwise.
        """
        if self.lines:
            return True
        if self.last:
            self.last = False
            return True
        return False

    def advance(self) -> None:
        """Reads the next command from the input and makes it the current command.
        Should be called only if has_more_commands() is true.
        """
        if self.has_more_commands():
            self.current_line = self.lines.pop()

    def command_type(self) -> str:
        """
        Returns:
            str: the type of the current command:
            "A_COMMAND" for @Xxx where Xxx is either a symbol or a decimal number
            "C_COMMAND" for dest=comp;jump
            "L_COMMAND" (actually, pseudo-command) for (Xxx) where Xxx is a symbol
        """
        if self.A_COMM_PATTERN.match(self.current_line):
            return "A_COMMAND"
        elif self.L_COMM_PATTERN.match(self.current_line):
            return "L_COMMAND"
        elif self.C_COMM_PATTERN.match(self.current_line):
            return "C_COMMAND"
        return None

    def symbol(self) -> str:
        """
        Returns:
            str: the symbol or decimal Xxx of the current command @Xxx or
            (Xxx). Should be called only when command_type() is "A_COMMAND" or
            "L_COMMAND".
        """
        if self.command_type() in ['A_COMMAND', 'L_COMMAND']:
            return re.sub(r"[@()]*", "", self.current_line)
        return None

    def dest(self) -> str:
        """
        Returns:
            str: the dest mnemonic in the current C-command. Should be called 
            only when commandType() is "C_COMMAND".
        """
        dest = self.C_COMM_PATTERN.match(self.current_line).groups()[0]
        return dest or ""

    def comp(self) -> str:
        """
        Returns:
            str: the comp mnemonic in the current C-command. Should be called 
            only when commandType() is "C_COMMAND".
        """
        comp = self.C_COMM_PATTERN.match(self.current_line).groups()[1]
        return comp

    def jump(self) -> str:
        """
        Returns:
            str: the jump mnemonic in the current C-command. Should be called 
            only when commandType() is "C_COMMAND".
        """
        jump = self.C_COMM_PATTERN.match(self.current_line).groups()[2]
        return jump or ""
