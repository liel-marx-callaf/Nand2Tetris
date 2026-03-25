"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""

class Code:
    """Translates Hack assembly language mnemonics into binary codes."""
    DEST_TABLE = {
        None: "000",
        "":  "000",
        "M": "001",
        "D": "010",
        "MD": "011",
        "A": "100",
        "AM": "101",
        "AD": "110",
        "AMD": "111",
    }

    JUMP_TABLE = {
        None: "000",
        "": "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111",
    }

    COMP_TABLE = {
        "0": ("11", "101010"),
        "1": ("11","111111"),
        "-1": ("11","111010"),
        "D": ("11", "001100"),
        "A": ("11","110000"),
        "!D": ("11","001101"),
        "!A": ("11","110001"),
        "-D": ("11","001111"),
        "-A": ("11","110011"),
        "D+1": ("11","011111"),
        "A+1": ("11","110111"),
        "D-1": ("11","001110"),
        "A-1": ("11","110010"),
        "D+A": ("11","000010"),
        "D-A": ("11","010011"),
        "A-D": ("11","000111"),
        "D&A": ("11","000000"),
        "D|A": ("11","010101"),
        "A<<": ("01","100000"),
        "D<<": ("01","110000"),
        "A>>": ("01","000000"),
        "D>>": ("01","010000"),
    }
    # 111 a c1 c2 c3 c4 c5 c6 d1 d2
    @staticmethod
    def dest(mnemonic: str) -> str:
        """
        Args:
            mnemonic (str): a dest mnemonic string.

        Returns:
            str: 3-bit long binary code of the given mnemonic.
        """
        return Code.DEST_TABLE.get(mnemonic, "")

    @staticmethod
    def comp(mnemonic: str) -> str:
        """
        Args:
            mnemonic (str): a comp mnemonic string.

        Returns:
            str: the binary code of the given mnemonic.
        """
        a = "1" if "M" in mnemonic else "0"
        key = mnemonic.replace("M", "A")
        starter, ending = Code.COMP_TABLE.get(key, "")
        return starter + a + ending

    @staticmethod
    def jump(mnemonic: str) -> str:
        """
        Args:
            mnemonic (str): a jump mnemonic string.

        Returns:
            str: 3-bit long binary code of the given mnemonic.
        """
        return Code.JUMP_TABLE.get(mnemonic, "")