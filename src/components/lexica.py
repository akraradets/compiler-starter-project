from sly import Lexer
import sly


def print_token(self):
    return "override!!!"


# def __repr__(self):
#     return f'Token(type={self.type!r}, value={self.value!r}, lineno={self.lineno}, index={self.index}, end={self.end})'

class MyLexer(Lexer):
    """
    MyLexer is a class that inherits from sly.Lexer
    It is used to tokenize the input string.
    ref: https://sly.readthedocs.io/en/latest/sly.html#sly-sly-lex-yacc
    """

    ### `tokens` ###
    # set `tokens` so it can be used in the parser.
    # This must be here and all Capitalized. 
    # Please, ignore IDE warning.
    tokens = { NAME, NUMBER, PLUS, TIMES, MINUS, DIVIDE, 
              ASSIGN, LPAREN, RPAREN }
    
    ### matching rule ###
    # The matching work from top to bottom
    # At least, all toekns must be defined here

    # Ignore spaces and tabs 
    ignore = ' \t'
    # Ignored pattern
    ignore_newline = r'\n+'

    ### EX1: simply define with regEX ###
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ### EX2: Define as a function ###
    @_(r'\d+')
    def NUMBER(self, token):
        # Note that this function set parse token.value to integer
        token.value = int(token.value)
        # Extra print for debug
        print(f"This print from NUMBER function: {token.type=} {token.value=} {type(token.value)=}")
        return token


    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'

    # Extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

if __name__ == '__main__':
    # Write a simple test that only run when you execute this file
    string_input:str = "1 + 1as"
    lex:Lexer = MyLexer()
    # assign type to `token`
    token: sly.lex.Token
    for token in lex.tokenize(string_input):
        print(f"{token.type=} {token.value=} {type(token.value)=}")