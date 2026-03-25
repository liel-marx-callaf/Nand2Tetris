"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing

from JackTokenizer import JackTokenizer


class CompilationEngine:
    """Gets input from a JackTokenizer and emits its parsed structure into an
    output stream.
    """
    XML_ESCAPES = {
        "<": "&lt;",
        ">": "&gt;",
        "&": "&amp;",
    }
    OPS = {"+", "-", "*", "/", "&", "|", "<", ">", "="}
    UNARY_OPS = {"-", "~", "^", "#"}
    TYPER = {"int_const": "integerConstant", "string_const": "stringConstant", }

    def __init__(self, input_stream: "JackTokenizer", output_stream) -> None:
        """
        Creates a new compilation engine with the given input and output. The
        next routine called must be compileClass()
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        """
        # Your code goes here!
        # Note that you can write to output_stream like so:
        # output_stream.write("Hello world! \n")
        self.tokenizer = input_stream
        self.output_stream = output_stream
        self.indent = 0

    # used for testing
    def compile_tokens(self) -> None:
        self.output_stream.write("<tokens>\n")
        while self.tokenizer.has_more_tokens():
            self.output_stream.write("<" + self.tokenizer.token_type().lower() + "> ")
            self.output_stream.write(self.tokenizer.current_token)
            self.output_stream.write(" </" + self.tokenizer.token_type().lower() + ">\n")
            self.tokenizer.advance()
        self.output_stream.write("</tokens>\n")
        self.output_stream.flush()

    def write(self, line: str) -> None:
        self.output_stream.write("  " * self.indent + line + "\n")

    def _escape(self, token: str) -> str:
        return self.XML_ESCAPES.get(token, token)

    def _write_terminal(self) -> None:
        """
        Writes the current terminal (lexical element) to the output stream.
        """
        ttype = self.tokenizer.token_type().lower()
        ttype = self.TYPER.get(ttype, ttype)
        if ttype == "integerConstant":
            value = self.tokenizer.int_val()
        elif ttype == "stringConstant":
            value = self.tokenizer.string_val()
        else:
            value = self._escape(self.tokenizer.current_token)
        self.write(f"<{ttype}> {value} </{ttype}>")
        self.tokenizer.advance()

    def compile_class(self) -> None:
        """
        Compiles a complete class.
        class: 'class' className '{' classVarDec* subroutineDec* '}'
        """
        # Your code goes here!
        self.write("<class>")
        self.indent += 1

        # 'class'
        self._write_terminal()

        # className
        self._write_terminal()

        # '{'
        self._write_terminal()

        # classVarDec*
        while self.tokenizer.current_token in ("static", "field"):
            self.compile_class_var_dec()

        # subroutineDec*
        while self.tokenizer.current_token in ("constructor", "function", "method"):
            self.compile_subroutine()

        # '}'
        self._write_terminal()

        self.indent -= 1
        self.write("</class>")

    def compile_class_var_dec(self) -> None:
        """
        Compiles a static declaration or a field declaration.
        classVarDec: ('static' | 'field') type varName (',' varName)* ';'
        """
        # Your code goes here!
        self.write("<classVarDec>")
        self.indent += 1

        # static | field
        self._write_terminal()

        # type
        self._write_terminal()

        # varName
        self._write_terminal()

        while self.tokenizer.current_token == ",":
            # ','
            self._write_terminal()
            # varName
            self._write_terminal()

        # ';'
        self._write_terminal()

        self.indent -= 1
        self.write("</classVarDec>")

    def compile_subroutine(self) -> None:
        """
        Compiles a complete method, function, or constructor.
        You can assume that classes with constructors have at least one field,
        you will understand why this is necessary in project 11.

        """
        # Your code goes here!

        # subroutineDec: ('constructor' | 'function' | 'method') ('void' | type)
        self.write("<subroutineDec>")
        self.indent += 1

        # constructor | function | method
        self._write_terminal()
        # return type
        self._write_terminal()

        # subroutineName '(' parameterList ')' subroutineBody
        # not an actual xml!

        # subroutine name
        self._write_terminal()
        # '('
        self._write_terminal()
        self.compile_parameter_list()
        # ')'
        self._write_terminal()

        # subroutineBody: '{' varDec* statements '}'
        self.write("<subroutineBody>")
        self.indent += 1

        # '{'
        self._write_terminal()
        while self.tokenizer.current_token == "var":
            self.compile_var_dec()
        self.compile_statements()
        # '}'
        self._write_terminal()

        self.indent -= 1
        self.write("</subroutineBody>")

        self.indent -= 1
        self.write("</subroutineDec>")

    def _compile_subroutine_call(self) -> None:
        """
        Compiles a complete subroutine call.
        subroutineCall: '(' expressionList ')' | (className | varName) '.' subroutineName '(' expressionList ')'
        """
        if self.tokenizer.current_token == ".":
            self._write_terminal()  # '.'
            self._write_terminal()  # subroutineName

        self._write_terminal()  # '('
        self.compile_expression_list()
        self._write_terminal()  # ')'

    def compile_parameter_list(self) -> None:
        """
        Compiles a (possibly empty) parameter list, not including the
        enclosing "()".
        parameterList: ((type varName) (',' type varName)*)?
        """
        # Your code goes here!
        self.write("<parameterList>")
        self.indent += 1

        if self.tokenizer.current_token != ")":
            # type
            self._write_terminal()
            # varName
            self._write_terminal()

            while self.tokenizer.current_token == ",":
                # ','
                self._write_terminal()
                # type
                self._write_terminal()
                # varName
                self._write_terminal()

        self.indent -= 1
        self.write("</parameterList>")

    def compile_var_dec(self) -> None:
        """
        Compiles a var declaration.
        varDec: 'var' type varName (',' varName)* ';'
        """
        # Your code goes here!
        self.write("<varDec>")
        self.indent += 1

        # 'var'
        self._write_terminal()
        # type
        self._write_terminal()
        # varName
        self._write_terminal()

        while self.tokenizer.current_token == ",":
            # ','
            self._write_terminal()
            # varName
            self._write_terminal()

        # ';'
        self._write_terminal()

        self.indent -= 1
        self.write("</varDec>")

    def compile_statements(self) -> None:
        """
        Compiles a sequence of statements, not including the enclosing "{}".
        statements: statement*
        statement: letStatement | ifStatement | whileStatement | doStatement |
                 returnStatement
        """
        # Your code goes here!
        self.write("<statements>")
        self.indent += 1

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

        self.indent -= 1
        self.write("</statements>")

    def compile_do(self) -> None:
        """
        Compiles a do statement.
        doStatement: 'do' subroutineCall ';'
        """
        # Your code goes here!
        self.write("<doStatement>")
        self.indent += 1

        self._write_terminal()  # 'do'
        self._write_terminal()  # subroutineName | className | varName
        self._compile_subroutine_call()
        self._write_terminal()  # ';'

        self.indent -= 1
        self.write("</doStatement>")

    def compile_let(self) -> None:
        """
        Compiles a let statement.
        letStatement: 'let' varName ('[' expression ']')? '=' expression ';'
        """
        # Your code goes here!
        self.write("<letStatement>")
        self.indent += 1

        # let
        self._write_terminal()
        # varName
        self._write_terminal()

        if self.tokenizer.current_token == "[":
            # "["
            self._write_terminal()
            # expression
            self.compile_expression()
            # "]"
            self._write_terminal()

        # '='
        self._write_terminal()
        # expression
        self.compile_expression()
        # ';'
        self._write_terminal()

        self.indent -= 1
        self.write("</letStatement>")

    def compile_while(self) -> None:
        """
        Compiles a while statement.
        whileStatement: 'while' '(' 'expression' ')' '{' statements '}'
        """
        # Your code goes here!
        self.write("<whileStatement>")
        self.indent += 1

        # while
        self._write_terminal()
        # '('
        self._write_terminal()
        # expression
        self.compile_expression()
        # ')'
        self._write_terminal()
        # '{'
        self._write_terminal()
        # statements
        self.compile_statements()
        # '}'
        self._write_terminal()

        self.indent -= 1
        self.write("</whileStatement>")

    def compile_return(self) -> None:
        """Compiles a return statement.
        returnStatement: 'return' expression? ';'
        """
        # Your code goes here!
        self.write("<returnStatement>")
        self.indent += 1

        # return
        self._write_terminal()
        if self.tokenizer.current_token != ";":
            self.compile_expression()

        # ';'
        self._write_terminal()

        self.indent -= 1
        self.write("</returnStatement>")

    def compile_if(self) -> None:
        """
        Compiles a if statement, possibly with a trailing else clause.
        ifStatement: 'if' '(' expression ')' '{' statements '}' ('else' '{' statements '}')?
                   """
        # Your code goes here!
        self.write("<ifStatement>")
        self.indent += 1

        self._write_terminal()  # if
        self._write_terminal()  # '('
        self.compile_expression()
        self._write_terminal()  # ')'
        self._write_terminal()  # '{'
        self.compile_statements()
        self._write_terminal()  # '}'

        if self.tokenizer.current_token == "else":
            self._write_terminal()  # 'else'
            self._write_terminal()  # '{'
            self.compile_statements()
            self._write_terminal()  # '}'

        self.indent -= 1
        self.write("</ifStatement>")

    def compile_expression(self) -> None:
        """
        Compiles an expression.
        term (op term)*
        """
        # Your code goes here!
        self.write("<expression>")
        self.indent += 1

        # term
        self.compile_term()

        # (op term)*
        while (
                self.tokenizer.token_type() == "SYMBOL"
                and self.tokenizer.current_token in self.OPS
        ):
            # op
            self._write_terminal()
            # term
            self.compile_term()

        self.indent -= 1
        self.write("</expression>")

    def compile_term(self) -> None:
        """Compiles a term. 
        This routine is faced with a slight difficulty when
        trying to decide between some of the alternative parsing rules.
        Specifically, if the current token is an identifier, the routing must
        distinguish between a variable, an array entry, and a subroutine call.
        A single look-ahead token, which may be one of "[", "(", or "." suffices
        to distinguish between the three possibilities. Any other token is not
        part of this term and should not be advanced over.

        term: integerConstant | stringConstant | keywordConstant | varName |
            varName '['expression']' | subroutineCall | '(' expression ')' |
            unaryOp term
        """
        # Your code goes here!
        self.write("<term>")
        self.indent += 1

        value = self.tokenizer.current_token
        token_type = self.tokenizer.token_type()

        # integerConstant | stringConstant | keywordConstant
        if token_type in {"INT_CONST", "STRING_CONST", "KEYWORD"}:
            self._write_terminal()

        # unaryOp term
        elif token_type == "SYMBOL" and value in self.UNARY_OPS:
            self._write_terminal()
            self.compile_term()

        # '(' expression ')'
        elif value == "(":
            self._write_terminal()
            self.compile_expression()
            self._write_terminal()

        # varName |  varName '['expression']' | subroutineCall
        elif token_type == "IDENTIFIER":
            self._write_terminal()
            next_token = self.tokenizer.current_token

            # varName '[' expression ']'
            if next_token == "[":
                self._write_terminal()
                self.compile_expression()
                self._write_terminal()

            # subroutineCall
            elif next_token in ("(", "."):
                self._compile_subroutine_call()

        self.indent -= 1
        self.write("</term>")

    def compile_expression_list(self) -> None:
        """
        Compiles a (possibly empty) comma-separated list of expressions.
        expressionList: (expression (',' expression)* )?
        """
        # Your code goes here!
        self.write("<expressionList>")
        self.indent += 1

        if self.tokenizer.current_token != ")":
            self.compile_expression()
            while self.tokenizer.current_token == ",":
                self._write_terminal()
                self.compile_expression()

        self.indent -= 1
        self.write("</expressionList>")
