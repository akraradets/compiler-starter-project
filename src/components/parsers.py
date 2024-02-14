from components.lexica import MyLexer
from components.memory import Memory
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
        self.memory:Memory = Memory()

    @_('NAME ASSIGN expr')
    def statement(self, p):
        var_name = p.NAME
        value = p.expr
        self.memory.set(variable_name=var_name,value=value, data_type=type(value))
        # Note that I did not return anything

    @_('expr')
    def statement(self, p) -> int:
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


from components.ast.statement import Expression, Expression_math, Expression_number, Operations
class ASTParser(Parser):
    debugfile = 'parser.out'
    start = 'statement'
    # Get the token list from the lexer (required)
    tokens = MyLexer.tokens
    precedence = (
        ('left', "+", MINUS),
        # ('left', TIMES, DIVIDE),
        # ('right', UMINUS),
        )

    @_('expr')
    def statement(self, p) -> int:
        p.expr.run()
        return p.expr.value

    @_('expr "+" expr')
    def expr(self, p) -> Expression:
        parameter1 = p.expr0
        parameter2 = p.expr1
        expr = Expression_math(operation=Operations.PLUS, parameter1=parameter1, parameter2=parameter2)
        return expr
    
    @_('expr MINUS expr')
    def expr(self, p) -> Expression:
        parameter1 = p.expr0
        parameter2 = p.expr1
        expr = Expression_math(operation=Operations.MINUS, parameter1=parameter1, parameter2=parameter2)
        return expr

    @_('NUMBER')
    def expr(self, p) -> Expression:
        return Expression_number(number=p.NUMBER)
        
        

        
if __name__ == "__main__":
    lexer = MyLexer()
    parser = MyParser()
    text = "a = 1 + 2 + 3"
    # memory = Memory()
    # parser = ASTParser()
    # text = "1 + 2 + 3"
    result = parser.parse(lexer.tokenize(text))
    print(result)
    print(memory)