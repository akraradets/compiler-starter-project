from enum import Enum
from abc import ABC, abstractmethod

class Statement:
    """What is statement?
    In this calculator project, a statement is each line of math expression.
    In this case, it will consit of tree of math expression
    """
    def __init__(self) -> None:
        root_node
        

class Operations(Enum):
    PLUS:int=0
    MINUS:int=1
    TIMES:int=2
    DIVIDE:int=3

class Expression(ABC): 
    @abstractmethod
    def __init__(self) -> None:
        self.signature:str = ""
        self.value:int = None
        pass

    @abstractmethod
    def run(self) -> None:
        pass

class Expression_math(Expression):
    def __init__(self, operation:Operations, parameter1:Expression, parameter2:Expression):
        # Init attribute
        self.operation:Operations = operation
        self.parameter1:Expression = parameter1
        self.parameter2:Expression = parameter2
        self.signature:str = ""
        self.value:int = None
        # Checking Logic
        assert operation in Operations

        # Create a children
        self.children = [self.parameter1, self.parameter2]
        
    def run(self) -> None:
        # evaluate child first
        for child in self.children:
            child.run()
            # print(child)

        # print(f"Calculating: {self.operation.name=} {self.parameter1=} {self.parameter2=}")
        if(self.operation == Operations.PLUS):
            self.value = self.parameter1.value + self.parameter2.value
        elif(self.operation == Operations.MINUS):
            self.value = self.parameter1.value - self.parameter2.value
        elif(self.operation == Operations.TIMES):
            self.value = self.parameter1.value * self.parameter2.value
        elif(self.operation == Operations.DIVIDE):
            self.value = self.parameter1.value / self.parameter2.value
        else:
            raise ValueError(f"{self.operation=} is not support. Please use class Statement.Operations. Actually, this should not happen.")
        
        self.signature = f"Expression: {self.operation.name} {self.parameter1.value} {self.parameter2.value}"
        print(self)

    def __repr__(self) -> str:
        return self.signature

class Expression_number(Expression):
    def __init__(self, number:int) -> None:
        self.value:int = number
        self.signature:str= str(number)
        
    def run(self) -> None:
        print(self)

    def __repr__(self) -> str:
        return f"Expression_number:{self.signature}"

if __name__ == "__main__":
    number1 = Expression_number(number=8)
    number2 = Expression_number(number=9)
    expr = Expression_math(Operations.MINUS, parameter1=number1, parameter2=number2)
    expr.run()
    # print(expr.hshow())
    print(expr.value)