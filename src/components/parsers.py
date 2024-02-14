from components.lexica import MyLexer
from sly import Parser

class MyParser(Parser):
    debugfile = 'parser.out'
    start = 'statement'
    # Get the token list from the lexer (required)
    tokens = MyLexer.tokens
    precedence = (
        ('left', "+", MINUS),
        ('left', TIMES, DIVIDE),
        ('right', UMINUS),
        )

    def __init__(self):
        self.names = { }


    @_('expr')
    def statement(self, p):
        return p.expr

    # The example with literals
    @_('expr "+" expr')
    def expr(self, p):
        # You can refer to the token 2 ways
        # Way1: using array
        print(p[0], p[1], p[2])
        # Way2: using symbol name. 
        # Here, if you have more than one symbols with the same name
        # You have to indiciate the number at the end.
        return p.expr0 + p.expr1

    # The example with normal token
    @_('expr MINUS expr')
    def expr(self, p):
        print(p[0], p[1], p[2])
        return p.expr0 - p.expr1

    @_('expr TIMES expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('expr DIVIDE expr')
    def expr(self, p):
        return p.expr0 / p.expr1

    # https://sly.readthedocs.io/en/latest/sly.html#dealing-with-ambiguous-grammars
    # `%prec UMINUS` is the way to override the `precedence` of MINUS to UMINUS.
    @_('MINUS expr %prec UMINUS')
    def expr(self, p):
        return -p.expr

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return int(p.NUMBER)

        
if __name__ == "__main__":
    lexer = MyLexer()
    parser = MyParser()
    text = "1 + 2 - 1"
    result = parser.parse(lexer.tokenize(text))
    print(result)