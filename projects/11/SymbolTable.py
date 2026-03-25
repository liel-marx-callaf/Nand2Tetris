"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing


class SymbolTable:
    """A symbol table that associates names with information needed for Jack
    compilation: type, kind and running index. The symbol table has two nested
    scopes (class/subroutine).
    """

    def __init__(self) -> None:
        """Creates a new empty symbol table."""
        # Class-level scope: static and field variables
        self.class_table = {}
        # Subroutine-level scope: argument and local (var) variables
        self.subroutine_table = {}
        # Counters for each kind of variable
        self.counters = {
            "STATIC": 0,
            "FIELD": 0,
            "ARG": 0,
            "VAR": 0
        }

    def start_subroutine(self) -> None:
        """Starts a new subroutine scope (i.e., resets the subroutine's 
        symbol table).
        """
        # Reset subroutine scope
        self.subroutine_table = {}
        # Reset subroutine-level counters
        self.counters["ARG"] = 0
        self.counters["VAR"] = 0

    def define(self, name: str, type: str, kind: str) -> None:
        """Defines a new identifier of a given name, type and kind and assigns 
        it a running index. "STATIC" and "FIELD" identifiers have a class scope, 
        while "ARG" and "VAR" identifiers have a subroutine scope.

        Args:
            name (str): the name of the new identifier.
            type (str): the type of the new identifier.
            kind (str): the kind of the new identifier, can be:
            "STATIC", "FIELD", "ARG", "VAR".
        """
        # Get current index for this kind
        index = self.counters[kind]
        
        # Create symbol entry
        symbol = {
            "type": type,
            "kind": kind,
            "index": index
        }
        
        # Add to appropriate table based on scope
        if kind in ("STATIC", "FIELD"):
            self.class_table[name] = symbol
        else:  # ARG or VAR
            self.subroutine_table[name] = symbol
        
        # Increment counter
        self.counters[kind] += 1

    def var_count(self, kind: str) -> int:
        """
        Args:
            kind (str): can be "STATIC", "FIELD", "ARG", "VAR".

        Returns:
            int: the number of variables of the given kind already defined in 
            the current scope.
        """
        return self.counters[kind]

    def kind_of(self, name: str) -> str:
        """
        Args:
            name (str): name of an identifier.

        Returns:
            str: the kind of the named identifier in the current scope, or None
            if the identifier is unknown in the current scope.
        """
        # Check subroutine scope first, then class scope
        if name in self.subroutine_table:
            return self.subroutine_table[name]["kind"]
        elif name in self.class_table:
            return self.class_table[name]["kind"]
        else:
            return None

    def type_of(self, name: str) -> str:
        """
        Args:
            name (str):  name of an identifier.

        Returns:
            str: the type of the named identifier in the current scope.
        """
        # Check subroutine scope first, then class scope
        if name in self.subroutine_table:
            return self.subroutine_table[name]["type"]
        elif name in self.class_table:
            return self.class_table[name]["type"]
        else:
            return None

    def index_of(self, name: str) -> int:
        """
        Args:
            name (str):  name of an identifier.

        Returns:
            int: the index assigned to the named identifier.
        """
        # Check subroutine scope first, then class scope
        if name in self.subroutine_table:
            return self.subroutine_table[name]["index"]
        elif name in self.class_table:
            return self.class_table[name]["index"]
        else:
            return None
