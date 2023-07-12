from rply import ParserGenerator
from primitives import binaryops, integer
class Parser:
    def __init__(self, lexer, ):
        self.lexer = lexer

        self.pg = ParserGenerator(
            ['INTEGER', 'VARIABLE', 'AGAR', 'DAR_GHEYRE_IN_SOORAT', 'BARAYE', 'TA', 'EZAFE', 'PLUS', 'MENHAYE', 'MINUS', 'ZARBDARE', 'MULTIPLY', 'TAGHSIM_BAR', 'DIVIDE', 'MOSAVIYE', 'EQUAL', 'MOSAVI_NIST_BA', 'NEQ']
        )

    def parse(self):
        @self.pg.production('expression : INTEGER')
        def expr_integer(p):
            return integer.Integer(p[0].value)
