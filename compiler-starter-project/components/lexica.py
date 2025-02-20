from sly import Lexer
import sly

class MyLexer(Lexer):
    """
    MyLexer is a class that inherits from sly.Lexer
    It is used to tokenize the input string.
    ref: https://sly.readthedocs.io/en/latest/sly.html#sly-sly-lex-yacc
    

    Python regEX: https://www.w3schools.com/python/python_regex.asp
    """

    ### `tokens` ###
    # set `tokens` so it can be used in the parser.
    # This must be here and all Capitalized. 
    # Please, ignore IDE warning.
    tokens = { ASSIGN, NAME, NUMBER, MINUS, DIVIDE, TIMES, LPAREN, RPAREN}
    
    # https://sly.readthedocs.io/en/latest/sly.html#literal-characters
    literals = { '+' }
    
    ### matching rule ###
    # The matching work from top to bottom
    # At least, all toekns must be defined here

    # Ignore spaces and tabs 
    ignore = ' \t'

    ### EX1: simply define with regEX ###
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ### EX2: Define as a function ###
    @_(r'\d+')
    def NUMBER(self, token):
        # Note that this function set parse token.value to integer
        token.value = int(token.value)
        # Extra print for debug
        print(f"====This print from NUMBER function: {token.type=} {token.value=} {type(token.value)=}")
        return token

    # Try uncomment this and run to see the differences between `token` and `literal`
    ASSIGN  = r'\='
    # PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    LPAREN  = r'\('
    RPAREN  = r'\)'

    # Extra action for newlines
    @_(r'\n+')
    def ignore_newline(self, t):
        # https://sly.readthedocs.io/en/latest/sly.html#line-numbers-and-position-tracking
        self.lineno += t.value.count('\n')

    def error(self, t):
        self.index += 1
        print(f"ERROR: Illegal character '{t.value[0]}' at line {self.lineno}")

if __name__ == '__main__':
    # Write a simple test that only run when you execute this file
    string_input:str = "x1 + 1as! * ()"
    lex:Lexer = MyLexer()
    # assign type to `token`
    token: sly.lex.Token
    for token in lex.tokenize(string_input):
        print(token)