from rply import ParserGenerator
from primitives import binaryops, integer
from unidecode import unidecode
class Parser:
    def __init__(self, lexer, ):
        self.lexer = lexer

        self.pg = ParserGenerator(
            ['INTEGER', 'VARIABLE', 'AGAR', 'DAR_GHEYRE_IN_SOORAT', 'BARAYE', 'TA', 'BE_ALAVEYE_LA', 'BE_ALAVEYE_FA', 'PLUS', 'MENHAYE_LA', 'MENHAYE_FA', 'MINUS', 'ZARBDARE_LA', 'ZARBDARE_FA', 'MULTIPLY', 'TAGHSIM_BAR_LA', 'TAGHSIM_BAR_FA', 'DIVIDE', 'MOSAVIYE_LA', 'MOSAVIYE_FA', 'EQUAL', 'MOSAVI_NIST_BA', 'NEQ', 'OPEN_PAREN', 'CLOSE_PAREN', 'OPEN_BRACE', 'CLOSE_BRACE']
        )

    def parse(self):
        @self.pg.production('expression : INTEGER')
        def expr_integer(p):
            return integer.Integer(int(p[0].getstr()))


        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def expr_parentheses(p):
            ## p[0] is (, p[1] is to be returned, p[2] is )
            return p[1]

        @self.pg.production('expression : expression PLUS expression')
        @self.pg.production('expression : expression BE_ALAVEYE_LA expression')
        @self.pg.production('expression : expression BE_ALAVEYE_FA expression')

        @self.pg.production('expression : expression MINUS expression')
        @self.pg.production('expression : expression MENHAYE_LA expression')
        @self.pg.production('expression : expression MENHAYE_FA expression')

        @self.pg.production('expression : expression MULTIPLY expression')
        @self.pg.production('expression : expression ZARBDARE_FA expression')
        @self.pg.production('expression : expression ZARBDARE_LA expression')

        @self.pg.production('expression : expression DIVIDE expression')
        @self.pg.production('expression : expression TAGHSIM_BAR_LA expression')
        @self.pg.production('expression : expression TAGHSIM_BAR_FA expression')

        ## Yes, I know this is sort of ugly, but I will refactor this later

        ## Can probably further abstract the binary operations and use more polymorphism to avoid reptitions like this
        def expr_binaryoperation(p):
            larg = p[0]
            rarg = p[2]
            operator = p[1].gettokentype()

            if operator == 'PLUS' or operator == 'BE_ALAVEYE_LA' or operator == 'BE_ALAVEYE_FA':
                return binaryops.Add(larg, rarg)

            elif operator == 'MINUS' or operator == 'MENHAYE_LA' or operator == 'MENHAYE_FA':
                return binaryops.Subtract(larg, rarg)

            elif operator == 'MULTIPLY' or operator == 'ZARBDARE_LA' or operator == 'ZARBDARE_FA':
                return binaryops.Multiply(larg, rarg)

            elif operator == 'DIVIDE' or operator == 'TAGHSIM_BAR_LA' or operator == 'TAGHSIM_BAR_FA':
                return binaryops.Divide(larg, rarg)

        @self.pg.production('statement : AGAR expression DAR_GHEYRE_IN_SOORAT statement')
        def statement_conditional(p):
            pass

        @self.pg.error
        def handle_err(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()