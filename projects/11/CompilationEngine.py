"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing
from JackTokenizer import JackTokenizer
from VMWriter import VMWriter
from SymbolTable import SymbolTable


class CompilationEngine:
    """Gets input from a JackTokenizer and emits VM code into an output stream."""
    
    def __init__(self, input_stream: "JackTokenizer", output_stream, 
                 vm_writer: "VMWriter", symbol_table: "SymbolTable") -> None:
        """
        Creates a new compilation engine with the given input and output.
        :param input_stream: The JackTokenizer.
        :param output_stream: The output stream (not used directly, VMWriter handles it).
        :param vm_writer: The VMWriter for generating VM code.
        :param symbol_table: The SymbolTable for managing variables.
        """
        self.tokenizer = input_stream
        self.output_stream = output_stream
        self.vm_writer = vm_writer
        self.symbol_table = symbol_table
        
        # Class-level information
        self.class_name = ""
        
        # Label counters for control flow
        self.if_label_counter = 0
        self.while_label_counter = 0
        
        # Operator mappings
        self.binary_ops = {
            "+": "ADD",
            "-": "SUB",
            "*": "MUL",  # Handled specially as Math.multiply
            "/": "DIV",  # Handled specially as Math.divide
            "&": "AND",
            "|": "OR",
            "<": "LT",
            ">": "GT",
            "=": "EQ"
        }
        
        self.unary_ops = {
            "-": "NEG",
            "~": "NOT",
            "^": "SHIFTLEFT",
            "#": "SHIFTRIGHT"
        }

    def compile_class(self) -> None:
        """
        Compiles a complete class.
        class: 'class' className '{' classVarDec* subroutineDec* '}'
        """
        # 'class' keyword (current token)
        self.tokenizer.advance()
        
        # className
        self.class_name = self.tokenizer.current_token
        self.tokenizer.advance()
        
        # '{'
        self.tokenizer.advance()
        
        # classVarDec*
        while self.tokenizer.current_token in ("static", "field"):
            self.compile_class_var_dec()
        
        # subroutineDec*
        while self.tokenizer.current_token in ("constructor", "function", "method"):
            self.compile_subroutine()

    def compile_class_var_dec(self) -> None:
        """
        Compiles a static declaration or a field declaration.
        classVarDec: ('static' | 'field') type varName (',' varName)* ';'
        """
        # static | field
        kind = self.tokenizer.current_token.upper()  # "STATIC" or "FIELD"
        self.tokenizer.advance()
        
        # type
        var_type = self.tokenizer.current_token
        self.tokenizer.advance()
        
        # varName
        var_name = self.tokenizer.current_token
        self.symbol_table.define(var_name, var_type, kind)
        self.tokenizer.advance()
        
        # (',' varName)*
        while self.tokenizer.current_token == ",":
            self.tokenizer.advance()  # ','
            var_name = self.tokenizer.current_token
            self.symbol_table.define(var_name, var_type, kind)
            self.tokenizer.advance()
        
        # ';'
        self.tokenizer.advance()

    def compile_subroutine(self) -> None:
        """
        Compiles a complete method, function, or constructor.
        """
        # Reset subroutine scope
        self.symbol_table.start_subroutine()
        
        # constructor | function | method
        subroutine_type = self.tokenizer.current_token
        self.tokenizer.advance()
        
        # return type ('void' | type)
        self.tokenizer.advance()
        
        # subroutineName
        subroutine_name = self.tokenizer.current_token
        self.tokenizer.advance()
        
        # If method, add implicit 'this' as first argument
        if subroutine_type == "method":
            self.symbol_table.define("this", self.class_name, "ARG")
        
        # '(' parameterList ')'
        self.tokenizer.advance()  # '('
        self.compile_parameter_list()
        self.tokenizer.advance()  # ')'
        
        # subroutineBody: '{' varDec* statements '}'
        self.tokenizer.advance()  # '{'
        
        # varDec*
        while self.tokenizer.current_token == "var":
            self.compile_var_dec()
        
        # Write function declaration
        n_locals = self.symbol_table.var_count("VAR")
        self.vm_writer.write_function(f"{self.class_name}.{subroutine_name}", n_locals)
        
        # Handle subroutine type-specific prologue
        if subroutine_type == "constructor":
            # Allocate memory for the object
            n_fields = self.symbol_table.var_count("FIELD")
            self.vm_writer.write_push("CONST", n_fields)
            self.vm_writer.write_call("Memory.alloc", 1)
            self.vm_writer.write_pop("POINTER", 0)  # anchor this at the base address
            
        elif subroutine_type == "method":
            # Set 'this' to point to the object
            self.vm_writer.write_push("ARG", 0)
            self.vm_writer.write_pop("POINTER", 0)
        
        # statements
        self.compile_statements()
        
        # '}'
        self.tokenizer.advance()

    def compile_parameter_list(self) -> None:
        """
        Compiles a (possibly empty) parameter list, not including the enclosing "()".
        parameterList: ((type varName) (',' type varName)*)?
        """
        if self.tokenizer.current_token != ")":
            # type
            param_type = self.tokenizer.current_token
            self.tokenizer.advance()
            
            # varName
            param_name = self.tokenizer.current_token
            self.symbol_table.define(param_name, param_type, "ARG")
            self.tokenizer.advance()
            
            # (',' type varName)*
            while self.tokenizer.current_token == ",":
                self.tokenizer.advance()  # ','
                param_type = self.tokenizer.current_token
                self.tokenizer.advance()
                param_name = self.tokenizer.current_token
                self.symbol_table.define(param_name, param_type, "ARG")
                self.tokenizer.advance()

    def compile_var_dec(self) -> None:
        """
        Compiles a var declaration.
        varDec: 'var' type varName (',' varName)* ';'
        """
        # 'var'
        self.tokenizer.advance()
        
        # type
        var_type = self.tokenizer.current_token
        self.tokenizer.advance()
        
        # varName
        var_name = self.tokenizer.current_token
        self.symbol_table.define(var_name, var_type, "VAR")
        self.tokenizer.advance()
        
        # (',' varName)*
        while self.tokenizer.current_token == ",":
            self.tokenizer.advance()  # ','
            var_name = self.tokenizer.current_token
            self.symbol_table.define(var_name, var_type, "VAR")
            self.tokenizer.advance()
        
        # ';'
        self.tokenizer.advance()

    def compile_statements(self) -> None:
        """
        Compiles a sequence of statements, not including the enclosing "{}".
        """
        while self.tokenizer.current_token in ("let", "if", "while", "do", "return"):
            if self.tokenizer.current_token == "let":
                self.compile_let()
            elif self.tokenizer.current_token == "if":
                self.compile_if()
            elif self.tokenizer.current_token == "while":
                self.compile_while()
            elif self.tokenizer.current_token == "do":
                self.compile_do()
            elif self.tokenizer.current_token == "return":
                self.compile_return()

    def compile_do(self) -> None:
        """
        Compiles a do statement.
        doStatement: 'do' subroutineCall ';'
        """
        # 'do'
        self.tokenizer.advance()
        
        # subroutineCall
        self.compile_subroutine_call()
        
        # Discard return value (do statements ignore the return)
        self.vm_writer.write_pop("TEMP", 0)
        
        # ';'
        self.tokenizer.advance()

    def compile_let(self) -> None:
        """
        Compiles a let statement.
        letStatement: 'let' varName ('[' expression ']')? '=' expression ';'
        """
        # 'let'
        self.tokenizer.advance()
        
        # varName
        var_name = self.tokenizer.current_token
        self.tokenizer.advance()
        
        # Check if array assignment
        is_array = self.tokenizer.current_token == "["
        
        if is_array:
            # '[' expression ']'
            self.tokenizer.advance()  # '['
            
            # Compile index expression first
            self.compile_expression()
            
            self.tokenizer.advance()  # ']'
            
            # Push array base address
            self.push_variable(var_name)
            
            # Add base + index
            self.vm_writer.write_arithmetic("ADD")
        
        # '='
        self.tokenizer.advance()
        
        # expression (the value to assign)
        self.compile_expression()
        
        if is_array:
            # Array assignment: arr[i] = value
            # Stack now has: [base+index, value]
            self.vm_writer.write_pop("TEMP", 0)      # Save value
            self.vm_writer.write_pop("POINTER", 1)   # Set THAT = base+index
            self.vm_writer.write_push("TEMP", 0)     # Push value back
            self.vm_writer.write_pop("THAT", 0)      # Store value at arr[i]
        else:
            # Simple assignment
            self.pop_variable(var_name)
        
        # ';'
        self.tokenizer.advance()

    def compile_while(self) -> None:
        """
        Compiles a while statement.
        whileStatement: 'while' '(' expression ')' '{' statements '}'
        """
        exp_label = f"WHILE_EXP{self.while_label_counter}"
        end_label = f"WHILE_END{self.while_label_counter}"
        self.while_label_counter += 1
        
        # 'while'
        self.tokenizer.advance()
        
        # Start of loop - evaluate expression
        self.vm_writer.write_label(exp_label)
        
        # '(' expression ')'
        self.tokenizer.advance()  # '('
        self.compile_expression()
        self.tokenizer.advance()  # ')'
        
        # Negate condition and jump to end if false
        self.vm_writer.write_arithmetic("NOT")
        self.vm_writer.write_if(end_label)
        
        # '{' statements '}'
        self.tokenizer.advance()  # '{'
        self.compile_statements()
        self.tokenizer.advance()  # '}'
        
        # Jump back to expression evaluation
        self.vm_writer.write_goto(exp_label)
        
        # End label
        self.vm_writer.write_label(end_label)

    def compile_return(self) -> None:
        """
        Compiles a return statement.
        returnStatement: 'return' expression? ';'
        """
        # 'return'
        self.tokenizer.advance()
        
        # Check if there's a return expression
        if self.tokenizer.current_token != ";":
            self.compile_expression()
        else:
            # Void return - push 0
            self.vm_writer.write_push("CONST", 0)
        
        # ';'
        self.tokenizer.advance()
        
        # Write return command
        self.vm_writer.write_return()

    def compile_if(self) -> None:
        """
        Compiles an if statement, possibly with a trailing else clause.
        ifStatement: 'if' '(' expression ')' '{' statements '}' 
                     ('else' '{' statements '}')?
        """
        true_label = f"IF_TRUE{self.if_label_counter}"
        false_label = f"IF_FALSE{self.if_label_counter}"
        end_label = f"IF_END{self.if_label_counter}"
        self.if_label_counter += 1
        
        # 'if'
        self.tokenizer.advance()
        
        # '(' expression ')'
        self.tokenizer.advance()  # '('
        self.compile_expression()
        self.tokenizer.advance()  # ')'
        
        # Jump to true label if condition is true
        self.vm_writer.write_if(true_label)
        # Otherwise goto false label
        self.vm_writer.write_goto(false_label)
        
        # True block
        self.vm_writer.write_label(true_label)
        # '{' statements '}'
        self.tokenizer.advance()  # '{'
        self.compile_statements()
        self.tokenizer.advance()  # '}'
        
        # Check for else clause
        has_else = self.tokenizer.current_token == "else"
        
        if has_else:
            # Jump to end (skip else block)
            self.vm_writer.write_goto(end_label)
            
            # False/else label
            self.vm_writer.write_label(false_label)
            
            self.tokenizer.advance()  # 'else'
            self.tokenizer.advance()  # '{'
            self.compile_statements()
            self.tokenizer.advance()  # '}'
            
            # End label
            self.vm_writer.write_label(end_label)
        else:
            # No else clause - false label IS the end label
            self.vm_writer.write_label(false_label)

    def compile_expression(self) -> None:
        """
        Compiles an expression.
        expression: term (op term)*
        """
        # Compile first term
        self.compile_term()
        
        # (op term)*
        while self.tokenizer.current_token in self.binary_ops:
            op = self.tokenizer.current_token
            self.tokenizer.advance()
            
            # Compile next term
            self.compile_term()
            
            # Apply operator
            if op == "*":
                self.vm_writer.write_call("Math.multiply", 2)
            elif op == "/":
                self.vm_writer.write_call("Math.divide", 2)
            else:
                self.vm_writer.write_arithmetic(self.binary_ops[op])

    def compile_term(self) -> None:
        """
        Compiles a term.
        term: integerConstant | stringConstant | keywordConstant | varName |
              varName '[' expression ']' | subroutineCall | '(' expression ')' |
              unaryOp term
        """
        token_type = self.tokenizer.token_type()
        token = self.tokenizer.current_token
        
        # integerConstant
        if token_type == "INT_CONST":
            self.vm_writer.write_push("CONST", self.tokenizer.int_val())
            self.tokenizer.advance()
        
        # stringConstant
        elif token_type == "STRING_CONST":
            string_val = self.tokenizer.string_val()
            # Create new String object
            self.vm_writer.write_push("CONST", len(string_val))
            self.vm_writer.write_call("String.new", 1)
            # Append each character
            for char in string_val:
                self.vm_writer.write_push("CONST", ord(char))
                self.vm_writer.write_call("String.appendChar", 2)
            self.tokenizer.advance()
        
        # keywordConstant (true, false, null, this)
        elif token_type == "KEYWORD":
            if token == "true":
                self.vm_writer.write_push("CONST", 0)
                self.vm_writer.write_arithmetic("NOT")  # true = -1
            elif token in ("false", "null"):
                self.vm_writer.write_push("CONST", 0)
            elif token == "this":
                self.vm_writer.write_push("POINTER", 0)
            self.tokenizer.advance()
        
        # '(' expression ')'
        elif token == "(":
            self.tokenizer.advance()  # '('
            self.compile_expression()
            self.tokenizer.advance()  # ')'
        
        # unaryOp term
        elif token in self.unary_ops:
            op = token
            self.tokenizer.advance()
            self.compile_term()
            # Apply unary operator
            if op == "^":
                self.vm_writer.write_call("Math.shiftleft", 1)
            elif op == "#":
                self.vm_writer.write_call("Math.shiftright", 1)
            else:
                self.vm_writer.write_arithmetic(self.unary_ops[op])
        
        # varName, varName[expression], or subroutineCall
        elif token_type == "IDENTIFIER":
            identifier = token
            self.tokenizer.advance()
            
            # Check next token to determine what kind of term this is
            next_token = self.tokenizer.current_token
            
            if next_token == "[":
                # Array access: varName '[' expression ']'
                self.tokenizer.advance()  # '['
                
                # Compile index expression first
                self.compile_expression()
                
                # Push array base address
                self.push_variable(identifier)
                
                # Add base + index
                self.vm_writer.write_arithmetic("ADD")
                
                # Set THAT to base+index and push value
                self.vm_writer.write_pop("POINTER", 1)
                self.vm_writer.write_push("THAT", 0)
                
                self.tokenizer.advance()  # ']'
            
            elif next_token in ("(", "."):
                # Subroutine call - backtrack by one token
                self.tokenizer.current_index -= 1
                self.tokenizer.current_token = identifier
                self.compile_subroutine_call()
            
            else:
                # Simple variable
                self.push_variable(identifier)

    def compile_expression_list(self) -> int:
        """
        Compiles a (possibly empty) comma-separated list of expressions.
        Returns the number of expressions in the list.
        """
        n_args = 0
        
        if self.tokenizer.current_token != ")":
            self.compile_expression()
            n_args = 1
            
            while self.tokenizer.current_token == ",":
                self.tokenizer.advance()  # ','
                self.compile_expression()
                n_args += 1
        
        return n_args

    def compile_subroutine_call(self) -> None:
        """
        Compiles a subroutine call.
        subroutineCall: subroutineName '(' expressionList ')' |
                       (className | varName) '.' subroutineName '(' expressionList ')'
        """
        # First identifier (could be subroutineName, className, or varName)
        first_name = self.tokenizer.current_token
        self.tokenizer.advance()
        
        n_args = 0
        
        if self.tokenizer.current_token == ".":
            # (className | varName) '.' subroutineName
            self.tokenizer.advance()  # '.'
            second_name = self.tokenizer.current_token
            self.tokenizer.advance()
            
            # Check if first_name is a variable (object) or a class name
            var_type = self.symbol_table.type_of(first_name)
            
            if var_type:
                # It's a method call on an object
                self.push_variable(first_name)
                n_args = 1
                full_name = f"{var_type}.{second_name}"
            else:
                # It's a function call or constructor
                full_name = f"{first_name}.{second_name}"
        
        else:
            # subroutineName '(' - method call on current object
            self.vm_writer.write_push("POINTER", 0)  # push this
            n_args = 1
            full_name = f"{self.class_name}.{first_name}"
        
        # '(' expressionList ')'
        self.tokenizer.advance()  # '('
        n_args += self.compile_expression_list()
        self.tokenizer.advance()  # ')'
        
        # Make the call
        self.vm_writer.write_call(full_name, n_args)

    def push_variable(self, var_name: str) -> None:
        """Helper method to push a variable onto the stack."""
        kind = self.symbol_table.kind_of(var_name)
        index = self.symbol_table.index_of(var_name)
        
        segment_map = {
            "STATIC": "STATIC",
            "FIELD": "THIS",
            "ARG": "ARG",
            "VAR": "LOCAL"
        }
        
        segment = segment_map[kind]
        self.vm_writer.write_push(segment, index)

    def pop_variable(self, var_name: str) -> None:
        """Helper method to pop from stack into a variable."""
        kind = self.symbol_table.kind_of(var_name)
        index = self.symbol_table.index_of(var_name)
        
        segment_map = {
            "STATIC": "STATIC",
            "FIELD": "THIS",
            "ARG": "ARG",
            "VAR": "LOCAL"
        }
        
        segment = segment_map[kind]
        self.vm_writer.write_pop(segment, index)
