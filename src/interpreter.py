from lexer import Lexer
from parser import Parser
from primitives import variable
def interpret(source_code):
    # Get a lexer
    lexer = Lexer().get_lexer()

    # Get a parser
    parser = Parser(lexer)
    parser.parse()
    pg = parser.get_parser()

    # Lex the source code
    tokens = lexer.lex(source_code)
    scope = variable.Scope()

    # Parse the token stream as a program
    try:
        program = pg.parse(iter(tokens))

        # Evaluate the program
        program.evaluate(scope)
    except Exception as e:
        print("An error occurred while interpreting the program:")
        print(str(e))
